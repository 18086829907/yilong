# 【直接将信息打印到终端】
import logging
logging.basicConfig(  # logging的基础配置信息
    level=logging.ERROR,  # logging的级别设置，用于控制输出哪个级别的信息，规则为输出指定级别及以上级别的信息
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(levelname)s - %(message)s'  # 输出信息的格式
)   # 格式：年月日时分秒毫秒 - 文件名代码行 - 信息级别输出信息

logging.debug('this is debug message')  # logging.debug表示'this is debug message'这条信息是debug级别的信息，当logging的级别设置为DEBUG时，终端会打印这条信息
logging.info('this is info message')  # logging.info表示'this is info message'这条信息是info级别的信息，当logging的级别设置为DEBUG或INFO时，终端会打印这条信息
logging.warning('this is warning message')  # 基本同上
logging.error('this is error message')  # 基本同上
logging.critical('this is critical message')  # 基本同上

# 在开发环境中，你在哪个位置写上logging.xxx(yyy)，终端就会在此处打印yyy的信息，可以简单理解为print()
