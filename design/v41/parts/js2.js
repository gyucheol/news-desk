
  /* ── 새 형식(제목 + 한줄 요약) 뉴스 ── */
  // 한줄 요약(one)이 있는 문서만 뉴스 목록에 나옵니다. 그 전의 요약 카드는 산업 한 페이지에 반영을 마쳐 '이전 기록'으로만 봅니다.
  const isFresh = n => typeof n.one === 'string' && n.one.trim() !== '';
  const fresh = () => news.filter(isFresh);
  const legacy = () => news.filter(n => !isFresh(n));
  const indTags = n => { const s = new Set(n.inds || []), mac = (n.nodes || []).filter(p => p.indexOf('macro/') === 0); if (mac.includes('macro/semis')) { s.add('semis'); if (mac.length === 1) s.delete('macro'); } if (n.ind) s.add(n.ind); return s; };
  const mainInd = n => n.ind || ((n.nodes || []).includes('macro/semis') ? 'semis' : (n.inds || [])[0] || 'macro');
  const indLabel = n => { const m = mainInd(n); const rest = (n.inds || []).filter(i => i !== m && !(m === 'semis' && i === 'macro')); return [m].concat(rest).map(i => IND[i] || i).join(' · '); };
  const dayOf = n => pubParts(n.published || n.processed).day;
  const srcName = n => n.source === '텔레그램' && n.channel ? '텔레그램 ' + n.channel : (n.source || '');
  const hasDetail = n => !!(n.detail && Array.isArray(n.detail.blocks) && n.detail.blocks.length);
  const hasIns2 = n => !!(n.insight2 && Array.isArray(n.insight2.parts) && n.insight2.parts.length);
  const pendingDetail = () => fresh().filter(n => dreqs[n.id] && !dsent[n.id] && !hasDetail(n));   // 체크만 하고 아직 '요청'을 누르지 않은 것
  const reqState = n => hasDetail(n) ? 'done' : dsent[n.id] ? 'sent' : dreqs[n.id] ? 'ck' : '';
  const pendingInsight = () => fresh().filter(n => reqs[n.id] && !hasIns2(n));
  const unreadCount = () => fresh().filter(n => !reads[n.id]).length;
  const ordInd = n => { const i = IND_ORDER.indexOf(mainInd(n)); return i < 0 ? 99 : i; };
  const byList = (a, b) => { const da = dayOf(a), db = dayOf(b); return da < db ? 1 : da > db ? -1 : ordInd(a) - ordInd(b) || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0); };
  function listFiltered(skip) {
    const q = st.q.trim().toLowerCase();
    return fresh().filter(n => {
      if (skip !== 'src' && st.src !== 'all' && n.source !== st.src) return false;
      if (skip !== 'ind' && st.nind !== 'all' && !indTags(n).has(st.nind)) return false;
      if (st.unreadOnly && reads[n.id]) return false;
      if (st.ckOnly && !dreqs[n.id] && !dsent[n.id]) return false;
      if (q && !plain(JSON.stringify([n.title, n.one, n.facts, n.origTitle, n.channel, n.source])).toLowerCase().includes(q)) return false;
      return true;
    });
  }

  /* 본문 표기: {{강조}}, {f:사실}·{p:회사 발표}·{a:증권사}·{i:추론}·{u:미확인} 꼬리표, [글자](주소) 링크. 예전 꼬리표 [사실]·[추론]도 읽습니다. */
  const EVK = { '사실': 'f', '추론': 'i', '귀납': 'i', '연역': 'i', '유추': 'i', '추측': 'i', '미확인': 'u' };
  function rt(t) {
    let s = esc(t);
    s = s.replace(/\{\{(.+?)\}\}/g, '<mark>$1</mark>');
    s = s.replace(/\[([^\[\]]+)\]\((https?:\/\/[^\s()]+)\)/g, (m, a, u) => '<a href="' + u + '" target="_blank" rel="noopener">' + a + '</a>');
    s = s.replace(/\s*\{([fpaiu]):([^{}]+)\}/g, (m, c, a) => '<span class="ev ' + c + '">' + a + '</span>');
    s = s.replace(/\s*\[(사실|추론|귀납|연역|유추|추측|미확인)\]/g, (m, a) => '<span class="ev ' + EVK[a] + '">' + a + '</span>');
    return s;
  }
  const EVLEGEND = '<p class="evlegend"><span><span class="ev f">사실</span>보도·공시로 확인</span><span><span class="ev p">회사 발표</span>회사 계획·발언</span><span><span class="ev a">증권사</span>분석 기관 견해</span><span><span class="ev i">추론</span>Claude의 판단</span><span><span class="ev u">미확인</span>원문 확인 못 함</span></p>';
  const li = arr => (arr || []).map(x => '<li>' + rt(x) + '</li>').join('');
  function blocksHtml(arr) {
    return (arr || []).map(b => {
      if (!b || typeof b !== 'object') return '';
      switch (b.k) {
        case 'h3': return '<h3>' + rt(b.t) + '</h3>';
        case 'h4': return '<h4>' + rt(b.t) + '</h4>';
        case 'lead': return '<p class="lead">' + rt(b.t) + '</p>';
        case 'p': return '<p>' + rt(b.t) + '</p>';
        case 'dim': return '<p class="dim">' + rt(b.t) + '</p>';
        case 'callout': return '<p class="callout">' + rt(b.t) + '</p>';
        case 'legend': return EVLEGEND;
        case 'pts': return '<ul class="pts">' + li(b.items) + '</ul>';
        case 'num': return '<ol class="num">' + li(b.items) + '</ol>';
        case 'src': return '<ul class="srcl">' + li(b.items) + '</ul>';
        case 'chain': return '<p class="mech">' + (b.items || []).map(x => '<span>' + rt(x) + '</span>').join('<i aria-hidden="true">→</i>') + '</p>';
        case 'vc': return '<div class="vc" role="group"' + (b.label ? ' aria-label="' + esc(b.label) + '"' : '') + '>' + (b.cols || []).map(c => '<div class="col' + (c.here ? ' here' : '') + '">' + (c.here ? '<span class="here-tag">' + esc(c.tag || '이번 변화') + '</span>' : '') + '<h4>' + rt(c.h) + '</h4><ul>' + (c.items || []).map(x => typeof x === 'string' ? '<li>' + rt(x) + '</li>' : '<li>' + (x.b ? '<b>' + esc(x.b) + '</b> ' : '') + rt(x.t) + '</li>').join('') + '</ul></div>').join('<span class="arrow" aria-hidden="true">→</span>') + '</div>';
        case 'seg': return '<ul class="segl">' + (b.items || []).map(x => '<li><span class="nm">' + rt(x.nm) + '</span><span class="stg ' + esc(x.tone || '') + '">' + rt(x.stage) + '</span><span class="why">' + rt(x.why) + '</span></li>').join('') + '</ul>';
        case 'hyps': return '<div class="hyps">' + (b.items || []).map(x => '<article class="hyp"><div class="hd"><span class="k">' + rt(x.kicker) + '</span><h4>' + rt(x.h) + '</h4></div><dl class="kv">' + (x.kv || []).map(p => '<dt>' + rt(p[0]) + '</dt><dd>' + rt(p[1]) + '</dd>').join('') + '</dl></article>').join('') + '</div>';
        case 'verdict': return '<div class="verdict">' + (b.items || []).map(x => '<div class="v ' + esc(x.tone || '') + '"><h4>' + rt(x.h) + '</h4><p>' + rt(x.t) + '</p></div>').join('') + '</div>';
        case 'cmp': return '<ul class="cmp">' + (b.items || []).map(p => '<li><span class="l">' + rt(p[0]) + '</span><span>' + rt(p[1]) + '</span></li>').join('') + '</ul>';
        case 'series': return '<dl class="series">' + (b.items || []).map(p => '<div><dt>' + rt(p[0]) + '</dt><dd>' + rt(p[1]) + '</dd></div>').join('') + '</dl>';
        case 'picks': return '<div class="picks">' + (b.items || []).map(x => '<div class="pick"><span class="k">' + rt(x.k) + '</span><span class="n">' + rt(x.n) + '</span><p>' + rt(x.t) + '</p></div>').join('') + '</div>';
        case 'co': return '<article class="cco"><div class="top"><h4>' + rt(b.name) + '</h4><span class="tk">' + rt(b.tk) + '</span></div>' + (b.px ? '<p class="px">' + rt(b.px) + '</p>' : '') + (b.role ? '<span class="role' + (b.cond ? ' cond' : '') + '">' + rt(b.role) + '</span>' : '') +
          (b.parts || []).map((p, i) => '<details' + (i === 0 ? ' open' : '') + '><summary>' + rt(p.h) + '</summary><div>' + blocksHtml(p.blocks) + '</div></details>').join('') + '</article>';
        default: return b.t ? '<p>' + rt(b.t) + '</p>' : '';
      }
    }).join('');
  }
  function detailHtml(n) {
    const d = n.detail || {};
    let out = '<section class="dsec"><div class="dsh"><span class="tag">자세한 정리' + (d.updated ? ' · ' + esc(kday(d.updated)) + ' 작성' : '') + '</span><p>원문이나 이전 기사를 읽지 않아도 앞뒤 맥락이 이해되도록 썼습니다.</p></div>' +
      '<div class="dpanel">' + EVLEGEND + blocksHtml(d.blocks) +
      '</div></section>';
    if (hasIns2(n)) out += n.insight2.parts.map(p => '<section class="dsec"><div class="dsh"><span class="tag">' + esc(p.tag || '투자 인사이트') + '</span><h3>' + rt(p.title || '') + '</h3>' + (p.sub ? '<p>' + rt(p.sub) + '</p>' : '') + '</div><div class="dpanel">' + blocksHtml(p.blocks) + '</div></section>').join('');
    return '<div class="dwrap" id="dw-' + esc(n.id) + '">' + out + '<div class="dfoot"><button type="button" class="tg" data-act="dopen" data-id="' + esc(n.id) + '">접기</button></div></div>';
  }
  const BASIS = { partial: ['u', '일부 미확인'], channel: ['i', '채널 전언'] };
  const pubDay = n => { const d = dayOf(n); return d ? kday(d) + ' ' + dowOf(d).replace('요일', '') : ''; };
  function reqBtn(n) {
    const id = esc(n.id), s = reqState(n);
    if (s === 'done') return '<button type="button" class="act done" data-act="goreq" data-id="' + id + '">내용·인사이트 보기</button>';
    if (s === 'sent') return '<span class="act wait">조사 중</span>';
    return '<button type="button" class="act" data-act="dreq" data-id="' + id + '" aria-pressed="' + !!dreqs[n.id] + '">' + (dreqs[n.id] ? '요청 담음' : '뉴스 내용 및 인사이트 요청') + '</button>';
  }
  function itemHtml(n) {
    const id = esc(n.id), read = !!reads[n.id];
    const bs = BASIS[n.basis];
    return '<li class="item' + (read ? ' is-read' : '') + '" id="row-' + id + '">' +
      '<div class="body"><p class="imeta"><span class="idate">' + esc(pubDay(n)) + '</span><span class="itag">' + esc(indLabel(n)) + '</span><span>' + esc(srcName(n)) + '</span>' + (bs ? '<span class="ev ' + bs[0] + '">' + bs[1] + '</span>' : '') + (n.dupOf ? '<span>이미 다룬 사건의 후속</span>' : '') + '</p>' +
        '<h3 class="ttl">' + esc(n.title) + '</h3><p class="one">' + esc(n.one) + '</p>' +
        '<div class="acts">' + reqBtn(n) +
          '<button type="button" class="act rd" data-act="read" data-id="' + id + '" aria-pressed="' + read + '">' + (read ? '읽음' : '읽음 처리') + '</button>' +
          (n.url ? '<a class="orig" href="' + esc(n.url) + '" target="_blank" rel="noopener">원문</a>' : '') + '</div></div></li>';
  }
  function reqItemHtml(n) {
    const s = reqState(n), id = esc(n.id);
    const tag = s === 'done' ? '<span class="rq done">작성 완료' + (n.detail && n.detail.updated ? ' · ' + esc(kday(n.detail.updated)) : '') + '</span>' : '<span class="rq">조사 중' + (dsent[n.id] ? ' · ' + esc(kday(new Date(dsent[n.id]).toISOString().slice(0, 10))) + ' 요청' : '') + '</span>';
    const open = st.dopen.has(n.id);
    return '<li class="item rqi" id="rq-' + id + '"><div class="body"><p class="imeta"><span class="idate">' + esc(pubDay(n)) + '</span><span class="itag">' + esc(indLabel(n)) + '</span><span>' + esc(srcName(n)) + '</span>' + tag + '</p>' +
      '<h3 class="ttl">' + esc(n.title) + '</h3><p class="one">' + esc(n.one) + '</p>' +
      (s === 'done' ? '<div class="acts"><button type="button" class="act" data-act="dopen" data-id="' + id + '" aria-expanded="' + open + '">' + (open ? '접기' : '자세한 내용·투자 인사이트 펼치기') + '</button></div>' + (open ? detailHtml(n) : '')
        : '<p class="rqnote">새 Claude Code 창에서 자세한 내용과 투자 인사이트를 조사하고 있습니다. 끝나면 이 자리에 나옵니다.</p>') + '</div></li>';
  }
  function renderReq() {
    const arr = fresh().filter(n => reqState(n) === 'sent' || reqState(n) === 'done').sort((a, b) => (reqState(a) === reqState(b) ? byList(a, b) : reqState(a) === 'sent' ? -1 : 1));
    $('main').innerHTML = '<div class="nb"><p class="guide">뉴스 목록에서 요청한 뉴스입니다. 조사 중인 뉴스가 위에, 작성이 끝난 뉴스가 아래에 나옵니다.</p></div>' +
      (arr.length ? '<ul class="news">' + arr.map(reqItemHtml).join('') + '</ul>' : '<div class="empty"><b>아직 요청한 뉴스가 없습니다.</b><br>뉴스 목록에서 <b>뉴스 내용 및 인사이트 요청</b>을 누르고 아래 막대의 <b>요청</b>을 누르면 여기에 모입니다.</div>');
  }
  const emptyBox = () => dbMissing
    ? '<div class="empty"><b>저장된 뉴스를 불러올 수 없습니다.</b><br>claude.ai에서 로그인한 상태로 이 페이지를 열면 목록이 보입니다.</div>'
    : !newsLoaded
    ? '<div class="empty">뉴스를 불러오는 중입니다. 날짜별로 제목과 한줄 요약이 여기에 나옵니다.</div>'
    : !fresh().length
    ? '<div class="empty"><b>아직 새 형식으로 정리한 뉴스가 없습니다.</b><br>Claude에게 뉴스 정리를 요청하면 제목과 한줄 요약이 날짜별로 쌓입니다. 예전 요약 카드는 이전 기록에 있습니다.</div>'
    : '<div class="empty"><b>조건에 맞는 뉴스가 없습니다.</b><br><button type="button" class="lnk" data-act="clearall">필터 모두 지우기</button></div>';
  function ensureNewsSkeleton() {
    if ($('nb')) return;
    $('main').innerHTML =
      '<div class="nb" id="nb">' +
        '<p class="guide">더 알고 싶은 뉴스는 <b>뉴스 내용 및 인사이트 요청</b>을 누르고 아래 막대의 <b>요청</b>을 누르세요. 다 본 뉴스는 <b>읽음 처리</b>를 누르세요.</p>' +
        '<div class="sg" role="group" aria-label="출처" id="nb-src"></div>' +
        '<div class="filters" role="group" aria-label="산업" id="nb-ind"></div>' +
        '<div class="tools"><input type="search" id="nq" placeholder="뉴스 검색" aria-label="뉴스 검색" autocomplete="off">' +
          '<button type="button" class="tg" id="nb-unread" data-act="unread" aria-pressed="false">안 읽은 것만</button>' +
          '<button type="button" class="tg" id="nb-ck" data-act="ckonly" aria-pressed="false">요청한 것만</button>' +
          '<span class="bulk" id="nb-bulk"></span></div>' +
      '</div><div id="nb-body"></div>';
    const inp = $('nq'); inp.value = st.q;
    inp.addEventListener('input', () => { st.q = inp.value; clearTimeout(inp._t); inp._t = setTimeout(() => { st.shown = PAGE; st.confirmAll = false; renderNews(); }, 250); });
  }
  function renderNews() {
    ensureNewsSkeleton();
    curRev = '';
    const all = fresh();
    const bySrc = {}; listFiltered('src').forEach(n => { bySrc[n.source] = (bySrc[n.source] || 0) + 1; });
    const srcTotal = listFiltered('src').length;
    const srcs = SRC_ORDER.filter(s => bySrc[s]).concat(Object.keys(bySrc).filter(s => !SRC_ORDER.includes(s)));
    if (st.src !== 'all' && !all.some(n => n.source === st.src)) st.src = 'all';
    $('nb-src').innerHTML = [['all', '전체 ' + srcTotal]].concat(srcs.map(s => [s, s + ' ' + bySrc[s]])).concat(st.src !== 'all' && !bySrc[st.src] ? [[st.src, st.src + ' 0']] : [])
      .map(p => '<button type="button" class="sgb" data-act="src" data-id="' + esc(p[0]) + '" aria-pressed="' + (st.src === p[0]) + '">' + esc(p[1]) + '</button>').join('');
    const base = listFiltered('ind'), cnt = {};
    base.forEach(n => indTags(n).forEach(i => { cnt[i] = (cnt[i] || 0) + 1; }));
    $('nb-ind').innerHTML = [['all', '전체 ' + base.length]].concat(IND_ORDER.filter(k => cnt[k] || k === st.nind).map(k => [k, IND[k] + ' ' + (cnt[k] || 0)]))
      .map(p => '<button type="button" class="chip" data-act="nind" data-id="' + p[0] + '" aria-pressed="' + (st.nind === p[0]) + '">' + esc(p[1]) + '</button>').join('');
    const nq = $('nq'); if (document.activeElement !== nq && nq.value !== st.q) nq.value = st.q;
    const ub = $('nb-unread'); ub.setAttribute('aria-pressed', String(st.unreadOnly)); ub.textContent = '안 읽은 것만 ' + all.filter(n => !reads[n.id]).length;
    const cb = $('nb-ck'); cb.setAttribute('aria-pressed', String(st.ckOnly)); cb.textContent = '요청한 것만 ' + all.filter(n => dreqs[n.id] || dsent[n.id]).length;
    const rows = listFiltered().sort(byList);
    const unreadShown = rows.filter(n => !reads[n.id]).length;
    $('nb-bulk').innerHTML = !unreadShown ? '' : st.confirmAll
      ? '<span>지금 조건에 맞는 ' + unreadShown + '건을 읽음으로 표시할까요?</span><button type="button" class="tg on" data-act="readall-yes">읽음으로 표시</button><button type="button" class="tg" data-act="readall-no">취소</button>'
      : '<button type="button" class="tg" data-act="readall">' + unreadShown + '건 모두 읽음</button>';
    let html;
    if (!rows.length) html = emptyBox();
    else {
      const shown = rows.slice(0, st.shown), days = [];
      shown.forEach(n => { const d = dayOf(n); let g = days[days.length - 1]; if (!g || g.day !== d) days.push(g = { day: d, xs: [] }); g.xs.push(n); });
      const total = {}; rows.forEach(n => { const d = dayOf(n); total[d] = (total[d] || 0) + 1; });
      html = '<div class="days">' + days.map(g => '<section aria-label="' + esc(kday(g.day)) + ' 뉴스"><div class="dayh"><h2>' + esc(kday(g.day) || '날짜 미상') + ' ' + esc(dowOf(g.day)) + '</h2><span>' + total[g.day] + '건</span></div><ul class="news">' + g.xs.map(itemHtml).join('') + '</ul></section>').join('') + '</div>' +
        (rows.length > st.shown ? '<p class="more-row"><button type="button" class="btn ghost" data-act="more">더 보기 (' + Math.min(PAGE, rows.length - st.shown) + '건)</button></p>' : '');
    }
    const body = $('nb-body'), a = document.activeElement, keep = a && body.contains(a) ? [a.dataset.act || a.dataset.ck || '', a.dataset.id || ''] : null;
    const opened = Array.from(body.querySelectorAll('details[open]')).map(d => { const it = d.closest('.item'); return (it ? it.id : '') + '|' + (d.className || '') + '|' + (d.querySelector('summary') || {}).textContent; });
    body.innerHTML = html;
    if (opened.length) body.querySelectorAll('details').forEach(d => { const it = d.closest('.item'); if (opened.includes((it ? it.id : '') + '|' + (d.className || '') + '|' + (d.querySelector('summary') || {}).textContent)) d.open = true; });
    if (keep) { const el = Array.from(body.querySelectorAll('[data-id]')).find(z => (z.dataset.act || z.dataset.ck || '') === keep[0] && z.dataset.id === keep[1]); if (el) el.focus({ preventScroll: true }); }
    renderBar();
  }
  function renderBar() {
    const nd = pendingDetail().length, bar = $('reqbar');
    bar.hidden = st.tab !== 'news' || !nd;
    $('n-detail').textContent = nd;
  }
  // 새 Claude Code 창 열기. 시안(PREVIEW)에서는 실제로 열지 않고 흉내만 냅니다. 실제 연결은 확정 뒤에 넣습니다.
  async function startResearch(list) {
    if (window.PREVIEW) return window.PREVIEW.start(list);
    throw new Error('아직 연결하지 않았습니다.');
  }
  function reqText() {
    const d = pendingDetail().sort(byList), i = pendingInsight().sort(byList), lines = [];
    if (d.length) { lines.push('체크한 뉴스 자세히 정리 요청 (' + d.length + '건)'); d.forEach(n => lines.push('- ' + n.title + ' [' + n.id + ']')); }
    if (i.length) { lines.push('체크한 뉴스 투자 인사이트 요청 (' + i.length + '건)'); i.forEach(n => lines.push('- ' + n.title + ' [' + n.id + ']')); }
    return lines.join('\n');
  }

  /* ── masthead and routing ── */
  function renderNav() {
    ['news', 'ind', 'req'].forEach(t => { const b = $('tab-' + t); if (st.tab === t) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current'); });
    const u = unreadCount();
    $('tab-news').innerHTML = '뉴스' + (u ? '<span class="badge" aria-label="안 읽은 뉴스 ' + u + '건">' + u + '</span>' : '');
    const f = fresh();
    if (f.length) {
      const days = f.map(dayOf).filter(Boolean).sort();
      $('sub').textContent = kday(days[days.length - 1]) + '부터 ' + kday(days[0]) + '까지 거슬러 올라가며 정리한 뉴스 ' + f.length + '건';
    }
  }
  function render() {
    renderNav();
    if (st.tab === 'ind') { const l = sortedInds(); if (l.length && (!st.ind || !chains[st.ind])) st.ind = l[0].id; renderInd(); }
    else if (st.tab === 'req') renderReq();
    else renderNews();
    renderBar();
  }
  const reduce = (() => { try { return matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } })();
  const scrollTo = el => { if (el) el.scrollIntoView({ block: 'start', behavior: reduce ? 'auto' : 'smooth' }); };
  function goNode(ind, node) {
    st.tab = 'ind'; st.ind = ind; st.flowNode = 'all'; st.flowMore = false; save(); render();
    const el = document.getElementById('node-' + ind + '-' + node);
    if (el) { el.classList.add('hl'); const d = el.querySelector('details'); if (d) d.open = true; scrollTo(el); setTimeout(() => el.classList.remove('hl'), 2400); }
  }
  // 산업 한 페이지의 출처 칩에서 뉴스로: 새 형식이면 뉴스 목록, 예전 요약 카드면 이전 기록에서 펼쳐 보여 줍니다.
  function goNews(id) {
    const n = news.find(z => z.id === id);
    if (n && !isFresh(n)) return;
    { st.tab = 'news'; st.src = 'all'; st.nind = 'all'; st.unreadOnly = false; st.ckOnly = false; st.q = ''; st.shown = 1e6; st.confirmAll = false; if (n && hasDetail(n)) st.dopen.add(id); }
    save(); render(); scrollTo(document.getElementById('row-' + id));
  }
  const setDoc = (ref, body) => { if (ref) writing = writing.then(() => ref.set(body)).catch(() => {}); };
  const saveReqs = () => setDoc(reqRef, { ids: Object.assign({}, reqs), done: Object.assign({}, reqDone) });
  const saveDreqs = () => setDoc(dreqRef, { ids: Object.assign({}, dreqs), sent: Object.assign({}, dsent), done: Object.assign({}, dreqDone) });
  const saveReads = () => setDoc(readRef, { ids: Object.assign({}, reads) });
  const rerender = () => { renderNav(); if (st.tab === 'req') renderReq(); else if (st.tab === 'news') renderNews(); renderBar(); };

  document.addEventListener('change', e => {
    const b = e.target; if (!b || !b.dataset || !b.dataset.ck) return;
    const id = b.dataset.id, map = b.dataset.ck === 'insight' ? reqs : dreqs;
    if (b.checked) map[id] = today; else delete map[id];
    if (b.dataset.ck === 'insight') saveReqs(); else saveDreqs();
    $('reqmsg').textContent = ''; rerender();
  });
  // '요청': 체크해 둔 뉴스를 '요청 보냄'으로 바꾸고 새 Claude Code 창(세션)에 조사를 맡깁니다. 실제 시작은 startResearch가 합니다.
  $('reqgo').addEventListener('click', async () => {
    const list = pendingDetail().sort(byList), msg = $('reqmsg'), btn = $('reqgo');
    if (!list.length) return;
    btn.disabled = true; msg.textContent = '새 Claude Code 창을 여는 중입니다.';
    try {
      await startResearch(list);
      const ts = Date.now(); list.forEach(n => { dsent[n.id] = ts; }); saveDreqs();
      msg.textContent = list.length + '건을 새 Claude Code 창에 맡겼습니다. 진행 상황은 요청한 뉴스 탭에서 볼 수 있습니다.';
      rerender();
    } catch (e) { msg.textContent = '새 창을 열지 못했습니다. ' + ((e && e.message) || '') + ' 잠시 뒤 다시 눌러 주세요.'; }
    btn.disabled = false;
  });
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-tab]');
    if (t) { st.tab = t.dataset.tab; save(); render(); return; }
    const b = e.target.closest('[data-act]'); if (!b) return;
    const act = b.dataset.act, id = b.dataset.id;
    if (act === 'ind') { st.tab = 'ind'; st.ind = id; st.flowNode = 'all'; st.flowMore = false; save(); render(); window.scrollTo(0, 0); }
    else if (act === 'node') goNode(b.dataset.ind, id);
    else if (act === 'flownode') { st.flowNode = id; st.flowMore = false; $('flowsBlk').innerHTML = flowsBlock(chains[st.ind]); }
    else if (act === 'flowmore') { st.flowMore = true; $('flowsBlk').innerHTML = flowsBlock(chains[st.ind]); }
    else if (act === 'gonews') goNews(id);
    else if (act === 'src') { st.src = id; st.shown = PAGE; st.confirmAll = false; renderNews(); }
    else if (act === 'nind') { st.nind = st.nind === id ? 'all' : id; st.shown = PAGE; st.confirmAll = false; renderNews(); }
    else if (act === 'unread') { st.unreadOnly = !st.unreadOnly; st.shown = PAGE; st.confirmAll = false; renderNews(); }
    else if (act === 'ckonly') { st.ckOnly = !st.ckOnly; st.shown = PAGE; st.confirmAll = false; renderNews(); }
    else if (act === 'clearall') { st.src = 'all'; st.nind = 'all'; st.unreadOnly = false; st.ckOnly = false; st.q = ''; st.confirmAll = false; renderNews(); }
    else if (act === 'more') { st.shown += PAGE; renderNews(); }
    else if (act === 'dopen') { const was = st.dopen.has(id); if (was) st.dopen.delete(id); else st.dopen.add(id); if (st.tab === 'req') renderReq(); else renderNews(); if (was) scrollTo(document.getElementById((st.tab === 'req' ? 'rq-' : 'row-') + id)); }
    else if (act === 'dreq') { if (dreqs[id]) delete dreqs[id]; else dreqs[id] = today; saveDreqs(); $('reqmsg').textContent = ''; rerender(); }
    else if (act === 'goreq') { st.tab = 'req'; st.dopen.add(id); save(); render(); scrollTo(document.getElementById('rq-' + id)); }
    else if (act === 'open') { if (st.open.has(id)) st.open.delete(id); else st.open.add(id); }
    else if (act === 'req') { if (reqs[id]) delete reqs[id]; else reqs[id] = today; saveReqs(); rerender(); }
    else if (act === 'read') { if (reads[id]) delete reads[id]; else reads[id] = Date.now(); saveReads(); rerender(); }
    else if (act === 'readall') { st.confirmAll = true; renderNews(); }
    else if (act === 'readall-no') { st.confirmAll = false; renderNews(); }
    else if (act === 'readall-yes') { const ts = Date.now(); listFiltered().forEach(n => { if (!reads[n.id]) reads[n.id] = ts; }); st.confirmAll = false; saveReads(); rerender(); }
  });

  render();

  (async () => {
    const status = $('status');
    const say = t => { status.textContent = t; status.hidden = !t; };
    const CL = window.PREVIEW_CLAUDE || window.claude;
    const db = CL && await CL.use('db');
    if (!db) { dbMissing = true; say('이 화면에서는 저장된 데이터를 불러올 수 없습니다. claude.ai에서 로그인한 상태로 열어 주세요.'); render(); return; }
    dbRef = db;
    db.collection('chains').onSnapshot(snap => {
      chains = {}; snap.docs.forEach(d => { chains[d.id] = Object.assign({ id: d.id }, d.data()); });
      say(''); if (st.tab === 'ind') render();
    }, () => { say('산업 데이터를 불러오지 못했습니다. 잠시 뒤 새로고침해 주세요.'); });
    // 뉴스가 1,000건을 넘어도 최근 정리분이 잘리지 않도록 정리한 날 역순으로 읽고, 그 읽기가 안 되면 문서 id순 1,000건으로 읽습니다.
    let newsVia = '', plainOn = false;
    const onNews = via => snap => {
      if (via === 'plain' && newsVia === 'ordered') return;
      newsVia = via; news = snap.docs.map(d => Object.assign({ id: d.id }, d.data())); newsLoaded = true; say(''); render();
    };
    const startPlain = () => { if (plainOn) return; plainOn = true; db.collection('news').limit(1000).onSnapshot(onNews('plain'), () => {}); };
    try { db.collection('news').orderBy('processed', 'desc').limit(1000).onSnapshot(onNews('ordered'), startPlain); } catch (e) { startPlain(); }
    setTimeout(() => { if (!newsLoaded) startPlain(); }, 6000);
    db.doc('meta/cycle').onSnapshot(snap => {
      const d = snap.exists ? snap.data() : null;
      if (d && Array.isArray(d.stages) && d.stages.length === 8) { stages = d.stages; cycUpdated = d.updated || ''; if (st.tab === 'ind') render(); }
    }, () => {});
    try {
      const user = await CL.use('user');
      const uid = user && await user.id();
      if (uid) {
        const watch = (name, fn) => { const ref = db.doc('data/users/' + uid + '/' + name); ref.onSnapshot(snap => { fn(snap.exists ? (snap.data() || {}) : {}); rerender(); }, () => {}); return ref; };
        readRef = watch('reads', d => { if (d.ids) reads = Object.assign({}, d.ids); });
        reqRef = watch('insightReq', d => { reqs = Object.assign({}, d.ids || {}); reqDone = Object.assign({}, d.done || {}); });
        dreqRef = watch('detailReq', d => { dreqs = Object.assign({}, d.ids || {}); dreqDone = Object.assign({}, d.done || {}); dsent = Object.assign({}, d.sent || {}); });
      }
    } catch (e) {}
  })();
})();
