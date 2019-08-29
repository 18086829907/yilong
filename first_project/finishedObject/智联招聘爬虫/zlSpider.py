import urllib.request
import urllib.parse
import json
import jsonpath
import pandas as pd
import time
import random

GjobName = []
GjobCity = []
GupdateDate = []
Gsalary = []
Gdistance = []
GeduLevel = []
GjobType = []
GfeedbackRation = []
GemplType = []
GpositionURL = []
Gwelfare = []
GtimeState = []
Gcompany = []
GcompanyType = []
GcompanySize = []
GcompanyUrl = []
GcompanyLogo = []
GbusinessArea = []


def saveDataFrame(cityId, wk):
    # 创建pandas
    dataFrame = pd.DataFrame({
        '岗位名称': GjobName,
        '工作城市': GjobCity,
        '更新时间': GupdateDate,
        '薪资待遇': Gsalary,
        '工作地点': Gdistance,
        '学历要求': GeduLevel,
        '岗位类型': GjobType,
        '响应速度': GfeedbackRation,
        '雇员类型': GemplType,
        '岗位详情': GpositionURL,
        '雇员福利': Gwelfare,
        '岗位状态': GtimeState,
        '公司名字': Gcompany,
        '公司体制': GcompanyType,
        '在职员工': GcompanySize,
        '公司详情': GcompanyUrl,
        '公司logo': GcompanyLogo,
        '商圈范围': GbusinessArea,
    })
    dataFrame.to_excel('城市编号{}的{}岗位.xlsx'.format(cityId, wk), encoding='utf8')
    return dataFrame

class zlSpider():
    def __init__(self, url, page, cityId, wk):
        self.url = url
        self.page = 90*page
        self.cityId = cityId
        self.wk = wk
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',}

    def jsonPath(self, obj):
        #解析json数据
        jobName = jsonpath.jsonpath(obj, '$..results[*].jobName')
        jobCity = jsonpath.jsonpath(obj, '$..results[*].city.display')
        updateDate = jsonpath.jsonpath(obj, '$..results[*].updateDate')
        salary = jsonpath.jsonpath(obj, '$..results[*].salary')
        distance = jsonpath.jsonpath(obj, '$..results[*].distance')
        eduLevel = jsonpath.jsonpath(obj, '$..results[*].eduLevel.name')
        jobType = jsonpath.jsonpath(obj, '$..results[*].jobType.items[*].name')
        feedbackRation = jsonpath.jsonpath(obj, '$..results[*].feedbackRation')
        emplType = jsonpath.jsonpath(obj, '$..results[*].emplType')
        positionURL = jsonpath.jsonpath(obj, '$..results[*].positionURL')
        welfare = jsonpath.jsonpath(obj, '$..results[*].welfare')
        timeState = jsonpath.jsonpath(obj, '$..results[*].timeState')
        company = jsonpath.jsonpath(obj, '$..results[*].company.name')
        companyType = jsonpath.jsonpath(obj, '$..results[*].company.type.name')
        companySize = jsonpath.jsonpath(obj, '$..results[*].company.size.name')
        companyUrl = jsonpath.jsonpath(obj, '$..results[*].company.url')
        companyLogo = jsonpath.jsonpath(obj, '$..results[*].companyLogo')
        businessArea = jsonpath.jsonpath(obj, '$..results[*].businessArea')
        #添加到全局变量中
        GjobName.extend(jobName)
        GjobCity.extend(jobCity)
        GupdateDate.extend(updateDate)
        Gsalary.extend(salary)
        Gdistance.extend(distance)
        GeduLevel.extend(eduLevel)
        GjobType.extend(jobType)
        GfeedbackRation.extend(feedbackRation)
        GemplType.extend(emplType)
        GpositionURL.extend(positionURL)
        Gwelfare.extend(welfare)
        GtimeState.extend(timeState)
        Gcompany.extend(company)
        GcompanyType.extend(companyType)
        GcompanySize.extend(companySize)
        GcompanyUrl.extend(companyUrl)
        GcompanyLogo.extend(companyLogo)
        GbusinessArea.extend(businessArea)

    def handler_request(self):
        url_new = self.url.format(self.page, self.cityId, self.wk)
        request = urllib.request.Request(url=url_new, headers=self.headers)
        return request

    def run(self):
        request = self.handler_request()
        json_txt = urllib.request.urlopen(request).read().decode()
        #解析json
        obj = json.loads(json_txt)
        #将遍历的所有数据保存到全局变量中
        self.jsonPath(obj)

def main():
    url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId={}&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&=0&at=fb56e0ff848b454d96b3aed7969c99af&rt=eaafa995cb03407293c812875876150a&_v=0.69207691&userCode=1025306053&x-zp-page-request-id=154a76fd6db2456384fdb8a8bc55b640-1562203709996-356095&x-zp-client-id=611bd170-7446-44da-9490-40b81d4cb975'
    start_page = int(input('开始页：'))
    end_page = int(input('结束页：'))
    cityId = int(input('城市编号：'))
    wk = input('搜索关键字：')
    #遍历所有页，得到dataFrame，可以调用dataFrame()函数返回总的dataFrame数据
    for page in range(start_page, end_page+1):
        spider = zlSpider(url, page, cityId, wk)
        spider.run()
        time.sleep(random.random()*10)
    saveDataFrame(cityId, wk)

if __name__ == '__main__':
    main()