// Sonido: el botón 🔊/🔉/🔇 cambia y se recuerda; la música cambia con la situación; 🏠 INICIO vuelve al título desde el mundo y desde un combate.
const path=require('path');const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']});const p=await b.newPage({viewport:{width:400,height:800}});const errs=[];p.on('pageerror',e=>errs.push(e.message));let bad=0;const fail=m=>{console.log('AUDIO: '+m);bad++};
 await p.route(/fonts\.(googleapis|gstatic)\.com/,r=>r.abort());
 await p.goto('file://'+path.join(__dirname,'..','dist','index.html'));await p.waitForTimeout(300);
 const mus=()=>p.evaluate(()=>MUS.name);
 if(await mus()!=='title')fail('sin música de título');
 await p.click('#bA');await p.waitForTimeout(200);if(!(await p.evaluate(()=>!!AC)))fail('no se creó el audio');
 const s0=await p.textContent('#bSnd');await p.click('#bSnd');const s1=await p.textContent('#bSnd');await p.click('#bSnd');const s2=await p.textContent('#bSnd');await p.click('#bSnd');const s3=await p.textContent('#bSnd');
 if(!(s0==='🔊'&&s1==='🔉'&&s2==='🔇'&&s3==='🔊'))fail('ciclo del botón '+[s0,s1,s2,s3]);
 await p.click('#bSnd');await p.click('#bSnd');await p.reload();await p.waitForTimeout(300);if(await p.textContent('#bSnd')!=='🔇')fail('no recuerda el silencio');
 await p.click('#bSnd');
 await p.click('#t1');for(let i=0;i<12&&(await p.evaluate(()=>MODE))!=='world';i++){await p.evaluate(()=>pressA());await p.waitForTimeout(80)}
 if(await mus()!=='walk')fail('sin música de caminata: '+await mus());
 await p.evaluate(()=>startWild());await p.waitForTimeout(100);if(await mus()!=='wild')fail('sin música de combate');
 await p.evaluate(()=>sfx.power('player','Alquilante'));
 await p.click('#bMenu');if(!(await p.$('#hY')))fail('sin opción de inicio en combate');await p.click('#hY');await p.waitForTimeout(100);
 if((await p.evaluate(()=>MODE))!=='title'||(await mus())!=='title')fail('no volvió al título desde combate');
 await p.click('#t1');for(let i=0;i<12&&(await p.evaluate(()=>MODE))!=='world';i++){await p.evaluate(()=>pressA());await p.waitForTimeout(80)}
 await p.click('#bMenu');await p.click('#m9');if((await p.evaluate(()=>MODE))!=='title')fail('🏠 INICIO del menú no volvió al título');
 await p.evaluate(()=>mapa(title));if(await mus()!=='map')fail('sin música de mapa');
 await p.evaluate(()=>torre(title));if(await mus()!=='torre')fail('sin música de torre');
 await p.evaluate(()=>{['door','locked','travel','roar','heal','faint','chal','item'].forEach(k=>sfx[k]())});await p.waitForTimeout(300);
 if(errs.length)fail(errs.join(' | '));console.log(bad?'AUDIO FALLA':'AUDIO PASA');await b.close();process.exit(bad?1:0)})();
