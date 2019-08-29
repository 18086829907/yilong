import win32api #系统api
import win32con
import win32gui
def setWillPaper(path):
    #打开注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE) #把注册表desktop打开，为了设置数据
    #系统内置接口.注册表设置值（修改内容，参数1：打开的注册表，参数2：当前注册表中的表名，参数3，当前表的值，参数4：当前表的类型，参数5：此类型的值，即背景图片的契合度，填充10、适应6、拉伸2、平铺、居中0、跨区）
    win32api.RegSetValueEx(reg_key, 'WallpaperStyle', 0, win32con.REG_SZ, '10')
    #
    #win32api.RegSetValueEx(reg_key)
    #win32api.RegSetValueEx(reg_key, 'WallPaper')
    #系统内置api.系统参数信息（修改壁纸，图片路径，立即生效）
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)
