# 申明
#   盒模型的content的宽
#       css属性为width
#       以下用content.width表示
#   盒模型的content的高
#       css属性为height
#       以下用content.height表示

# 确定content.width
        # content.width + padding.left + padding.right + border.left + border.right = 400px
        # padding.left=15px, padding.right=15px, border.left=0px, border.right=0px
        # 因此：content.width = 400px - 30px - 0px = 360px
# 确定content.height
        # content.height + padding.top + padding.bottom + border.top + border.bottom = 54px
        # content.height=20px, border.top=1px, boder.bottom=3px
        # ∴padding.top + padding.bottom = 54px - 1px - 3px - 20px= 30px
        # ∵保持文字居中
        # ∴padding.top=15px, padding.bottom=15px

