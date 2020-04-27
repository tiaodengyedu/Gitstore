from robot.libraries.BuiltIn import logger

GSTORE = {}


def ERROR(info):
    """
    在运行终端和测试报告中打印 错误信息，
    使得 运行报告更加清晰

    参数：

    info: 信息描述
    """
    logger.error(f'{info}', True)

def INFO(info):
    """
    在运行终端和测试报告中打印 重要信息，
    使得 运行报告更加清晰

    参数：

    info: 信息描述
    """
    logger.info(f'{info}', True, True)


def STEP(stepNo, desc):
    """


    stepNo:
    desc:
    """
    logger.info(f'\n-- 第 {stepNo} 步 -- {desc} \n', True, True)


def CHECK_POINT(desc, condition):
    """

    desc:
    condition:
    """

    logger.info(f'\n *** 检查点 *** {desc} \n', True, True)
    if condition:
        logger.info('-->通过')
    else:
        logger.info(' -->不通过', True, True)
        raise AssertionError(f'*** 检查点不通过*** {desc}')
