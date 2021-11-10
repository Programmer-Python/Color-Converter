import re
rgbString=r'^rgb\(\s*?(\-?\d+)\s*?\,\s*?(\-?\d+)\s*?\,\s*?(\-?\d+)\s*?\)$'
rgbaString=r'^rgba\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,(\-?0?\.?\d+)\)$'
wrongRgbaString=r'^rgba\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\)$'
wrongRgbString=r'^rgb\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,(\-?0?\.?\d+)\)$'
# sampleRgbString='rgb(150,150,252)'
# compiled=re.compile(rgbString).findall(sampleRgbString)
def hasall(obj,*args):
    """check if given object has all property name or not"""
    return False if False in [True if i in obj else False for i in args] else True
def getinorder(obj,*args):
    all=hasall(obj,*args)
    vals=[]
    if all:
        for i in args:
            vals.append(obj.get(i))
    return vals or False
def isrgb(*rgb):
    rl=len(rgb)
    if rl==1:
        arg=rgb[0]
        if isinstance(arg,dict):
            a=hasall(arg,'r','g','b','a') or hasall(arg,'r','g','b')
            values = getinorder(arg,'r','g','b','a') or getinorder(arg,'r','g','b') 
            return [int(v) for v in values] if a else False
        elif isinstance(arg,str):
            values=re.findall(rgbaString,arg) or re.findall(rgbString,arg) or re.findall(wrongRgbaString,arg) or re.findall(wrongRgbString,arg)
            return [float(v) for v in values[0]] if values else False
        elif isinstance(arg,(list,tuple)):
            return [*arg] if  len(arg) in [3,4] else False
    elif rl in [3,4]:
        return [*rgb]
    return False
def typergb(*rgb):
    check=isrgb(*rgb)
    if check:
        rl=len(check)
        return 'rgba' if rl==4 else 'rgb' if rl==3 else False
        # if rl==1:
        #     arg=rgb[0]
        #     if isinstance(arg,dict):
        #         rgba=hasall(arg,'r','g','b','a')
        #         return 'rgba' if rgba else 'rgb' if hasall(arg,'r','g','b') else False
        #     elif isinstance(arg,str):
        #             if re.match(wrongRgbaString,arg):
        #                 return 'rgb'
        #             elif re.match(wrongRgbString,arg):
        #                 return 'rgba'
        #             return 'rgba' if bool(re.match(rgbaString,arg)) else 'rgb' if bool(re.match(rgbString,arg)) else False
        #     elif isinstance(arg,(list,tuple)):
        #         return 'rgba' if len(arg)==4 else 'rgb' if len(arg)==3 else False
        # elif rl in [3,4]:
        #     return 'rgba' if rl==4 else 'rgb' if rl==3 else False

# deprecated method current is method : isrgb
def rgbtoarray(*rgb):
    check=isrgb(*rgb)
    if check:
        rl=len(rgb)
        if rl==1:
            arg=rgb[0]
            if isinstance(arg,dict):
                return [arg['r'],arg['g'],arg['b'],arg['a']] if 'a' in arg else [arg['r'],arg['g'],arg['b']]
            elif isinstance(arg,str):
                values=bool(re.match(rgbaString,arg)) or bool(re.match(rgbString,arg))
                if values:
                    pass
                else:
                    if re.match(wrongRgbaString,arg):
                        arg=arg.replace('rgba','rgb')
                    elif re.match(wrongRgbString,arg):
                        arg=arg.replace('rgb','rgba')
                return [int(v) for v in re.sub(r'^rgba?\(','',arg).replace(')','').split(',')]
            elif isinstance(arg,(list,tuple)):
                return [int(a) for a in arg]
        elif rl in [3,4]:
            return [int(a) for a in rgb]
# print(rgbtoarray('rgba(255,255,255)'))