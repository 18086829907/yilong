import logging

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # log等级总开关


# 第二步，创建一个handler，用于写入日志文件
logfile = './log.txt'
fh = logging.FileHandler(logfile, mode='a')  # open的打开模式
fh.setLevel(logging.DEBUG)  # 输出到file的log等级开关


# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到console的log等级开关


# 第四步，定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)


# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)


# 日志
logger.debug('this is debug message')
logger.info('this is info message')
logger.warning('this is warning message')
logger.error('this is error message')
logger.critical('this is critical message')
