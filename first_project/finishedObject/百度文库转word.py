import re
import win32com
import win32com.client
import os
a = '''
<p class="reader-word-layer reader-word-s1-0 reader-word-s1-2" style="width:2170px;height:240px;line-height:240px;top:1282px;left:3685px;z-index:234;font-weight:600;font-size:240px;letter-spacing:0.78px;false">租房合同范本标准版</p>
<p class="reader-word-layer reader-word-s1-0 reader-word-s1-5" style="width:120px;height:240px;line-height:240px;top:1282px;left:5856px;z-index:236;font-weight:600;font-size:240px;font-family:simsun;"></p>
<p class="reader-word-layer reader-word-s1-6" style="width:72px;height:144px;line-height:144px;top:1920px;left:4698px;z-index:237;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-6" style="width:72px;height:144px;line-height:144px;top:1920px;left:4842px;z-index:239;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:2204px;left:1442px;z-index:240;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:2204px;left:1611px;z-index:241;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-11" style="width:673px;height:169px;line-height:169px;top:2204px;left:1780px;z-index:242;false">出租方：</p>
<p class="reader-word-layer reader-word-s1-14" style="width:1177px;height:169px;line-height:169px;top:2204px;left:2453px;z-index:243;false">______________</p>
<p class="reader-word-layer reader-word-s1-15" style="width:1346px;height:169px;line-height:169px;top:2204px;left:3631px;z-index:244;false">，以下简称甲方。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:2204px;left:4975px;z-index:246;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:2516px;left:1442px;z-index:247;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:2516px;left:1611px;z-index:248;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-11" style="width:673px;height:169px;line-height:169px;top:2516px;left:1780px;z-index:249;false">承租方：</p>
<p class="reader-word-layer reader-word-s1-14" style="width:1177px;height:169px;line-height:169px;top:2516px;left:2453px;z-index:250;false">______________</p>
<p class="reader-word-layer reader-word-s1-15" style="width:1346px;height:169px;line-height:169px;top:2516px;left:3631px;z-index:251;false">，以下简称乙方。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:2516px;left:4975px;z-index:253;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:2829px;left:1442px;z-index:254;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:2829px;left:1611px;z-index:255;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-10" style="width:1667px;height:169px;line-height:169px;top:2829px;left:1780px;z-index:256;letter-spacing:-2.56px;false">根据《中华人民共和国</p>
<p class="reader-word-layer reader-word-s1-16 reader-word-s1-18" style="width:505px;height:169px;line-height:169px;top:2829px;left:3448px;z-index:257;letter-spacing:-0.8699999999999999px;false">合同法</p>
<p class="reader-word-layer reader-word-s1-10" style="width:4148px;height:169px;line-height:169px;top:2829px;left:3954px;z-index:259;letter-spacing:-3.2px;false">》及有关规定，为明确甲、乙双方的权利义务关系，经双</p>
<p class="reader-word-layer reader-word-s1-19" style="width:2021px;height:169px;line-height:169px;top:3141px;left:1442px;z-index:260;false">方协商一致，签订本合同。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:3141px;left:3464px;z-index:262;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:3454px;left:1442px;z-index:263;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:3454px;left:1611px;z-index:264;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:3454px;left:1780px;z-index:265;false">第一条</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:3454px;left:2284px;z-index:266;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:1515px;height:169px;line-height:169px;top:3454px;left:2369px;z-index:267;false">甲方将自有的坐落在</p>
<p class="reader-word-layer reader-word-s1-7" style="width:338px;height:169px;line-height:169px;top:3454px;left:3883px;z-index:268;false">____</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:3454px;left:4219px;z-index:269;">市</p>
<p class="reader-word-layer reader-word-s1-23" style="width:336px;height:169px;line-height:169px;top:3454px;left:4388px;z-index:270;false">____</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:3454px;left:4725px;z-index:271;">街</p>
<p class="reader-word-layer reader-word-s1-7" style="width:338px;height:169px;line-height:169px;top:3454px;left:4892px;z-index:272;false">____</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:3454px;left:5229px;z-index:273;">巷</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:3454px;left:5398px;z-index:274;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:3454px;left:5650px;z-index:275;">号</p>
<p class="reader-word-layer reader-word-s1-7" style="width:505px;height:169px;line-height:169px;top:3454px;left:5819px;z-index:276;letter-spacing:-0.34px;false">______</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:3454px;left:6244px;z-index:277;">（</p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:3454px;left:6412px;z-index:278;false">小区）</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:3454px;left:6839px;z-index:279;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:3454px;left:7089px;z-index:280;">栋</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:3454px;left:7258px;z-index:281;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:338px;height:169px;line-height:169px;top:3454px;left:7510px;z-index:282;false">单元</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:3454px;left:7849px;z-index:284;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:3766px;left:1442px;z-index:285;">楼</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:3766px;left:1611px;z-index:286;false">___</p>
<p class="reader-word-layer reader-word-s1-25" style="width:675px;height:169px;line-height:169px;top:3766px;left:1863px;z-index:287;false">号的房屋</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:3766px;left:2538px;z-index:288;false">___</p>
<p class="reader-word-layer reader-word-s1-20" style="width:1515px;height:169px;line-height:169px;top:3766px;left:2790px;z-index:289;false">间（套），建筑面积</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:3766px;left:4306px;z-index:290;false">___</p>
<p class="reader-word-layer reader-word-s1-15" style="width:1346px;height:169px;line-height:169px;top:3766px;left:4558px;z-index:291;false">平方米、使用面积</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:3766px;left:5904px;z-index:292;false">___</p>
<p class="reader-word-layer reader-word-s1-26" style="width:1009px;height:169px;line-height:169px;top:3766px;left:6156px;z-index:293;false">平方米，类型</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:3766px;left:7164px;z-index:294;false">___</p>
<p class="reader-word-layer reader-word-s1-11" style="width:673px;height:169px;line-height:169px;top:3766px;left:7418px;z-index:296;false">出租给乙</p>
<p class="reader-word-layer reader-word-s1-10" style="width:338px;height:169px;line-height:169px;top:4079px;left:1442px;z-index:297;false">方作</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:4079px;left:1780px;z-index:298;false">___</p>
<p class="reader-word-layer reader-word-s1-20" style="width:1852px;height:169px;line-height:169px;top:4079px;left:2032px;z-index:299;false">使用。装修及设备情况：</p>
<p class="reader-word-layer reader-word-s1-7" style="width:2692px;height:169px;line-height:169px;top:4079px;left:3883px;z-index:301;letter-spacing:-0.44999999999999996px;false">______________________________. </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:4391px;left:1442px;z-index:302;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:4391px;left:1611px;z-index:303;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:4391px;left:1780px;z-index:304;false">第二条</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:4391px;left:2284px;z-index:305;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-11" style="width:673px;height:169px;line-height:169px;top:4391px;left:2369px;z-index:306;false">租赁期限</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:4391px;left:3040px;z-index:308;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:4705px;left:1442px;z-index:309;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:4705px;left:1611px;z-index:310;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-11" style="width:673px;height:169px;line-height:169px;top:4705px;left:1780px;z-index:311;false">租赁期共</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:4705px;left:2453px;z-index:312;false">___</p>
<p class="reader-word-layer reader-word-s1-26" style="width:1009px;height:169px;line-height:169px;top:4705px;left:2705px;z-index:313;false">个月，甲方从</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:4705px;left:3715px;z-index:314;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:4705px;left:3967px;z-index:315;">年</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:4705px;left:4137px;z-index:316;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:4705px;left:4388px;z-index:317;">月</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:4705px;left:4556px;z-index:318;false">___</p>
<p class="reader-word-layer reader-word-s1-20" style="width:2525px;height:169px;line-height:169px;top:4705px;left:4808px;z-index:319;false">日起将出租房屋交付乙方使用，至</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:4705px;left:7333px;z-index:320;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:4705px;left:7585px;z-index:321;">年</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:4705px;left:7754px;z-index:323;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:5016px;left:1442px;z-index:324;">月</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:5016px;left:1611px;z-index:325;false">___</p>
<p class="reader-word-layer reader-word-s1-25" style="width:675px;height:169px;line-height:169px;top:5016px;left:1863px;z-index:326;false">日收回。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5016px;left:2536px;z-index:328;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5330px;left:1442px;z-index:329;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5330px;left:1611px;z-index:330;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-19" style="width:4209px;height:169px;line-height:169px;top:5330px;left:1780px;z-index:331;false">乙方有下列情形之一的，甲方可以终止合同，收回房屋：</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5330px;left:5989px;z-index:333;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5641px;left:1442px;z-index:334;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5641px;left:1611px;z-index:335;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:169px;height:169px;line-height:169px;top:5641px;left:1780px;z-index:336;false">1.</p>
<p class="reader-word-layer reader-word-s1-27" style="width:5388px;height:169px;line-height:169px;top:5641px;left:1948px;z-index:337;false">擅自将房屋转租、分租、转让、转借、联营、入股或与他人调剂交换的；</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5641px;left:7335px;z-index:339;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5955px;left:1442px;z-index:340;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5955px;left:1611px;z-index:341;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:169px;height:169px;line-height:169px;top:5955px;left:1780px;z-index:342;false">2.</p>
<p class="reader-word-layer reader-word-s1-27" style="width:3536px;height:169px;line-height:169px;top:5955px;left:1948px;z-index:343;false">利用承租房屋进行非法活动，损害公共利益的；</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:5955px;left:5483px;z-index:345;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6266px;left:1442px;z-index:346;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6266px;left:1611px;z-index:347;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:169px;height:169px;line-height:169px;top:6266px;left:1780px;z-index:348;false">3.</p>
<p class="reader-word-layer reader-word-s1-25" style="width:675px;height:169px;line-height:169px;top:6266px;left:1948px;z-index:349;false">拖欠租金</p>
<p class="reader-word-layer reader-word-s1-7" style="width:169px;height:169px;line-height:169px;top:6266px;left:2621px;z-index:350;false">__</p>
<p class="reader-word-layer reader-word-s1-20" style="width:842px;height:169px;line-height:169px;top:6266px;left:2790px;z-index:351;false">个月或空置</p>
<p class="reader-word-layer reader-word-s1-7" style="width:169px;height:169px;line-height:169px;top:6266px;left:3633px;z-index:352;false">__</p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:6266px;left:3800px;z-index:353;false">月的。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6266px;left:4304px;z-index:355;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6579px;left:1442px;z-index:356;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6579px;left:1611px;z-index:357;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-10" style="width:4713px;height:169px;line-height:169px;top:6579px;left:1780px;z-index:358;letter-spacing:-0.8300000000000001px;false">合同期满后，如甲方仍继续出租房屋的，乙方拥有优先承租权。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6579px;left:6492px;z-index:360;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6891px;left:1442px;z-index:361;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6891px;left:1611px;z-index:362;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-13 reader-word-s1-18" style="width:673px;height:169px;line-height:169px;top:6891px;left:1780px;z-index:363;letter-spacing:-1.1600000000000001px;false">租赁合同</p>
<p class="reader-word-layer reader-word-s1-15" style="width:1346px;height:169px;line-height:169px;top:6891px;left:2453px;z-index:364;false">因期满而终止时，</p>
<p class="reader-word-layer reader-word-s1-28" style="width:2019px;height:169px;line-height:169px;top:6891px;left:3721px;z-index:365;false">如乙方确实无法找到房屋，</p>
<p class="reader-word-layer reader-word-s1-15" style="width:2523px;height:169px;line-height:169px;top:6891px;left:5662px;z-index:366;false">可与甲方协商酌情延长租赁期限。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:6891px;left:8099px;z-index:368;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:7205px;left:1442px;z-index:369;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:7205px;left:1611px;z-index:370;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:7205px;left:1780px;z-index:371;false">第三条</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:7205px;left:2284px;z-index:372;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-28" style="width:2019px;height:169px;line-height:169px;top:7205px;left:2369px;z-index:373;false">租金、交纳期限和交纳方式</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:7205px;left:4387px;z-index:375;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:7516px;left:1442px;z-index:376;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:7516px;left:1611px;z-index:377;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:1515px;height:169px;line-height:169px;top:7516px;left:1780px;z-index:378;false">甲乙双方议定月租金</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:7516px;left:3294px;z-index:379;false">___</p>
<p class="reader-word-layer reader-word-s1-20" style="width:1178px;height:169px;line-height:169px;top:7516px;left:3546px;z-index:380;false">元，交纳方式为</p>
<p class="reader-word-layer reader-word-s1-23" style="width:336px;height:169px;line-height:169px;top:7516px;left:4725px;z-index:381;false">____</p>
<p class="reader-word-layer reader-word-s1-20" style="width:1852px;height:169px;line-height:169px;top:7516px;left:5062px;z-index:382;false">支付，计人们币（大写）</p>
<p class="reader-word-layer reader-word-s1-7" style="width:1009px;height:169px;line-height:169px;top:7516px;left:6914px;z-index:383;letter-spacing:-0.47px;false">____________</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:7516px;left:7922px;z-index:385;">元</p>
<p class="reader-word-layer reader-word-s1-10" style="width:507px;height:169px;line-height:169px;top:7830px;left:1442px;z-index:386;false">（元）</p>
<p class="reader-word-layer reader-word-s1-25" style="width:675px;height:169px;line-height:169px;top:7830px;left:1929px;z-index:387;false">由乙方在</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:7830px;left:2603px;z-index:388;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:7830px;left:2855px;z-index:389;">年</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:7830px;left:3023px;z-index:390;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:169px;height:169px;line-height:169px;top:7830px;left:3275px;z-index:391;">月</p>
<p class="reader-word-layer reader-word-s1-7" style="width:253px;height:169px;line-height:169px;top:7830px;left:3444px;z-index:392;false">___</p>
<p class="reader-word-layer reader-word-s1-25" style="width:1180px;height:169px;line-height:169px;top:7830px;left:3696px;z-index:393;false">日交纳给甲方。</p>
<p class="reader-word-layer reader-word-s1-10" style="width:844px;height:169px;line-height:169px;top:7830px;left:4856px;z-index:394;letter-spacing:-0.42999999999999994px;false">先付后用。</p>
<p class="reader-word-layer reader-word-s1-25" style="width:675px;height:169px;line-height:169px;top:7830px;left:5679px;z-index:395;false">以后每个</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:7830px;left:6354px;z-index:396;false">___</p>
<p class="reader-word-layer reader-word-s1-10" style="width:1011px;height:169px;line-height:169px;top:7830px;left:6606px;z-index:397;letter-spacing:-0.6900000000000001px;false">月付款一次，</p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:7830px;left:7596px;z-index:399;false">应在付</p>
<p class="reader-word-layer reader-word-s1-25" style="width:675px;height:169px;line-height:169px;top:8141px;left:1442px;z-index:400;false">款期末前</p>
<p class="reader-word-layer reader-word-s1-24" style="width:251px;height:169px;line-height:169px;top:8141px;left:2117px;z-index:401;false">___</p>
<p class="reader-word-layer reader-word-s1-11" style="width:673px;height:169px;line-height:169px;top:8141px;left:2369px;z-index:402;false">天支付。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:8141px;left:3040px;z-index:404;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:8455px;left:1442px;z-index:405;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:8455px;left:1611px;z-index:406;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:8455px;left:1780px;z-index:407;false">第四条</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:8455px;left:2284px;z-index:408;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:1515px;height:169px;line-height:169px;top:8455px;left:2369px;z-index:409;false">租赁期间的房屋修缮</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:8455px;left:3883px;z-index:411;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:8766px;left:1442px;z-index:412;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:8766px;left:1611px;z-index:413;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-29" style="width:6396px;height:169px;line-height:169px;top:8766px;left:1780px;z-index:415;false">甲方对出租房屋及其设备应定期检查，及时修缮，做到不漏、不淹、三通（户内上水、</p>
<p class="reader-word-layer reader-word-s1-10" style="width:5558px;height:169px;line-height:169px;top:9080px;left:1442px;z-index:416;letter-spacing:-0.76px;false">下水、照明电）和门窗好，以保障乙方安全正常使用。乙方应当积极配合。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:9080px;left:6998px;z-index:418;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:9391px;left:1442px;z-index:419;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:9391px;left:1611px;z-index:420;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:9391px;left:1780px;z-index:421;false">第五条</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:9391px;left:2284px;z-index:422;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-11" style="width:1177px;height:169px;line-height:169px;top:9391px;left:2369px;z-index:423;false">租赁双方的变更</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:9391px;left:3546px;z-index:425;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:9705px;left:1442px;z-index:426;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:9705px;left:1611px;z-index:427;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:169px;height:169px;line-height:169px;top:9705px;left:1780px;z-index:428;false">1.</p>
<p class="reader-word-layer reader-word-s1-10" style="width:4042px;height:169px;line-height:169px;top:9705px;left:1948px;z-index:429;letter-spacing:-0.75px;false">如甲方按法定手续程序将房产所有权转移给第三方时，</p>
<p class="reader-word-layer reader-word-s1-10" style="width:1517px;height:169px;line-height:169px;top:9705px;left:5950px;z-index:430;letter-spacing:-0.65px;false">在无约定的情况下，</p>
<p class="reader-word-layer reader-word-s1-25" style="width:675px;height:169px;line-height:169px;top:9705px;left:7427px;z-index:432;false">本合同对</p>
<p class="reader-word-layer reader-word-s1-19" style="width:2021px;height:169px;line-height:169px;top:10017px;left:1442px;z-index:433;false">新的房产所有者继续有效；</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:10017px;left:3464px;z-index:435;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:10330px;left:1442px;z-index:436;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:10330px;left:1611px;z-index:437;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:169px;height:169px;line-height:169px;top:10330px;left:1780px;z-index:438;false">2.</p>
<p class="reader-word-layer reader-word-s1-10" style="width:2357px;height:169px;line-height:169px;top:10330px;left:1948px;z-index:439;letter-spacing:-0.8px;false">乙方需要与第三人互换用房时，</p>
<p class="reader-word-layer reader-word-s1-10" style="width:1684px;height:169px;line-height:169px;top:10330px;left:4225px;z-index:440;letter-spacing:-0.77px;false">应事先征得甲方同意，</p>
<p class="reader-word-layer reader-word-s1-10" style="width:2356px;height:169px;line-height:169px;top:10330px;left:5829px;z-index:441;letter-spacing:-0.9199999999999999px;false">甲方应当支持乙方的合理要求。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:10330px;left:8099px;z-index:443;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:10642px;left:1442px;z-index:444;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:10642px;left:1611px;z-index:445;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:10642px;left:1780px;z-index:446;false">第六条</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:10642px;left:2284px;z-index:447;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-29" style="width:5723px;height:169px;line-height:169px;top:10642px;left:2369px;z-index:449;false">乙方必须遵守当地暂住区域内的各项规章制度。按时交纳水、电气、收视、电</p>
<p class="reader-word-layer reader-word-s1-10" style="width:5827px;height:169px;line-height:169px;top:10955px;left:1442px;z-index:450;letter-spacing:-2.62px;false">话、卫生及物管等费用。乙方的民事纠纷均自行负责。水、电、气底数各是：水</p>
<p class="reader-word-layer reader-word-s1-23" style="width:336px;height:169px;line-height:169px;top:10955px;left:7270px;z-index:451;false">____</p>
<p class="reader-word-layer reader-word-s1-10" style="width:494px;height:169px;line-height:169px;top:10955px;left:7606px;z-index:453;letter-spacing:-6.33px;false">吨，电</p>
<p class="reader-word-layer reader-word-s1-7" style="width:338px;height:169px;line-height:169px;top:11266px;left:1442px;z-index:454;false">____</p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:11266px;left:1780px;z-index:455;false">度，气</p>
<p class="reader-word-layer reader-word-s1-7" style="width:338px;height:169px;line-height:169px;top:11266px;left:2284px;z-index:456;false">____</p>
<p class="reader-word-layer reader-word-s1-10" style="width:338px;height:169px;line-height:169px;top:11266px;left:2621px;z-index:457;false">方。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:11266px;left:2957px;z-index:459;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:11580px;left:1442px;z-index:460;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:11580px;left:1611px;z-index:461;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-20" style="width:505px;height:169px;line-height:169px;top:11580px;left:1780px;z-index:462;false">第七条</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:11580px;left:2284px;z-index:463;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s1-11" style="width:1177px;height:169px;line-height:169px;top:11580px;left:2369px;z-index:464;false">甲方收乙方押金</p>
<p class="reader-word-layer reader-word-s1-7" style="width:338px;height:169px;line-height:169px;top:11580px;left:3546px;z-index:465;false">____</p>
<p class="reader-word-layer reader-word-s1-19" style="width:4209px;height:169px;line-height:169px;top:11580px;left:3883px;z-index:467;false">元，乙方退房时，结清水、电、气费，交还钥匙后，由甲</p>
<p class="reader-word-layer reader-word-s1-25" style="width:1180px;height:169px;line-height:169px;top:11891px;left:1442px;z-index:468;false">方退还乙方押金</p>
<p class="reader-word-layer reader-word-s1-7" style="width:338px;height:169px;line-height:169px;top:11891px;left:2621px;z-index:469;false">____</p>
<p class="reader-word-layer reader-word-s1-10" style="width:338px;height:169px;line-height:169px;top:11891px;left:2957px;z-index:470;false">元。</p>
<p class="reader-word-layer reader-word-s1-7" style="width:84px;height:169px;line-height:169px;top:11891px;left:3294px;z-index:471;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1271px;left:1442px;z-index:267;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1271px;left:1611px;z-index:268;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-5" style="width:505px;height:169px;line-height:169px;top:1271px;left:1780px;z-index:269;false">第八条</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1271px;left:2284px;z-index:270;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-7" style="width:673px;height:169px;line-height:169px;top:1271px;left:2369px;z-index:271;false">违约责任</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1271px;left:3040px;z-index:273;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1585px;left:1442px;z-index:274;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1585px;left:1611px;z-index:275;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:1585px;left:1780px;z-index:276;false">1.</p>
<p class="reader-word-layer reader-word-s2-8" style="width:5388px;height:169px;line-height:169px;top:1585px;left:1948px;z-index:277;false">甲方未按本合同第一、二条的约定向乙方交付符合要求的房屋，负责赔偿</p>
<p class="reader-word-layer reader-word-s2-9" style="width:251px;height:169px;line-height:169px;top:1585px;left:7337px;z-index:278;false">___</p>
<p class="reader-word-layer reader-word-s2-10" style="width:336px;height:169px;line-height:169px;top:1585px;left:7589px;z-index:279;false">元。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1585px;left:7924px;z-index:281;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1897px;left:1442px;z-index:282;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1897px;left:1611px;z-index:283;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:1897px;left:1780px;z-index:284;false">2.</p>
<p class="reader-word-layer reader-word-s2-8" style="width:5388px;height:169px;line-height:169px;top:1897px;left:1948px;z-index:285;false">租赁双方如有一方未履行第四条约定的有关条款的，违约方负责赔偿对方</p>
<p class="reader-word-layer reader-word-s2-9" style="width:251px;height:169px;line-height:169px;top:1897px;left:7337px;z-index:286;false">___</p>
<p class="reader-word-layer reader-word-s2-10" style="width:336px;height:169px;line-height:169px;top:1897px;left:7589px;z-index:287;false">元。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:1897px;left:7924px;z-index:289;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:2210px;left:1442px;z-index:290;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:2210px;left:1611px;z-index:291;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:2210px;left:1780px;z-index:292;false">3.</p>
<p class="reader-word-layer reader-word-s2-5" style="width:1515px;height:169px;line-height:169px;top:2210px;left:1948px;z-index:293;false">乙方逾期交付租金，</p>
<p class="reader-word-layer reader-word-s2-5" style="width:1515px;height:169px;line-height:169px;top:2210px;left:3438px;z-index:294;false">除仍应补交欠租外，</p>
<p class="reader-word-layer reader-word-s2-5" style="width:842px;height:169px;line-height:169px;top:2210px;left:4927px;z-index:295;false">并按租金的</p>
<p class="reader-word-layer reader-word-s2-0 reader-word-s2-12" style="width:336px;height:169px;line-height:169px;top:2210px;left:5769px;z-index:296;font-family:'宋体','37926e78b84ae45c3b358c980020002','宋体';false">___%</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:2210px;left:6104px;z-index:297;">，</p>
<p class="reader-word-layer reader-word-s2-13" style="width:1853px;height:169px;line-height:169px;top:2210px;left:6248px;z-index:299;false">以天数计算向甲方交付违</p>
<p class="reader-word-layer reader-word-s2-3" style="width:507px;height:169px;line-height:169px;top:2522px;left:1442px;z-index:300;false">约金。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:2522px;left:1948px;z-index:302;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:2835px;left:1442px;z-index:303;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:2835px;left:1611px;z-index:304;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:2835px;left:1780px;z-index:305;false">4.</p>
<p class="reader-word-layer reader-word-s2-14" style="width:2694px;height:169px;line-height:169px;top:2835px;left:1948px;z-index:306;false">乙方擅自将承租房屋转给他人使用，</p>
<p class="reader-word-layer reader-word-s2-5" style="width:2188px;height:169px;line-height:169px;top:2835px;left:4617px;z-index:307;false">甲方有权责令停止转让行为，</p>
<p class="reader-word-layer reader-word-s2-5" style="width:1178px;height:169px;line-height:169px;top:2835px;left:6781px;z-index:308;false">终止租赁合同。</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:2835px;left:7933px;z-index:310;">同</p>
<p class="reader-word-layer reader-word-s2-15" style="width:1180px;height:169px;line-height:169px;top:3147px;left:1442px;z-index:311;false">时按约定租金的</p>
<p class="reader-word-layer reader-word-s2-0" style="width:338px;height:169px;line-height:169px;top:3147px;left:2621px;z-index:312;false">___%</p>
<p class="reader-word-layer reader-word-s2-3" style="width:3032px;height:169px;line-height:169px;top:3147px;left:2957px;z-index:313;letter-spacing:-0.71px;false">，以天数计算由乙方向甲方支付违约金。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:3147px;left:5989px;z-index:315;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:3460px;left:1442px;z-index:316;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:3460px;left:1611px;z-index:317;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:3460px;left:1780px;z-index:318;false">5.</p>
<p class="reader-word-layer reader-word-s2-3" style="width:5161px;height:169px;line-height:169px;top:3460px;left:1948px;z-index:319;letter-spacing:-2.6100000000000003px;false">本合同期满时，乙方未经甲方同意，继续使用承租房屋，按约定租金的</p>
<p class="reader-word-layer reader-word-s2-0" style="width:338px;height:169px;line-height:169px;top:3460px;left:7110px;z-index:320;false">___%</p>
<p class="reader-word-layer reader-word-s2-3" style="width:655px;height:169px;line-height:169px;top:3460px;left:7447px;z-index:322;letter-spacing:-6.6000000000000005px;false">，以天数</p>
<p class="reader-word-layer reader-word-s2-3" style="width:4211px;height:169px;line-height:169px;top:3771px;left:1442px;z-index:323;letter-spacing:-0.72px;false">计算向甲方支付违约金后，甲方仍有终止合同的申诉权。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:3771px;left:5652px;z-index:325;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4085px;left:1442px;z-index:326;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4085px;left:1611px;z-index:327;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-5" style="width:505px;height:169px;line-height:169px;top:4085px;left:1780px;z-index:328;false">第九条</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4085px;left:2284px;z-index:329;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-7" style="width:673px;height:169px;line-height:169px;top:4085px;left:2369px;z-index:330;false">免责条款</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4085px;left:3040px;z-index:332;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4397px;left:1442px;z-index:333;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4397px;left:1611px;z-index:334;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:4397px;left:1780px;z-index:335;false">1.</p>
<p class="reader-word-layer reader-word-s2-16" style="width:5894px;height:169px;line-height:169px;top:4397px;left:1948px;z-index:336;false">房屋如因不可抗拒的原因导致损毁或造成乙方损失的，甲乙双方互不承担责任。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4397px;left:7841px;z-index:338;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4710px;left:1442px;z-index:339;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4710px;left:1611px;z-index:340;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:4710px;left:1780px;z-index:341;false">2.</p>
<p class="reader-word-layer reader-word-s2-8" style="width:6062px;height:169px;line-height:169px;top:4710px;left:1948px;z-index:342;false">因市政建设需要拆除或改造已租赁的房屋，使甲乙双方造成损失，互不承担责任。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:4710px;left:8008px;z-index:344;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5022px;left:1442px;z-index:345;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5022px;left:1611px;z-index:346;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-3" style="width:4883px;height:169px;line-height:169px;top:5022px;left:1780px;z-index:347;letter-spacing:-0.8px;false">因上述原因而终止合同的，租金按实际使用时间计算，多退少补。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5022px;left:6662px;z-index:349;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5335px;left:1442px;z-index:350;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5335px;left:1611px;z-index:351;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-5" style="width:505px;height:169px;line-height:169px;top:5335px;left:1780px;z-index:352;false">第十条</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5335px;left:2284px;z-index:353;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-7" style="width:1177px;height:169px;line-height:169px;top:5335px;left:2369px;z-index:354;false">争议解决的方式</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5335px;left:3546px;z-index:356;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5647px;left:1442px;z-index:357;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5647px;left:1611px;z-index:358;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-5" style="width:2188px;height:169px;line-height:169px;top:5647px;left:1780px;z-index:359;false">本合同在履行中如发生争议，</p>
<p class="reader-word-layer reader-word-s2-17" style="width:1348px;height:169px;line-height:169px;top:5647px;left:3942px;z-index:360;false">双方应协商解决；</p>
<p class="reader-word-layer reader-word-s2-18" style="width:1009px;height:169px;line-height:169px;top:5647px;left:5265px;z-index:361;false">协商不成时，</p>
<p class="reader-word-layer reader-word-s2-5" style="width:1852px;height:169px;line-height:169px;top:5647px;left:6250px;z-index:363;false">任何一方均可向房屋租赁</p>
<p class="reader-word-layer reader-word-s2-19" style="width:1517px;height:169px;line-height:169px;top:5960px;left:1442px;z-index:364;false">管理机关申请调解，</p>
<p class="reader-word-layer reader-word-s2-13" style="width:1011px;height:169px;line-height:169px;top:5960px;left:2904px;z-index:365;false">调解无效时，</p>
<p class="reader-word-layer reader-word-s2-14" style="width:2694px;height:169px;line-height:169px;top:5960px;left:3859px;z-index:366;false">可向经济合同仲裁委员会申请仲裁，</p>
<p class="reader-word-layer reader-word-s2-15" style="width:675px;height:169px;line-height:169px;top:5960px;left:6498px;z-index:367;false">也可向人</p>
<p class="reader-word-layer reader-word-s2-11" style="width:336px;height:169px;line-height:169px;top:5960px;left:7172px;z-index:368;color:#0000ff;false">民法</p>
<p class="reader-word-layer reader-word-s2-15" style="width:675px;height:169px;line-height:169px;top:5960px;left:7508px;z-index:369;false">院起诉。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:5960px;left:8099px;z-index:371;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:6272px;left:1442px;z-index:372;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:6272px;left:1611px;z-index:373;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-7" style="width:673px;height:169px;line-height:169px;top:6272px;left:1780px;z-index:374;false">第十一条</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:6272px;left:2453px;z-index:375;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-18" style="width:1009px;height:169px;line-height:169px;top:6272px;left:2536px;z-index:376;false">其他约定事宜</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:6272px;left:3546px;z-index:378;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:6585px;left:1442px;z-index:379;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:6585px;left:1611px;z-index:381;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-20" style="width:6646px;height:169px;line-height:169px;top:6897px;left:1442px;z-index:383;false">1.___________________________________________________________________________. </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:7211px;left:1442px;z-index:384;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:7211px;left:1611px;z-index:386;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-20" style="width:6646px;height:169px;line-height:169px;top:7522px;left:1442px;z-index:388;false">2.___________________________________________________________________________. </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:7835px;left:1442px;z-index:389;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:7835px;left:1611px;z-index:390;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-7" style="width:673px;height:169px;line-height:169px;top:7835px;left:1780px;z-index:391;false">第十二条</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:7835px;left:2453px;z-index:392;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-14" style="width:3031px;height:169px;line-height:169px;top:7835px;left:2536px;z-index:393;false">本合同未尽事宜，甲乙双方可共同协商。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:7835px;left:5566px;z-index:395;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8147px;left:1442px;z-index:396;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8147px;left:1611px;z-index:397;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-3" style="width:840px;height:169px;line-height:169px;top:8147px;left:1780px;z-index:398;letter-spacing:-1.3px;false">本合同一式</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8147px;left:2663px;z-index:399;">2</p>
<p class="reader-word-layer reader-word-s2-5" style="width:1178px;height:169px;line-height:169px;top:8147px;left:2790px;z-index:400;false">份，甲乙方各执</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8147px;left:4012px;z-index:401;">1</p>
<p class="reader-word-layer reader-word-s2-14" style="width:3031px;height:169px;line-height:169px;top:8147px;left:4137px;z-index:402;false">份。从签字之日起生效，到期自动作废。</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8147px;left:7168px;z-index:404;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8460px;left:1442px;z-index:405;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8460px;left:1611px;z-index:406;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-3" style="width:1346px;height:169px;line-height:169px;top:8460px;left:1780px;z-index:407;letter-spacing:-0.99px;false">甲方（签字盖章）</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8460px;left:3127px;z-index:408;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8460px;left:3294px;z-index:409;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:926px;height:169px;line-height:169px;top:8460px;left:3464px;z-index:410;letter-spacing:-0.34px;false">           </p>
<p class="reader-word-layer reader-word-s2-17" style="width:1348px;height:169px;line-height:169px;top:8460px;left:4388px;z-index:411;false">乙方（签字盖章）</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8460px;left:5735px;z-index:413;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8772px;left:1442px;z-index:414;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8772px;left:1611px;z-index:415;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-18" style="width:1009px;height:169px;line-height:169px;top:8772px;left:1780px;z-index:416;false">身份证号码：</p>
<p class="reader-word-layer reader-word-s2-21" style="width:167px;height:169px;line-height:169px;top:8772px;left:2790px;z-index:417;false">  </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8772px;left:3042px;z-index:418;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:1177px;height:169px;line-height:169px;top:8772px;left:3212px;z-index:419;letter-spacing:-0.53px;false">              </p>
<p class="reader-word-layer reader-word-s2-18" style="width:1009px;height:169px;line-height:169px;top:8772px;left:4388px;z-index:420;false">身份证号码：</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:8772px;left:5398px;z-index:422;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9085px;left:1442px;z-index:423;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9085px;left:1611px;z-index:424;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-5" style="width:842px;height:169px;line-height:169px;top:9085px;left:1780px;z-index:425;false">联系电话：</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9085px;left:2621px;z-index:426;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9085px;left:2790px;z-index:427;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-22" style="width:1430px;height:169px;line-height:169px;top:9085px;left:2957px;z-index:428;false">                 </p>
<p class="reader-word-layer reader-word-s2-5" style="width:842px;height:169px;line-height:169px;top:9085px;left:4388px;z-index:429;false">联系电话：</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9085px;left:5229px;z-index:431;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9397px;left:1442px;z-index:432;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9397px;left:1611px;z-index:433;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-5" style="width:505px;height:169px;line-height:169px;top:9397px;left:1780px;z-index:434;false">住址：</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9397px;left:2284px;z-index:435;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9397px;left:2453px;z-index:436;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-22" style="width:1767px;height:169px;line-height:169px;top:9397px;left:2621px;z-index:437;false">                     </p>
<p class="reader-word-layer reader-word-s2-5" style="width:505px;height:169px;line-height:169px;top:9397px;left:4388px;z-index:438;false">住址：</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9397px;left:4892px;z-index:440;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9710px;left:1442px;z-index:441;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9710px;left:1611px;z-index:442;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-9" style="width:251px;height:169px;line-height:169px;top:9710px;left:1780px;z-index:443;false">   </p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:9710px;left:2032px;z-index:444;">年</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9710px;left:2202px;z-index:445;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:9710px;left:2284px;z-index:446;">月</p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:9710px;left:2453px;z-index:447;false">  </p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:9710px;left:2621px;z-index:448;">日</p>
<p class="reader-word-layer reader-word-s2-21" style="width:167px;height:169px;line-height:169px;top:9710px;left:2790px;z-index:449;false">  </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9710px;left:3042px;z-index:450;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:1429px;height:169px;line-height:169px;top:9710px;left:3212px;z-index:451;letter-spacing:-0.54px;false">                 </p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:9710px;left:4640px;z-index:452;">年</p>
<p class="reader-word-layer reader-word-s2-21" style="width:167px;height:169px;line-height:169px;top:9710px;left:4810px;z-index:453;false">  </p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:9710px;left:4977px;z-index:454;">月</p>
<p class="reader-word-layer reader-word-s2-21" style="width:249px;height:169px;line-height:169px;top:9710px;left:5146px;z-index:455;false">   </p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:9710px;left:5396px;z-index:456;">日</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:9710px;left:5564px;z-index:458;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-19" style="width:1517px;height:169px;line-height:169px;top:10022px;left:1442px;z-index:459;false">附件：房屋大件清单</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10022px;left:2957px;z-index:461;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10336px;left:1442px;z-index:462;">1</p>
<p class="reader-word-layer reader-word-s2-3" style="width:842px;height:169px;line-height:169px;top:10336px;left:1527px;z-index:463;letter-spacing:-0.8999999999999999px;false">、格力空调</p>
<p class="reader-word-layer reader-word-s2-0" style="width:588px;height:169px;line-height:169px;top:10336px;left:2369px;z-index:464;letter-spacing:-0.59px;false">      2</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:10336px;left:3000px;z-index:465;">部</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10336px;left:3167px;z-index:467;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10647px;left:1442px;z-index:468;">2</p>
<p class="reader-word-layer reader-word-s2-3" style="width:674px;height:169px;line-height:169px;top:10647px;left:1527px;z-index:469;letter-spacing:-0.62px;false">、热水器</p>
<p class="reader-word-layer reader-word-s2-0" style="width:842px;height:169px;line-height:169px;top:10647px;left:2200px;z-index:470;letter-spacing:-0.39px;false">         1</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:10647px;left:3083px;z-index:471;">件</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10647px;left:3250px;z-index:473;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10961px;left:1442px;z-index:474;">3</p>
<p class="reader-word-layer reader-word-s2-16" style="width:1348px;height:169px;line-height:169px;top:10961px;left:1527px;z-index:475;false">、海尔滚筒洗衣机</p>
<p class="reader-word-layer reader-word-s2-0" style="width:254px;height:169px;line-height:169px;top:10961px;left:2873px;z-index:476;letter-spacing:0.21999999999999997px;false">  1</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:10961px;left:3167px;z-index:477;">部</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10961px;left:3335px;z-index:479;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11272px;left:1442px;z-index:480;">4</p>
<p class="reader-word-layer reader-word-s2-16" style="width:1348px;height:169px;line-height:169px;top:11272px;left:1527px;z-index:481;false">、海信冰箱（新）</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11272px;left:2873px;z-index:482;">1</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:11272px;left:3000px;z-index:483;">部</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11272px;left:3167px;z-index:485;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11586px;left:1442px;z-index:486;">5</p>
<p class="reader-word-layer reader-word-s2-3" style="width:1009px;height:169px;line-height:169px;top:11586px;left:1527px;z-index:487;letter-spacing:-1.06px;false">、沁园饮水机</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11586px;left:2578px;z-index:488;">1</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:11586px;left:2705px;z-index:489;">部</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11586px;left:2873px;z-index:491;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11897px;left:1442px;z-index:492;">6</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:11897px;left:1527px;z-index:493;">、</p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:11897px;left:1694px;z-index:494;false">42</p>
<p class="reader-word-layer reader-word-s2-18" style="width:1009px;height:169px;line-height:169px;top:11897px;left:1905px;z-index:495;false">寸平板电视机</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11897px;left:2957px;z-index:496;">1</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:11897px;left:3083px;z-index:497;">部</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11897px;left:3250px;z-index:499;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10336px;left:5058px;z-index:500;">7</p>
<p class="reader-word-layer reader-word-s2-3" style="width:1178px;height:169px;line-height:169px;top:10336px;left:5143px;z-index:501;letter-spacing:-0.8799999999999999px;false">、老板抽油烟机</p>
<p class="reader-word-layer reader-word-s2-21" style="width:167px;height:169px;line-height:169px;top:10336px;left:6321px;z-index:502;false"> 1</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:10336px;left:6531px;z-index:503;">部</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10336px;left:6698px;z-index:505;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10647px;left:5058px;z-index:506;">8</p>
<p class="reader-word-layer reader-word-s2-3" style="width:673px;height:169px;line-height:169px;top:10647px;left:5143px;z-index:507;letter-spacing:-1.18px;false">、实木床</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10647px;left:5858px;z-index:508;">3</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:10647px;left:5985px;z-index:509;">张</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10647px;left:6152px;z-index:511;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10961px;left:5058px;z-index:512;">9</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:10961px;left:5143px;z-index:513;">、</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10961px;left:5310px;z-index:514;">3</p>
<p class="reader-word-layer reader-word-s2-5" style="width:505px;height:169px;line-height:169px;top:10961px;left:5437px;z-index:515;false">人沙发</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10961px;left:5985px;z-index:516;">1</p>
<p class="reader-word-layer reader-word-s2-5" style="width:842px;height:169px;line-height:169px;top:10961px;left:6110px;z-index:517;false">张带小茶几</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:10961px;left:6950px;z-index:519;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:11272px;left:5058px;z-index:520;false">10</p>
<p class="reader-word-layer reader-word-s2-23" style="width:505px;height:169px;line-height:169px;top:11272px;left:5227px;z-index:521;false">、餐桌</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11272px;left:5775px;z-index:522;">1</p>
<p class="reader-word-layer reader-word-s2-10" style="width:336px;height:169px;line-height:169px;top:11272px;left:5900px;z-index:523;false">张带</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11272px;left:6279px;z-index:524;">4</p>
<p class="reader-word-layer reader-word-s2-5" style="width:842px;height:169px;line-height:169px;top:11272px;left:6406px;z-index:525;false">把实木椅子</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11272px;left:7247px;z-index:527;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:11586px;left:5058px;z-index:528;false">11</p>
<p class="reader-word-layer reader-word-s2-23" style="width:505px;height:169px;line-height:169px;top:11586px;left:5227px;z-index:529;false">、窗帘</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11586px;left:5775px;z-index:530;">4</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:11586px;left:5900px;z-index:531;">付</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11586px;left:6067px;z-index:533;font-family:simsun;"> </p>
<p class="reader-word-layer reader-word-s2-0" style="width:169px;height:169px;line-height:169px;top:11897px;left:5058px;z-index:534;false">12</p>
<p class="reader-word-layer reader-word-s2-23" style="width:505px;height:169px;line-height:169px;top:11897px;left:5227px;z-index:535;false">、衣柜</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11897px;left:5775px;z-index:536;">4</p>
<p class="reader-word-layer reader-word-s2-5" style="width:505px;height:169px;line-height:169px;top:11897px;left:5900px;z-index:537;false">个书柜</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11897px;left:6448px;z-index:538;">1</p>
<p class="reader-word-layer reader-word-s2-3" style="width:169px;height:169px;line-height:169px;top:11897px;left:6573px;z-index:539;">个</p>
<p class="reader-word-layer reader-word-s2-0" style="width:84px;height:169px;line-height:169px;top:11897px;left:6741px;z-index:540;font-family:simsun;"> </p></div>
'''
obj = re.compile('>(.*?)<')
lis = obj.findall(a,re.S)
lis = [re.sub('\u2002', '', x) for x in lis]
lis = [x for x in lis if len(x)>0]

def makeWorkFile(path, lis):
    word = win32com.client.Dispatch('Word.Application')#打开word软件
    #让文档可见
    word.Visible = True
    #创建文档
    doc = word.Documents.Add()
    #写内容
    #从头开始写
    r = doc.Range(0, 0) #光标定位到最开始
    for li in lis:
        r.InsertAfter(li)
        if '。' in li or '.' in li:
            r.InsertAfter('\n')
    #存储文件
    doc.SaveAs(path)
    #关闭文件
    doc.Close()
    #退出软件
    word.Quit()

path = r'C:\Users\Administrator\Desktop\租房管理\租房模板.docx'
makeWorkFile(path, lis)