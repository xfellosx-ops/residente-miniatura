const {JSDOM}=require('jsdom');const fs=require('fs');
const MODEARG=process.argv[2]||'correct';
const html=fs.readFileSync(process.argv[3]||(__dirname+'/../dist/index.html'),'utf8');
const dom=new JSDOM(html,{url:'https://x.test/',runScripts:'dangerously',pretendToBeVisual:true,beforeParse(w){
 w.HTMLCanvasElement.prototype.getContext=()=>new Proxy({},{get:(t,k)=>()=>{},set:()=>true});w.speechSynthesis={cancel(){},speak(){}};
 w.requestAnimationFrame=cb=>setTimeout(()=>cb(Date.now()),0);}});
const w=dom.window,d=w.document;const errs=[];w.addEventListener('error',e=>errs.push(e.message+' '+(e.error&&e.error.stack||'').split('\n')[1]));
const $=s=>d.querySelector(s);const G=()=>w.__G;
let ticks=0,lastZone=-1,stuck=0,lastPos='',stats={wild:0,trainer:0,gate:0,mini:0,q:0,wrong:0,lose:0};
let STORY=null;
function key(k,type='keydown'){w.dispatchEvent(new w.KeyboardEvent(type,{key:k,bubbles:true}))}
function step(){ticks++;
 const g=G();if(!g)return;STORY=g.STORY;
 const m=$('.modal button');if(m){if(/REPASO DE RECUPERACI/.test(d.body.textContent))stats.lose++;m.click();return}
 if(g.MODE==='title'){$('#t1').click();return}
 if($('#rb')){stats.rb=(stats.rb||0)+1;$('#rb').click();return}
 if($('#nx')){$('#nx').click();return}
 if($('#cont')){$('#cont').click();return}
 // river
 if(g.MODE==='river'&&g.RIV){const R=g.RIV,r=R.rounds[R.i];if(r){const want=r.opts.indexOf(r.ans);const sel=[...d.querySelectorAll('.opt')];if(sel[want])sel[want].click()}return}
 // question
 const q=$('.q');const opts=[...d.querySelectorAll('.opt:not([disabled])')];
 if(q&&opts.length&&opts[0].dataset.l){const Q=(q.dataset.id&&g.ALL[q.dataset.id])||Object.values(g.ALL).find(x=>x.enunciado===q.textContent);if(!Q){console.log('unknown',q.textContent.slice(0,50));process.exit(1)}
   stats.q++;let pick=Q.clave;if(MODEARG==='errors'&&Math.random()<.35){pick=opts.map(o=>o.dataset.l).find(l=>l!==Q.clave);stats.wrong++}
   opts.find(o=>o.dataset.l===pick).click();return}
 // battle menus
 if($('#bf')){$('#bf').click();return}
 const mv=d.querySelector('.opt[data-i]');if(mv&&g.MODE==='battle'){mv.click();return}
 // stones
 const st=[...d.querySelectorAll('.stone')];if(st.length){const z=STORY.zones[g.S.zone];const done=d.querySelector('.box.small').textContent;const mg=z.minigames.find(m=>m.items.some(it=>st.some(s=>s.dataset.t===it)));const nxt=mg.items.find(it=>st.some(s=>s.dataset.t===it)&&!done.includes(it));st.find(s=>s.dataset.t===nxt).click();return}
 // memorama con memoria
 const cards=[...d.querySelectorAll('.card')];if(cards.length){global.MEM=global.MEM||{};const z=STORY.zones[g.S.zone];
   const pairs=z.minigames.flatMap(m=>m.type==='indices'?m.items.filter(s=>s.lastIndexOf('=')>0).map(s=>{const i=s.lastIndexOf('=');return[s.slice(0,i).trim(),'Vale '+s.slice(i+1).trim()]}):m.pairs);
   cards.forEach(c=>{if(c.textContent!=='?')MEM[c.dataset.j]=c.textContent});
   const up=cards.filter(c=>c.classList.contains('up'));if(up.length>=2)return;
   const mateOf=t=>{const p=pairs.find(p=>p[0]===t||p[1]===t);return p?(p[0]===t?p[1]:p[0]):null};
   if(up.length===1){const mate=mateOf(up[0].textContent);const known=cards.find(c=>c!==up[0]&&!c.classList.contains('done')&&MEM[c.dataset.j]===mate);const c=known||cards.find(c=>c.textContent==='?'&&!MEM[c.dataset.j])||cards.find(c=>c.textContent==='?');c&&c.click();return}
   // look for known pair
   const hid=cards.filter(c=>c.textContent==='?');for(const a of hid){const ta=MEM[a.dataset.j];if(!ta)continue;const m=mateOf(ta);const b=hid.find(b=>b!==a&&MEM[b.dataset.j]===m);if(b){a.click();return}}
   const c=hid.find(c=>!MEM[c.dataset.j])||hid[0];c&&c.click();return}
 else global.MEM=null;
 if(g.MODE==='world'){const S=g.S,M=g.MAP;if(S.zone!==lastZone){lastZone=S.zone;console.log('zone',S.zone,STORY.zones[S.zone].name,'W',M.W,'q',stats.q)}
   if(global.MOVING&&Date.now()-global.MOVING<40)return;
   const gone=o=>o.k==='trainer'?!!S.flags[o.id]:o.k==='gate'?!!S.flags['g_'+M.zi+'_'+o.gi]:o.k==='mini'?!!S.flags['m_'+M.zi+'_'+o.i]:false;
   const block=M.objs.filter(o=>['trainer','gate','mini'].includes(o.k)&&!gone(o)).sort((a,b)=>a.x-b.x)[0];
   const pass=(x,y)=>{if(x<0||y<0||x>=M.W||y>=M.H)return false;const t=M.g[y][x];if(M.objs.some(o=>['npc','sign','nurse'].includes(o.k)&&o.x===x&&o.y===y))return false;if(M.objs.some(o=>o.k==='trainer'&&S.flags[o.id]&&o.x===x&&o.y-1===y))return false;
     if(t==='#'){const o=M.objs.find(o=>o.x===x&&o.y===y&&['trainer','gate','mini'].includes(o.k));return !!o&&gone(o)}return true};
   let tx,ty;if(block){tx=block.x-1;ty=block.y}else{ty=5;tx=M.W-1}
   if(S.x===tx&&S.y===ty){if(block){if(S.dir!=='right'){key('ArrowRight');setTimeout(()=>key('ArrowRight','keyup'),2)}else key('z')}return}
   // BFS
   const Q=[[S.x,S.y]],prev={};prev[S.x+','+S.y]=null;let found=false;while(Q.length){const [x,y]=Q.shift();if(x===tx&&y===ty){found=true;break}for(const [dx,dy,k] of [[1,0],[0,1],[0,-1],[-1,0]]){const nx=x+dx,ny=y+dy,kk=nx+','+ny;if(kk in prev)continue;if(!pass(nx,ny))continue;prev[kk]=[x,y];Q.push([nx,ny])}}
   if(!found){console.log('NO PATH',S.zone,S.x,S.y,'->',tx,ty);process.exit(2)}
   let cur=[tx,ty];while(prev[cur[0]+','+cur[1]]&&!(prev[cur[0]+','+cur[1]][0]===S.x&&prev[cur[0]+','+cur[1]][1]===S.y))cur=prev[cur[0]+','+cur[1]];
   const dx=cur[0]-S.x,dy=cur[1]-S.y;const k=dx>0?'ArrowRight':dx<0?'ArrowLeft':dy>0?'ArrowDown':'ArrowUp';key(k);global.MOVING=Date.now();setTimeout(()=>key(k,'keyup'),1);return}
 if(g.MODE==='battle'&&$('#bk')){$('#bk').click();return}
}
const iv=setInterval(()=>{try{step()}catch(e){console.log('ERR',e.stack);process.exit(1)}
 const g=G();if(g&&g.S.done&&$('#e1')){clearInterval(iv);console.log('DONE',JSON.stringify(stats),'ticks',ticks,'stats',JSON.stringify(g.S.stats),'team',g.S.team.map(c=>c.id+':'+c.lvl+(c.evo?'*':'')).join(' '),'nefro',g.S.nefro.length,'errors',errs.slice(0,5),'WRONG',Object.entries(g.S.srs).filter(([i,r])=>r.last===0).map(([i])=>i+':'+(g.ALL[i].enunciado||'').slice(0,40)));process.exit(0)}
 if(ticks%20000===0){const g=G();console.log("tick",ticks,g.MODE,"z",g.S.zone,g.S.x,g.S.y,JSON.stringify(stats),d.querySelector("#pn").textContent.slice(0,90))}
 if(ticks>400000){console.log('TIMEOUT',G().MODE,G().S.zone,G().S.x,G().S.y,d.querySelector('#pn').textContent.slice(0,200),errs.slice(0,5));process.exit(1)}},1);
