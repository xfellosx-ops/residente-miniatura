// Partida: exportar/importar y sincronización entre dos "dispositivos" con una nube simulada.
const {JSDOM,VirtualConsole}=require('jsdom');const fs=require('fs');
const html=fs.readFileSync(__dirname+'/../dist/index.html','utf8');const cloud={};let online=true;
const fake={use:async n=>n==='user'?{id:async()=>'u1'}:n==='db'?{collection:()=>({get:async()=>{if(!online)throw new Error('off');return{docs:Object.entries(cloud).map(([id,v])=>({id,data:()=>v}))}},doc:id=>({set:async v=>{if(!online)throw new Error('off');cloud[id]=JSON.parse(JSON.stringify(v))}})})}:null};
const open=(ls,withCloud)=>new JSDOM(html,{url:'https://x.test/',runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:new VirtualConsole(),beforeParse(w){
 w.HTMLCanvasElement.prototype.getContext=()=>new Proxy({},{get:()=>()=>{},set:()=>true});w.speechSynthesis={cancel(){},speak(){}};w.requestAnimationFrame=()=>0;
 for(const k in ls)w.localStorage.setItem(k,ls[k]);if(withCloud)w.claude=fake;w.__errs=[];w.addEventListener('error',e=>w.__errs.push(e.message))}}).window;
const dump=w=>{const o={};for(let i=0;i<w.localStorage.length;i++){const k=w.localStorage.key(i);o[k]=w.localStorage.getItem(k)}return o};
const wait=ms=>new Promise(r=>setTimeout(r,ms));let bad=0;const fail=m=>{console.log('SYNC: '+m);bad++};
(async()=>{
 // dispositivo A juega un poco (sin nube) y exporta
 let a=open({},false);a.document.querySelector('#t1').click();await wait(50);const S=a.__G.S;S.stats.ok=7;S.flags.prueba=1;a.document.querySelector('#bMenu');
 a.__G.S.potions=9;a.eval('save()');const code=a.__G.exportar();if(!/rm_v3_1/.test(code))fail('exportar sin nivel 1');
 // dispositivo B importa
 let b=open({},false);const n=b.__G.importar(code);if(n<1)fail('importar 0');b=open(dump(b),false);if(b.__G.S.potions!==9)fail('B no recibió la partida');
 if(b.__G.importar(code)!==0)fail('reimportar debió ser 0');
 // caso real: B abrió el juego DESPUÉS (copia casi vacía pero más reciente); el código de A debe ganar por avance
 let d=open({},false);d.document.querySelector('#t1').click();await wait(50);d.eval('save()');await wait(20);
 const ts=JSON.parse(d.localStorage.getItem('rm_ts'));for(const k in ts)ts[k]=Date.now()+60000;d.localStorage.setItem('rm_ts',JSON.stringify(ts));
 if(d.__G.importar(code)<1)fail('la copia vacía y más reciente ganó al código con avance');d=open(dump(d),false);if(d.__G.S.potions!==9)fail('D no recibió el avance');
 // forzar reemplaza aunque lo local tenga más avance
 let e2=open({},false);e2.__G.importar(code);e2=open(dump(e2),false);e2.__G.S.stats.n=99;e2.eval('save()');if(e2.__G.importar(code)!==0)fail('importó encima de más avance');if(e2.__G.importar(code,true)<1)fail('forzar no reemplazó');
 // niveles superados se unen
 let g1=open({rm_global:JSON.stringify({done:{'1':1},team:[]})},false),c1=g1.__G.exportar();let g2=open({rm_global:JSON.stringify({done:{'2':1},team:[]})},false);g2.__G.importar(c1);if(Object.keys(JSON.parse(g2.localStorage.getItem('rm_global')).done).sort().join()!=='1,2')fail('no unió niveles superados');
 // nube: A sube, B (vacío) baja solo en el título
 a=open(dump(a),true);await wait(300);if(!cloud['rm_v3_1'])fail('A no subió: '+Object.keys(cloud));
 let c=open({},true);await wait(300);c=open(dump(c),true);await wait(100);if(c.__G.S.potions!==9)fail('C no bajó de la nube');
 // sin conexión: C sigue jugando, guarda local; al reconectar sube
 online=false;c.__G.S.potions=3;c.eval('save()');await c.__G.syncPush();if(JSON.parse(cloud['rm_v3_1'].v).potions!==9)fail('subió sin conexión');
 if(c.__G.SYNC.state!=='off')fail('estado sin conexión: '+c.__G.SYNC.state);
 online=true;await c.__G.syncPush();if(JSON.parse(cloud['rm_v3_1'].v).potions!==3)fail('no subió al reconectar');
 // archivo sin conexión: es HTML completo y arranca solo
 const f=c.__G.gameFile();if(!/^<!DOCTYPE html>/.test(f)||!/id="eng"/.test(f))fail('archivo de juego');
 const off=new JSDOM(f,{url:'https://y.test/',runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:new VirtualConsole(),beforeParse(w){w.HTMLCanvasElement.prototype.getContext=()=>new Proxy({},{get:()=>()=>{},set:()=>true});w.speechSynthesis={cancel(){},speak(){}};w.requestAnimationFrame=()=>0}}).window;
 if(!off.__G||off.__G.LEVELS.length!==a.__G.LEVELS.length||!off.document.querySelector('#t1'))fail('el archivo descargado no arranca');
 for(const w of [a,b,c])if(w.__errs.length)fail(w.__errs.join('|'));
 console.log(bad?'SYNC FALLA':'SYNC PASA');process.exit(bad?1:0)})();
