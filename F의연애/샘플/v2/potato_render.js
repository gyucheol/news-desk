// Render the doodle potato (same design as sample v1) to transparent PNGs, one per expression.
const { chromium } = require('playwright');
const BODY="M152 16 C196 12 236 30 258 66 C276 96 270 122 278 150 C288 190 276 236 256 270 C232 312 188 332 146 328 C104 326 66 306 44 270 C24 236 22 196 30 160 C36 128 30 100 48 70 C72 34 110 18 152 16 Z";
const S='stroke="#3b2a18" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"';
const EX={
 basic:`<circle cx="118" cy="160" r="10" fill="#22170c"/><circle cx="186" cy="158" r="10" fill="#22170c"/><path d="M130 214 Q154 220 178 212" fill="none" ${S}/>`,
 anx:`<circle cx="118" cy="158" r="9" fill="#22170c"/><circle cx="186" cy="156" r="9" fill="#22170c"/><path d="M104 132 L132 140 M200 138 L172 140" fill="none" ${S}/><path d="M122 218 q8 -9 16 0 t16 0 t16 0 t16 0" fill="none" ${S}/><path d="M250 92 q16 24 0 34 q-16 -10 0 -34z" fill="#bcd9e6" stroke="#3b2a18" stroke-width="5"/>`,
 aha:`<circle cx="118" cy="158" r="12" fill="#22170c"/><circle cx="186" cy="156" r="12" fill="#22170c"/><path d="M100 124 Q118 112 136 122 M168 120 Q186 110 204 120" fill="none" ${S}/><ellipse cx="154" cy="214" rx="11" ry="14" fill="#3b2a18"/>`,
 smile:`<path d="M104 166 q14 -16 28 0 M172 164 q14 -16 28 0" fill="none" ${S}/><path d="M124 204 Q154 252 186 204 Z" fill="#3b2a18" stroke="#3b2a18" stroke-width="5" stroke-linejoin="round"/><path d="M140 224 Q154 238 170 224 Q160 216 150 220Z" fill="#c9786f"/>`
};
const SIREN=`<rect x="112" y="-8" width="80" height="22" rx="5" fill="#2a2622" stroke="#140f0b" stroke-width="5"/><path d="M122 -8 Q152 -70 182 -8 Z" fill="#c4372b" stroke="#4a140e" stroke-width="6" stroke-linejoin="round"/><ellipse cx="140" cy="-34" rx="7" ry="12" fill="#fff" opacity=".7"/>`;
function svg(k,siren){return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="-30 -80 360 420" width="760" height="887">${siren?SIREN:''}
<path d="${BODY}" fill="#cfa86b" ${S}/>
<ellipse cx="92" cy="108" rx="10" ry="6" fill="#a9824a"/><ellipse cx="212" cy="252" rx="12" ry="7" fill="#a9824a"/><ellipse cx="232" cy="120" rx="7" ry="5" fill="#a9824a"/><ellipse cx="80" cy="232" rx="8" ry="5" fill="#a9824a"/>${EX[k]}</svg>`;}
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:760,height:887}});
 for(const [name,k,s] of [['basic','basic',0],['anx','anx',0],['aha','aha',0],['smile','smile',0],['anx_siren','anx',1],['aha_siren','aha',1]]){
  await p.setContent(`<html><body style="margin:0;background:transparent">${svg(k,s)}</body></html>`);
  await p.screenshot({path:process.argv[2]+`/pot_${name}.png`,omitBackground:true,clip:{x:0,y:0,width:760,height:887}});}
 await b.close();})();
