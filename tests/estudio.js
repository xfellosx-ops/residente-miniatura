// Estudio: GUARDIA de hoy (20 del banco completo) alimenta el repaso global; DOMINIO, SIESTA, despertar y diario de cierre funcionan.
const path=require('path');const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:400,height:860}});const errs=[];p.on('pageerror',e=>errs.push(e.message));let bad=0;const fail=m=>{console.log('ESTUDIO: '+m);bad++};
 await p.route(/fonts\.(googleapis|gstatic)\.com/,r=>r.abort());await p.goto('file://'+path.join(__dirname,'..','dist','index.html'));await p.waitForTimeout(300);
 if(!/Faltan \d+ días/.test(await p.textContent('#pn')))fail('sin cuenta regresiva');
 const live=async()=>!!(await p.$('.opt:not([disabled])'))&&!(await p.$('.modal'));
 const clr=async()=>{for(let i=0;i<4&&await p.$('.modal button');i++)await p.click('.modal button')};
 const answer=async(right)=>{const l=await p.evaluate(r=>{const id=document.querySelector('.q').dataset.id;const q=window.__G.TB[id]||window.__G.ALL[id];return r?q.clave:Object.keys(q.opciones).find(k=>k!==q.clave)},right);await p.click('.opt[data-l="'+l+'"]');await p.click('#cont')};
 await p.click('#tg');let n=0;while(await live()&&n<25){await answer(n%3!==0);n++}
 if(n!==20)fail('la guardia no tuvo 20 preguntas: '+n);
 const st=await p.evaluate(()=>({gs:gsIds().length,dia:G.dia.n}));if(st.gs<20||st.dia<20)fail('no alimentó el repaso global '+JSON.stringify(st));
 await p.evaluate(()=>{Object.values(GS).forEach(r=>{if(r&&r.due)r.due=Date.now()-1})});
 if(await p.evaluate(()=>dueCount())<5)fail('sin vencidas globales');
 await p.evaluate(()=>review(title));let k=0;while(await live()&&k<25){await answer(true);k++}if(k<1||k>20)fail('repaso global sin tope: '+k);await clr();
 await p.evaluate(()=>dominio(title));if(!(await p.$('#d1')))fail('sin DOMINIO');
 await p.evaluate(()=>siesta(title));if(await p.$('#z1')){await p.click('#z1');let z=0;while(await live()&&z<10){await answer(true);z++}}
 if(!(await p.$('#zw')))fail('la siesta no llegó a dormir');if(!(await p.evaluate(()=>G.siesta&&G.siesta.hasta>Date.now())))fail('sin pausa de alarma');
 await p.click('#zw');await p.click('.modal button');if(!(await p.$('#pv')))fail('sin chequeo al despertar');
 await p.evaluate(()=>{S.done=true;ending()});const dj=await p.$$('[data-dj]');if(dj.length!==3)fail('sin diario');else{await dj[0].click();await p.click('.modal button');if(!(await p.$('#e5')))fail('sin PRÓXIMO CASO')}
 if(errs.length)fail(errs.join(' | '));console.log(bad?'ESTUDIO FALLA':'ESTUDIO PASA');await b.close();process.exit(bad?1:0)})();
