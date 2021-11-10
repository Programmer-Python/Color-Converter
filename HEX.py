import re
from helper import HEX
def HEX2RGB(hex,inthe=[]):
    outputin={} if inthe=='dict' else []
    c=HEX.ishex(hex)
    l=HEX.hexlen(hex) if c else False
    hex=hex.replace('#','')
    rgb=[]
    if l and (l in [6,8,3]):
        if l==3:
            for i in range(0,l,1):
                rgb.append(int(hex[i:i+1]*2,16))
        else:
            for i in range(0,l,2):
                rgb.append(int(hex[i:i+2],16))
            if len(rgb)==4:
                rgb[len(rgb)-1]=float(format(rgb[len(rgb)-1]/255,'.2f'))
    if isinstance(outputin,dict):
        outputin['r']=rgb[0]
        outputin['g']=rgb[1]
        outputin['b']=rgb[2]
        if len(rgb)==4:
            outputin['a']=rgb[3]
        return outputin
    elif isinstance(outputin,list):
        return rgb
# print(HEX2RGB('#f07839'))
# print(HEX2RGB("#def")) ->  221, 238, 255
def HEX2HSL(*args):
    hue=sat=light=0
    rv=HEX2RGB(args[0])
    hasA=rv[3] if len(rv)==4 else False
    rv=rv[0:3] if bool(hasA) else rv
    r,g,b=(v/255 for v in rv)
    minimum=min(r,g,b)
    maximum=max(r,g,b)
    chroma=maximum-minimum
    light=float(format((maximum+minimum)/2,'.2f'))
    if minimum==maximum:
        hue=sat=0
        return {'h':hue,'s':sat,'l':light}
    if light<=0.5:
        sat=float(format((maximum-minimum)/(maximum+minimum),'.2f'))
    else:
        sat=float(format((maximum-minimum)/(2-maximum-minimum),'.2f'))
    if maximum==r:
        hue=(r-b)/(maximum-minimum)
    if maximum==g:
        hue=2+(b-r)/(maximum-minimum)
    if maximum==b:
        hue=4+(r-g)/(maximum-minimum)
    hue=round(hue*60)
    return [hue,sat,light,hasA] if not isinstance(hasA,bool) else [hue,sat,light]
    # return [hue,sat*100,light*100,hasA] if isinstance(hasA,(int,float)) else [hue,sat*100,light*100]
def HEX2HSV(hex):
    hv=HEX2HSL(hex)
    hue=sat=value=0
    hue=hv[0]
    value=hv[2]+hv[1]*min(hv[2],1-hv[2])
    if value==0:
        sat=0
    else:
        sat=2*(1-(hv[2]/value))
    # print(value,sat,hue)
    return [hue,sat,value,hv[3]] if len(hv)==4 else [hue,sat,value]
# print(HEX2RGB('#F09639'))