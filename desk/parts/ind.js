  /* ── industry one-pager ── */
  function renderInd() {
    const list = sortedInds();
    if (!list.length) { $('main').innerHTML = '<div class="empty"><b>산업 데이터를 기다리는 중입니다.</b> 잠시 뒤에도 비어 있으면 새로고침해 주세요.</div>'; return; }
    if (!st.ind || !chains[st.ind]) st.ind = list[0].id;
    const c = chains[st.ind];
    curRev = c.rev || '';
    const ui = c.ui || {};
    // 산업이 많아져(v67) 정사각 타일 대신 줄바꿈 칩으로 고릅니다.
    const chooser = '<div class="ichips" role="group" aria-label="산업 고르기">' + list.map(x => '<button type="button" class="ichip" data-act="ind" data-id="' + esc(x.id) + '" aria-pressed="' + (x.id === c.id) + '"><span class="ic" aria-hidden="true">' + esc(x.icon || '') + '</span>' + brk(x.short || x.name) + (stageMark(x) ? '<span class="ts">' + brk(stageMark(x)) + '</span>' : '') + '</button>').join('') + '</div>';
    const cy = c.cycle || {};
    const split = (cy.split || []).length ? '<div class="split">' + cy.split.map(p => '<div><b>' + CIRC[p.stage] + ' ' + esc(stageName(p.stage, c)) + '</b> ' + esc(p.label) + '<br><span class="nnote">' + (p.nodes || []).map(id => { const n = (c.nodes || []).find(z => z.id === id); return esc(n ? (n.short || n.name) : id); }).join(' · ') + '</span></div>').join('') + '</div>' : '';
    const ins = c.insight || {};
    const insOn = Object.keys(ins).some(k => (ins[k] || []).length);
    const qs = GROUPS.map(g => '<div class="qg">' + g.map(k => { const q = QS.find(z => z[0] === k); return '<div class="q' + (/2$/.test(k) ? ' opp' : '') + '"><div class="qh"><span class="qk">' + q[1] + '</span>' + esc(qLabel(k, c)) + '</div>' + lineList(ins[k]) + '</div>'; }).join('') + '</div>').join('');
    const nodes = (c.nodes || []).map(n => nodeCard(c, n)).join('');
    const hist = (c.history || []).slice().reverse().map(x => '<li>' + esc(x.rev) + ' — ' + esc(x.note || '') + '</li>').join('');
    $('main').innerHTML = chooser +
      '<article class="ind" id="ind-' + esc(c.id) + '">' +
      '<header class="ind-h"><div class="ind-icon" aria-hidden="true">' + esc(c.icon || '') + '</div><div><h2>' + esc(c.name) + '</h2><div class="ind-meta"><span class="stage-badge">' + (cy.stage ? CIRC[cy.stage] + ' ' + esc(stageName(cy.stage, c)) : '국면 판정 전') + '</span>' + (cy.conf ? '<span>판정 확신도 ' + esc(cy.conf) + '</span>' : '') + '<span>' + esc(md(c.rev || c.asOf)) + ' 갱신</span></div></div></header>' +
      '<p class="summary">' + rich(c.summary) + '</p>' +
      (hasFed(c) ? '<section class="blk fed" id="fedBlk">' + fedBlock(c) + '</section>' : '') +
      introHtml(c) +
      '<section class="blk"><h3>' + esc(ui.cycle || '사이클 위치') + '</h3>' + split + lineList(cy.why) +
        ((cy.flags || []).length ? '<div class="flags"><p class="fh">재검토 신호 — 국면은 그대로 두고 새 뉴스가 가리키는 다른 국면을 모아 둡니다</p><ul class="lines">' + cy.flags.slice().reverse().map(f => '<li>' + isNew(f) + rich(f.t) + (f.nid ? srcChips([newsSrc(f.nid)]) : '') + '</li>').join('') + '</ul></div>' : '') +
        (cy.next ? '<p class="next"><span class="k">다음 국면 조건</span>' + rich(cy.next) + '</p>' : '') +
        ((cy.watch || []).length ? '<div class="watch"><span class="kk">볼 지표</span>' + cy.watch.map(w => '<span class="w">' + esc(w) + '</span>').join('') + '</div>' : '') + '</section>' +
      (insOn ? '<section class="blk"><h3>투자 인사이트</h3><div class="qs">' + qs + '</div></section>' : '') +
      '<section class="blk"><h3>' + esc(ui.chain || '밸류체인') + '</h3><p class="hint">' + esc(ui.chainHint || '상류에서 하류 순서입니다. 자세히를 누르면 역할·지표·연관 노드·근거·흐름이 열립니다.') + '</p><div class="chain">' + nodes + '</div></section>' +
      '<section class="blk" id="flowsBlk">' + flowsBlock(c) + '</section>' +
      (c.gaps ? '<section class="blk gaps"><details><summary>조사에서 확인하지 못한 것</summary><p>' + esc(c.gaps) + '</p></details></section>' : '') +
      (hist ? '<section class="blk hist"><details><summary>업데이트 이력</summary><ul>' + hist + '</ul></details></section>' : '') +
      '</article>';
  }
  function nodeCard(c, n) {
    const cos = (n.companies || []).map(x => '<span class="co" title="' + esc(plain(x.note)) + '">' + (x.t ? '<b class="tk">' + esc(x.t) + '</b>' : '') + '<span class="nm">' + esc((x.n || '').replace(/\(.*?\)/g, '').trim()) + '</span>' + mkt(x.m) + '</span>').join('');
    const links = (n.links || []).map(l => {
      if (l.to) { const [ci, ni] = l.to.split('/'); const tc = chains[ci]; const tn = tc && (tc.nodes || []).find(z => z.id === ni);
        return '<button type="button" class="lk" data-act="node" data-ind="' + esc(ci) + '" data-id="' + esc(ni) + '">' + esc(tc ? tc.icon : '') + ' ' + esc(tn ? (tn.short || tn.name) : l.to) + ' <small>' + esc(l.why || '') + '</small></button>'; }
      return '<span class="lk ext">' + esc(l.ext || '') + ' <small>' + esc(l.why || '') + '</small></span>';
    }).join('');
    const ev = (n.state || []).slice().reverse().map(x => '<li>' + isNew(x) + rich(x.t) + srcChips([{ o: x.o, d: x.d, u: x.u }]) + '</li>').join('');
    const fl = allFlows(c).filter(f => f.node === n.id).slice(0, 8).map(f => '<li>' + isNew(f) + '<span class="mono" style="color:var(--faint);font-size:.76rem">' + esc(md(f.d)) + '</span> ' + flowText(f) + '</li>').join('');
    const conotes = (n.companies || []).filter(x => x.note).map(x => '<li><b class="mono" style="font-size:.78rem">' + esc(x.t || '—') + '</b> ' + esc((x.n || '').replace(/\(.*?\)/g, '').trim()) + ' <span class="conote">' + rich(x.note) + '</span></li>').join('');
    const ind = (n.indicators || []).map(x => '<li>' + esc(x.n) + (x.src ? ' <span class="conote">(' + esc(x.src) + ')</span>' : '') + '</li>').join('');
    return '<div class="node" id="node-' + esc(c.id) + '-' + esc(n.id) + '">' +
      '<div class="node-h"><h4>' + esc(n.name) + '</h4>' + (n.stage ? '<span class="nstage">' + CIRC[n.stage] + ' ' + esc(stageName(n.stage, c)) + '</span>' : '') + (n.stageNote ? '<span class="nnote">' + esc(n.stageNote) + '</span>' : '') + '</div>' +
      (n.bottleneck ? '<p class="bneck"><span class="kk">' + esc((c.ui || {}).bneck || '병목') + '</span>' + rich(n.bottleneck) + '</p>' : '') +
      (cos ? '<div class="cos">' + cos + '</div>' : '') +
      '<details><summary>자세히</summary><div class="nd-body">' +
        (n.role ? '<div><h5>' + esc((c.ui || {}).role || '역할과 돈의 흐름') + '</h5><p>' + rich(n.role) + '</p></div>' : '') +
        (ind ? '<div><h5>핵심 지표</h5><ul>' + ind + '</ul></div>' : '') +
        (links ? '<div><h5>연관 노드</h5><div>' + links + '</div></div>' : '') +
        (ev ? '<div><h5>최근 상태 근거</h5><ul>' + ev + '</ul></div>' : '') +
        (fl ? '<div><h5>이 노드의 최근 흐름</h5><ul>' + fl + '</ul></div>' : '') +
        (conotes ? '<div><h5>기업 메모</h5><ul>' + conotes + '</ul></div>' : '') +
      '</div></details></div>';
  }
  // 최근 흐름 = 저장된 흐름(저녁 업데이트) + 밸류체인 한 줄(vc)이 이 산업을 가리키는 뉴스(v67). 최신순.
  function allFlows(c) {
    const out = (c.flows || []).map(f => Object.assign({ kind: 'f' }, f));
    news.forEach(n => { if (!isFresh(n)) return; vcList(n).forEach(v => { if (v.ind === c.id) out.push({ kind: 'n', d: dayOf(n), node: v.node || '', n, v }); }); });
    return out.sort((a, b) => (a.d || '') < (b.d || '') ? 1 : (a.d || '') > (b.d || '') ? -1 : 0);
  }
  const flowText = f => f.kind === 'n'
    ? '<button type="button" class="fnews" data-act="gonews" data-id="' + esc(f.n.id) + '">' + hl(f.n.title) + '</button> <span class="vf">' + esc(vcWhat(f.v)) + '</span>' + (f.v.t ? ' <span class="vt">' + hl(f.v.t) + '</span>' : '')
    : rich(f.t) + srcChips(f.src);
  function flowsBlock(c) {
    const all = allFlows(c), nodeIds = Array.from(new Set(all.map(f => f.node)));
    const btn = (id, label) => '<button type="button" class="ff" data-act="flownode" data-id="' + esc(id) + '" aria-pressed="' + (st.flowNode === id) + '">' + esc(label) + '</button>';
    const filt = '<div class="fl-filter">' + btn('all', '전체') + (c.nodes || []).filter(n => nodeIds.includes(n.id)).map(n => btn(n.id, n.short || n.name)).join('') + '</div>';
    let arr = all.filter(f => st.flowNode === 'all' || f.node === st.flowNode);
    const total = arr.length; if (!st.flowMore) arr = arr.slice(0, 15);
    const nm = id => { const n = (c.nodes || []).find(z => z.id === id); return n ? (n.short || n.name) : (id || '기타'); };
    const items = arr.map(f => '<li><time>' + esc(md(f.d)) + '</time><div>' + isNew(f) + '<span class="ndtag">' + esc(nm(f.node)) + '</span>' + flowText(f) + '</div></li>').join('');
    const nn = fresh().filter(n => indTags(n).has(c.id)).length;
    const hint = (c.flows || []).length ? ((c.ui || {}).flowsHint || '기존 카드 110건에서 옮긴 사실과 새 뉴스가 저녁 업데이트로 쌓입니다.') + ' 뉴스의 밸류체인 한 줄이 이 산업을 가리키면 함께 나옵니다. 최신순입니다.' : '뉴스의 밸류체인 한 줄이 이 산업을 가리키면 여기에 쌓입니다. 최신순입니다.';
    return '<h3>최근 흐름</h3><p class="hint">' + esc(hint) + '</p>' + filt +
      (items ? '<ul class="flows">' + items + '</ul>' : '<p class="hint">아직 흐름이 없습니다.</p>') +
      (total > 15 && !st.flowMore ? '<button type="button" class="more" data-act="flowmore">' + (total - 15) + '건 더 보기</button>' : '') +
      (nn ? '<p class="indnews"><button type="button" class="more" data-act="indnews" data-id="' + esc(c.id) + '">이 산업 뉴스 ' + nn + '건 목록으로 보기</button></p>' : '');
  }
  // 연준 인사 발언(v69, 사용자 지시 10월 15일): 의장·부의장·이사·지역 연은 총재의 발언과 FOMC·인사 관련 뉴스.
  // 매크로 산업의 fed.items(지난 뉴스에서 옮긴 것) + 뉴스 문서의 fed 목록(새 회차부터 작성 단계에서 씀). 같은 주소는 뉴스 쪽을 씁니다.
  const hasFed = c => !!(c.fed || (c.id === 'macro' && news.some(n => (n.fed || []).length)));
  function fedItems(c) {
    const by = new Map();
    ((c.fed || {}).items || []).forEach(f => by.set(f.u || (f.d + f.t), Object.assign({}, f)));
    news.forEach(n => (n.fed || []).forEach(f => by.set(f.u || (f.d + f.t), Object.assign({}, f, { nid: n.id }))));
    return Array.from(by.values()).sort((a, b) => (a.d || '') < (b.d || '') ? 1 : (a.d || '') > (b.d || '') ? -1 : 0);
  }
  const STANCE = { '매파': 'hawk', '비둘기파': 'dove', '중립': 'mid' };
  function fedBlock(c) {
    const fd = c.fed || {}, all = fedItems(c), roster = fd.roster || [];
    const cnt = {}; all.forEach(f => { if (f.k) cnt[f.k] = (cnt[f.k] || 0) + 1; });
    const people = roster.filter(p => cnt[p.k]).concat(Object.keys(cnt).filter(k => !roster.some(p => p.k === k)).map(k => ({ k, n: (all.find(f => f.k === k) || {}).who || k })));
    if (st.fedWho !== 'all' && !cnt[st.fedWho]) st.fedWho = 'all';
    const btn = (id, label) => '<button type="button" class="ff" data-act="fedwho" data-id="' + esc(id) + '" aria-pressed="' + (st.fedWho === id) + '">' + esc(label) + '</button>';
    const filt = '<div class="fl-filter">' + btn('all', '전체') + people.map(p => btn(p.k, p.n.split(' ').pop() + ' ' + cnt[p.k])).join('') + '</div>';
    let arr = all.filter(f => st.fedWho === 'all' || f.k === st.fedWho);
    const total = arr.length; if (!st.fedMore) arr = arr.slice(0, 12);
    const row = f => '<li><time>' + esc(md(f.d)) + '</time><div><div class="fw"><b>' + esc(f.who || '') + '</b>' + (f.role ? '<span class="fr">' + esc(f.role) + '</span>' : '') +
      (f.kind ? '<span class="ndtag">' + esc(f.kind) + '</span>' : '') + (STANCE[f.stance] ? '<span class="stc ' + STANCE[f.stance] + '">' + esc(f.stance) + '</span>' : '') + '</div>' +
      '<p class="ft">' + esc(f.t || '') + (f.nid ? ' <button type="button" class="src" data-act="gonews" data-id="' + esc(f.nid) + '">뉴스 보기</button>' : '') +
      (f.u ? ' <a class="src" href="' + esc(f.u) + '" target="_blank" rel="noopener">원문' + (f.o ? ' · ' + esc(f.o) : '') + '</a>' : '') + '</p></div></li>';
    const vote = roster.length ? '<details class="froster"><summary>연준 인사 명단 ' + roster.length + '명 (2026년 FOMC 투표권)</summary><ul>' +
      roster.map(p => '<li><b>' + esc(p.n) + '</b> ' + esc(p.role) + ' <span class="conote">' + (p.vote ? '투표권 있음' : p.alt ? '대체 위원' : '투표권 없음') + '</span></li>').join('') + '</ul>' +
      (fd.note ? '<p class="hint">' + esc(fd.note) + '</p>' : '') + ((fd.src || []).length ? '<p>' + srcChips(fd.src) + '</p>' : '') + '</details>' : '';
    return '<h3>연준 인사 발언</h3><p class="hint">의장·부의장·이사·지역 연은 총재(뉴욕연은 포함)의 발언과 FOMC·연준 인사 관련 뉴스입니다. 최신순입니다. 매파·비둘기파는 발언 내용으로 나눈 것입니다(추론).</p>' + filt +
      (arr.length ? '<ul class="flows fedl">' + arr.map(row).join('') + '</ul>' : '<p class="hint">아직 발언이 없습니다.</p>') +
      (total > 12 && !st.fedMore ? '<button type="button" class="more" data-act="fedmore">' + (total - 12) + '건 더 보기</button>' : '') + vote;
  }
  // 입문(v67): 처음 보는 사람을 위한 산업 설명 — 무엇을 팔고, 돈을 어디서 벌고, 무엇이 업황을 움직이고, 무엇을 보고, 뉴스를 어떻게 읽는지.
  function introHtml(c) {
    const it = c.intro; if (!it || typeof it !== 'object') return '';
    const dl = [['무엇을 만들어 누구에게 파나', it.what], ['돈은 어디서 버나', it.money], ['무엇이 업황을 움직이나', it.drivers]].filter(p => p[1]).map(p => '<dt>' + esc(p[0]) + '</dt><dd>' + rich(p[1]) + '</dd>').join('');
    const watch = (it.watch || []).map(w => '<li><b>' + esc(w.n) + '</b>' + (w.why ? ' — ' + esc(w.why) : '') + (w.where ? ' <span class="conote">(' + esc(w.where) + ')</span>' : '') + '</li>').join('');
    const reading = (it.reading || []).map(r => '<li><span class="rn">' + esc(r.news) + '</span>' + rich(r.means) + '</li>').join('');
    const players = (it.players || []).map(p => '<li><span class="co">' + (p.t ? '<b class="tk">' + esc(p.t) + '</b>' : '') + '<span class="nm">' + esc(p.n) + '</span>' + mkt(p.m) + '</span> ' + esc(p.role || '') + '</li>').join('');
    const terms = (it.terms || []).map(t => '<dt>' + esc(t.k) + '</dt><dd>' + esc(t.v) + '</dd>').join('');
    return '<section class="blk intro"><h3>입문 — 이 산업을 처음 보는 분께</h3>' +
      (dl ? '<dl class="ik">' + dl + '</dl>' : '') +
      (watch ? '<h4>먼저 볼 지표</h4><ul class="iw">' + watch + '</ul>' : '') +
      (reading ? '<h4>이런 뉴스는 이렇게 읽습니다</h4><ul class="ir">' + reading + '</ul>' : '') +
      (players ? '<details><summary>' + ((it.players || []).every(p => !p.t) ? '주요 기관 ' : '주요 기업 ') + (it.players || []).length + '곳</summary><ul class="pl">' + players + '</ul></details>' : '') +
      (terms ? '<details><summary>용어 ' + (it.terms || []).length + '개</summary><dl class="it">' + terms + '</dl></details>' : '') +
      '</section>';
  }

