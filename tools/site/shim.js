// Claude 밖(일반 웹사이트)에서 데스크 페이지를 열 때 쓰는 대체 연결.
// 데스크 페이지는 window.PREVIEW_CLAUDE가 있으면 window.claude 대신 이것을 씁니다.
// 데이터는 같은 폴더의 data/*.json(회차 저장 뒤 tools/site/build.py가 만듦)에서 읽기만 합니다.
// 사용자 정보가 없으므로 읽음 표시는 이 브라우저(localStorage)에만 남습니다.
(() => {
  const V = (window.SITE_BUILD || '') + '';
  const load = name => fetch('data/' + name + '.json?v=' + encodeURIComponent(V), { cache: 'no-cache' }).then(r => {
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return r.json();
  });
  // 데스크 읽음 기록 사본(data/reads.json)을 이 브라우저의 읽음 기록(deskReads:anon)에 합칩니다. 사본이 바뀔 때(asof)마다 한 번.
  const seed = fetch('data/reads.json?v=' + encodeURIComponent(V), { cache: 'no-cache' }).then(r => r.ok ? r.json() : null).then(s => {
    if (!s || !s.ids) return;
    try {
      if (localStorage.getItem('siteReadsAsof') === s.asof) return;
      const cur = JSON.parse(localStorage.getItem('deskReads:anon') || '{}') || {};
      Object.keys(s.ids).forEach(k => { if (!(cur[k] >= s.ids[k])) cur[k] = s.ids[k]; });
      localStorage.setItem('deskReads:anon', JSON.stringify(cur));
      localStorage.setItem('siteReadsAsof', s.asof);
    } catch (e) {}
  }).catch(() => {});
  const snapOf = arr => ({ docs: arr.map(d => ({ id: d.id, data: () => d })) });
  const query = name => {
    const q = {
      orderBy: () => q, limit: () => q, where: () => q,
      get: () => (name === 'news' || name === 'chains' ? load(name) : Promise.resolve([])).then(snapOf),
      onSnapshot: (ok, err) => { q.get().then(ok, e => err && err(e)); return () => {}; }
    };
    return q;
  };
  const doc = path => ({
    onSnapshot: (ok, err) => {
      if (path === 'meta/cycle') load('cycle').then(d => ok({ exists: !!d, data: () => d }), e => err && err(e));
      else ok({ exists: false, data: () => ({}) });
      return () => {};
    },
    set: () => Promise.resolve(), update: () => Promise.resolve()
  });
  const db = { collection: query, doc };
  window.PREVIEW_CLAUDE = {
    use: async name => { await seed; return name === 'db' ? db : name === 'user' ? { id: async () => null } : null; }
  };
})();
