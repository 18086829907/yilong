from myClass.speechRecognition import SpeechRecognition
import time
from 词库 import 三年级下册
from word import volumeTwoGradeThree

def 生词听写():
    dict1 = 三年级下册()
    words = dict1['读书'] #单词修改
    speechRecognition = SpeechRecognition()
    for word in words:
        speechRecognition.machineReading(word)
        time.sleep(20) #间隔时间

def listenWord():
    dict1 = volumeTwoGradeThree()
    words = dict1['Unit5,lesson1'] #单词修改
    speechRecognition = SpeechRecognition()
    for word in words:
        speechRecognition.machineReading(word)
        time.sleep(20) #间隔时间

if __name__ == '__main__':
    生词听写()
    listenWord()