import tkinter
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title('主窗体')
win.geometry('800x800+200+200')

path = r'D:\qian_feng_education'
infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)

win.mainloop()