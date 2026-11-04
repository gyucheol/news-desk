# plan_sleep.py -> lines.json(자막 줄: 글자, 자리, 화면, 읽은 말), units.json(음절 맞춤용 읽은 말). 04편 lines_full.json과 같은 꼴.
import json, sys
sys.path.insert(0, '.')
from plan_sleep import SECTIONS
KIND = {'b': 'bottom', 'c': 'center', 'i': 'italic'}
lines, units = [], []
n = 0; si = 0
for sec in SECTIONS:
    for sent in sec['sents']:
        si += 1
        for pi, p in enumerate(sent):
            n += 1
            text, pos, vis = p[0], p[1], p[2]
            say = p[3] if len(p) > 3 else text
            vid = f'V{n:03d}'
            lines.append({'id': vid, 'sent': si, 'pi': pi, 'kind': KIND[pos], 'pos': pos, 'text': text,
                          'spoken': say, 'say': say, 'lead': '', 'vis': vis})
            units.append({'id': vid, 'text': say})
json.dump(lines, open('lines.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(units, open('units.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(lines), 'lines,', si, 'sentences')
