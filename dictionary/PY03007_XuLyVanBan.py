import re
doc = ''
while True:
    try:
        doc += input()
    except:
        break
sen = re.split('[.?!]', doc)
for s in sen:
    if len(s) == 0:
        continue
    s = s.lower().split()
    s[0] = s[0][:1].upper() + s[0][1:]
    print(' '.join(s))