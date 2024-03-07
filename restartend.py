# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys
string=sys.stdin
s=[]
for line in string:
    s.append(line.rstrip())
c=0
final=[]
for i in range(len(s[0])):
    str2=s[0][i:]
    m=re.search(s[1],str2)
    if m is not None:
        start=m.start()+c
        end=m.end()+c-1
        final.append((start,end))
    c+=1
if final:
    final=set(final)
    for j in final:
        print(j)
else:
    final.append((-1,-1))
    print(final[0])
