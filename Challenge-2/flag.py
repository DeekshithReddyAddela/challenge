file = open("ping", "r")
l=""
for line in file:
    dir=line[line.find('ttl=')+4:line.find('(',line.find('ttl=')+4)].strip()
    l=l+dir
n=3
L=[int(l[i:i+n]) for i in range(0, len(l), n)]
print(L)
print(''.join(map(chr,L)))
