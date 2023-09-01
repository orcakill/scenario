# @Time: 2023年08月05日 15:48
# @Author: orcakill
# @File: test_ComplexService.py
# @Description: TODO
import datetime
from unittest import TestCase

from src.model.enum import Onmyoji
from src.service.airtest_service import AirtestService
from src.service.complex_service import ComplexService
from src.service.image_service import ImageService
from src.utils.my_logger import logger


class TestComplexService(TestCase):

    def test_fight(self):
        AirtestService.auto_setup("0")
        fight_fight = Onmyoji.awaken_TZ
        fight_win = Onmyoji.awaken_ZDSL
        fight_fail = Onmyoji.awaken_ZDSB
        fight_again = Onmyoji.awaken_ZCTZ
        fight_end = Onmyoji.awaken_TCTZ
        logger.debug("开始")
        now = datetime.datetime.now()
        for i in range(10):
            logger.debug("测试，挑战{}次", i + 1)
            is_fight = ImageService.touch(fight_fight)
            if is_fight:
                logger.debug("判断是否未挑战")
                is_fight = ImageService.touch(fight_fight, wait=2)
                if is_fight:
                    logger.debug("再次点击挑战")
            logger.debug("等待战斗结果")
            ComplexService.fight_end(fight_win, fight_fail, fight_again, fight_end, fight_fight, 60, 1)
        logger.debug("结束")
        now1 = datetime.datetime.now()
        print(now1 - now)

    def test_fight_end(self):
        AirtestService.auto_setup("0")
        logger.debug("开始")
        now = datetime.datetime.now()
        ComplexService.fight_end(Onmyoji.border_ZDSL, Onmyoji.border_ZDSB,
                                 Onmyoji.border_ZCTZ, Onmyoji.border_TCTZ, Onmyoji.border_GRJJ,
                                 300, 1)
        logger.debug("结束")
        now1 = datetime.datetime.now()
        print(now1 - now)

    def test_swipe_floor(self):
        AirtestService.auto_setup("0")
        logger.debug("开始")
        now = datetime.datetime.now()
        ComplexService.swipe_floor(Onmyoji.awaken_C, Onmyoji.awaken_SC, 1, 5)
        logger.debug("结束")
        now1 = datetime.datetime.now()
        print(now1 - now)

    def test_top_addition(self):
        AirtestService.auto_setup("0")
        logger.debug("开始")
        now = datetime.datetime.now()
        ComplexService.top_addition(Onmyoji.soul_BQ_JC, Onmyoji.soul_BQ_YHJC, Onmyoji.soul_BQ_JCG, Onmyoji.soul_BQ_JCG,
                                    1)
        logger.debug("结束")
        now1 = datetime.datetime.now()
        print(now1 - now)

    def test_debris_fight(self):
        """
        式神碎片
        :return: 
        """
        AirtestService.auto_setup("1")
        logger.debug("开始")
        now = datetime.datetime.now()
        for i in range(20):
            ImageService.touch(Onmyoji.explore_SPTZ)
            ComplexService.fight_end(Onmyoji.explore_ZDSL, Onmyoji.explore_ZDSB, Onmyoji.explore_ZCTZ,
                                     Onmyoji.explore_TCTZ, Onmyoji.explore_SPTZ, 60, 1)
        logger.debug("结束")
        now1 = datetime.datetime.now()
        print(now1 - now)
