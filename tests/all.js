// Construye y juega cada nivel (o los indicados: node tests/all.js levels/9-6-anca) en modo correcto y con 35 % de errores.
const {execFileSync,spawn}=require('child_process');const fs=require('fs');const path=require('path');
const root=path.join(__dirname,'..');
const levels=process.argv.slice(2).length?process.argv.slice(2):fs.readdirSync(path.join(root,'levels')).filter(d=>fs.existsSync(path.join(root,'levels',d,'story.json'))).map(d=>'levels/'+d);
const run=(file,mode)=>new Promise(res=>{const p=spawn('node',[path.join(__dirname,'play.js'),mode,file],{cwd:root});let out='';p.stdout.on('data',d=>{out+=d});p.stderr.on('data',d=>process.stderr.write(d));p.on('close',code=>res({code,out}))});
(async()=>{const jobs=[],todo=[];
 for(const l of levels){const id=JSON.parse(fs.readFileSync(path.join(root,l,'story.json'),'utf8')).meta.id;execFileSync('python3',['build.py',l],{cwd:root,stdio:'inherit'});
  for(const m of ['correct','errors'])todo.push([l,m,path.join(root,'dist',id+'.html')])}
 const worker=async()=>{while(todo.length){const [l,m,f]=todo.shift();jobs.push({l,m,...await run(f,m)})}};await Promise.all(Array.from({length:6},worker));
 const rs=await Promise.all(jobs);let bad=0;
 execFileSync("python3",["build.py"],{cwd:root,stdio:"inherit"});execFileSync("python3",["build.py","--pwa"],{cwd:root,stdio:"inherit"});
 for(const f of ["map.js","torre.js","sync.js","pwa.js"])try{execFileSync("node",[path.join(__dirname,f)],{cwd:root,stdio:"inherit"})}catch(e){bad++}
 for(const r of rs){const ok=r.code===0&&/DONE/.test(r.out)&&/errors \[\]/.test(r.out);if(!ok)bad++;console.log((ok?'PASA ':'FALLA')+' '+r.l+' '+r.m)}
 process.exit(bad?1:0)})();
