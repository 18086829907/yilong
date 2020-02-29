# 申明
#   盒模型的content的宽
#       css属性为width
#       以下用content.width表示
#   盒模型的content的高
#       css属性为height
#       以下用content.height表示
#   总高
#       由题目中得：总高=54px

# 1、观察整体宽高
#   width = 400px
#   height = 总高-border.top-border.bottom = 54px-1px-3px = 50px

# 2、设置字体大小颜色
#     font: normal 20px 'Microsoft YaHei'; /*倾斜 大小/行高 字体*/
#     color: #333;

# 3、文字是垂直居中对齐——line-height = height = 50px
#   line-height:50px

# 4、文字有缩进
#   text-indent: 20px;

# 5、绘制border
#     border-top:1px solid #f00;
#     border-bottom:3px solid #666;