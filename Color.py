import re
# Colors
colors={"indian red":"#B0171F","crimson":"#DC143C","lightpink":"#FFB6C1","lightpink 1":"#FFAEB9","lightpink 2":"#EEA2AD","lightpink 3":"#CD8C95","lightpink 4":"#8B5F65","pink":"#FFC0CB","pink 2":"#EEA9B8","pink 3":"#CD919E","pink 4":"#8B636C","palevioletred":"#DB7093","palevioletred 1":"#FF82AB","palevioletred 2":"#EE799F","palevioletred 3":"#CD6889","palevioletred 4":"#8B475D","lavenderblush":"#FFF0F5","lavenderblush 2":"#EEE0E5","lavenderblush 3":"#CDC1C5","lavenderblush 4":"#8B8386","violetred 1":"#FF3E96","violetred 2":"#EE3A8C","violetred 3":"#CD3278","violetred 4":"#8B2252","hotpink":"#FF69B4","hotpink 1":"#FF6EB4","hotpink 2":"#EE6AA7","hotpink 3":"#CD6090","hotpink 4":"#8B3A62","raspberry":"#872657","deeppink":"#FF1493","deeppink 2":"#EE1289","deeppink 3":"#CD1076","deeppink 4":"#8B0A50","maroon 1":"#FF34B3","maroon 2":"#EE30A7","maroon 3":"#CD2990","maroon 4":"#8B1C62","mediumvioletred":"#C71585","violetred":"#D02090","orchid":"#DA70D6","orchid 1":"#FF83FA","orchid 2":"#EE7AE9","orchid 3":"#CD69C9","orchid 4":"#8B4789","thistle":"#D8BFD8","thistle 1":"#FFE1FF","thistle 2":"#EED2EE","thistle 3":"#CDB5CD","thistle 4":"#8B7B8B","plum 1":"#FFBBFF","plum 2":"#EEAEEE","plum 3":"#CD96CD","plum 4":"#8B668B","plum":"#DDA0DD","violet":"#EE82EE","magenta":"#FF00FF","fuchsia":"#FF00FF","magenta 2":"#EE00EE","magenta 3":"#CD00CD","magenta 4":"#8B008B","darkmagenta":"#8B008B","purple":"#800080","mediumorchid":"#BA55D3","mediumorchid 1":"#E066FF","mediumorchid 2":"#D15FEE","mediumorchid 3":"#B452CD","mediumorchid 4":"#7A378B","darkviolet":"#9400D3","darkorchid":"#9932CC","darkorchid 1":"#BF3EFF","darkorchid 2":"#B23AEE","darkorchid 3":"#9A32CD","darkorchid 4":"#68228B","indigo":"#4B0082","blueviolet":"#8A2BE2","purple 1":"#9B30FF","purple 2":"#912CEE","purple 3":"#7D26CD","purple 4":"#551A8B","mediumpurple":"#9370DB","mediumpurple 1":"#AB82FF","mediumpurple 2":"#9F79EE","mediumpurple 3":"#8968CD","mediumpurple 4":"#5D478B","darkslateblue":"#483D8B","lightslateblue":"#8470FF","mediumslateblue":"#7B68EE","slateblue":"#6A5ACD","slateblue 1":"#836FFF","slateblue 2":"#7A67EE","slateblue 3":"#6959CD","slateblue 4":"#473C8B","ghostwhite":"#F8F8FF","lavender":"#E6E6FA","blue":"#0000FF","blue 2":"#0000EE","blue 3":"#0000CD","mediumblue":"#0000CD","blue 4":"#00008B","darkblue":"#00008B","navy":"#000080","midnightblue":"#191970","cobalt":"#3D59AB","royalblue":"#4169E1","royalblue 1":"#4876FF","royalblue 2":"#436EEE","royalblue 3":"#3A5FCD","royalblue 4":"#27408B","cornflowerblue":"#6495ED","lightsteelblue":"#B0C4DE","lightsteelblue 1":"#CAE1FF","lightsteelblue 2":"#BCD2EE","lightsteelblue 3":"#A2B5CD","lightsteelblue 4":"#6E7B8B","lightslategray":"#778899","slategray":"#708090","slategray 1":"#C6E2FF","slategray 2":"#B9D3EE","slategray 3":"#9FB6CD","slategray 4":"#6C7B8B","dodgerblue":"#1E90FF","dodgerblue 2":"#1C86EE","dodgerblue 3":"#1874CD","dodgerblue 4":"#104E8B","aliceblue":"#F0F8FF","steelblue":"#4682B4","steelblue 1":"#63B8FF","steelblue 2":"#5CACEE","steelblue 3":"#4F94CD","steelblue 4":"#36648B","lightskyblue":"#87CEFA","lightskyblue 1":"#B0E2FF","lightskyblue 2":"#A4D3EE","lightskyblue 3":"#8DB6CD","lightskyblue 4":"#607B8B","skyblue 1":"#87CEFF","skyblue 2":"#7EC0EE","skyblue 3":"#6CA6CD","skyblue 4":"#4A708B","skyblue":"#87CEEB","deepskyblue":"#00BFFF","deepskyblue 2":"#00B2EE","deepskyblue 3":"#009ACD","deepskyblue 4":"#00688B","peacock":"#33A1C9","lightblue":"#ADD8E6","lightblue 1":"#BFEFFF","lightblue 2":"#B2DFEE","lightblue 3":"#9AC0CD","lightblue 4":"#68838B","powderblue":"#B0E0E6","cadetblue 1":"#98F5FF","cadetblue 2":"#8EE5EE","cadetblue 3":"#7AC5CD","cadetblue 4":"#53868B","turquoise 1":"#00F5FF","turquoise 2":"#00E5EE","turquoise 3":"#00C5CD","turquoise 4":"#00868B","cadetblue":"#5F9EA0","darkturquoise":"#00CED1","azure":"#F0FFFF","azure 2":"#E0EEEE","azure 3":"#C1CDCD","azure 4":"#838B8B","lightcyan":"#E0FFFF","lightcyan 2":"#D1EEEE","lightcyan 3":"#B4CDCD","lightcyan 4":"#7A8B8B","paleturquoise 1":"#BBFFFF","paleturquoise 2":"#AEEEEE","paleturquoise":"#AEEEEE","paleturquoise 3":"#96CDCD","paleturquoise 4":"#668B8B","darkslategray":"#2F4F4F","darkslategray 1":"#97FFFF","darkslategray 2":"#8DEEEE","darkslategray 3":"#79CDCD","darkslategray 4":"#528B8B","cyan":"#00FFFF","aqua":"#00FFFF","cyan 2":"#00EEEE","cyan 3":"#00CDCD","cyan 4":"#008B8B","darkcyan":"#008B8B","teal":"#008080","mediumturquoise":"#48D1CC","lightseagreen":"#20B2AA","manganeseblue":"#03A89E","turquoise":"#40E0D0","coldgrey":"#808A87","turquoiseblue":"#00C78C","aquamarine":"#7FFFD4","aquamarine 2":"#76EEC6","aquamarine 3":"#66CDAA","mediumaquamarine":"#66CDAA","aquamarine 4":"#458B74","mediumspringgreen":"#00FA9A","mintcream":"#F5FFFA","springgreen":"#00FF7F","springgreen 1":"#00EE76","springgreen 2":"#00CD66","springgreen 3":"#008B45","mediumseagreen":"#3CB371","seagreen 1":"#54FF9F","seagreen 2":"#4EEE94","seagreen 3":"#43CD80","seagreen":"#2E8B57","emeraldgreen":"#00C957","mint":"#BDFCC9","cobaltgreen":"#3D9140","honeydew":"#F0FFF0","honeydew 2":"#E0EEE0","honeydew 3":"#C1CDC1","honeydew 4":"#838B83","darkseagreen":"#8FBC8F","darkseagreen 1":"#C1FFC1","darkseagreen 2":"#B4EEB4","darkseagreen 3":"#9BCD9B","darkseagreen 4":"#698B69","palegreen":"#98FB98","palegreen 1":"#9AFF9A","palegreen 2":"#90EE90","lightgreen":"#90EE90","palegreen 3":"#7CCD7C","palegreen 4":"#548B54","limegreen":"#32CD32","forestgreen":"#228B22","lime":"#00FF00","green 2":"#00EE00","green 3":"#00CD00","green 4":"#008B00","green":"#008000","darkgreen":"#006400","sapgreen":"#308014","lawngreen":"#7CFC00","chartreuse":"#7FFF00","chartreuse 2":"#76EE00","chartreuse 3":"#66CD00","chartreuse 4":"#458B00","greenyellow":"#ADFF2F","darkolivegreen 1":"#CAFF70","darkolivegreen 2":"#BCEE68","darkolivegreen 3":"#A2CD5A","darkolivegreen 4":"#6E8B3D","darkolivegreen":"#556B2F","olivedrab":"#6B8E23","olivedrab 1":"#C0FF3E","olivedrab 2":"#B3EE3A","olivedrab 3":"#9ACD32","yellowgreen":"#9ACD32","olivedrab 4":"#698B22","ivory":"#FFFFF0","ivory 2":"#EEEEE0","ivory 3":"#CDCDC1","ivory 4":"#8B8B83","beige":"#F5F5DC","lightyellow":"#FFFFE0","lightyellow 2":"#EEEED1","lightyellow 3":"#CDCDB4","lightyellow 4":"#8B8B7A","lightgoldenrodyellow":"#FAFAD2","yellow":"#FFFF00","yellow 2":"#EEEE00","yellow 3":"#CDCD00","yellow 4":"#8B8B00","warmgrey":"#808069","olive":"#808000","darkkhaki":"#BDB76B","khaki 1":"#FFF68F","khaki 2":"#EEE685","khaki 3":"#CDC673","khaki 4":"#8B864E","khaki":"#F0E68C","palegoldenrod":"#EEE8AA","lemonchiffon":"#FFFACD","lemonchiffon 2":"#EEE9BF","lemonchiffon 3":"#CDC9A5","lemonchiffon 4":"#8B8970","lightgoldenrod 1":"#FFEC8B","lightgoldenrod 2":"#EEDC82","lightgoldenrod 3":"#CDBE70","lightgoldenrod 4":"#8B814C","banana":"#E3CF57","gold":"#FFD700","gold 2":"#EEC900","gold 3":"#CDAD00","gold 4":"#8B7500","cornsilk":"#FFF8DC","cornsilk 2":"#EEE8CD","cornsilk 3":"#CDC8B1","cornsilk 4":"#8B8878","goldenrod":"#DAA520","goldenrod 1":"#FFC125","goldenrod 2":"#EEB422","goldenrod 3":"#CD9B1D","goldenrod 4":"#8B6914","darkgoldenrod":"#B8860B","darkgoldenrod 1":"#FFB90F","darkgoldenrod 2":"#EEAD0E","darkgoldenrod 3":"#CD950C","darkgoldenrod 4":"#8B6508","orange 1":"#FFA500","orange":"#FF8000","orange 2":"#EE9A00","orange 3":"#CD8500","orange 4":"#8B5A00","floralwhite":"#FFFAF0","oldlace":"#FDF5E6","wheat":"#F5DEB3","wheat 1":"#FFE7BA","wheat 2":"#EED8AE","wheat 3":"#CDBA96","wheat 4":"#8B7E66","moccasin":"#FFE4B5","papayawhip":"#FFEFD5","blanchedalmond":"#FFEBCD","navajowhite 1":"#FFDEAD","navajowhite":"#FFDEAD","navajowhite 2":"#EECFA1","navajowhite 3":"#CDB38B","navajowhite 4":"#8B795E","eggshell":"#FCE6C9","tan":"#D2B48C","brick":"#9C661F","cadmiumyellow":"#FF9912","antiquewhite":"#FAEBD7","antiquewhite 1":"#FFEFDB","antiquewhite 2":"#EEDFCC","antiquewhite 3":"#CDC0B0","antiquewhite 4":"#8B8378","burlywood":"#DEB887","burlywood 1":"#FFD39B","burlywood 2":"#EEC591","burlywood 3":"#CDAA7D","burlywood 4":"#8B7355","bisque":"#FFE4C4","bisque 2":"#EED5B7","bisque 3":"#CDB79E","bisque 4":"#8B7D6B","melon":"#E3A869","carrot":"#ED9121","darkorange":"#FF8C00","darkorange 1":"#FF7F00","darkorange 2":"#EE7600","darkorange 3":"#CD6600","darkorange 4":"#8B4500","tan 1":"#FFA54F","tan 2":"#EE9A49","tan 3":"#CD853F","peru":"#CD853F","tan 4":"#8B5A2B","linen":"#FAF0E6","peachpuff":"#FFDAB9","peachpuff 2":"#EECBAD","peachpuff 3":"#CDAF95","peachpuff 4":"#8B7765","seashell":"#FFF5EE","seashell 2":"#EEE5DE","seashell 3":"#CDC5BF","seashell 4":"#8B8682","sandybrown":"#F4A460","rawsienna":"#C76114","chocolate":"#D2691E","chocolate 1":"#FF7F24","chocolate 2":"#EE7621","chocolate 3":"#CD661D","chocolate 4":"#8B4513","saddlebrown":"#8B4513","ivoryblack":"#292421","flesh":"#FF7D40","cadmiumorange":"#FF6103","burntsienna":"#8A360F","sienna":"#A0522D","sienna 1":"#FF8247","sienna 2":"#EE7942","sienna 3":"#CD6839","sienna 4":"#8B4726","lightsalmon":"#FFA07A","lightsalmon 2":"#EE9572","lightsalmon 3":"#CD8162","lightsalmon 4":"#8B5742","coral":"#FF7F50","orangered":"#FF4500","orangered 2":"#EE4000","orangered 3":"#CD3700","orangered 4":"#8B2500","sepia":"#5E2612","darksalmon":"#E9967A","salmon 1":"#FF8C69","salmon 2":"#EE8262","salmon 3":"#CD7054","salmon 4":"#8B4C39","coral 1":"#FF7256","coral 2":"#EE6A50","coral 3":"#CD5B45","coral 4":"#8B3E2F","burntumber":"#8A3324","tomato":"#FF6347","tomato 2":"#EE5C42","tomato 3":"#CD4F39","tomato 4":"#8B3626","salmon":"#FA8072","mistyrose":"#FFE4E1","mistyrose 2":"#EED5D2","mistyrose 3":"#CDB7B5","mistyrose 4":"#8B7D7B","snow":"#FFFAFA","snow 2":"#EEE9E9","snow 3":"#CDC9C9","snow 4":"#8B8989","rosybrown":"#BC8F8F","rosybrown 1":"#FFC1C1","rosybrown 2":"#EEB4B4","rosybrown 3":"#CD9B9B","rosybrown 4":"#8B6969","lightcoral":"#F08080","indianred":"#CD5C5C","indianred 1":"#FF6A6A","indianred 2":"#EE6363","indianred 4":"#8B3A3A","indianred 3":"#CD5555","brown":"#A52A2A","brown 1":"#FF4040","brown 2":"#EE3B3B","brown 3":"#CD3333","brown 4":"#8B2323","firebrick":"#B22222","firebrick 1":"#FF3030","firebrick 2":"#EE2C2C","firebrick 3":"#CD2626","firebrick 4":"#8B1A1A","red":"#FF0000","red 2":"#EE0000","red 3":"#CD0000","red 4":"#8B0000","darkred":"#8B0000","maroon":"#800000","sgi beet":"#8E388E","sgi slateblue":"#7171C6","sgi lightblue":"#7D9EC0","sgi teal":"#388E8E","sgi chartreuse":"#71C671","sgi olivedrab":"#8E8E38","sgi brightgray":"#C5C1AA","sgi salmon":"#C67171","sgi darkgray":"#555555","sgi gray 12":"#1E1E1E","sgi gray 16":"#282828","sgi gray 32":"#515151","sgi gray 36":"#5B5B5B","sgi gray 52":"#848484","sgi gray 56":"#8E8E8E","sgi lightgray":"#AAAAAA","sgi gray 72":"#B7B7B7","sgi gray 76":"#C1C1C1","sgi gray 92":"#EAEAEA","sgi gray 96":"#F4F4F4","white":"#FFFFFF","white smoke":"#F5F5F5","gray 96":"#F5F5F5","gainsboro":"#DCDCDC","lightgrey":"#D3D3D3","silver":"#C0C0C0","darkgray":"#A9A9A9","gray":"#808080","dimgray":"#696969","gray 42":"#696969","black":"#000000","gray 99":"#FCFCFC","gray 98":"#FAFAFA","gray 97":"#F7F7F7","gray 95":"#F2F2F2","gray 94":"#F0F0F0","gray 93":"#EDEDED","gray 92":"#EBEBEB","gray 91":"#E8E8E8","gray 90":"#E5E5E5","gray 89":"#E3E3E3","gray 88":"#E0E0E0","gray 87":"#DEDEDE","gray 86":"#DBDBDB","gray 85":"#D9D9D9","gray 84":"#D6D6D6","gray 83":"#D4D4D4","gray 82":"#D1D1D1","gray 81":"#CFCFCF","gray 80":"#CCCCCC","gray 79":"#C9C9C9","gray 78":"#C7C7C7","gray 77":"#C4C4C4","gray 76":"#C2C2C2","gray 75":"#BFBFBF","gray 74":"#BDBDBD","gray 73":"#BABABA","gray 72":"#B8B8B8","gray 71":"#B5B5B5","gray 70":"#B3B3B3","gray 69":"#B0B0B0","gray 68":"#ADADAD","gray 67":"#ABABAB","gray 66":"#A8A8A8","gray 65":"#A6A6A6","gray 64":"#A3A3A3","gray 63":"#A1A1A1","gray 62":"#9E9E9E","gray 61":"#9C9C9C","gray 60":"#999999","gray 59":"#969696","gray 58":"#949494","gray 57":"#919191","gray 56":"#8F8F8F","gray 55":"#8C8C8C","gray 54":"#8A8A8A","gray 53":"#878787","gray 52":"#858585","gray 51":"#828282","gray 50":"#7F7F7F","gray 49":"#7D7D7D","gray 48":"#7A7A7A","gray 47":"#787878","gray 46":"#757575","gray 45":"#737373","gray 44":"#707070","gray 43":"#6E6E6E","gray 40":"#666666","gray 39":"#636363","gray 38":"#616161","gray 37":"#5E5E5E","gray 36":"#5C5C5C","gray 35":"#595959","gray 34":"#575757","gray 33":"#545454","gray 32":"#525252","gray 31":"#4F4F4F","gray 30":"#4D4D4D","gray 29":"#4A4A4A","gray 28":"#474747","gray 27":"#454545","gray 26":"#424242","gray 25":"#404040","gray 24":"#3D3D3D","gray 23":"#3B3B3B","gray 22":"#383838","gray 21":"#363636","gray 20":"#333333","gray 19":"#303030","gray 18":"#2E2E2E","gray 17":"#2B2B2B","gray 16":"#292929","gray 15":"#262626","gray 14":"#242424","gray 13":"#212121","gray 12":"#1F1F1F","gray 11":"#1C1C1C","gray 10":"#1A1A1A","gray 9":"#171717","gray 8":"#141414","gray 7":"#121212","gray 6":"#0F0F0F","gray 5":"#0D0D0D","gray 4":"#0A0A0A","gray 3":"#080808","gray 2":"#050505","gray 1":"#030303","whitesmoke":"#F5F5F5"}
# helpers
def hasall(obj,*args):
    # """check if given object has all property name or not"""
    return False if False in [True if i in obj else False for i in args] else True
def gio(obj,*args):
    # """return the object keys in order as args"""
    return [obj.get(i) for i in args] if hasall(obj,*args) else False
def cr(n):
    # """return the number javascript style of flooring"""
    from math import ceil,floor
    return floor(n) if (n-floor(n))<0.5 else ceil(n)
def getByName(obj,name):
    # """return the value of perticular key of dict object"""
    return obj.get(name)
def getByValue(obj,val):
    """return the perticualr key of object based on given value"""
    for key,value in obj.items():
        if value==val:
            return key

# Regular Expressions
# rgb
rgbString=r'^rgb\(\s*?(\-?\d+)\s*?\,\s*?(\-?\d+)\s*?\,\s*?(\-?\d+)\s*?\)$'
rgbaString=r'^rgba\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,(\-?0?\.?\d+)\)$'
wrongRgbaString=r'^rgba\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\)$'
wrongRgbString=r'^rgb\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,(\-?0?\.?\d+)\)$'
# hsl
hslString=r'^hsl\((\d+)\,(\d+)%\,(\d+)%\)$'
hslaString=r'^hsla\((\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHslaString=r'^hsl\((\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHslString=r'^hsla\((\d+)\,(\d+)%\,(\d+)%\)$'
# hsv
hsvString=r'^hsv\((\-?\d+)\,(\d+)%\,(\d+)%\)$'
hsvaString=r'^hsva\((\-?\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHsvaString=r'^hsv\((\-?\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHsvString=r'^hsva\((\-?\d+)\,(\d+)%\,(\d+)%\)$'
# cmyk
cmykString=r'^cmyk\((\-?\d+)%\,(\-?\d+)%?\,(\-?\d+)%\,(\-?\d+)%\)$'
# hex
hexString=r'^#[a-fA-F\d]{3}$|^#[a-fA-F\d]{6}$|^#[a-fA-F\d]{8}$'

# Checkers
# cmyk
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

# rgb
def isrgb(*rgb):
    rl=len(rgb)
    if rl==1:
        arg=rgb[0]
        if isinstance(arg,dict):
            a=hasall(arg,'r','g','b','a') or hasall(arg,'r','g','b')
            values = gio(arg,'r','g','b','a') or gio(arg,'r','g','b') 
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

# hsl
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

# hsv
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

# hex
def ishex(hex):
    return bool(re.compile(hexString).search(hex))

def hexlen(hex):
    return len(hex.replace('#','')) if ishex(hex) else False

# Converters
# rgb to color
def RGB2HEX(*rgb):
    check,A,hex=isrgb(*rgb),False,'#'
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
    check=isrgb(*rgb)
    if check:
        h=s=v=0
        tr=typergb(check)
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
    check=isrgb(*rgb)
    if check:
        h=s=l=0
        tr=typergb(check)
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
    check=isrgb(*rgb)
    if check:
        c=m=y=k=0
        check=check.pop() and check if len(check)==4 else [0 if v<0 else 255 if v>255 else v for v in check]
        r,g,b=[v/255 for v in check]
        k=1-max(r,g,b)
        c,m,y=[float(format((1-v-k)/(1-k),'.3f')) for v in [r,g,b]]
        return [float(format(v,'.2f')) for v in [c,m,y,k]]
    else:return False

def RGB2NAME(*rgb):
    hexValue=RGB2HEX(*rgb)
    if hexValue:
        return getByValue(colors,hexValue.upper())
# def rgbtostring(*rgb):
#     check=isrgb(*rgb)
#     if check:
#         trgb=typergb(check)
#         A=check.pop() if typergb(check)=='rgba' else False
#         STRING='rgb(' if trgb=='rgb' else 'rgba('
#         check=[str(int(v)) for v in check]
#         STRING+=','.join(check)+')'
#         return STRING
# print(rgbtostring('rgb(255,255,255,0.6)'))

# # hsl to color

def HSL2RGB(*hsl):
    check=ishsl(*hsl)
    if check:
        r=g=b=0
        tl=typehsl(check)
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
    return False

def HSL2HSV(*hsl):
    check=ishsl(*hsl)
    h=s=v=0
    if check:
        A=float(check.pop()) if typehsl(check)=='hsla' else False
        h,s,l=[*check]
        s,l=[item if item<=1 else item/100 for item in [s,l]]
        h=int(h)
        s*=l if check[0]<.5 else 1-l
        v=l+s
        s=2*s/(l+s)
        s,v=[cr(item*100) for item in [s,v]]
        return [h,s,v,A] if A else [h,s,v]
    return False

def HSL2HEX(*hsl):
    check=ishsl(*hsl)
    if check:
        rgb=HSL2RGB(check)
        A=rgb.pop() if typehsl(check)=='hsla' else False
        hex='#'
        hex+='%02x%02x%02x'%tuple(rgb)
        hex=hex+'%02x'%(cr(float(A)*255)) if A else hex
        return hex
    return False

def HSL2CMYK(*hsl):
    check=ishsl(*hsl)
    if check:
        rgb=HSL2RGB(check)
        rgb.pop() if typergb(rgb)=='rgba' else rgb
        if typehsl(check)=='hsla':check.pop()
        c=m=y=k=0
        R,G,B=[v/255 for v in rgb]
        k=1-max(R,G,B)
        c,m,y=[(1-v-k)/(1-k) for v in [R,G,B]]
        print(c,k)
        c,m,y,k=[cr(v*100) for v in [c,m,y,k]]
        return [c,m,y,k]
    return False

# # # hsv to color

def HSV2RGB(*hsv):
    check=ishsv(*hsv)
    if check:
        A=check.pop() if typehsv(check)=='hsva' else False
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

def HSV2HSL(*hsv):
    c=ishsv(*hsv)
    if c:
        A=c.pop() if typehsv(c)=='hsva' else False
        h,s,v=c
        s,v=[a/100 if a>0 and a<100 else a for a in [s,v]]
        L=v*(1-(s/2))
        S = 0 if (L==0 or L==1) else (v-L)/min(L,1-L)
        S,L=[cr(vv*100) for vv in [S,L]]
        return [cr(h),S,L,A] if A else [h,S,L]
    else:return False

def HSV2CMYK(*hsv):
    ch=ishsv(*hsv)
    if ch:
        if typehsv(ch)=='hsva':ch.pop()
        r,g,b=[v/255 for v in HSV2RGB(ch)]
        k=1-max(r,g,b)
        c,m,y=[(1-v-k)/(1-k) for v in [r,g,b]]
        c,m,y,k=[cr(v*100) for v in [c,m,y,k]]
        return [c,m,y,k]
    else:return False
def HSV2HEX(*hsv):
    check=ishsv(*hsv)
    if check:
        rgb=HSV2RGB(check)
        A=rgb.pop() if typehsv(check)=='hsva' else False
        hex='#'
        hex+='%02x%02x%02x'%tuple(rgb)
        hex=hex+'%02x'%(cr(float(A)*255)) if A else hex
        return hex
    return False

# # # hex to color

def HEX2RGB(hex,inthe=[]):
    outputin={} if inthe=='dict' else []
    c=ishex(hex)
    l=hexlen(hex) if c else False
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
    return [hue,sat,value,hv[3]] if len(hv)==4 else [hue,sat,value]
# print(HEX2RGB('#F09639'))
def HEX2CMYK(hex):
    check=ishex(hex)
    if check:
        RGB=HEX2RGB(hex)
        RGB.pop() if typergb(RGB)=='rgba' else None
        R,G,B=[v/255 for v in RGB]
        c=m=y=k=0
        k=1-max(R,G,B)
        c,m,y=[float(format((1-v-k)/(1-k),'.3f')) for v in [R,G,B]]
        return [cr(v*100) for v in [c,m,y,k]]

# # # cmyk to color

def CMYK2RGB(*cmyk):
    check=iscmyk(*cmyk)
    if check:
        check=[float(v/100) for v in check]
        k=check.pop()
        r,g,b=[cr(255*(1-v)*(1-k)) for v in check]
        return [r,g,b]
def CMYK2HEX(*cmyk):
    check=iscmyk(*cmyk)
    if check:
        r,g,b=CMYK2RGB(check)
        hex='#%02x%02x%02x'%(r,g,b)
        return hex
print(HEX2CMYK(CMYK2HEX([0,33,33,0])))
print(CMYK2HEX(HEX2CMYK('#ffabab')))
def CMYK2HSL(*cmyk):
    check=iscmyk(*cmyk)
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
    check=iscmyk(*cmyk)
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




def typeColor(*col):
    """isrgb,ishsl,iscmyk,ishsv,ishex"""
    if isrgb(*col):return "rgb"
    elif ishsl(*col):return 'hsl'
    elif ishsv(*col):return 'hsv'
    elif ishex(*col):return 'hex'
    elif iscmyk(*col):return 'cmyk'
    else:return 'unknown'
def which(*col):
    TYPE=typeColor(*col)
    if TYPE=='rgb':
        # return "rgba" if len(isrgb(*col))==4 else "rgb"
        return typergb(isrgb(*col))
    elif TYPE=='hsl':
        return typehsl(ishsl(*col))
    elif TYPE=='hsv':
        return typehsv(ishsv(*col))
    elif TYPE=='hex':
        return "hexa" if hexlen(*col)==8 else "hex"

import re
# Colors
colors={"indian red":"#B0171F","crimson":"#DC143C","lightpink":"#FFB6C1","lightpink 1":"#FFAEB9","lightpink 2":"#EEA2AD","lightpink 3":"#CD8C95","lightpink 4":"#8B5F65","pink":"#FFC0CB","pink 2":"#EEA9B8","pink 3":"#CD919E","pink 4":"#8B636C","palevioletred":"#DB7093","palevioletred 1":"#FF82AB","palevioletred 2":"#EE799F","palevioletred 3":"#CD6889","palevioletred 4":"#8B475D","lavenderblush":"#FFF0F5","lavenderblush 2":"#EEE0E5","lavenderblush 3":"#CDC1C5","lavenderblush 4":"#8B8386","violetred 1":"#FF3E96","violetred 2":"#EE3A8C","violetred 3":"#CD3278","violetred 4":"#8B2252","hotpink":"#FF69B4","hotpink 1":"#FF6EB4","hotpink 2":"#EE6AA7","hotpink 3":"#CD6090","hotpink 4":"#8B3A62","raspberry":"#872657","deeppink":"#FF1493","deeppink 2":"#EE1289","deeppink 3":"#CD1076","deeppink 4":"#8B0A50","maroon 1":"#FF34B3","maroon 2":"#EE30A7","maroon 3":"#CD2990","maroon 4":"#8B1C62","mediumvioletred":"#C71585","violetred":"#D02090","orchid":"#DA70D6","orchid 1":"#FF83FA","orchid 2":"#EE7AE9","orchid 3":"#CD69C9","orchid 4":"#8B4789","thistle":"#D8BFD8","thistle 1":"#FFE1FF","thistle 2":"#EED2EE","thistle 3":"#CDB5CD","thistle 4":"#8B7B8B","plum 1":"#FFBBFF","plum 2":"#EEAEEE","plum 3":"#CD96CD","plum 4":"#8B668B","plum":"#DDA0DD","violet":"#EE82EE","magenta":"#FF00FF","fuchsia":"#FF00FF","magenta 2":"#EE00EE","magenta 3":"#CD00CD","magenta 4":"#8B008B","darkmagenta":"#8B008B","purple":"#800080","mediumorchid":"#BA55D3","mediumorchid 1":"#E066FF","mediumorchid 2":"#D15FEE","mediumorchid 3":"#B452CD","mediumorchid 4":"#7A378B","darkviolet":"#9400D3","darkorchid":"#9932CC","darkorchid 1":"#BF3EFF","darkorchid 2":"#B23AEE","darkorchid 3":"#9A32CD","darkorchid 4":"#68228B","indigo":"#4B0082","blueviolet":"#8A2BE2","purple 1":"#9B30FF","purple 2":"#912CEE","purple 3":"#7D26CD","purple 4":"#551A8B","mediumpurple":"#9370DB","mediumpurple 1":"#AB82FF","mediumpurple 2":"#9F79EE","mediumpurple 3":"#8968CD","mediumpurple 4":"#5D478B","darkslateblue":"#483D8B","lightslateblue":"#8470FF","mediumslateblue":"#7B68EE","slateblue":"#6A5ACD","slateblue 1":"#836FFF","slateblue 2":"#7A67EE","slateblue 3":"#6959CD","slateblue 4":"#473C8B","ghostwhite":"#F8F8FF","lavender":"#E6E6FA","blue":"#0000FF","blue 2":"#0000EE","blue 3":"#0000CD","mediumblue":"#0000CD","blue 4":"#00008B","darkblue":"#00008B","navy":"#000080","midnightblue":"#191970","cobalt":"#3D59AB","royalblue":"#4169E1","royalblue 1":"#4876FF","royalblue 2":"#436EEE","royalblue 3":"#3A5FCD","royalblue 4":"#27408B","cornflowerblue":"#6495ED","lightsteelblue":"#B0C4DE","lightsteelblue 1":"#CAE1FF","lightsteelblue 2":"#BCD2EE","lightsteelblue 3":"#A2B5CD","lightsteelblue 4":"#6E7B8B","lightslategray":"#778899","slategray":"#708090","slategray 1":"#C6E2FF","slategray 2":"#B9D3EE","slategray 3":"#9FB6CD","slategray 4":"#6C7B8B","dodgerblue":"#1E90FF","dodgerblue 2":"#1C86EE","dodgerblue 3":"#1874CD","dodgerblue 4":"#104E8B","aliceblue":"#F0F8FF","steelblue":"#4682B4","steelblue 1":"#63B8FF","steelblue 2":"#5CACEE","steelblue 3":"#4F94CD","steelblue 4":"#36648B","lightskyblue":"#87CEFA","lightskyblue 1":"#B0E2FF","lightskyblue 2":"#A4D3EE","lightskyblue 3":"#8DB6CD","lightskyblue 4":"#607B8B","skyblue 1":"#87CEFF","skyblue 2":"#7EC0EE","skyblue 3":"#6CA6CD","skyblue 4":"#4A708B","skyblue":"#87CEEB","deepskyblue":"#00BFFF","deepskyblue 2":"#00B2EE","deepskyblue 3":"#009ACD","deepskyblue 4":"#00688B","peacock":"#33A1C9","lightblue":"#ADD8E6","lightblue 1":"#BFEFFF","lightblue 2":"#B2DFEE","lightblue 3":"#9AC0CD","lightblue 4":"#68838B","powderblue":"#B0E0E6","cadetblue 1":"#98F5FF","cadetblue 2":"#8EE5EE","cadetblue 3":"#7AC5CD","cadetblue 4":"#53868B","turquoise 1":"#00F5FF","turquoise 2":"#00E5EE","turquoise 3":"#00C5CD","turquoise 4":"#00868B","cadetblue":"#5F9EA0","darkturquoise":"#00CED1","azure":"#F0FFFF","azure 2":"#E0EEEE","azure 3":"#C1CDCD","azure 4":"#838B8B","lightcyan":"#E0FFFF","lightcyan 2":"#D1EEEE","lightcyan 3":"#B4CDCD","lightcyan 4":"#7A8B8B","paleturquoise 1":"#BBFFFF","paleturquoise 2":"#AEEEEE","paleturquoise":"#AEEEEE","paleturquoise 3":"#96CDCD","paleturquoise 4":"#668B8B","darkslategray":"#2F4F4F","darkslategray 1":"#97FFFF","darkslategray 2":"#8DEEEE","darkslategray 3":"#79CDCD","darkslategray 4":"#528B8B","cyan":"#00FFFF","aqua":"#00FFFF","cyan 2":"#00EEEE","cyan 3":"#00CDCD","cyan 4":"#008B8B","darkcyan":"#008B8B","teal":"#008080","mediumturquoise":"#48D1CC","lightseagreen":"#20B2AA","manganeseblue":"#03A89E","turquoise":"#40E0D0","coldgrey":"#808A87","turquoiseblue":"#00C78C","aquamarine":"#7FFFD4","aquamarine 2":"#76EEC6","aquamarine 3":"#66CDAA","mediumaquamarine":"#66CDAA","aquamarine 4":"#458B74","mediumspringgreen":"#00FA9A","mintcream":"#F5FFFA","springgreen":"#00FF7F","springgreen 1":"#00EE76","springgreen 2":"#00CD66","springgreen 3":"#008B45","mediumseagreen":"#3CB371","seagreen 1":"#54FF9F","seagreen 2":"#4EEE94","seagreen 3":"#43CD80","seagreen":"#2E8B57","emeraldgreen":"#00C957","mint":"#BDFCC9","cobaltgreen":"#3D9140","honeydew":"#F0FFF0","honeydew 2":"#E0EEE0","honeydew 3":"#C1CDC1","honeydew 4":"#838B83","darkseagreen":"#8FBC8F","darkseagreen 1":"#C1FFC1","darkseagreen 2":"#B4EEB4","darkseagreen 3":"#9BCD9B","darkseagreen 4":"#698B69","palegreen":"#98FB98","palegreen 1":"#9AFF9A","palegreen 2":"#90EE90","lightgreen":"#90EE90","palegreen 3":"#7CCD7C","palegreen 4":"#548B54","limegreen":"#32CD32","forestgreen":"#228B22","lime":"#00FF00","green 2":"#00EE00","green 3":"#00CD00","green 4":"#008B00","green":"#008000","darkgreen":"#006400","sapgreen":"#308014","lawngreen":"#7CFC00","chartreuse":"#7FFF00","chartreuse 2":"#76EE00","chartreuse 3":"#66CD00","chartreuse 4":"#458B00","greenyellow":"#ADFF2F","darkolivegreen 1":"#CAFF70","darkolivegreen 2":"#BCEE68","darkolivegreen 3":"#A2CD5A","darkolivegreen 4":"#6E8B3D","darkolivegreen":"#556B2F","olivedrab":"#6B8E23","olivedrab 1":"#C0FF3E","olivedrab 2":"#B3EE3A","olivedrab 3":"#9ACD32","yellowgreen":"#9ACD32","olivedrab 4":"#698B22","ivory":"#FFFFF0","ivory 2":"#EEEEE0","ivory 3":"#CDCDC1","ivory 4":"#8B8B83","beige":"#F5F5DC","lightyellow":"#FFFFE0","lightyellow 2":"#EEEED1","lightyellow 3":"#CDCDB4","lightyellow 4":"#8B8B7A","lightgoldenrodyellow":"#FAFAD2","yellow":"#FFFF00","yellow 2":"#EEEE00","yellow 3":"#CDCD00","yellow 4":"#8B8B00","warmgrey":"#808069","olive":"#808000","darkkhaki":"#BDB76B","khaki 1":"#FFF68F","khaki 2":"#EEE685","khaki 3":"#CDC673","khaki 4":"#8B864E","khaki":"#F0E68C","palegoldenrod":"#EEE8AA","lemonchiffon":"#FFFACD","lemonchiffon 2":"#EEE9BF","lemonchiffon 3":"#CDC9A5","lemonchiffon 4":"#8B8970","lightgoldenrod 1":"#FFEC8B","lightgoldenrod 2":"#EEDC82","lightgoldenrod 3":"#CDBE70","lightgoldenrod 4":"#8B814C","banana":"#E3CF57","gold":"#FFD700","gold 2":"#EEC900","gold 3":"#CDAD00","gold 4":"#8B7500","cornsilk":"#FFF8DC","cornsilk 2":"#EEE8CD","cornsilk 3":"#CDC8B1","cornsilk 4":"#8B8878","goldenrod":"#DAA520","goldenrod 1":"#FFC125","goldenrod 2":"#EEB422","goldenrod 3":"#CD9B1D","goldenrod 4":"#8B6914","darkgoldenrod":"#B8860B","darkgoldenrod 1":"#FFB90F","darkgoldenrod 2":"#EEAD0E","darkgoldenrod 3":"#CD950C","darkgoldenrod 4":"#8B6508","orange 1":"#FFA500","orange":"#FF8000","orange 2":"#EE9A00","orange 3":"#CD8500","orange 4":"#8B5A00","floralwhite":"#FFFAF0","oldlace":"#FDF5E6","wheat":"#F5DEB3","wheat 1":"#FFE7BA","wheat 2":"#EED8AE","wheat 3":"#CDBA96","wheat 4":"#8B7E66","moccasin":"#FFE4B5","papayawhip":"#FFEFD5","blanchedalmond":"#FFEBCD","navajowhite 1":"#FFDEAD","navajowhite":"#FFDEAD","navajowhite 2":"#EECFA1","navajowhite 3":"#CDB38B","navajowhite 4":"#8B795E","eggshell":"#FCE6C9","tan":"#D2B48C","brick":"#9C661F","cadmiumyellow":"#FF9912","antiquewhite":"#FAEBD7","antiquewhite 1":"#FFEFDB","antiquewhite 2":"#EEDFCC","antiquewhite 3":"#CDC0B0","antiquewhite 4":"#8B8378","burlywood":"#DEB887","burlywood 1":"#FFD39B","burlywood 2":"#EEC591","burlywood 3":"#CDAA7D","burlywood 4":"#8B7355","bisque":"#FFE4C4","bisque 2":"#EED5B7","bisque 3":"#CDB79E","bisque 4":"#8B7D6B","melon":"#E3A869","carrot":"#ED9121","darkorange":"#FF8C00","darkorange 1":"#FF7F00","darkorange 2":"#EE7600","darkorange 3":"#CD6600","darkorange 4":"#8B4500","tan 1":"#FFA54F","tan 2":"#EE9A49","tan 3":"#CD853F","peru":"#CD853F","tan 4":"#8B5A2B","linen":"#FAF0E6","peachpuff":"#FFDAB9","peachpuff 2":"#EECBAD","peachpuff 3":"#CDAF95","peachpuff 4":"#8B7765","seashell":"#FFF5EE","seashell 2":"#EEE5DE","seashell 3":"#CDC5BF","seashell 4":"#8B8682","sandybrown":"#F4A460","rawsienna":"#C76114","chocolate":"#D2691E","chocolate 1":"#FF7F24","chocolate 2":"#EE7621","chocolate 3":"#CD661D","chocolate 4":"#8B4513","saddlebrown":"#8B4513","ivoryblack":"#292421","flesh":"#FF7D40","cadmiumorange":"#FF6103","burntsienna":"#8A360F","sienna":"#A0522D","sienna 1":"#FF8247","sienna 2":"#EE7942","sienna 3":"#CD6839","sienna 4":"#8B4726","lightsalmon":"#FFA07A","lightsalmon 2":"#EE9572","lightsalmon 3":"#CD8162","lightsalmon 4":"#8B5742","coral":"#FF7F50","orangered":"#FF4500","orangered 2":"#EE4000","orangered 3":"#CD3700","orangered 4":"#8B2500","sepia":"#5E2612","darksalmon":"#E9967A","salmon 1":"#FF8C69","salmon 2":"#EE8262","salmon 3":"#CD7054","salmon 4":"#8B4C39","coral 1":"#FF7256","coral 2":"#EE6A50","coral 3":"#CD5B45","coral 4":"#8B3E2F","burntumber":"#8A3324","tomato":"#FF6347","tomato 2":"#EE5C42","tomato 3":"#CD4F39","tomato 4":"#8B3626","salmon":"#FA8072","mistyrose":"#FFE4E1","mistyrose 2":"#EED5D2","mistyrose 3":"#CDB7B5","mistyrose 4":"#8B7D7B","snow":"#FFFAFA","snow 2":"#EEE9E9","snow 3":"#CDC9C9","snow 4":"#8B8989","rosybrown":"#BC8F8F","rosybrown 1":"#FFC1C1","rosybrown 2":"#EEB4B4","rosybrown 3":"#CD9B9B","rosybrown 4":"#8B6969","lightcoral":"#F08080","indianred":"#CD5C5C","indianred 1":"#FF6A6A","indianred 2":"#EE6363","indianred 4":"#8B3A3A","indianred 3":"#CD5555","brown":"#A52A2A","brown 1":"#FF4040","brown 2":"#EE3B3B","brown 3":"#CD3333","brown 4":"#8B2323","firebrick":"#B22222","firebrick 1":"#FF3030","firebrick 2":"#EE2C2C","firebrick 3":"#CD2626","firebrick 4":"#8B1A1A","red":"#FF0000","red 2":"#EE0000","red 3":"#CD0000","red 4":"#8B0000","darkred":"#8B0000","maroon":"#800000","sgi beet":"#8E388E","sgi slateblue":"#7171C6","sgi lightblue":"#7D9EC0","sgi teal":"#388E8E","sgi chartreuse":"#71C671","sgi olivedrab":"#8E8E38","sgi brightgray":"#C5C1AA","sgi salmon":"#C67171","sgi darkgray":"#555555","sgi gray 12":"#1E1E1E","sgi gray 16":"#282828","sgi gray 32":"#515151","sgi gray 36":"#5B5B5B","sgi gray 52":"#848484","sgi gray 56":"#8E8E8E","sgi lightgray":"#AAAAAA","sgi gray 72":"#B7B7B7","sgi gray 76":"#C1C1C1","sgi gray 92":"#EAEAEA","sgi gray 96":"#F4F4F4","white":"#FFFFFF","white smoke":"#F5F5F5","gray 96":"#F5F5F5","gainsboro":"#DCDCDC","lightgrey":"#D3D3D3","silver":"#C0C0C0","darkgray":"#A9A9A9","gray":"#808080","dimgray":"#696969","gray 42":"#696969","black":"#000000","gray 99":"#FCFCFC","gray 98":"#FAFAFA","gray 97":"#F7F7F7","gray 95":"#F2F2F2","gray 94":"#F0F0F0","gray 93":"#EDEDED","gray 92":"#EBEBEB","gray 91":"#E8E8E8","gray 90":"#E5E5E5","gray 89":"#E3E3E3","gray 88":"#E0E0E0","gray 87":"#DEDEDE","gray 86":"#DBDBDB","gray 85":"#D9D9D9","gray 84":"#D6D6D6","gray 83":"#D4D4D4","gray 82":"#D1D1D1","gray 81":"#CFCFCF","gray 80":"#CCCCCC","gray 79":"#C9C9C9","gray 78":"#C7C7C7","gray 77":"#C4C4C4","gray 76":"#C2C2C2","gray 75":"#BFBFBF","gray 74":"#BDBDBD","gray 73":"#BABABA","gray 72":"#B8B8B8","gray 71":"#B5B5B5","gray 70":"#B3B3B3","gray 69":"#B0B0B0","gray 68":"#ADADAD","gray 67":"#ABABAB","gray 66":"#A8A8A8","gray 65":"#A6A6A6","gray 64":"#A3A3A3","gray 63":"#A1A1A1","gray 62":"#9E9E9E","gray 61":"#9C9C9C","gray 60":"#999999","gray 59":"#969696","gray 58":"#949494","gray 57":"#919191","gray 56":"#8F8F8F","gray 55":"#8C8C8C","gray 54":"#8A8A8A","gray 53":"#878787","gray 52":"#858585","gray 51":"#828282","gray 50":"#7F7F7F","gray 49":"#7D7D7D","gray 48":"#7A7A7A","gray 47":"#787878","gray 46":"#757575","gray 45":"#737373","gray 44":"#707070","gray 43":"#6E6E6E","gray 40":"#666666","gray 39":"#636363","gray 38":"#616161","gray 37":"#5E5E5E","gray 36":"#5C5C5C","gray 35":"#595959","gray 34":"#575757","gray 33":"#545454","gray 32":"#525252","gray 31":"#4F4F4F","gray 30":"#4D4D4D","gray 29":"#4A4A4A","gray 28":"#474747","gray 27":"#454545","gray 26":"#424242","gray 25":"#404040","gray 24":"#3D3D3D","gray 23":"#3B3B3B","gray 22":"#383838","gray 21":"#363636","gray 20":"#333333","gray 19":"#303030","gray 18":"#2E2E2E","gray 17":"#2B2B2B","gray 16":"#292929","gray 15":"#262626","gray 14":"#242424","gray 13":"#212121","gray 12":"#1F1F1F","gray 11":"#1C1C1C","gray 10":"#1A1A1A","gray 9":"#171717","gray 8":"#141414","gray 7":"#121212","gray 6":"#0F0F0F","gray 5":"#0D0D0D","gray 4":"#0A0A0A","gray 3":"#080808","gray 2":"#050505","gray 1":"#030303","whitesmoke":"#F5F5F5"}
# helpers
def hasall(obj,*args):
    # """check if given object has all property name or not"""
    return False if False in [True if i in obj else False for i in args] else True
def gio(obj,*args):
    # """return the object keys in order as args"""
    return [obj.get(i) for i in args] if hasall(obj,*args) else False
def cr(n):
    # """return the number javascript style of flooring"""
    from math import ceil,floor
    return floor(n) if (n-floor(n))<0.5 else ceil(n)
def getByName(obj,name):
    # """return the value of perticular key of dict object"""
    return obj.get(name)
def getByValue(obj,val):
    """return the perticualr key of object based on given value"""
    for key,value in obj.items():
        if value==val:
            return key

# Regular Expressions
# rgb
rgbString=r'^rgb\(\s*?(\-?\d+)\s*?\,\s*?(\-?\d+)\s*?\,\s*?(\-?\d+)\s*?\)$'
rgbaString=r'^rgba\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,(\-?0?\.?\d+)\)$'
wrongRgbaString=r'^rgba\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\)$'
wrongRgbString=r'^rgb\(\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,\s*(\-?\d+)\s*\,(\-?0?\.?\d+)\)$'
# hsl
hslString=r'^hsl\((\d+)\,(\d+)%\,(\d+)%\)$'
hslaString=r'^hsla\((\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHslaString=r'^hsl\((\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHslString=r'^hsla\((\d+)\,(\d+)%\,(\d+)%\)$'
# hsv
hsvString=r'^hsv\((\-?\d+)\,(\d+)%\,(\d+)%\)$'
hsvaString=r'^hsva\((\-?\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHsvaString=r'^hsv\((\-?\d+)\,(\d+)%\,(\d+)%\,(0?\.?\d+)\)$'
wrongHsvString=r'^hsva\((\-?\d+)\,(\d+)%\,(\d+)%\)$'
# cmyk
cmykString=r'^cmyk\((\-?\d+)%\,(\-?\d+)%?\,(\-?\d+)%\,(\-?\d+)%\)$'
# hex
hexString=r'^#[a-fA-F\d]{3}$|^#[a-fA-F\d]{6}$|^#[a-fA-F\d]{8}$'

# Checkers
# cmyk
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

# rgb
def isrgb(*rgb):
    rl=len(rgb)
    if rl==1:
        arg=rgb[0]
        if isinstance(arg,dict):
            a=hasall(arg,'r','g','b','a') or hasall(arg,'r','g','b')
            values = gio(arg,'r','g','b','a') or gio(arg,'r','g','b') 
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

# hsl
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

# hsv
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

# hex
def ishex(hex):
    return bool(re.compile(hexString).search(hex))

def hexlen(hex):
    return len(hex.replace('#','')) if ishex(hex) else False

# Converters
# rgb to color
def RGB2HEX(*rgb):
    check,A,hex=isrgb(*rgb),False,'#'
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
    check=isrgb(*rgb)
    if check:
        h=s=v=0
        tr=typergb(check)
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
    check=isrgb(*rgb)
    if check:
        h=s=l=0
        tr=typergb(check)
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
    check=isrgb(*rgb)
    if check:
        c=m=y=k=0
        check=check.pop() and check if len(check)==4 else [0 if v<0 else 255 if v>255 else v for v in check]
        r,g,b=[v/255 for v in check]
        k=1-max(r,g,b)
        c,m,y=[float(format((1-v-k)/(1-k),'.3f')) for v in [r,g,b]]
        return [float(format(v,'.2f')) for v in [c,m,y,k]]
    else:return False

def RGB2NAME(*rgb):
    hexValue=RGB2HEX(*rgb)
    if hexValue:
        return getByValue(colors,hexValue.upper())
# def rgbtostring(*rgb):
#     check=isrgb(*rgb)
#     if check:
#         trgb=typergb(check)
#         A=check.pop() if typergb(check)=='rgba' else False
#         STRING='rgb(' if trgb=='rgb' else 'rgba('
#         check=[str(int(v)) for v in check]
#         STRING+=','.join(check)+')'
#         return STRING
# print(rgbtostring('rgb(255,255,255,0.6)'))

# # hsl to color

def HSL2RGB(*hsl):
    check=ishsl(*hsl)
    if check:
        r=g=b=0
        tl=typehsl(check)
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
    return False

def HSL2HSV(*hsl):
    check=ishsl(*hsl)
    h=s=v=0
    if check:
        A=float(check.pop()) if typehsl(check)=='hsla' else False
        h,s,l=[*check]
        s,l=[item if item<=1 else item/100 for item in [s,l]]
        h=int(h)
        s*=l if check[0]<.5 else 1-l
        v=l+s
        s=2*s/(l+s)
        s,v=[cr(item*100) for item in [s,v]]
        return [h,s,v,A] if A else [h,s,v]
    return False

def HSL2HEX(*hsl):
    check=ishsl(*hsl)
    if check:
        rgb=HSL2RGB(check)
        A=rgb.pop() if typehsl(check)=='hsla' else False
        hex='#'
        hex+='%02x%02x%02x'%tuple(rgb)
        hex=hex+'%02x'%(cr(float(A)*255)) if A else hex
        return hex
    return False

def HSL2CMYK(*hsl):
    check=ishsl(*hsl)
    if check:
        rgb=HSL2RGB(check)
        rgb.pop() if typergb(rgb)=='rgba' else rgb
        if typehsl(check)=='hsla':check.pop()
        c=m=y=k=0
        R,G,B=[v/255 for v in rgb]
        k=1-max(R,G,B)
        c,m,y=[(1-v-k)/(1-k) for v in [R,G,B]]
        print(c,k)
        c,m,y,k=[cr(v*100) for v in [c,m,y,k]]
        return [c,m,y,k]
    return False

# # # hsv to color

def HSV2RGB(*hsv):
    check=ishsv(*hsv)
    if check:
        A=check.pop() if typehsv(check)=='hsva' else False
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

def HSV2HSL(*hsv):
    c=ishsv(*hsv)
    if c:
        A=c.pop() if typehsv(c)=='hsva' else False
        h,s,v=c
        s,v=[a/100 if a>0 and a<100 else a for a in [s,v]]
        L=v*(1-(s/2))
        S = 0 if (L==0 or L==1) else (v-L)/min(L,1-L)
        S,L=[cr(vv*100) for vv in [S,L]]
        return [cr(h),S,L,A] if A else [h,S,L]
    else:return False

def HSV2CMYK(*hsv):
    ch=ishsv(*hsv)
    if ch:
        if typehsv(ch)=='hsva':ch.pop()
        r,g,b=[v/255 for v in HSV2RGB(ch)]
        k=1-max(r,g,b)
        c,m,y=[(1-v-k)/(1-k) for v in [r,g,b]]
        c,m,y,k=[cr(v*100) for v in [c,m,y,k]]
        return [c,m,y,k]
    else:return False
def HSV2HEX(*hsv):
    check=ishsv(*hsv)
    if check:
        rgb=HSV2RGB(check)
        A=rgb.pop() if typehsv(check)=='hsva' else False
        hex='#'
        hex+='%02x%02x%02x'%tuple(rgb)
        hex=hex+'%02x'%(cr(float(A)*255)) if A else hex
        return hex
    return False

# # # hex to color

def HEX2RGB(hex,inthe=[]):
    outputin={} if inthe=='dict' else []
    c=ishex(hex)
    l=hexlen(hex) if c else False
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
    return [hue,sat,value,hv[3]] if len(hv)==4 else [hue,sat,value]
# print(HEX2RGB('#F09639'))
def HEX2CMYK(hex):
    check=ishex(hex)
    if check:
        RGB=HEX2RGB(hex)
        RGB.pop() if typergb(RGB)=='rgba' else None
        R,G,B=[v/255 for v in RGB]
        c=m=y=k=0
        k=1-max(R,G,B)
        c,m,y=[float(format((1-v-k)/(1-k),'.3f')) for v in [R,G,B]]
        return [cr(v*100) for v in [c,m,y,k]]

# # # cmyk to color

def CMYK2RGB(*cmyk):
    check=iscmyk(*cmyk)
    if check:
        check=[float(v/100) for v in check]
        k=check.pop()
        r,g,b=[cr(255*(1-v)*(1-k)) for v in check]
        return [r,g,b]
def CMYK2HEX(*cmyk):
    check=iscmyk(*cmyk)
    if check:
        r,g,b=CMYK2RGB(check)
        hex='#%02x%02x%02x'%(r,g,b)
        return hex
print(HEX2CMYK(CMYK2HEX([0,33,33,0])))
print(CMYK2HEX(HEX2CMYK('#ffabab')))
def CMYK2HSL(*cmyk):
    check=iscmyk(*cmyk)
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
    check=iscmyk(*cmyk)
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




def typeColor(*col):
    """isrgb,ishsl,iscmyk,ishsv,ishex"""
    if isrgb(*col):return "rgb"
    elif ishsl(*col):return 'hsl'
    elif ishsv(*col):return 'hsv'
    elif ishex(*col):return 'hex'
    elif iscmyk(*col):return 'cmyk'
    else:return 'unknown'
def which(*col):
    TYPE=typeColor(*col)
    if TYPE=='rgb':
        # return "rgba" if len(isrgb(*col))==4 else "rgb"
        return typergb(isrgb(*col))
    elif TYPE=='hsl':
        return typehsl(ishsl(*col))
    elif TYPE=='hsv':
        return typehsv(ishsv(*col))
    elif TYPE=='hex':
        return "hexa" if hexlen(*col)==8 else "hex"
    else:return TYPE