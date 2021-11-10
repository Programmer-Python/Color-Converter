from helper import HSL

def cr(n):
    from math import ceil,floor
    return floor(n) if (n-floor(n))<0.5 else ceil(n)

def HSL2RGB(*hsl):
    check=HSL.ishsl(*hsl)
    if check:
        r=g=b=0
        tl=HSL.typehsl(check)
        A=float(check.pop()) if len(check)==4 else False
        h,s,l=[v for v in check]
        s,l=s if s<=1 else s/100,l if l<=1 else l/100
        c=(1-abs((2*l)-1))*s
        x=c*(1-abs((h/60)%2-1))
        m=l-(c/2)
        if h>=0 and h<60:
            r,g,b=c,x,0
        elif h>=60 and  h<120:
            r,g,b=x,c,0
        elif h>=120 and  h<180:
            r,g,b=0,c,x
        elif h>=180 and  h<240:
            r,g,b=0,x,c
        elif h>=240 and  h<300:
            r,g,b=x,0,c
        elif h>=300 and  h<360:
            r,g,b=c,0,x
        R,G,B=(r+m)*255,(g+m)*255,(b+m)*255
        R,G,B=[cr(v) for v in [R,G,B]]
        return [R,G,B,A] if tl=='hsla' else [R,G,B]


def HSL2HSV(*hsl):
    check=HSL.ishsl(*hsl)
    h=s=v=0
    if check:
        A=float(check.pop()) if HSL.typehsl(check)=='hsla' else False
        h,s,l=[*check]
        s,l=s if s<=1 else s/100,l if l<=1 else l/100
        h=h
        s*=l if check[0]<.5 else 1-l
        v=l+s
        s=2*s/(l+s)
        return [h,s,v,A] if A else [h,s,v]

def HSL2HEX(*hsl):
    check=HSL.ishsl(*hsl)
    if check:
        rgb=HSL2RGB(check)
        A=rgb.pop() if HSL.typehsl(check)=='hsla' else False
        hex='#'
        hex+='%02x%02x%02x'%tuple(rgb)
        hex=hex+'%02x'%(cr(float(A)*255)) if A else hex
        return hex
    else:
        return False

def HSL2CMYK(*hsl):
    check=HSL.ishsl(*hsl)
    if check:
        rgb=HSL2RGB(check)
        if HSL.typehsl(check)=='hsla':check.pop()
        c=m=y=k=0
        R,G,B=[v/255 for v in rgb]
        k=1-max(R,G,B)
        c,m,y=[(1-v-k)/(1-k) for v in [R,G,B]]
        c,m,y,k=[float(format(v,'.4f')) for v in [c,m,y,k]]
        return [c,m,y,k]
    else:
        return False
print(HSL2CMYK(50,100,50))