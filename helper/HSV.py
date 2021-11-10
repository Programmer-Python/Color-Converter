import re

hsvString=r'^hsv\((\-?\d+)\,(\d+)%\,(\d+)%\)$'
hsvaString=r'^hsva\((\-?\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHsvaString=r'^hsv\((\-?\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHsvString=r'^hsva\((\-?\d+)\,(\d+)%\,(\d+)%\)$'
def hasall(obj,*args):
    return False if False in [True if i in obj else False for i in args] else True
def gio(obj,*args):
    all=hasall(obj,*args)
    vals=[]
    if all:
        for i in args:
            vals.append(obj.get(i))
    return vals
def ishsv(*hsv):
    rl=len(hsv)
    if rl==1:
        arg=hsv[0]
        if isinstance(arg,dict):
            a=hasall(arg,'h','s','v','a') or hasall(arg,'h','s','v')
            values = gio(arg,'h','s','v','a') or gio(arg,'h','s','v')
            return [int(v) for v in values] if a else False
        elif isinstance(arg,str):
            values=re.findall(hsvaString,arg) or re.findall(hsvString,arg) or re.findall(wrongHsvaString,arg) or re.findall(wrongHsvString,arg)
            return [float(v) for v in values[0]] if values else False
        elif isinstance(arg,(list,tuple)):
            return [*arg] if len(arg) in [3,4] else False
    elif rl in [3,4]:
        return [*hsv]
    return False
def typehsv(*hsv):
    check=ishsv(*hsv)
    if check:
        return 'hsva' if len(check)==4 else 'hsv'
    else:
        return False