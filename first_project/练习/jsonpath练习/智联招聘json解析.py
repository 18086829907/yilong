import json
import jsonpath
obj = json.load(open('智联招聘.json', 'r', encoding='utf8'))

#工作信息
jobName = jsonpath.jsonpath(obj, '$..results[*].jobName')
jobCity = jsonpath.jsonpath(obj, '$..results[*].city.display')
updateDate = jsonpath.jsonpath(obj, '$..results[*].updateDate')
salary = jsonpath.jsonpath(obj, '$..results[*].salary')
distance = jsonpath.jsonpath(obj, '$..results[*].distance')
eduLevel = jsonpath.jsonpath(obj, '$..results[*].eduLevel.name')
jobType = jsonpath.jsonpath(obj, '$..results[*].jobType.items[*].name')
feedbackRation = jsonpath.jsonpath(obj, '$..results[*].feedbackRation')
# workingExp = jsonpath练习.jsonpath练习(obj, '$..results[*].workingExp.name') #数据缺失
emplType = jsonpath.jsonpath(obj, '$..results[*].emplType')
positionURL = jsonpath.jsonpath(obj, '$..results[*].positionURL')
welfare = jsonpath.jsonpath(obj, '$..results[*].welfare')
timeState = jsonpath.jsonpath(obj, '$..results[*].timeState')

#公司信息
company = jsonpath.jsonpath(obj, '$..results[*].company.name')
companyType = jsonpath.jsonpath(obj, '$..results[*].company.type.name')
companySize = jsonpath.jsonpath(obj, '$..results[*].company.size.name')
companyUrl = jsonpath.jsonpath(obj, '$..results[*].company.url')
companyLogo = jsonpath.jsonpath(obj, '$..results[*].companyLogo')
businessArea = jsonpath.jsonpath(obj, '$..results[*].businessArea')
