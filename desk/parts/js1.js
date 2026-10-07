  const IND = { macro: '매크로', semis: '반도체·AI 투자', power: '전력·재생에너지', gas: '가스·LNG', coal: '석탄', uranium: '원전·우라늄', drilling: '시추·해양', petchem: '석유화학·정유', jpins: '일본 보험·금융', beauty: '화장품' };
  const IND_ORDER = ['semis', 'macro', 'power', 'gas', 'petchem', 'uranium', 'drilling', 'coal', 'jpins', 'beauty'];
  const SRC_ORDER = ['블룸버그', '로이터', '텔레그램'];
  const PAGE = 80;
  const coarse = (() => { try { return matchMedia('(pointer:coarse)').matches; } catch (e) { return false; } })();

  let stages = FALLBACK_STAGES;
  let cycUpdated = '';
  let chains = {};
  let news = [], newsLoaded = false, dbMissing = false;
  let reads = {};
  let readRef = null, writing = Promise.resolve();
  let archive = null, archLoading = false, dbRef = null;
  let reqs = {}, reqDone = {}, reqRef = null;      // 투자 인사이트 요청
  let dreqs = {}, dreqDone = {}, dreqRef = null;   // 자세히 요청
  const st = {
    tab: 'news', src: 'all', nind: 'all', unreadOnly: false, ckOnly: false, q: '', shown: PAGE, confirmAll: false, dopen: new Set(),
    ind: null, flowNode: 'all', flowMore: false, aq: '', archMode: 'cards', archMore: false, cq: '', cardsMore: false, open: new Set()
  };
  try {
    const s = JSON.parse(localStorage.getItem('v6state') || localStorage.getItem('v5state') || '{}');
    if (['news', 'ind', 'arch'].includes(s.tab)) st.tab = s.tab;
    if (s.ind) st.ind = s.ind;
  } catch (e) {}
  const h = (location.hash || '').replace('#', '');
  if (h === 'news' || h === 'arch') st.tab = h;
  else if (/^[a-z]+$/.test(h)) { st.tab = 'ind'; st.ind = h; }
  const save = () => { try { localStorage.setItem('v6state', JSON.stringify({ tab: st.tab, ind: st.ind })); } catch (e) {} };
