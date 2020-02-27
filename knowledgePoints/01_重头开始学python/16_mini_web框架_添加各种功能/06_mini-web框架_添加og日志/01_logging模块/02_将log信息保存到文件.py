# 【将log日志存放到文件中】
import logging
logging.basicConfig(
    filename='./log.txt',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(levelname)s - %(message)s'
)

logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is warning message')
logging.error('this is error message')
logging.critical('this is critical message')