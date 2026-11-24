// Estudio: GUARDIA de hoy con predicción, apuesta de confianza (SEGURO/DUDÉ) y reaprendizaje en la misma sesión; repaso global, DOMINIO,
// SIESTA, despertar con alerta baja, diario de cierre, caso del día, jefe de región y prueba de entrada.
const path=require('path');const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:400,height:860}});const errs=[];p.on('pageerror',e=>errs.push(e.message));let bad=0;const fail=m=>{console.log('ESTUDIO: '+m);bad++};
 await p.route(/fonts\.(googleapis|gstatic)\.com/,r=>r.abort());await p.goto('file://'+path.join(__dirname,'..','dist','index.html'));await p.waitForTimeout(300);
 if(!/Faltan \d+ días/.test(await p.textContent('#pn')))fail('sin cuenta regresiva');
 if(!/ritmo necesario \d+\/día/.test(await p.textContent('#pn')))fail('sin meta dinámica en HOY');
 if(!/Logros/.test(await p.textContent('#pn')))fail('sin logros en el título');
 const live=async()=>!!(await p.$('.q'))&&(!!(await p.$('.opt[data-l]:not([disabled])'))||!!(await p.$('#gen')))&&!(await p.$('.modal'));
 const clr=async()=>{for(let i=0;i<4&&await p.$('.modal button');i++)await p.click('.modal button')};
 const answer=async(right,conf='#cont')=>{if(await p.$('#gen'))await p.click('#gen');const l=await p.evaluate(r=>{const id=document.querySelector('.q').dataset.id;const q=window.__G.TB[id]||window.__G.ALL[id];return r?q.clave:Object.keys(q.opciones).find(k=>k!==q.clave)},right);await p.click('.opt[data-l="'+l+'"]');
  if(!(await p.$('#dud')))fail('sin botones SEGURO/DUDÉ');await p.click(conf)};
 // GUARDIA: predicción → 20 camas; los fallos (con SEGURO = error confiado) vuelven 3–5 preguntas después
 await p.click('#tg');if(!(await p.$('[data-pr]')))fail('sin predicción antes de la guardia');else await p.click('[data-pr="14"]');
 const seen=new Set();let n=0,re=0;while(await live()&&n<60){const id=await p.$eval('.q',e=>e.dataset.id);const again=seen.has(id);if(again)re++;seen.add(id);await answer(again||n%3!==0);n++}
 if(seen.size<20)fail('la guardia no tuvo 20 preguntas distintas: '+seen.size);if(re<3)fail('sin reaprendizaje en la sesión: '+re+' reingresos');
 const txt=await p.textContent('#pn');if(!/\/20 pacientes estables/.test(txt))fail('sin pacientes estables: '+txt.slice(0,80));if(!/Predijiste 14/.test(txt))fail('sin predicho vs real');
 const st=await p.evaluate(()=>({gs:gsIds().length,dia:G.dia.n,ec:gsIds().filter(i=>GS[i].ec).length,cal:Object.keys(G.cal||{}).length}));if(st.gs<20||st.dia<20)fail('no alimentó el repaso global '+JSON.stringify(st));
 if(!st.ec)fail('el error con SEGURO no quedó como error confiado');if(!st.cal)fail('sin calibración por tema');
 // DUDÉ: acierto con duda no sube de caja y vuelve pronto
 const du=await p.evaluate(()=>{const q=Object.values(window.__G.TB).find(q=>!GS[q.id]);GS[q.id]={b:3,due:Date.now()-1,t:Date.now()-5*864e5,last:1};grade(q,true,{glob:1,conf:0});const r=GS[q.id];return{b:r.b,d:(r.due-Date.now())/864e5,ln:r.ln}});
 if(du.b!==3||du.d>2.01)fail('DUDÉ promovió la pregunta '+JSON.stringify(du));if(du.ln!==1)fail('sin exactitud a largo plazo');
 await p.evaluate(()=>{Object.values(GS).forEach(r=>{if(r&&r.due)r.due=Date.now()-1})});
 if(await p.evaluate(()=>dueCount())<5)fail('sin vencidas globales');
 await p.evaluate(()=>review(title));let k=0;const rs=new Set();while(await live()&&k<45){rs.add(await p.$eval('.q',e=>e.dataset.id));await answer(true);k++}if(rs.size<1||rs.size>20)fail('repaso global sin tope: '+rs.size);await clr();
 await p.evaluate(()=>dominio(title));if(!(await p.$('#d1')))fail('sin DOMINIO');if(!/Pronóstico|Calibración/.test(await p.textContent('#pn')))fail('DOMINIO sin pronóstico/calibración');if(!(await p.$('#dall')))fail('DOMINIO sin ver todos');
 await p.evaluate(()=>siesta(title));if(await p.$('#z1')){await p.click('#z1');let z=0;while(await live()&&z<20){await answer(true);z++}}
 if(!(await p.$('#zw')))fail('la siesta no llegó a dormir');if(!(await p.evaluate(()=>G.siesta&&G.siesta.hasta>Date.now())))fail('sin pausa de alarma');
 await p.click('#zw');await p.click('.modal button');if(!(await p.$('#pv')))fail('sin chequeo al despertar');
 const low=await p.evaluate(()=>({low:lowA(),nuevas:guardiaList(20).filter(q=>!GS[q.id]).length}));if(!low.low)fail('al despertar no hay alerta baja');if(low.nuevas)fail('con alerta baja la guardia trae nuevas: '+low.nuevas);
 await p.evaluate(()=>{G.lowUntil=0;gsave()});
 await p.evaluate(()=>{S.done=true;ending()});const dj=await p.$$('[data-dj]');if(dj.length!==3)fail('sin diario');else{await dj[0].click();await p.click('.modal button');if(!(await p.$('#e5')))fail('sin PRÓXIMO CASO')}
 // caso del día
 await p.evaluate(()=>casoDia(title));let c=0;while(await live()&&c<10){await answer(true);c++}await clr();if(!(await p.evaluate(()=>G.cdd&&G.cdd.f===hoyF()&&G.cddR>=1)))fail('sin caso del día');
 // prueba de entrada: el nivel 2 está tras el 1; 5 aciertos lo saltan
 await p.evaluate(()=>{G.done={};G.skip={};gsave();mapa(title)});const lk=await p.$eval('[data-lv="2"]',e=>e.dataset.lock||'');if(lk!=='1')fail('el nivel 2 no espera al 1: '+lk);
 await p.click('[data-lv="2"]');await p.click('#pe');let e=0;while(await live()&&e<8){await answer(true);e++}if(e!==5)fail('prueba de entrada de '+e);await clr();
 if(!(await p.evaluate(()=>G.skip&&G.skip["1"])))fail('la prueba de entrada no saltó el nivel 1');if(await p.$eval('[data-lv="2"]',e=>e.dataset.lock||''))fail('el nivel 2 sigue cerrado');
 // jefe de región 1 (opcional): se abre al superar la región y paga con nefronas y ficha
 await p.evaluate(()=>{G.done={"1":1,"2":1,"3":1};G.fichas=0;gsave();mapa(title)});if(!(await p.$('[data-rb="1"]')))fail('sin jefe de región');else{const nef0=await p.evaluate(()=>G.nef||0);await p.click('[data-rb="1"]');
  let r=0;while(r<120&&!(await p.evaluate(()=>!!(G.rboss&&G.rboss[1])))){r++;if(await p.$('.modal button')){await p.click('.modal button');continue}if(await p.$('#nx')){await p.click('#nx');continue}if(await live()){await answer(true);continue}if(await p.$('#bq')){await p.click('#bq');continue}await p.waitForTimeout(150)}
  const R=await p.evaluate(()=>({rb:G.rboss&&G.rboss[1],f:G.fichas,nef:G.nef}));if(!R.rb)fail('no se venció al jefe de región: '+(await p.evaluate(()=>MODE+' '+JSON.stringify(BAT&&{a:BAT.asked,h:BAT.hits,hp:BAT.foes[0].hp})+' '+document.querySelector('#pn').textContent.slice(0,150))));else if(!(R.f>=1&&R.nef>nef0))fail('sin recompensa del jefe de región '+JSON.stringify(R))}
 if(errs.length)fail(errs.join(' | '));console.log(bad?'ESTUDIO FALLA':'ESTUDIO PASA');await b.close();process.exit(bad?1:0)})();
