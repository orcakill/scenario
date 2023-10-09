# @Time: 2023年08月07日 14:41
# @Author: orcakill
# @File: test_ocr_service.py
# @Description: 图像文字识别测试类
from unittest import TestCase

from src.model.enum import Onmyoji
from src.service.image_service import ImageService
from src.service.ocr_service import OcrService
from src.utils.my_logger import my_logger as logger


class TestOcrService(TestCase):
    def test_border_bond(self):
        ImageService.auto_setup("1")
        result = OcrService.get_word(Onmyoji.friends_HYSQY)
        logger.debug(result)
        logger.debug("结束")
