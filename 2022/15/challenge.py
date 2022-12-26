import re
xPos = set()
yLine = 2000000
with open("data.txt") as fp: 
    lines = fp.read().splitlines()  
    for line in lines[:]:
        row = re.sub("[^0-9=-]","", line)[1:].split('=')
        sx,sy,bx,by = row
        sx = int(sx); sy = int(sy); bx = int(bx); by = int(by)
        myBDist = abs(bx-sx)+abs(by-sy)
        myYDist = abs(yLine-sy)
        if myYDist <= myBDist:
            for i in range (sx-(myBDist-myYDist),sx+(myBDist-myYDist)):
                xPos.add(i)
print("Def not beacon Pos: ", len(xPos))

import re
locs=[list(map(int,re.findall(r'(-?[0-9]+)',y)))for y in open("data.txt").read().split('\n')]
dists=[abs(l[0]-l[2])+abs(l[1]-l[3]) for l in locs]
b,n=4000000+1,0
found=False
for y in range(b):
    segs=[]
    for i in range(len(locs)):
        l,d=locs[i],dists[i]
        h=abs(y-l[1])
        if h<=d:
            segs.append([max(0,l[0]-(d-h)),min(l[0]+(d-h),b)])
    segs=sorted(segs)
    curmax=segs[0][1]
    for i in range(len(segs)-1):
        curmax=max(curmax,segs[i][1])
        if curmax+1<segs[i+1][0]:
            print(4000000*(segs[i][1]+1)+y)
            found=True
    if found:
        break