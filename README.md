# Color-Converter
Convert into any color between `cmyk`, `rgb`, `rgba`, `hex`, `hsl`, `hsla`, `hsv`, `hsva`

# files
- hex.py
- rgb.py
- cmyk.py
- hsl.py
- hsv.py
- color.py


sample code for use Color library 
```python
import Color
RGBSTR='rgb(255,0,147)'
HSVValue=Color.RGB2HSV(RGBSTR) # an input can be anything like valid rgb string,list,dict,tuple
print(HSVValue) #should print --> [325,1.0,1.0]
```
![image_128](https://user-images.githubusercontent.com/93695068/140856006-8e7ebb6e-da8f-40c2-8985-adcab83e80e4.png)

![image_129](https://user-images.githubusercontent.com/93695068/140856323-ce627229-6a4b-4d37-bacb-6c990c9462e9.png)
