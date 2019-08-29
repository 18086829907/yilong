from myClass.rwfile import RwFile
import win32com.client
import tkinter
def wordVoiceReading(path, lineNum=0):
    rwFile = RwFile()
    word = rwFile.readWord(path)
    for line in range(lineNum, len(word)):
        dehua = win32com.client.Dispatch('SAPI.SPVOICE')
        dehua.Speak(word[line])
        lineNumTxtPath = r'D:\qian_feng_education\first_project\myClass\糗事百科\lineNum.txt'
        print(line)
        with open(lineNumTxtPath, 'a') as f:
            f.write(str(line))
    return

if __name__ == '__main__':
    lineNumTxtPath = r'D:\qian_feng_education\first_project\myClass\糗事百科\lineNum.txt'
    with open(lineNumTxtPath, 'r') as f:
        line = f.read()
        line = int(line[-1])
    wordPath = r'D:\qian_feng_education\first_project\myClass\糗事百科\joke.docx'
    wordVoiceReading(wordPath, line)
    '''
    win = tkinter.Tk()
    win.title('糗事百科爬虫')
    win.geometry('810x540+400+200')

    label1 = tkinter.Label(win, text='段子不够，糗事来凑', font=('微软雅黑', 30))
    label1.pack()
    label2 = tkinter.Label(win, text='当事人:', font=('微软雅黑', 15))
    label2.place(x=100, y=100)

    sv = tkinter.StringVar()
    button = tkinter.Button(win, text='继续糗事', command=wordVoiceReading, width=10, height=2, font=('微软雅黑', 10), textvariable=sv)
    button.place(x=370, y=440)

    text1 = tkinter.Text(win, width=10, height=2)
    text1.place(x=170, y=100)
    text1.insert(tkinter.INSERT, sv)

    win.mainloop()
    '''