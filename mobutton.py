import PIL
import configparser
from PIL import Image,ImageGrab,ImageDraw,ImageFont,ImageFilter

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    
def button():
    configs= configparser.ConfigParser()
    configs.read(".\\Resources\\Ir\\color.ini")
    color_hex=configs.get("color","button")
    red,green,blue=hex_to_rgb(color_hex)

    origin=Image.open(".\\Resources\\Ir\\sample.png").convert("RGBA")
    allsize=[75,92,97,110,121,133,142,160]
    for k in range(0,8):
        size=allsize[k]
        height=25
    
        ui_bg = origin.resize((size, height), resample=Image.LANCZOS)
        ui_bg.save(".\\Resources\\"+str(size)+"pxbtn.png")

#绘制渐变边缘
        for i in range(0,6):
            alpha = 255-int(255/5*i)
            sidelen=10
            uplen=30
            sidelight = Image.new('RGBA',(1,sidelen),(int(red),int(green),int(blue),alpha))
            uplight = Image.new('RGBA',(uplen,1),(int(red),int(green),int(blue),alpha))
            ui_bg.paste(uplight,(0,i),mask=uplight)
            ui_bg.paste(uplight,(0,height-i-1),mask=uplight)
            ui_bg.paste(uplight,(size-uplen,i),mask=uplight)
            ui_bg.paste(uplight,(size-uplen,height-i-1),mask=uplight)
    
            ui_bg.paste(sidelight,(i,0),mask=sidelight)
            ui_bg.paste(sidelight,(size-i-1,0),mask=sidelight)
            ui_bg.paste(sidelight,(i,height-sidelen),mask=sidelight)
            ui_bg.paste(sidelight,(size-i-1,height-sidelen),mask=sidelight)
    
#去透明度
        for i in range(0,size):
            for j in range(0,height):
                r,g,b,a = ui_bg.getpixel((i,j))
                ui_bg.putpixel((i,j),(r,g,b,255))


#组合保存
        ui_bg.save(".\\Resources\\"+str(size)+"pxbtn_c.png")

