import re
from helper import RGB

def cr(n):
    from math import ceil,floor
    return floor(n) if (n-floor(n))<0.5 else ceil(n)

def RGB2HEX(*rgb):
    check,A,hex=RGB.isrgb(*rgb),False,'#'
    if check:
        if len(check) ==4:
            A=check[3]
            check=check[0:len(check)-1]
        for i in check:
            hex+='%02x'%int(i)
        if A:
            hex+='%02x'%(int(float(A)*255))
        return hex
    else:
        return False
def RGB2HSV(*rgb):
    check=RGB.isrgb(*rgb)
    if check:
        h=s=v=0
        tr=RGB.typergb(check)
        A=float(check.pop()) if len(check)==4 else False
        check=[0 if v<0 else 255 if v>255 else v for v in check]
        r,g,b=[int(v)/255 for v in check]
        maxi,mini=max(r,g,b),min(r,g,b)
        if maxi==mini:
            h=s=0
            v=maxi
            return [h,s,v,A] if tr=='rgba' else [h,s,v]
        s=0 if maxi==0 else (maxi-mini)/maxi
        if maxi==r:
            h=((g-b)/(maxi-mini))%6
        elif maxi==g:
            h=(b-r)/(maxi-mini)+2
        elif maxi==b:
            h=(r-g)/(maxi-mini)+4
        h=cr(h*60)
        v=maxi
        return [h,s,v,A] if tr=='rgba' else [h,s,v]
    else:return False


def RGB2HSL(*rgb):
    check=RGB.isrgb(*rgb)
    if check:
        h=s=l=0
        tr=RGB.typergb(check)
        A=float(check.pop()) if tr=='rgba' else False
        check=[0 if v<0 else 255 if v>255 else v for v in check]
        r,g,b=[int(v)/255 for v in check]
        maxi,mini=max(r,g,b),min(r,g,b)
        l=(maxi+mini)/2
        if maxi==mini:
            h=s=0
            return [h,s,l,A] if tr=='rgba' else [h,s,l]
        else:
            s=(maxi-mini)/(1-abs(2*l-1))
        if maxi==r:
            h=((g-b)/(maxi-mini))%6
        if maxi==g:
            h=(b-r)/(maxi-mini)+2
        if maxi==b:
            h=(r-g)/(maxi-mini)+4
        h=cr(h*60)
        return [h,s,l,A] if tr=='rgba' else [h,s,l]
    else:return False


def RGB2CMYK(*rgb):
    check=RGB.isrgb(*rgb)
    if check:
        c=m=y=k=0
        check=check.pop() and check if len(check)==4 else [0 if v<0 else 255 if v>255 else v for v in check]
        r,g,b=[v/255 for v in check]
        k=1-max(r,g,b)
        c,m,y=[float(format((1-v-k)/(1-k),'.3f')) for v in [r,g,b]]
        return [float(format(v,'.2f')) for v in [c,m,y,k]]
    else:return False


def RGB2XYZ(*rgb):
    return '**under construction**'
RGB2XYZ(255,255,255)
def RGB2LAB(*rgb):
    return '**under construction**'