import re

hslString=r'^hsl\((\d+)\,(\d+)%\,(\d+)%\)$'
hslaString=r'^hsla\((\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHslaString=r'^hsl\((\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHslString=r'^hsla\((\d+)\,(\d+)%\,(\d+)%\)$'
def hasall(obj,*args):
    return False if False in [True if i in obj else False for i in args] else True
def gio(obj,*args):
    all=hasall(obj,*args)
    vals=[]
    if all:
        for i in args:
            vals.append(obj.get(i))
    return vals
def ishsl(*hsl):
    rl=len(hsl)
    if rl==1:
        arg=hsl[0]
        if isinstance(arg,dict):
            a=hasall(arg,'h','s','l','a') or hasall(arg,'h','s','l')
            values = gio(arg,'h','s','l','a') or gio(arg,'h','s','l') 
            return [int(v) for v in values] if a else False
        elif isinstance(arg,str):
            values=re.findall(hslaString,arg) or re.findall(hslString,arg) or re.findall(wrongHslaString,arg) or re.findall(wrongHslString,arg)
            return [float(v) for v in values[0]] if values else False
        elif isinstance(arg,(list,tuple)):
            return [*arg] if len(arg) in [3,4] else False
    elif rl in [3,4]:
        return [*hsl]
    return False
def typehsl(*hsl):
    check=ishsl(*hsl)
    if check:
        return 'hsla' if len(check)==4 else 'hsl'
    else:
        return False