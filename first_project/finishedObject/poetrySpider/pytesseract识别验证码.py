#打开图片数据
import pytesseract
from PIL import Image
from PIL import ImageEnhance

img = Image.open('./code/code4.jpg')
#图片数据预处理
#图片数据预处理第一步
img = img.convert('RGB')
enhancer = ImageEnhance.Color(img)
enhancer = enhancer.enhance(0)
enhancer = ImageEnhance.Brightness(enhancer)
enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
enhancer = enhancer.enhance(20)

#图片数据预处理第二步——灰度处理
img = img.convert('L')
# img.show()
#图片数据预处理第三步——二值化处理
threshold = 140
table = []
for i in range(256):
  if i < threshold:
      table.append(0)
  else:
      table.append(1)
out = img.point(table, '1')
out.show()

#学习验证码图片
print(pytesseract.image_to_string(img))