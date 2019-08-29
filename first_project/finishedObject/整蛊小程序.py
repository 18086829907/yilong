#在后台运行小程序

import time
import pygame
import win32api
import win32con
import win32gui
import os
import threading #线程模块
def musicGo():
    musicPath = r'D:\qian_feng_education\first_project\music'
    pygame.mixer.init()
    while True:
        for fileName in os.listdir(musicPath):
            absFile = os.path.join(musicPath, fileName)
            track = pygame.mixer.music.load(absFile)
            pygame.mixer.music.play()
            time.sleep(20)
            pygame.mixer.music.stop()
def setWillPaper():
    imgPath = r'D:\qian_feng_education\first_project\img'
    while True:
        for imgName in os.listdir(imgPath):
            img = os.path.join(imgPath, imgName)
            reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE) #把注册表desktop打开，为了设置数据
            win32api.RegSetValueEx(reg_key, 'WallpaperStyle', 0, win32con.REG_SZ, '10')
            win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img, win32con.SPIF_SENDWININICHANGE)
            time.sleep(10)
#增加一个线程来进行musicGo()
th = threading.Thread(target=musicGo, name='LoopThread') #target只给函数名，不要调用，否则无法执行多线程
th.start()
setWillPaper()