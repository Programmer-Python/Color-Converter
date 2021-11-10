import re
cmykString=r'^cmyk\((\-?\d+)%\,(\-?\d+)%?\,(\-?\d+)%\,(\-?\d+)%\)$'

def hasall(obj,*args):
    """check if given object has all property name or not"""
    return False if False in [True if i in obj else False for i in args] else True
def gio(obj,*args):
    "return the object keys in order as args"
    return [obj.get(i) for i in args] if hasall(obj,*args) else False
def iscmyk(*cmyk):
    rl=len(cmyk)
    if rl==1:
        arg=cmyk[0]
        if isinstance(arg,dict):
            a=hasall(arg,'c','m','y','k')
            values = gio(arg,'c','m','y','k') 
            return [int(v) for v in values] if a else False
        elif isinstance(arg,str):
            values=re.findall(cmykString,arg)
            return [float(v) for v in values[0]] if values else False
        elif isinstance(arg,(list,tuple)):
            return [*arg] if  len(arg) ==4 else False
    elif rl==4:
        return [*cmyk]
    return False