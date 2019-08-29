import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np
from PIL import Image

imgPath = r'D:\qian_feng_education\first_project\data\img\1.jpg'
txtfile = r'D:\qian_feng_education\first_project\data\txt\test.txt'
fontPath = r'D:\qian_feng_education\first_project\data\ttf\simkai.ttf'

with open(txtfile, 'r') as f:
    text= f.read()

wordlist = jieba.cut_for_search(text) #'['我','爱','你']'
space_list = ' '.join(wordlist) #链接词语 '我 爱 你'
background = np.array(Image.open(imgPath)) #背景图片
mywordcloud = WordCloud(background_color='white', #词云图片背景颜色
                        mask=background,  #颜色抽取到文字上
                        max_words=20, #最大词语数量
                        stopwords=STOPWORDS, #停止的默认词语
                        font_path=fontPath, #字体
                        max_font_size=200, #最大字体尺寸
                        random_state=50, #随机角度
                        scale=2).generate(space_list) #将文本文件传入设定好的词云格式中

image_color = ImageColorGenerator(background) #生成词云的颜色
plt.imshow(mywordcloud) #显示
plt.axis('off') #关闭保存
plt.show() #显示词云