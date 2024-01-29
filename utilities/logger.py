import inspect
import logging
import allure


def init_logger():
    log_name = inspect.stack()[1][3]
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("", mode="a")
    file_handler.setFormatter("'%(asctime)s - %(name)s - %(levelname)s - %(message)s'")
    logger.addHandler(file_handler)
    return logger


def allure_report(text):
    with allure.step(text):
        return
