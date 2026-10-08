import sys
old = open(sys.argv[1], encoding='utf-8').read().split('\n')
L = lambda a, b: '\n'.join(old[a-1:b])
P = lambda n: open(n, encoding='utf-8').read().rstrip('\n')
cardbox = L(755, 784).replace("data-act=\"open\" data-id=\"' + esc(n.id) + '\" data-fk=\"c:' + esc(n.id) + '\">접기", "data-act=\"open\" data-id=\"' + esc(n.id) + '\">접기")
assert cardbox != L(755, 784)
out = ['<title>다운턴 뉴스 선별 데스크</title>',
 '<link rel="preconnect" href="https://fonts.googleapis.com">',
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&display=swap">',
 '<style>', L(7, 7), P('new.css'), '', L(258, 374), P('tail.css'), '</style>', '', P('body.html'), '',
 '<script>', '(() => {', L(475, 490), P('js1.js'), '', L(524, 596), '', L(687, 752), '', cardbox, '', L(1042, 1076), P('js2.js'), '</script>', '']
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out))
print('built', sum(len(x) for x in out))
