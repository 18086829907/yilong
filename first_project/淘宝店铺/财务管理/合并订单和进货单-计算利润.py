import pandas as pd

#客户订单
khdd_tb40319388 = pd.read_excel(r'C:\Users\justin\DataGit\yilong\first_project\淘宝店铺\财务管理\1、客户订单\tb40319388\2019_11_30.xlsx')
khdd_父爱如山jjkk = pd.read_excel(r'C:\Users\justin\DataGit\yilong\first_project\淘宝店铺\财务管理\1、客户订单\父爱如山jjkk\2019_11_11.xlsx')

#进货单 注意进货单需要手动将订单编号修改为对应的客户订单编号
tbsj_jhd = pd.read_excel(r'C:\Users\justin\DataGit\yilong\first_project\淘宝店铺\财务管理\2、进货单\淘宝上家进货单\淘宝上家进货单.xlsx')
# scfm_jhd = pd.read_excel(r'C:\Users\justin\DataGit\yilong\first_project\淘宝店铺\财务管理\2、进货单\三创飞梦进货单\三创飞梦.xlsx')

#正式报表
zsbb = pd.read_excel(r'C:\Users\justin\DataGit\yilong\first_project\淘宝店铺\财务管理\3、正式报表\allData.xlsx')
zsbb.reset_index(drop=True,inplace=True)

def jslr(khdd, jhd): #计算利润
    #提取客户订单中的有效字段
    khdd = khdd[['订单编号', '买家会员名', '买家支付宝账号', '支付单号', '买家实际支付金额', '订单状态', '收货人姓名', '联系手机', '订单创建时间', '订单付款时间 ', '宝贝标题 ', '物流单号 ', '物流公司', '店铺名称', '退款金额', '确认收货时间']]
    jhd = jhd[['订单编号','进货总价','省','市','区','地']]
    #合并客户订单和进货单
    report = pd.merge(khdd, jhd, how='left', left_on='订单编号', right_on='订单编号')
    #计算利润
    porfit = report['买家实际支付金额'] - report['进货总价']
    report['利润'] = porfit
    return report

#生成各店报表
report1 = jslr(khdd_tb40319388, tbsj_jhd)
report2 = jslr(khdd_父爱如山jjkk, tbsj_jhd)

#将数据合并到正式报表
report = pd.concat([zsbb,report1])
report.reset_index(drop=True, inplace=True)

#导出数据
report.to_excel(r'C:\Users\justin\DataGit\yilong\first_project\淘宝店铺\财务管理\3、正式报表\allData1.xlsx')
