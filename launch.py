#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket,requests,json,PIL
import os,configparser,sys,glob,random,string,shutil,time
import mobutton,moframe
from PIL import Image,ImageGrab,ImageDraw,ImageFont,ImageFilter



def isNetOK(testserver=('v1.hitokoto.cn',443)):
  s=socket.socket()
  s.settimeout(3)
  try:
    status = s.connect_ex(testserver)
    if status == 0:
      s.close()
      return True
    else:
      return False
  except Exception as e:
    return False

def getHitokoto():
    r=requests.get("https://v1.hitokoto.cn/")
    r=json.loads(r.text)
    hito=str(r['hitokoto'])
    return hito

def putHito():
    net = isNetOK()
    try:
        if net:
            hito=getHitokoto()
            return hito
        else:
            return "== Building In Progress =="
    except Exception as e: 
        return "== Building In Progress =="
        
mobutton.button()
moframe.frame()
sc = len(glob.glob(f'.\\Resources\\Ir\\Loadingscreen\\*.png'))
if int(sc) >0:
    sc = random.randint(1,sc) #2
    shutil.copyfile(f'.\\Resources\\Ir\\Loadingscreen\\{sc}.png',f".\\Resources\\Loadingscreen.png")

mc = len(glob.glob(f'.\\Resources\\Ir\\BGM\\*.wma'))
if int(mc) >0:
    mc = random.randint(1,mc) #2
    shutil.copyfile(f'.\\Resources\\Ir\\BGM\\{mc}.wma',f".\\Resources\\chaoticimpulse.wma")
    
theme = len(glob.glob(f'.\\Resources\\Ir\\theme\\*'))
if int(theme) >0:
    theme = random.randint(1,theme) #2
    themelist = glob.glob(f'.\\Resources\\Ir\\theme\\{theme}\\*.png')
    for i in range(0,11):
        filepath=themelist[i]
        subpath=filepath.replace('\\Ir\\theme\\'+str(theme),'')
        if subpath=='.\\Resources\\mainmenubg.png':
            subpath=subpath.replace('.\\Resources','.\\Resources\\MainMenu')
        shutil.copyfile(f'{filepath}' ,f"{subpath}")
        
ico = len(glob.glob(f'.\\Resources\\Ir\\ico\\*.ico'))
if int(ico) >0:
    mc = random.randint(1,ico) #2
    shutil.copyfile(f'.\\Resources\\Ir\\ico\\{ico}.ico',f".\\Resources\\clienticon.ico")
    
hito=putHito()
xx = 645-(len(hito.encode('gbk'))*5)
lds = Image.open(".\\Resources\\Loadingscreen.png")
draw = ImageDraw.Draw(lds)
font = ImageFont.truetype('.\\Resources\\Ir\\Fonts\\moneko.ttf', 20)
draw.text((xx,700),hito , font=font, fill=(210,235,238))
lds.save(".\\Resources\\Loadingscreen.png")

os.system("start /high "" .\Resources\clientdx.exe")
sys.exit(0)

#打开
#image3 = Image.open("head3.png")

#重置大小
#imager = image.resize((1000, 200), resample=Image.LANCZOS)

#组合图片
#imager.paste(image2, (0, 0), mask=image2)

#保存图片
#imager.save("top3.png")

#绘制文字
#draw = ImageDraw.Draw(image4)
#font = ImageFont.truetype('kyokasho.ttf', 30)
#draw.text((190,90), '一只天上的大萝卜', font=font, fill=(192,64,128))

#绘制文字大小
#draw = ImageDraw.Draw(image4)
#font = ImageFont.truetype('kyokasho.ttf', 30)
#sizex = draw.textsize('一只天上的大萝卜')

#制图
#image5 = Image.new('RGB', (1000, 800), (255, 255, 255))

#裁切
#imagen = image5.crop(box=(0,0,18,20))

#画线
#draw = ImageDraw.Draw(image5)
#shape = [(50,250), (400,250)]
#draw.line(shape, fill=(128,128,128), width = 3)