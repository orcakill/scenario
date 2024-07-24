# @Time: 2024年06月19日 15:26
# @Author: orcakill
# @File: impl_ocr.py
# @Description: 图像文字识别
from src.service.airtest_service import AirtestService
from src.service.ocr_service import OcrService
from src.utils.my_logger import logger


class ImplOcr:
    @staticmethod
    def ocr_touch(words):
        logger.debug("获取当前页面截图")
        screen = AirtestService.snapshot()
        try:
            if screen is not None:
                logger.debug("检查文字坐标:{}", words)
                pos = OcrService.ocr_paddle(screen, words)
                if pos:
                    logger.debug("点击文字坐标:{}", words)
                    AirtestService.touch_coordinate(pos)
                    return True
                else:
                    logger.debug("未识别到文字坐标:{}", words)
            else:
                logger.debug("未截取到图片")
        except Exception as e:
            logger.error("异常{}", e)
        return False
