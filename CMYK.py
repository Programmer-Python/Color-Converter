from helper import CMYK

def cr(n):
    from math import ceil,floor
    return floor(n) if (n-floor(n))<0.5 else ceil(n)

def CMYK2RGB(*cmyk):
    check=CMYK.iscmyk(*cmyk)
    if check:
        check=[float(v/100) for v in check]
        k=check.pop()
        r,g,b=[cr(255*(1-v)*(1-k)) for v in check]
        return [r,g,b]
def CMYK2HEX(*cmyk):
    check=CMYK.iscmyk(*cmyk)
    if check:
        r,g,b=CMYK2RGB(check)
        hex='#%02x%02x%02x'%(r,g,b)
        return hex
def CMYK2HSL(*cmyk):
    check=CMYK.iscmyk(*cmyk)
    if check:
        h=s=l=0
        r,g,b=[float(v/255) for v in CMYK2RGB(check)]
        maxi,mini=max(r,g,b),min(r,g,b)
        l=(maxi+mini)/2
        diff=maxi-mini
        if diff==0:
            h=s=0
            return [h,s,l]
        else:s=(maxi-mini)/(1-abs(2*l-1))

        if maxi==r:
            h=((g-b)/(maxi-mini))%6
        elif maxi==g:
            h=((b-r)/(maxi-mini))+2
        elif maxi==b:
            h=((r-g)/(maxi-mini))+4
        h=cr(h*60)
        s,l=[float(format(v,'.4f')) for v in [s,l]]
        return [h,s,l]
def CMYK2HSV(*cmyk):
    check=CMYK.iscmyk(*cmyk)
    if check:
        h=s=v=0
        r,g,b=[float(w/255) for w in CMYK2RGB(check)]
        maxi,mini=max(r,g,b),min(r,g,b)
        diff=maxi-mini
        if diff==0:
            return[h,s,maxi]
        s=0 if maxi==0 else (maxi-mini)/maxi
        if maxi==r:
            h=((g-b)/(maxi-mini))%6
        elif maxi==g:
            h=(b-r)/(maxi-mini)+2
        elif maxi==b:
            h=(r-g)/(maxi-mini)+4
        h=cr(h*60)
        v=maxi
        s,v=[float(format(w,'.4f')) for w in [s,v]]
        return [h,s,v]