const {chromium}=require('C:/Users/Kell/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path');const {pathToFileURL}=require('url');
const out=__dirname;
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe'});
 try{
 const page=await browser.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:1});
 const approved=JSON.parse(fs.readFileSync(path.join(out,'copy.json'),'utf8'));let findings=[];
 for(let i=1;i<=5;i++){
  await page.goto(pathToFileURL(path.join(out,`slide-0${i}.html`)).href);
  await page.evaluate(()=>Promise.all([...document.images].map(im=>im.decode())));
  await page.evaluate(()=>document.fonts.ready);
  const check=await page.evaluate(()=>{
   const copy=[...document.querySelectorAll('[data-copy]')].map(el=>el.innerText).join(' ').replace(/\s+/g,' ').trim();
   const text=[...document.querySelectorAll('.copy')].map(el=>{
    const r=el.getBoundingClientRect(),style=getComputedStyle(el);const range=document.createRange();range.selectNodeContents(el);
    const glyphBounds=[...range.getClientRects()].filter(r=>r.width&&r.height).map(r=>({x:r.x,y:r.y,width:r.width,height:r.height,inside:r.left>=24&&r.top>=24&&r.right<=1056&&r.bottom<=1326}));
    return {text:el.innerText,bounds:[r.x,r.y,r.width,r.height],inside:r.left>=24&&r.top>=24&&r.right<=1056&&r.bottom<=1326,glyphBounds,clipped:style.overflowY!=='visible'&&el.scrollHeight>el.clientHeight+1,fontPx:parseFloat(style.fontSize),mobile390Px:parseFloat(style.fontSize)*390/1080};
   });
   return {copy,text,missing:[...document.images].filter(im=>!im.complete||!im.naturalWidth).map(im=>im.src)};
  });
  if(check.copy!==approved[i-1])throw Error(`Copy mismatch ${i}: ${check.copy}`);
  if(check.missing.length||check.text.some(t=>!t.inside||t.clipped||t.glyphBounds.some(g=>!g.inside)))throw Error(`Text bounds failed ${i}: ${JSON.stringify(check)}`);
  findings.push({frame:i,...check});
  await page.screenshot({path:path.join(out,`slide-0${i}.png`)});
 }
 fs.writeFileSync(path.join(out,'render-check.json'),JSON.stringify(findings,null,2));
 console.log('Exact approved copy, loaded images, element and text range bounds verified in five PNGs.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e.message);process.exit(1)});
