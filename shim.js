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
    use: async name => (name === 'db' ? db : name === 'user' ? { id: async () => null } : null)
  };
})();
