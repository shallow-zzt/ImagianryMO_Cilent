import PIL
import configparser
from PIL import Image,ImageGrab,ImageDraw,ImageFont,ImageFilter

path=".\\Resources\\"
#颜色代码转换
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    
def frame():
    configs= configparser.ConfigParser()
    configs.read(".\\Resources\\Ir\\color.ini")
    color_hex=configs.get("color","frame")
    red,green,blue=hex_to_rgb(color_hex)

    ui_fr = Image.new('RGBA',(633,568),(255,255,255,0))
    size = 633
    size2 = 568
    radius = 20

#绘制渐变边缘
    for i in range(0,6):
        alpha = int(255/4*min((6-i),4))
        sidelight = Image.new('RGBA',(1,75),(int(red),int(green),int(blue),alpha))
        uplight = Image.new('RGBA',(75,1),(int(red),int(green),int(blue),alpha))
        ui_fr.paste(uplight,(0,i),mask=uplight)
        ui_fr.paste(uplight,(0,size2-i-1),mask=uplight)
        ui_fr.paste(uplight,(size-75,i),mask=uplight)
        ui_fr.paste(uplight,(size-75,size2-i-1),mask=uplight)
    
        ui_fr.paste(sidelight,(i,0),mask=sidelight)
        ui_fr.paste(sidelight,(size-i-1,0),mask=sidelight)
        ui_fr.paste(sidelight,(i,size2-75),mask=sidelight)
        ui_fr.paste(sidelight,(size-i-1,size2-75),mask=sidelight)
    
    ui_fr.save(path+"bigframe.png")
    rabl = ui_fr.crop(box=(0,9,9,size2-9))
    rabr = ui_fr.crop(box=(size-9,9,size,size2-9))
    rabt = ui_fr.crop(box=(9,0,size-9,9))
    rabb = ui_fr.crop(box=(9,size2-9,size-9,size2))

    racbl = ui_fr.crop(box=(0,size2-9,9,size2))
    racbr = ui_fr.crop(box=(size-9,size2-9,size,size2))
    ractl = ui_fr.crop(box=(0,0,9,9))
    ractr = ui_fr.crop(box=(size-9,0,size,9))

    rabl.save(path+"rabl.png")
    rabr.save(path+"rabr.png")
    rabt.save(path+"rabt.png")
    rabb.save(path+"rabb.png")
    racbl.save(path+"racbl.png")
    racbr.save(path+"racbr.png")
    ractl.save(path+"ractl.png")
    ractr.save(path+"ractr.png")