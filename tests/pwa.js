// App instalable: sirve docs/ en una subruta (como GitHub Pages), deja que el service worker guarde el juego,
// corta la red y comprueba que recarga, cambia de nivel y conserva la partida sin conexión.
const http=require('http'),fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const root=path.join(__dirname,'..','docs');const mime={'.html':'text/html; charset=utf-8','.js':'text/javascript','.png':'image/png','.webmanifest':'application/manifest+json'};
const srv=http.createServer((q,r)=>{let u=decodeURIComponent(q.url.split('?')[0]);if(!u.startsWith('/residente-miniatura/')){r.writeHead(404);return r.end()}u=u.slice('/residente-miniatura/'.length)||'index.html';
 const f=path.join(root,u);if(!f.startsWith(root)||!fs.existsSync(f)){r.writeHead(404);return r.end()}r.writeHead(200,{'content-type':mime[path.extname(f)]||'text/plain'});fs.createReadStream(f).pipe(r)});
(async()=>{await new Promise(r=>srv.listen(0,r));const url='http://localhost:'+srv.address().port+'/residente-miniatura/';let bad=0;const fail=m=>{console.log('PWA: '+m);bad++};
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:400,height:800}});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await ctx.route(/fonts\.(googleapis|gstatic)\.com/,r=>r.abort());
 await p.goto(url);await p.waitForFunction(()=>navigator.serviceWorker&&navigator.serviceWorker.controller,null,{timeout:20000}).catch(()=>fail('el service worker no tomó control'));
 const man=await p.evaluate(async()=>{const r=await fetch(document.querySelector('link[rel=manifest]').href);return r.json()});if(man.display!=='standalone'||man.icons.length<2)fail('manifest');
 await p.waitForTimeout(800);await ctx.setOffline(true);
 await p.reload();if(!(await p.$('#t1')))fail('no recarga sin conexión');
 await p.click('#t1');await p.waitForTimeout(300);await p.evaluate(()=>{window.__G.S.potions=7;save()});
 await p.click('#bMenu').catch(()=>{});await p.reload();if((await p.evaluate(()=>window.__G.S.potions))!==7)fail('no conservó la partida sin conexión');
 await p.click('#t4');await p.click('[data-lv="9-6"]');await p.waitForLoadState('load');await p.waitForTimeout(300);
 if((await p.evaluate(()=>window.__G.STORY.meta.id))!=='9-6')fail('no cambió de nivel sin conexión');
 if(errs.length)fail(errs.join(' | '));console.log(bad?'PWA FALLA':'PWA PASA');await b.close();srv.close();process.exit(bad?1:0)})();
