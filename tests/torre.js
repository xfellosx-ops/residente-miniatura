// Torre del Consejo: arma el examen de 300, lo responde completo y revisa el resultado; también un piso con explicación.
const {JSDOM,VirtualConsole}=require('jsdom');const fs=require('fs');
const html=fs.readFileSync(__dirname+'/../dist/index.html','utf8');
const w=new JSDOM(html,{url:'https://x.test/',runScripts:'dangerously',pretendToBeVisual:true,virtualConsole:new VirtualConsole(),beforeParse(w){
 w.HTMLCanvasElement.prototype.getContext=()=>new Proxy({},{get:()=>()=>{},set:()=>true});w.speechSynthesis={cancel(){},speak(){}};w.requestAnimationFrame=()=>0;w.__errs=[];w.addEventListener('error',e=>w.__errs.push(e.message))}}).window;
const d=w.document,$=s=>d.querySelector(s),g=w.__G;let bad=0;const fail=m=>{console.log('TORRE: '+m);bad++};
const ids=g.torreBuild(300);if(ids.length!==300||new Set(ids).size!==300)fail('examen con '+ids.length+' preguntas ('+new Set(ids).size+' únicas)');
const temas=new Set(ids.map(i=>g.TB[i].tema_id));if(temas.size<24)fail('solo '+temas.size+' temas');
// series completas y en orden
for(let i=1;i<ids.length;i++){const a=g.TB[ids[i-1]],b=g.TB[ids[i]];if(a.serie_id===b.serie_id&&b.orden<a.orden)fail('serie desordenada '+b.id)}
$('#t4').click();$('#tw').click();
d.querySelector('[data-ex="72"]').click();d.querySelector('.modal button').click();
let n=0;while($('.q[data-torre]')&&n<400){const q=g.TB[$('.q').dataset.id];const wrong=n%10===0;const pick=wrong?Object.keys(q.opciones).find(k=>k!==q.clave):q.clave;d.querySelector('.opt[data-l="'+pick+'"]').click();n++}
if(n!==300)fail('respondidas '+n);if(!/270 \/ 300 \(90 %\)/.test($('#pn').textContent))fail('resultado: '+$('#pn').textContent.slice(0,80));
if(!/La Esclerosis cae/.test($('#pn').textContent))fail('sin desenlace');
$('#tb').click();if(!/Revancha de errores \(30\)/.test($('#pn').textContent))fail('revancha: '+$('#t0').textContent);
d.querySelector('[data-fl="1"]').click();n=0;while($('.q[data-torre]')&&n<60){const q=g.TB[$('.q').dataset.id];d.querySelector('.opt[data-l="'+q.clave+'"]').click();if(!$('#cont'))fail('sin explicación');$('#cont').click();n++}
if(n!==50||!/50 \/ 50/.test($('#pn').textContent))fail('piso: '+n+' '+$('#pn').textContent.slice(0,60));
if(w.__errs.length)fail(w.__errs.join(' | '));
console.log(bad?'TORRE FALLA':'TORRE PASA','banco',Object.keys(g.TB).length,'temas',temas.size);process.exit(bad?1:0);
