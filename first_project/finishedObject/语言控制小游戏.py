#游戏地址：http://www.4399.com/flash/122374.htm#sim2|122374
import win32com.client
from win32com.client import constants
import win32com.client
import pythoncom
import win32con
import win32api
import time
import os
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
        if voiceCommand == '上':
            print('上')
            win32api.keybd_event(38, 0, 0, 0)  # 点击
            time.sleep(0.1)
            win32api.keybd_event(38, 0, win32con.KEYEVENTF_KEYUP, 0)

        elif voiceCommand == '下':
            print('下')
            win32api.keybd_event(40, 0, 0, 0)  # 点击
            time.sleep(0.1)
            win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)

        elif voiceCommand == '左':
            print('左')
            win32api.keybd_event(37, 0, 0, 0)  # 点击
            time.sleep(0.1)
            win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)

        elif voiceCommand == '右':
            print('右')
            win32api.keybd_event(39, 0, 0, 0)  # 点击
            time.sleep(0.1)
            win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == '__main__':
    wordsToAdd = ['上', '下', '左', '右']
    speechReco = SpeechRecognition(wordsToAdd)
    while True:
        pythoncom.PumpWaitingMessages()