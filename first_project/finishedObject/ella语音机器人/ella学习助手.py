# -*- coding:utf-8 -*-
import win32com.client
from win32com.client import constants
import os
import win32com.client
import pythoncom
import pickle

mia = win32com.client.Dispatch('SAPI.SPVOICE')  # 生成speaker对象
mia.Speak('你好，我的名字叫ella，很高兴认识你')
print('你好，我的名字叫ella，很高兴认识你')

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
        for k in dictKeyWord():
            if voiceCommand == k:
                v = dictKeyWord()[k]
                mia.Speak(v)
                print('ella说:', v)

def dictKeyWord():
    path = r'C:\Users\justin\DataGit\yilong\first_project\finishedObject\ella语音机器人\ella的语言库.txt'
    with open(path, 'rb') as f:
        dict1 = pickle.load(f)
    return dict1

if __name__ == '__main__':
    wordsToAdd = list(dictKeyWord())
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()


'''
#TypeError: NoneType takes no arguments
#解决办法：重载MicrosoftSpeechObjectLibrary5.4
import os
path = r'C:\ Users\surface\Anaconda3\Lib\site-packages\pythonwin\Pythonwin.exe'
r_v = os.system(path)
print(r_v)
#Tools>COM Makepy utility>microsoft speech object library [5.4]
'''