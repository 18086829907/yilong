import win32com.client
from win32com.client import constants
import os
import pythoncom
import win32process
import win32con
import win32gui
import win32api
import ctypes

mia = win32com.client.Dispatch('SAPI.SPVOICE')  # 生成speaker对象
mia.Speak('你好，我的名字叫米亚，我可以帮你轻松通过植物大战僵尸')

class SpeechRecognition:
    def __init__(self, wordsToAdd):
        self.speaker = win32com.client.Dispatch('SAPI.SpVoice')
        self.listener = win32com.client.Dispatch('SAPI.SpSharedRecognizer')
        self.context = self.listener.CreateRecoContext()
        self.grammar = self.context.CreateGrammar()
        self.grammar.DictationSetState(0)
        self.wordsRule = self.grammar.Rules.Add('wordsRule', constants.SRATopLevel + constants.SRADynamic, 0)
        self.wordsRule.Clear()
        [self.wordsRule.InitialState.AddWordTransition(None, word) for word in wordsToAdd]
        self.grammar.Rules.Commit()
        self.grammar.CmdSetRuleState('wordsRule', 1)
        self.grammar.Rules.Commit()
        self.eventHandler = ContextEvents(self.context)
        self.say('Started successfully')
    def say(self, phrase):
        self.speaker.Speak(phrase)

class ContextEvents(win32com.client.getevents('SAPI.SpSharedRecoContext')):
    def OnRecognition(self, StreamNumber, StreamPosition, RecognitionType, Result):
        newResult = win32com.client.Dispatch(Result) #生成语音识别对象
        voiceCommand = newResult.PhraseInfo.GetText()  # 生成语音转文字变量
        print('我说:', voiceCommand)
        for i in listKeyWord():
            if voiceCommand == i:
                Sunshine()

def listKeyWord():
    list1 = ['阳光']
    return list1

def Sunshine():
    #修改器部分
    PROCESS_ALL_ACCESS = (0X000F0000 | 0X00100000 | 0XFFF)  # 最高全向变量，最高权限是通过二进制数进行|是位运算的到的值
    win = win32gui.FindWindow('MainWindow', '植物大战僵尸中文版')  # 找窗体
    hid, pid = win32process.GetWindowThreadProcessId(win)  # 根据窗体找到进程号（任务管理器中的pid号）
    p = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)  # 以最高权限打开pid进程
    md = ctypes.windll.LoadLibrary(r'c:\windows\system32\kernel32.dll')  # md——mydata加载内核模块，内核模块存放于c:\windows\system32\kernel32.dll
    data = ctypes.c_long()  # 定义一个数据类型为c语言中的长整型数据类型的变量，用于存放指定内存中的值
    md.ReadProcessMemory(int(p), 441160144, ctypes.byref(data), 4, None)  # 用内核模块读取p进程的485053864内存，将值保存到data中，保存4个字节，None表示内存信息错误我们不处理。内存地址通过memsearch软件查到
    newData = ctypes.c_long(200)  # 设置新值
    md.WriteProcessMemory(int(p), 441160144, ctypes.byref(newData), 4, None)  # 用内核模块将新值写入p进程485053864内存，写入4个字节，None表示内存信息错误我们不处理

if __name__ == '__main__':
    wordsToAdd = list(listKeyWord())
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()