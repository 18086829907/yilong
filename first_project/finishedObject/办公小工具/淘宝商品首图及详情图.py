import re
import urllib.request
import time
import win32com
import win32com.client
import os
import requests

#word函数
def makeWorkFile(path, content):
    word = win32com.client.Dispatch('Word.Application')#打开word软件
    #让文档可见
    word.Visible = False
    #创建文档
    doc = word.Documents.Add()
    #写内容
    #从头开始写
    r = doc.Range(0, 0) #光标定位到最开始
    r.InsertAfter(content)
    #存储文件
    doc.SaveAs(path)
    #关闭文件
    doc.Close()
    #退出软件
    word.Quit()

#需要填写的内容

# dirname = r'G:\PS\酷派新衣\1购物\3详情页\产品详情图' + r'\1米喜迪mecity童装2019秋新款女童上衣彩色葱小格型长袖毛衫'
# st = '<div style="position:relative;width:0;height:0;overflow:hidden;"><img src="https://img.alicdn.com/imgextra/i1/2660257049/O1CN010FjU1p21wUQlQzWxm_!!2660257049.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i1/2660257049/O1CN010FjU1p21wUQlQzWxm_!!2660257049.jpg_q30.jpg"><img src="https://img.alicdn.com/imgextra/i1/2660257049/O1CN010FjU1p21wUQlQzWxm_!!2660257049.jpg"><img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01KJYf0j21wUQkEmb5I_!!2660257049.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01KJYf0j21wUQkEmb5I_!!2660257049.jpg"><img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01x06IBL21wUQj27Gud_!!2660257049.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01x06IBL21wUQj27Gud_!!2660257049.jpg"><img src="https://img.alicdn.com/imgextra/i1/2660257049/O1CN01zG7eJX21wUQkzWb0b_!!2660257049.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i1/2660257049/O1CN01zG7eJX21wUQkzWb0b_!!2660257049.jpg"><img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01BSGPpW21wUQfRmwJk_!!2660257049.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01BSGPpW21wUQfRmwJk_!!2660257049.jpg"></div>'
# xqt = '<div class="content ke-post" style="height: auto;"><img class="desc_anchor img-ks-lazyload" id="desc-module-1" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div data-title="宝贝产品" data-id="63e34373-a349-4c1f-9bf0-0b56f7eb29a4" style="">  <div data-id="afe892bf-0e11-4d9e-98f4-4051a4030d91">   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i4/2660257049/O1CN01GyUV9J21wUQZr6vKn_!!2660257049.jpg" class="img-ks-lazyload">   </div>  </div> </div><img class="desc_anchor img-ks-lazyload" id="desc-module-2" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div data-title="宝贝尺寸" data-id="2416881b-4df2-4ce3-bc28-3f748e69aa08" style="">  <div data-id="300ab172-7714-4f20-84c7-980d3ff2de45">   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i1/2660257049/O1CN01qqVRs121wUQhiebmL_!!2660257049.jpg" class="img-ks-lazyload">   </div>  </div>  <div data-id="2fd45d69-e634-443f-a120-89df3c8608cd">   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i4/2660257049/O1CN01r27zKI21wUQjwcp2O_!!2660257049.jpg" class="img-ks-lazyload">   </div>   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01NJ8da921wUQhZGbew_!!2660257049.jpg" class="img-ks-lazyload">   </div>  </div>  <div data-id="d26b8495-80e7-4cff-84d2-61ea4c5857be">   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01cFBeWZ21wUQlR1fwm_!!2660257049.jpg" class="img-ks-lazyload">   </div>  </div> </div><img class="desc_anchor img-ks-lazyload" id="desc-module-3" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div data-title="宝贝模特" class="aa" data-id="4c3a3500-b3cc-472b-b710-4ce78a05e80d" style="">  <div data-id="8b3aa9d0-abd6-48b0-8a2c-6367b908465a">   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i3/2660257049/O1CN01oSmvQr21wUQkzWnTv_!!2660257049.jpg" class="img-ks-lazyload">   </div>  </div>  <div data-id="3499e01e-2a97-49c6-aa28-0c52c8784c75">   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i4/2660257049/O1CN01gnwbkF21wUQZr6WOc_!!2660257049.jpg" class="img-ks-lazyload">   </div>   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i3/2660257049/O1CN01jjAh8x21wUQkzX8Hd_!!2660257049.jpg" class="img-ks-lazyload">   </div>   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i4/2660257049/O1CN015v4jli21wUQlQzfHL_!!2660257049.jpg" class="img-ks-lazyload">   </div>   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i1/2660257049/O1CN01uvA1x221wUQlQzfHP_!!2660257049.jpg" class="img-ks-lazyload">   </div>  </div> </div><img class="desc_anchor img-ks-lazyload" id="desc-module-4" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div data-title="宝贝细节" data-id="b4be6d7b-5603-4231-a930-585accbc908e" style="">  <div data-id="4e8c5a8c-d3db-472c-a30d-393cec057663">   <div>    <div style="font-size: 0.0px;">     <img src="https://img.alicdn.com/imgextra/i3/2660257049/O1CN018CveRM21wUQkUjURj_!!2660257049.jpg" class="img-ks-lazyload">    </div>   </div>  </div>  <div data-id="d5eada4c-ce3a-4f76-a280-161298043d15">   <div>    <div style="font-size: 0.0px;">     <img src="https://img.alicdn.com/imgextra/i1/2660257049/O1CN01Qfwunq21wUQlR0jmx_!!2660257049.jpg" class="img-ks-lazyload">    </div>    <div style="font-size: 0.0px;">     <img src="https://img.alicdn.com/imgextra/i3/2660257049/O1CN01gtJWlI21wUQeUgP66_!!2660257049.jpg" class="img-ks-lazyload">    </div>    <div style="font-size: 0.0px;">     <img src="https://img.alicdn.com/imgextra/i3/2660257049/O1CN01Js9L7821wUQhIFvjx_!!2660257049.jpg" class="img-ks-lazyload">    </div>    <div style="font-size: 0.0px;">     <img src="https://img.alicdn.com/imgextra/i3/2660257049/O1CN019MR2mE21wUQlR0bTL_!!2660257049.jpg" class="img-ks-lazyload">    </div>    <div style="font-size: 0.0px;">     <img src="https://img.alicdn.com/imgextra/i4/2660257049/O1CN0198tPMj21wUQhicOa2_!!2660257049.jpg" class="img-ks-lazyload">    </div>    <div style="font-size: 0.0px;">     <img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN018pzFRS21wUQjDKv3w_!!2660257049.jpg" class="img-ks-lazyload">    </div>   </div>  </div>  <div data-id="308bd74b-99c8-4a23-8302-9e29e6b7e147">   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i3/2660257049/O1CN01iwNWam21wUQh0QDxB_!!2660257049.jpg" class="img-ks-lazyload">   </div>  </div>  <div data-id="d20a1483-ed30-4c0f-af1b-51f15dcd3bde">   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i2/2660257049/O1CN01HFML1a21wUQhidjie_!!2660257049.jpg" class="img-ks-lazyload">   </div>   <div style="font-size: 0.0px;">    <img src="https://img.alicdn.com/imgextra/i4/2660257049/O1CN01HhuBQH21wUQjDK2zX_!!2660257049.jpg" class="img-ks-lazyload">   </div>  </div> </div></div>'
# content = '¥ 299.00 \n品牌名称：Me&City Kids/米喜迪\n产品参数：\n品牌: Me&City Kids/米喜迪适用年龄: 3岁 4岁 5岁 6岁 7岁 8岁 9岁 11岁 12岁针织面料: 其他图案: 其他风格: 休闲领型: 圆领适用性别: 女模特实拍: 实拍有模特衣门襟: 套头毛线粗细: 细毛线是否带帽子: 无颜色分类: 米白花纱货号: 591911参考身高: 110/56 120/60 130/64 140/64 150/72 160/84A适用季节: 春秋上市年份季节: 2019年秋季袖长: 长袖厚薄: 常规安全等级: B类材质成分: 聚丙烯腈纤维(腈纶)52% 聚'

# dirname = r'G:\PS\酷派新衣\1购物\3详情页\产品详情图' + r'\2Gap女童撞色条纹束脚运动裤496915 E 2019新款童装裤子儿童休闲裤'
# st = '<div style="position:relative;width:0;height:0;overflow:hidden;"><img src="//img.alicdn.com/imgextra/i1/669642169/O1CN01YOmKiD1RtRclkOmz1-669642169.jpg_430x430q90.jpg"><img src="//img.alicdn.com/imgextra/i1/669642169/O1CN01YOmKiD1RtRclkOmz1-669642169.jpg"><img src="https://img.alicdn.com/imgextra/i2/669642169/O1CN01Ybqh6O1RtRd6NkYm1_!!0-item_pic.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/669642169/O1CN01Ybqh6O1RtRd6NkYm1_!!0-item_pic.jpg"><img src="https://img.alicdn.com/imgextra/i2/669642169/O1CN01fUs2y21RtRchkHFGD-669642169.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/669642169/O1CN01fUs2y21RtRchkHFGD-669642169.jpg"><img src="https://img.alicdn.com/imgextra/i2/669642169/O1CN01zxjMk11RtRclJoQtR-669642169.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/669642169/O1CN01zxjMk11RtRclJoQtR-669642169.jpg"><img src="https://img.alicdn.com/imgextra/i3/669642169/O1CN01bp1ywA1RtRd6KtwTI-669642169.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i3/669642169/O1CN01bp1ywA1RtRd6KtwTI-669642169.jpg"><img src="https://img.alicdn.com/imgextra/i4/669642169/O1CN01IG34na1RtRcfxCW4v-669642169.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i4/669642169/O1CN01IG34na1RtRcfxCW4v-669642169.jpg"></div>'
# xqt = '''
# <div id="description" class="J_DetailSection tshop-psm tshop-psm-bdetaildes">
# 	<h4 class="hd">商品详情</h4>
#         <div class="content ke-post" style="height: auto;"><img class="desc_anchor img-ks-lazyload" id="desc-module-1" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div style="width: 790.0px;margin: auto;">  <div class="placeholder-reminder">  </div>  <div class="crop-unit product-details generate2Image">   <img src="https://img.alicdn.com/imgextra/i4/669642169/O1CN01pmooKT1RtRcGLoW2e-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">  </div>  <div class="crop-unit swap_item generate2Image" style="margin-top: 30.0px;">   <img src="https://img.alicdn.com/imgextra/i4/669642169/O1CN01wVShgj1RtRcEWQeyH-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">  </div>  <div class="crop-unit swap_item generate2Image" style="margin-top: 30.0px;">   <img src="https://img.alicdn.com/imgextra/i4/669642169/O1CN01J2wDZV1RtRcDiVoL5-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">  </div>  <div class="crop-unit sliceBanner isPicTextMixed" style="width: 790.0px;display: inline-block;">   <div style="width: 100.0%;display: inline-block;float: left;margin-top: 30.0px;">    <img class="i18n_header img-ks-lazyload" src="https://img.alicdn.com/imgextra/i1/669642169/O1CN01EcPh6k1RtRag0tkM1-669642169.jpg">   </div>  </div>  <div class="crop-unit isPicTextMixed generate2Image" style="width: 790.0px;display: inline-block;margin-top: 30.0px;">   <img src="https://img.alicdn.com/imgextra/i2/669642169/O1CN01ITR5RI1RtRcDpaPq9-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">  </div>  <div class="crop-unit sliceBanner isPicTextMixed" style="width: 790.0px;display: inline-block;margin-top: 30.0px;">   <div style="width: 100.0%;display: inline-block;float: left;">    <img class="i18n_header img-ks-lazyload" src="https://img.alicdn.com/imgextra/i1/669642169/O1CN01j87nH21RtRaiZoUEt-669642169.jpg">   </div>  </div>  <div class="crop-unit isPicTextMixed " style="width: 790.0px;display: inline-block;">   <div class="generate2Image" style="width: 790.0px;margin: auto;">    <img src="https://img.alicdn.com/imgextra/i3/669642169/O1CN01pbDGLZ1RtRcForc1f-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">   </div>   <div class="generate2Image" style="width: 790.0px;margin: auto;">    <img src="https://img.alicdn.com/imgextra/i3/669642169/O1CN01SXNVgo1RtRcGLnZnZ-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">   </div>   <div class="generate2Image" style="width: 790.0px;margin: auto;">    <img src="https://img.alicdn.com/imgextra/i4/669642169/O1CN01CWaKE01RtRcFoqPBp-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">   </div>   <div class="generate2Image" style="width: 790.0px;margin: auto;">    <img src="https://img.alicdn.com/imgextra/i1/669642169/O1CN01CCAxif1RtRc6AbkvI-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">   </div>  </div> </div><img class="desc_anchor img-ks-lazyload" id="desc-module-2" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div style="width: 790.0px;margin: auto;">  <div class="prod-size-container">   <div class="crop-unit sliceBanner isPicTextMixed generate2Image" style="width: 790.0px;display: inline-block;margin-top: 30.0px;">    <img src="https://img.alicdn.com/imgextra/i1/669642169/O1CN018jYYn41RtRcDpWzTH-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">   </div>   <div class="crop-unit sliceBanner isPicTextMixed generate2Image" style="width: 790.0px;display: inline-block;margin-top: 30.0px;">    <img src="https://img.alicdn.com/imgextra/i1/669642169/O1CN018iXNOA1RtRcGmEKV3-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">   </div>   <div class="generate2Image">    <img src="https://img.alicdn.com/imgextra/i4/669642169/O1CN01nQIU1k1RtRcDiTWsX-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">   </div>  </div> </div><img class="desc_anchor img-ks-lazyload" id="desc-module-3" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div style="width: 790.0px;margin: auto;">  <div class="crop-unit isPicTextMixed generate2Image" style="width: 790.0px;display: inline-block;">   <img src="https://img.alicdn.com/imgextra/i3/669642169/O1CN01SS65Cl1RtRcBhg149-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">  </div>  <div class="crop-unit sliceBanner isPicTextMixed PDP_790 PDP_NEW_STYLE" style="width: 790.0px;display: inline-block;margin-top: 30.0px;">   <div style="width: 100.0%;display: inline-block;float: left;">    <img class="i18n_header img-ks-lazyload" src="https://img.alicdn.com/imgextra/i4/669642169/O1CN01TE9lN91RtRaaJ5New-669642169.jpg">   </div>  </div>  <div class="crop-unit isPicTextMixed generate2Image " style="width: 790.0px;display: inline-block;">   <img src="https://img.alicdn.com/imgextra/i3/669642169/O1CN01I04BhE1RtRcF6AIv1-669642169.jpg" style="width: 100.0%;" class="img-ks-lazyload">  </div>  <div class="crop-unit isPicTextMixed" style="width: 790.0px;display: inline-block;">  </div>  <div class="crop-unit sliceBanner isPicTextMixed" style="width: 790.0px;display: inline-block;margin-top: 30.0px;">   <div style="width: 100.0%;display: inline-block;float: left;">    <img class="i18n_header img-ks-lazyload" src="https://img.alicdn.com/imgextra/i1/669642169/O1CN01zrc0kL1RtRajpdmRn-669642169.jpg">   </div>  </div>  <div class="crop-unit isPicTextMixed removeForEA" style="width: 790.0px;display: inline-block;">   <div style="width: 100.0%;display: inline-block;float: left;">    <img class="i18n_header img-ks-lazyload" src="https://img.alicdn.com/imgextra/i3/669642169/O1CN01Vo81kL1RtRbZPLwy7-669642169.jpg">   </div>  </div> </div></div>
#  </div>
#  <div id="J_DcBottomRightWrap">
# 			<div id="J_DcBottomRight" class="J_DcAsyn tb-shop"><div class="J_TModule" data-widgetid="16466809952" id="shop16466809952" data-componentid="5003" data-spm="110.0.5003-16466809952" microscope-data="5003-16466809952" data-title="自定义内容区">	        <div class="skin-box tb-module tshop-pbsm tshop-pbsm-shop-self-defined">
#
#         <s class="skin-box-tp"><b></b></s>
# 		        <div class="skin-box-bd clear-fix">
#             <span>
# 								    <p><img src="//gdp.alicdn.com/imgextra/i1/669642169/O1CN01bALbCw1RtRaS4oH1a_!!669642169.jpg" alt="" class="img-ks-lazyload"></p> <p><img src="//gdp.alicdn.com/imgextra/i2/669642169/O1CN01vlZTGF1RtRZ3e4W0s_!!669642169.jpg" alt="" class="img-ks-lazyload"></p>
# 							</span>
#         </div>
#         <s class="skin-box-bt"><b></b></s>
#
# 	</div>
# </div>
# <div class="J_TModule" data-widgetid="18432777999" id="shop18432777999" data-componentid="17977515" data-spm="110.0.17977515-18432777999" microscope-data="17977515-18432777999" data-title="【F15】宝贝展示">
#
#
#
#
#
#
#
#
# <div class="tb-module tshop-um tshop-um-gd_zs" style="margin-bottom:10px;">
# <div style="width:790px;overflow:hidden;"><a target="_blank" href="//gap.tmall.com/category-300532200-1303053497.htm?spm=a1z10.15-b-s.w5002-18427458497.6.3eb57df3rNH51P&amp;search=y&amp;catName=%C5%AE%BA%A2"><img class="hd_pic img-ks-lazyload" src="//gdp.alicdn.com/imgextra/i1/669642169/TB2zonHrQCWBuNjy0FaXXXUlXXa_!!669642169.jpg"></a><div class="mk_bd" style=""><ul style="width:800px;padding-left:0px;padding-top:0px;*padding-bottom:0px;"><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=599954067538" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i3/669642169/O1CN01iaJidI1RtRd1TpKFo-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥199.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=599954067538" style="">Gap女童天鹅绒连帽卫衣2019秋装休闲宽松Logo徽标拉链外套510007</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">199.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:299</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=599954067538"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">802</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">338</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=600895057006" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i1/669642169/O1CN01LCRqN11RtRd6JbW6f-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥199.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=600895057006" style="">Gap女童棉质抓绒连帽卫衣秋装2019新款创意刺绣洋气上衣潮510006</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">199.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:299</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=600895057006"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">710</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">370</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=598102216829" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i4/669642169/O1CN01XSS7Kr1RtRd3XXEw7-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥564.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=598102216829" style="">Gap女童中长款羽绒服秋冬装2019新款儿童脱卸毛领连帽外套473736</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">564.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:799</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=598102216829"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">21</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">78</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=598376354633" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i2/669642169/O1CN01SbaYGd1RtRcvfwXB3-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥704.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=598376354633" style="">Gap女童中长款连帽羽绒服473701-1 2019新款中大童儿童纯色外套</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">704.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:799</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=598376354633"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">10</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">46</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=597952058595" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i1/669642169/O1CN011cqGLf1RtRd1GQSnz-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥284.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=597952058595" style="">Gap女童纯色拉链连帽棉服473695 2019新款女孩时尚上衣女童外套</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">284.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:399</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=597952058595"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">123</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">128</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=598375072066" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i2/669642169/O1CN01TR8ut91RtRd3aB6rQ-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥198.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=598375072066" style="">Gap女童纯棉圆领套头毛衣496845 E 2019新款中大童儿童印花针织衫</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">198.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:279</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=598375072066"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">141</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">66</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=598783346044" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i4/669642169/O1CN01I4wIHu1RtRd2pQqV0-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥91.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=598783346044" style="">Gap女童纯棉印花长袖T恤499181 2019新款中大童儿童圆领上衣童装</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">91.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:129</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=598783346044"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">1484</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">300</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=562540498707" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i3/669642169/O1CN01VUuXxp1RtRcvfBXKK-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥131.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=562540498707" style="">Gap女童洋气休闲裤童装秋装360179EW 2019新款长裤儿童运动裤子</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">131.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:199</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=562540498707"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">8236</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">2768</strong> 人</div>
#                     </div>
#                 </div></li></ul></div></div></div>
# </div>
# <div class="J_TModule" data-widgetid="18432863657" id="shop18432863657" data-componentid="17977515" data-spm="110.0.17977515-18432863657" microscope-data="17977515-18432863657" data-title="【F15】宝贝展示">
#
#
#
#
#
#
#
#
# <div class="tb-module tshop-um tshop-um-gd_zs" style="margin-bottom:10px;">
# <div style="width:790px;overflow:hidden;"><a target="_blank" href="//gap.tmall.com/category-1193802331-1303053499.htm?spm=a1z10.15-b-s.w5002-18427458497.7.6cfc3893QK0tKE&amp;search=y&amp;catName=%D3%D7%B6%F9"><img class="hd_pic img-ks-lazyload" src="//gdp.alicdn.com/imgextra/i1/669642169/TB2T6OYrQKWBuNjy1zjXXcOypXa_!!669642169.jpg"></a><div class="mk_bd" style=""><ul style="width:800px;padding-left:0px;padding-top:0px;*padding-bottom:0px;"><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=556002563380" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i3/669642169/O1CN01e1pBlG1RtRd3NNu3C-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥179.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=556002563380" style="">Gap婴儿纯棉针织连体衣秋装2019新款宝宝爬服哈衣毛线衣844020W</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">179.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:249</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=556002563380"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">9636</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">7136</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=579092153956" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i4/669642169/O1CN01C0qC4o1RtRd5kwg1E-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥141.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=579092153956" style="">Gap婴儿纯棉套头针织衫400208 女宝宝儿童毛衣童装</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">141.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:199</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=579092153956"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">1767</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">1746</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=601095250785" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i1/669642169/O1CN01GB5CFr1RtRd2pZhsT-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥345.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=601095250785" style="">Gap男婴幼童加绒三合一外套秋冬2019新款宝宝潮夹克背心473807</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">345.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:499</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=601095250785"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">72</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">126</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=598498935550" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i3/669642169/O1CN0154O0Vs1RtRd3OBNub-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥354.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=598498935550" style="">Gap女婴幼童印花连帽羽绒服秋装2019新款女孩上衣儿童外套473662</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">354.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:499</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=598498935550"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">322</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">358</strong> 人</div>
#                     </div>
#                 </div></li></ul></div></div></div>
# </div>
# <div class="J_TModule" data-widgetid="18432887643" id="shop18432887643" data-componentid="17977515" data-spm="110.0.17977515-18432887643" microscope-data="17977515-18432887643" data-title="【F15】宝贝展示">
#
#
#
#
#
#
#
#
# <div class="tb-module tshop-um tshop-um-gd_zs" style="margin-bottom:10px;">
# <div style="width:790px;overflow:hidden;"><a target="_blank" href="//gap.tmall.com/category-1230274519-1303053496.htm?spm=a1z10.15-b-s.w5002-18427458497.3.4c757df3WDTyBB&amp;search=y&amp;catName=%C4%D0%D7%B0"><img class="hd_pic img-ks-lazyload" src="//gdp.alicdn.com/imgextra/i4/669642169/TB26xJ3jyCYBuNkSnaVXXcMsVXa_!!669642169.jpg"></a><div class="mk_bd" style=""><ul style="width:800px;padding-left:0px;padding-top:0px;*padding-bottom:0px;"><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=564361347981" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i3/669642169/O1CN015jsz4B1RtRd1FilGX-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥189.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=564361347981" style="">Gap男装圆领套头卫衣111735WE logo休闲上衣运动衫2019新款潮秋装</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">189.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:299</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=564361347981"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">15260</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">13252</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=602188984318" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i3/669642169/O1CN017rwHii1RtRd1GnQGM-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥1049.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=602188984318" style="">Gap男装长袖毛领连帽羽绒服 2019新款休闲时尚加绒外套479909</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">1,049.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:1499</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=602188984318"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">20</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">86</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=599471683269" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i4/669642169/O1CN01NP8pUj1RtRd4HdQ9F-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥269.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=599471683269" style="">Gap男装 Logo徽标圆领长袖针织衫474794羊毛衫套头毛衣男2019新款</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">269.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:399</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=599471683269"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">227</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">248</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=584177175166" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i2/669642169/O1CN01yCDFY31RtRd36dgHN-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥229.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=584177175166" style="">Gap男装弹力宽松休闲裤子844140 2019新款长裤男士时尚卡其裤</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">229.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:399</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=584177175166"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">1671</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">1406</strong> 人</div>
#                     </div>
#                 </div></li></ul></div></div></div>
# </div>
# <div class="J_TModule" data-widgetid="18432882617" id="shop18432882617" data-componentid="17977515" data-spm="110.0.17977515-18432882617" microscope-data="17977515-18432882617" data-title="【F15】宝贝展示">
#
#
#
#
#
#
#
#
# <div class="tb-module tshop-um tshop-um-gd_zs" style="margin-bottom:10px;">
# <div style="width:790px;overflow:hidden;"><a target="_blank" href="//gap.tmall.com/category-1230268819-1303053495.htm?spm=a1z10.15-b-s.w5002-18427458497.4.32165a4eATRoXJ&amp;search=y&amp;catName=%C5%AE%D7%B0"><img class="hd_pic img-ks-lazyload" src="//gdp.alicdn.com/imgextra/i3/669642169/TB2VJdNf8jTBKNjSZFwXXcG4XXa_!!669642169.jpg"></a><div class="mk_bd" style=""><ul style="width:800px;padding-left:0px;padding-top:0px;*padding-bottom:0px;"><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=597937880527" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i2/669642169/O1CN01fIsYSz1RtRd4rC3Ha-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥199.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=597937880527" style="">Gap女装休闲加绒套头卫衣451202 W E 潮流女士logo上衣连帽运动衫</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">199.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:349</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=597937880527"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">1436</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">2396</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=602274150238" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i1/669642169/O1CN01vQ05k51RtRd7G2Z2U-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥559.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=602274150238" style="">Gap女装蔡依林明星同款连帽外套474536 2019新款抽绳棉服中长款</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">559.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:799</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=602274150238"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">16</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">120</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=601845106775" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i4/669642169/O1CN01XwgywN1RtRd2phcqR-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥129.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=601845106775" style="">Gap女装休闲圆领长袖T恤秋季2019新款女生套头上衣打底衫510010</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">129.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:199</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=601845106775"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">331</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">274</strong> 人</div>
#                     </div>
#                 </div></li><li style="margin-right:10px;margin-bottom:10px;width:190px;">
#                 <a class="gd_img" target="_blank" href="//detail.tmall.com/item.htm?id=598252757402" style="height:190px;">
#                 	<span class="pic_z" style="background:url(//gdp.alicdn.com/bao/uploaded/i1/669642169/O1CN01249uO51RtRd1GTcNz-669642169.jpg_190x190.jpg) no-repeat center center;"></span>
#                 	<span class="pic_f" style=""></span>
#                 	<div class="gd_mc" style="left:33px;">
#                 		<div class="tit">CLICK ENTER</div>
#                 		<p>¥249.00</p>
#                 	</div>
#                 </a>
#                 <div class="gd_info" style="">
#                     <p class="gd_name" style="height:18px;"><a target="_blank" href="//detail.tmall.com/item.htm?id=598252757402" style="">Gap女装束脚休闲裤九分裤469873-1 E 2019新款女士纯棉工装小脚裤</a></p>
#                     <div class="price_btn">
#                     	<div class="info">
#                 			<p class="price" style="display:block;"><span>¥</span><em style="font-family:arial;font-weight:700;">249.00</em></p>
#                 			<p class="price_old" style="display:block;"><del>专柜价:399</del></p>
#                     	</div><a class="J_CartPluginTrigger" title="加入购物车" target="_blank" href="//detail.tmall.com/item.htm?id=598252757402"><img class="buttom img-ks-lazyload" src="//gdp.alicdn.com/L1/142/439977554/modules/tshop-um-gd_zs/assets/images/btn2.png" style="display:block;"></a></div>
#                     <div class="sale_sc" style="">
#                     	<div class="gd_sale" style="display:block;">近30天售出 <strong style="">952</strong> 件</div>
#                     	<div class="gd_sc" style="">收藏 <strong style="">776</strong> 人</div>
#                     </div>
#                 </div></li></ul></div></div></div>
# </div>
# </div>
#
#     <div id="J_ZebraPriceDesc" class="j-mdv"><img width="790" src="//img.alicdn.com/tfs/TB1.CUdsY9YBuNjy0FgXXcxcXXa-1572-394.png"></div>
# 	</div>
# '''
#content = '品牌: Gap型号: 000496915适用年龄: 4岁 5岁 6岁 7岁 8岁 9岁 10岁 11岁 12岁 13岁 14岁面料: 棉涤是否开裆: 不开裆风格: 休闲裤腰: 中腰适用性别: 女模特实拍: 实拍有模特颜色分类: 海军蓝色货号: 496915-1参考身高: 110cm(XS) 120cm(S) 130cm(M) 140cm(L) 150cm(XL) 160cm(XXL)适用季节: 春秋上市年份季节: 2019年秋季裤长: 九分裤裤子分类: 普通休闲裤材质成分: 棉60% 聚酯纤维40%'

#需要填写的内容
# dirname = r'G:\PS\酷派新衣\1购物\3详情页\产品详情图' + r'\3巴拉巴拉童装儿童套装女童秋装2019新款宝宝两件套灯芯绒裙子T恤'
# st = '<div style="position:relative;width:0;height:0;overflow:hidden;"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01BvQP7B1IH7x5PJe9H_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01BvQP7B1IH7x5PJe9H_!!642320867.jpg_q30.jpg"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01iOuyBy1IH7x5tt3Py_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01iOuyBy1IH7x5tt3Py_!!642320867.jpg"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01m8mGOt1IH7vdkXTmO_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01m8mGOt1IH7vdkXTmO_!!642320867.jpg"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01X7y4ht1IH7vdluLIV_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01X7y4ht1IH7vdluLIV_!!642320867.jpg"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN016n2EtA1IH7vfAJGkP_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN016n2EtA1IH7vfAJGkP_!!642320867.jpg"></div>'
# xqt = '<div style="font-size: 0.0px;"> <img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN012rIUbD1IH7vicDxMg_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01ha9q901IH7vlsQzzI_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01g4a2bp1IH7vlpZ1Nx_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01DU1SbO1IH7vlsP3Tb_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN01dS2zwu1IH7vicExhJ_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN013iAPFt1IH7vizPm8G_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN015cDTcC1IH7vnG3aij_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01TqrOCI1IH7vhivjRK_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01yZc2Eh1IH7vnG4riK_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01UcNHAf1IH7vmZUjmG_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01A15feQ1IH7vkMO1SE_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01xhpBp91IH7vlWzWso_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01VPvSaC1IH7vhivOfg_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01qhO1Rf1IH7vhitvBw_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN01wAq7E11IH7vkMNDb3_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN01InU3dy1IH7vnVBGCH_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN0173hyxE1IH7vjyDB0s_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"> </div>'
# content = '店铺链接：https://detail.tmall.com/item.htm?spm=a230r.1.14.6.7f5254f102In26&id=597044732437&cm_id=140105335569ed55e27b&abbucket=6\n巴拉巴拉童装儿童套装女童秋装2019新款宝宝两件套灯芯绒裙子T恤\n¥ 159.90\n品牌名称：巴拉巴拉\n产品参数：\n品牌: 巴拉巴拉适用年龄: 2岁 3岁 4岁 5岁 6岁 7岁面料: 棉混纺布图案: 圆点风格: 韩版产地: 中国大陆适用性别: 女模特实拍: 实拍有模特衣门襟: 套头件数: 2件是否带帽子: 无颜色分类: 梦幻粉6311 红色调0366 黄色调0333组合形式: 长袖+裙子货号: 28043190250参考身高: 90cm 100cm 110cm 120cm 130cm适用季节: 春秋上市年份季节: 2019年秋季厚薄: 常规安全等级: 其他材质成分: 棉95.5% 聚氨酯弹性纤维(氨'
# video = 'https://cloud.video.taobao.com/play/u/642320867/p/1/e/6/t/1/230381163273.mp4'

dirname = r'G:\PS\酷派新衣\1购物\3详情页\产品详情图' + r'\4巴拉巴拉童装女童裤子2019新款秋装儿童运动裤中大童经典潮酷长裤'
st = '<div style="position:relative;width:0;height:0;overflow:hidden;"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01L97lAb1IH7x3x1Uz0_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01L97lAb1IH7x3x1Uz0_!!642320867.jpg_q30.jpg"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01L97lAb1IH7x3x1Uz0_!!642320867.jpg"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN01jA1d5b1IH7x2TRvFL_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN01jA1d5b1IH7x2TRvFL_!!642320867.jpg"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01nVYvaR1IH7wOlRvM9_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01nVYvaR1IH7wOlRvM9_!!642320867.jpg"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01uMVfEw1IH7vooMGlX_!!642320867.jpg_430x430q90.jpg"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01uMVfEw1IH7vooMGlX_!!642320867.jpg"></div>'
xqt = '<div class="content ke-post" style="height: auto;"><img class="desc_anchor img-ks-lazyload" id="desc-module-1" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div data-title="商品参数" style="background-color: #ffffff;margin: 0 auto;overflow: hidden;color: #555555;width: 750.0px;font-family: 微软雅黑;" data-id="7e65b4c8-4f4e-4f2a-89f5-fa105a5c7a35"> <div data-id="7988c51d-af25-4b2e-a91e-fc1f9ac2d080"> <div style="font-size: 0.0px;"> &nbsp; </div> </div> <div data-id="9149f7c1-68a9-48a4-ad6e-3e49c2b98228"> <div style="font-size: 0.0px;"> &nbsp; </div> </div> <div data-id="a1551ad4-0623-4b4c-99f6-a6bcb74c1553"> <div style="font-size: 0.0px;"> &nbsp; </div> </div> <div data-id="d3dd79c0-aca4-4503-bbf8-8a971360007e"> <div style="font-size: 0.0px;"> &nbsp; </div> <div style="font-size: 0.0px;"> <img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01prbkvW1IH7vw6D48A_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01qaWGsA1IH7vvzjWQ3_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN01VYps7w1IH7vvzjn38_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01MBFGO01IH7vyyWeJc_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01LXwKnY1IH7vw71kqA_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01JyVanv1IH7vu0aODm_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01tILcoV1IH7voWd90B_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"> </div> </div> </div><div class="hlg_rand_634183974" style="opacity: 0;height: 0;width: 0;">1355383497</div><img class="desc_anchor img-ks-lazyload" id="desc-module-2" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div data-title="商品实拍" style="background-color: #ffffff;margin: 0 auto;overflow: hidden;color: #555555;width: 750.0px;font-family: 微软雅黑;" data-id="e6d8a4b4-b60d-45a1-ae38-138066998c53"> <div data-id="48af960c-d670-499f-9d1b-340e6435192c"> <div style="font-size: 0.0px;"> &nbsp; </div> </div> <div data-id="5816edd1-5f7f-4edc-8071-550edf243089"> <div style="font-size: 0.0px;"> <img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01p5UFbB1IH7vw72IC7_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN01A0Zbxt1IH7vgI30cm_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"> </div> </div> <div data-id="019d07d2-59a5-4558-834c-6b5a12dab118"> <div class="screenshot wxts _m" style="background-color: #ffffff;overflow: hidden;color: #555555;width: 750.0px;font-size: 0.0px;font-family: 微软雅黑;position: static;"> <div style="margin-left: 13.0px;display: inline-block;width: 62.134%;vertical-align: top;margin-top: 58.0px;"> <img id="matchImg" width="100%" src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01hjYBg01IH7vbw5UVl_!!642320867.jpg" style="overflow: hidden;display: block;" class="img-ks-lazyload"> </div> <div style="margin-left: 39.0px;display: inline-block;vertical-align: top;margin-top: 263.0px;"> <div> <img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01Yhb4oe1IH7vUk0Fne_!!642320867.jpg" style="overflow: hidden;display: block;" class="img-ks-lazyload"> </div> <div style="margin-top: 58.0px;"> <div> <a target="_blank" style="text-decoration: none;" href="http://detail.tmall.com/item.htm?id=595706718280"><img id="matchImg1_1" src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01SeRiRq1IH7vd5iuYZ_!!642320867.jpg" style="border: none;overflow: hidden;display: block;" class="img-ks-lazyload"></a> </div> <div> <img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01rQCuth1IH7vcFhhZK_!!642320867.jpg" style="overflow: hidden;display: block;" class="img-ks-lazyload"> </div> </div> </div> </div> </div> <div data-id="2692d313-9a3e-4c0e-817a-a446d7840f9c"> <div style="font-size: 0.0px;"> <img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN012kxYQs1IH7vUjz78n_!!642320867.jpg" class="img-ks-lazyload"> </div> <div style="font-size: 0.0px;"> <img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01Lowgho1IH7vcFi2LV_!!642320867.jpg" class="img-ks-lazyload"> </div> <div style="font-size: 0.0px;"> <img src="https://img.alicdn.com/imgextra/i4/642320867/O1CN01Iv3MWm1IH7vyybcAL_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN011cYU0R1IH7vxKHGvg_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01rSz9QM1IH7vzSAFvu_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01EQp3e31IH7vwvmcAQ_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01PZvFHo1IH7vw72Ukv_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"> </div> <div style="font-size: 0.0px;"> &nbsp; </div> <div style="font-size: 0.0px;"> &nbsp; </div> </div> <div data-id="32e8871d-8b15-4684-8d54-c29b37518714"> <div style="font-size: 0.0px;"> &nbsp; </div> </div> </div><div class="hlg_rand_634183974" style="opacity: 0;height: 0;width: 0;">1355383497</div><img class="desc_anchor img-ks-lazyload" id="desc-module-3" src="https://assets.alicdn.com/kissy/1.0.0/build/imglazyload/spaceball.gif"><div data-title="商品尺码表" style="background-color: #ffffff;margin: 0 auto;overflow: hidden;color: #555555;width: 750.0px;font-family: 微软雅黑;" data-id="86308ffe-51eb-4dc1-9f77-e9a05e95d61a"> <div data-id="6c1f79aa-96c1-4747-83fc-0cddecedd396"> <div> <div style="font-size: 0.0px;"> &nbsp; </div> <div style="font-size: 0.0px;"> &nbsp; </div> <div style="font-size: 0.0px;"> &nbsp; </div> <div style="font-size: 0.0px;"> &nbsp; </div> </div> <div style="font-size: 0.0px;"> <img src="https://img.alicdn.com/imgextra/i2/642320867/O1CN01WSAmNM1IH7vvJvwM6_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i1/642320867/O1CN01lUGsbj1IH7vyh7rR0_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"><img src="https://img.alicdn.com/imgextra/i3/642320867/O1CN01WZ1XKk1IH7vyyaXhi_!!642320867.jpg" align="absmiddle" class="img-ks-lazyload"> </div> </div> </div><div class="hlg_rand_634183974" style="opacity: 0;height: 0;width: 0;">1355383497</div></div>'
content = '店铺链接：\nhttps://detail.tmall.com/item.htm?spm=a230r.1.14.14.7f5254f102In26&id=597254157571&cm_id=140105335569ed55e27b&abbucket=6\n巴拉巴拉童装女童裤子2019新款秋装儿童运动裤中大童经典潮酷长裤\n¥ 89.90\n品牌名称：巴拉巴拉\n产品参数：\n品牌: 巴拉巴拉型号: 28083190502适用年龄: 8岁 9岁 10岁 11岁 12岁 13岁 14岁面料: 棉混纺布是否开裆: 不开裆风格: 简约裤腰: 中腰产地: 中国大陆适用性别: 女模特实拍: 实拍有模特颜色分类: 黑色-侧边标语 中花灰-侧边标语 紫罗兰-侧边标语 深蓝-侧边织带 中花灰-侧边织带 黑色-侧边单杠 中花灰-侧边单杠 紫罗兰-侧边单杠裤门襟: 皮筋腰带货号: 28083190502参考身高: 140cm 150cm 160cm 165cm 170cm适用季节: 春秋上市年份季节: 2019年秋季裤长: 长裤裤子分类: 普通休闲裤安全等级: B类材质成分: 棉84.6% 聚酯纤维15.4%'
video = ''

#操作锁
imglocal = True  #图片下载
wordlocal = True  #参数下载
videolocal = False  #视频下载

#创建文件夹
if not os.path.exists(dirname):
    os.mkdir(dirname)

#提取url
par = 'src="(.*?)"'
obj = re.compile(par, re.S)
result1 = obj.findall(st)
result2 = obj.findall(xqt)

#清洗url
result = []
for res in result1:
    if not '430x430q90' in res:
        result.append(res)
for res in result2:
    if 'imgextra' in res:
        result.append(res)

#下载图片
if imglocal == True:
    n = 0
    for res in result:
        # 图片的名字叫啥
        filename = str(n) + '.' + res.split('/')[-1].split('.')[-1]
        abspath = os.path.join(dirname, filename)
        n += 1
        if not 'https:' in res:
            res = 'https:' + res
        print('%s图片正在下载...' % filename)
        urllib.request.urlretrieve(res, abspath)
        print('%s图片下载结束...' % filename)
        time.sleep(1)

#word内容
if wordlocal == True:
    abspath = os.path.join(dirname, '参数') + '.docx'
    makeWorkFile(abspath, content)

#保存视频
if videolocal == True:
    abspath = os.path.join(dirname, '视频') + '.mp4'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}
    r = requests.get(url=video, headers=headers)
    with open(abspath, 'wb') as f:
        f.write(r.content)