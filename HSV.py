from helper import HSV

def cr(n):
    from math import ceil,floor
    return floor(n) if (n-floor(n))<0.5 else ceil(n)


def HSV2RGB(*hsv):
    check=HSV.ishsv(*hsv)
    if check:
        A=check.pop() if HSV.typehsv(check)=='hsva' else False
        h,s,v=check
        s,v=[a/100 if a>=0 and a<=100 else a for a in [s,v]]
        R=G=B=0
        C=v*s
        X=C*(1-abs(h/60%2-1))
        m=v-C
        if h>=0 and h<60:
            R,G=C,X
        if h>=60 and h<120:
            R,G=X,C
        if h>=120 and h<180:
            G,B=C,X
        if h>=180 and h<240:
            G,B=X,C
        if h>=240 and h<300:
            R,B=X,C
        if h>=240 and h<360:
            R,B=C,X
        r,g,b=[(vv+m)*255 for vv in [R,G,B]]
        r,g,b=[cr(vv) for vv in [r,g,b]]
        return [r,g,b,A] if A else [r,g,b]
    else:return False
# print(HSV2RGB('hsv(20,25%,50%)'))
def HSV2HSL(*hsv):
    c=HSV.ishsv(*hsv)
    if c:
        A=c.pop() if HSV.typehsv(c)=='hsva' else False
        h,s,v=c
        s,v=[a/100 if a>0 and a<100 else a for a in [s,v]]
        L=v*(1-(s/2))
        S = 0 if (L==0 or L==1) else (v-L)/min(L,1-L)
        S,L=[float(format(vv,'.2f')) for vv in [S,L]]
        return [h,S,L,A] if A else [h,S,L]
    else:return False
# print(HSV2HSL(20,50,50))
def HSV2CMYK(*hsv):
    ch=HSV.ishsv(*hsv)
    if ch:
        if HSV.typehsv(ch)=='hsva':ch.pop()
        r,g,b=[v/255 for v in HSV2RGB(ch)]
        k=1-max(r,g,b)
        c,m,y=[(1-v-k)/(1-k) for v in [r,g,b]]
        c,m,y,k=[float(format(v,'.2f')) for v in [c,m,y,k]]
        return [c,m,y,k]
    else:return False
# print(HSV2CMYK(50,100,10))
def HSV2HEX(*hsv):
    check=HSV.ishsv(*hsv)
    if check:
        rgb=HSV2RGB(check)
        A=rgb.pop() if HSV.typehsv(check)=='hsva' else False
        hex='#'
        hex+='%02x%02x%02x'%tuple(rgb)
        hex=hex+'%02x'%(cr(float(A)*255)) if A else hex
        return hex
    else:
        return False