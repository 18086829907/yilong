# -*- coding:utf8 -*-

import re


def main():
    html = '''<dl class="job_detail" id="job_detail">
        <dt class="clearfix join_tc_icon">
        </dt>
        <dd class="job-advantage">
            <span class="advantage">职位诱惑：</span>
            <p>周末双休，无加班，办公环境好，氛围好。</p>
        </dd>
        <dd class="job_bt">
            <h3 class="description">职位描述：</h3>
            <div class="job-detail">
            <p>岗位职责：</p><p>*&nbsp;研发高效可靠的数据平台；</p><p>*&nbsp;研发灵活易用的研究平台；</p><p>*&nbsp;为策略研究和系统开发提供技术支持。</p><p><br></p><p>任职要求：</p><p>*&nbsp;计算机、数学、物理、统计、金融等相关专业，本科或以上学历；</p><p>*&nbsp;三年以上Python&nbsp;WEB开发经验，精通Django、Tornado、web.py、Flask等至少一个Python&nbsp;WEB框架；</p><p>*&nbsp;熟练掌握HTML、CSS、JS等前端技术；</p><p>*&nbsp;熟悉Linux环境，熟练掌握MySQL数据库及其它Redis、MongoDB等NOSQL数据库；</p><p>*&nbsp;热爱技术工作，能独立承担项目开发工作，具备良好的团队协作能力、自我驱动能力和沟通协调能力。</p><p><br></p><p>具有以下条件之一或以上者优先考虑：</p><p>*&nbsp;熟悉c++编程，能够使用Cython或pybind11进行python和c++混合编程；</p><p>*&nbsp;处理过金融高频数据，或有金融市场投资经验；</p><p>*&nbsp;持续开发和维护github项目，个人项目或者开源项目均可（请在简历中附上项目地址）。</p>
            </div>
        </dd>
    '''
    res = re.sub(r'<.*?>|\*|&nbsp;|\s', '', html)
    print(res)
    return res

if __name__ == '__main__':
    main()




