import pandas as pd
#订单个人信息
orderReport_tb40319388 = pd.read_excel(r'C:\Users\justin\DataGit\yilong\first_project\finishedObject\淘宝自动化管理\订单详情\淘宝自动生成信息\tb40319388\订单个人信息_2019_11_11.xlsx')
orderReport_父爱如山jjkk = pd.read_excel(r'C:\Users\justin\DataGit\yilong\first_project\finishedObject\淘宝自动化管理\订单详情\淘宝自动生成信息\父爱如山jjkk\订单个人信息_2019_11_11.xlsx')
#三创飞梦_订单信息
orderReport_scfm = pd.read_excel(r'C:\Users\justin\DataGit\yilong\first_project\finishedObject\淘宝自动化管理\订单详情\三创飞梦_订单信息.xlsx')

def myMerge(tbOrder, scOrder):
    #过滤无效字段
    tbOrder = tbOrder[['订单编号', '买家会员名', '买家支付宝账号', '支付单号', '买家实际支付金额', '订单状态', '收货人姓名', '联系手机', '订单创建时间', '订单付款时间 ', '宝贝标题 ', '物流单号 ', '物流公司', '店铺名称', '退款金额', '确认收货时间']]
    #合并数据
    report = pd.merge(tbOrder, scOrder, how='left', left_on='物流单号 ', right_on='物流单号')
    #计算利润
    porfit = report['买家实际支付金额'] - report['进货总价']
    report['利润'] = porfit
    return report

#生成各店报表
report1 = myMerge(orderReport_tb40319388, orderReport_scfm)
report2 = myMerge(orderReport_父爱如山jjkk, orderReport_scfm)

#合并所有店铺报表
report = pd.concat([report1,report2])

#导出数据
report.to_excel('./完整报表/2019_11_11.xlsx')