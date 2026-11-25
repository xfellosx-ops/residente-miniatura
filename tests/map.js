// Prueba del juego completo (dist/index.html): cada nivel abre desde el mapa y el equipo se comparte.
const {JSDOM,VirtualConsole}=require('jsdom');const fs=require('fs');
const html=fs.readFileSync(__dirname+'/../dist/index.html','utf8');
const open=(ls)=>new JSDOM(html,{url:'https://x.test/',runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:new VirtualConsole(),beforeParse(w){
 w.HTMLCanvasElement.prototype.getContext=()=>new Proxy({},{get:()=>()=>{},set:()=>true});w.speechSynthesis={cancel(){},speak(){}};w.requestAnimationFrame=()=>0;
 for(const k in ls)w.localStorage.setItem(k,ls[k]);w.__errs=[];w.addEventListener('error',e=>w.__errs.push(e.message))}}).window;
let w=open({});const ids=w.__G.LEVELS.map(l=>l.story.meta.id);let bad=0;
w.document.querySelector('#t4').click();const btns=[...w.document.querySelectorAll('[data-lv]')].map(b=>b.dataset.lv);
if(String(btns)!==String(ids)){console.log('mapa',btns,'niveles',ids);bad++}
const team=JSON.stringify({team:[{id:'rituxi',lvl:9,xp:0,max:40,hp:40,evo:false}],box:[],done:{}});
for(const id of ids){w=open({rm_cur:id,rm_global:team});const g=w.__G;
 if(g.STORY.meta.id!==id){console.log('no abrió',id);bad++}
 if(!g.S.team.length||g.S.team[0].id!=='rituxi'){console.log('equipo no compartido en',id);bad++}
 if(w.__errs.length){console.log(id,w.__errs);bad++}}
console.log(bad?'MAPA FALLA':'MAPA PASA',ids.join(' '));process.exit(bad?1:0);
