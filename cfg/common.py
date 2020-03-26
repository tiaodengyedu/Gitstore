from robot.libraries.BuiltIn import logger

GSTORE={}

def INFO(info):
    '''
    在运行终端和测试报告中打印重要信息
    使报告更清晰
    参数：
    info：信息描述
    '''
    logger.info(f'{info}',True,True)

def STEP(stepNo,desc):
    '''
    在运行终端和测试报告中打印 测试步骤说明
    使报告更清晰
    :param stepNo: 指定 是第几步
    :param des: 步骤说明

    '''
    logger.info(f'\n-- 第 {stepNo} 步 -- {desc} \n',True,True)

def CHECKPOINT(desc,condition):
    '''
    检查点
    :param desc:    检查点文字描述
    :param condition:  检查点表达式

    '''
    logger.info( f'\n **检查点** {desc}',True,True)
    if condition:
        logger.info('-->通过\n',True,True)
    else:
        logger.info('-->!!不通过!!\n',True,True)
        raise  AssertionError (f'\n ** 检查点不通过 ** {desc}')