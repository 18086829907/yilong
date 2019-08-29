import tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, other):
        #创建容器
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=0)

        #创建树结构
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

        #添加滚动条
        sc = tkinter.Scrollbar(frame)
        sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        sc.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=sc.set)

        #加入一级树
        root = self.tree.insert('', 'end', text=os.path.split(path)[-1], open=False, values=(path))
        self.loadTree(root, path)#递归遍历所有文件目录及文件名，创建所有树枝

        #绑定树视野选择事件
        self.tree.bind('<<TreeviewSelect>>', self.treeViewSelect)

        #传入infoWindows对象
        self.other = other

    def treeViewSelect(self, event):
        self.v = event.widget.selection()
        for i in self.v:
            file = self.tree.item(i)['text']
            print(self.tree.item(i))
            self.other.ev.set(file)
            absPath = self.tree.item(i)['values'][0]
            #if '.txt' in absPath:
                #with open(absPath) as f:
                    #f.read
            ######难点absPath为什么没有\?

    def loadTree(self, parent, parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath, fileName)
            #插入树枝
            tree1 = self.tree.insert(parent, 'end', text=fileName, open=False, values=(absPath))
            if os.path.isdir(absPath):
                self.loadTree(tree1, absPath)

