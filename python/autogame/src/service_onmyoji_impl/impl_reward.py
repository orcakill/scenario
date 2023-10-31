# @Time: 2023年09月01日 17:20
# @Author: orcakill
# @File: impl_reward.py
# @Description: 每日奖励
import time

from src.dao.mapper import Mapper
from src.model.enum import Onmyoji, Cvstrategy
from src.model.models import GameProjectLog, GameAccount, GameProject, GameDevices, GameProjectsRelation
from src.service.complex_service import ComplexService
from src.service.image_service import ImageService
from src.service_onmyoji_impl import impl_initialization
from src.utils.my_logger import logger
from src.utils.utils_time import UtilsTime


def daily_rewards(game_task: []):
    game_account = GameAccount(game_task[2])
    game_project = GameProject(game_task[3])
    game_devices = GameDevices(game_task[4])
    # 开始时间
    time_start = time.time()
    # 账号信息
    logger.debug("1.邮箱奖励")
    is_mail = ImageService.exists(Onmyoji.reward_YX)
    if is_mail:
        logger.debug("点击邮箱")
        ImageService.touch_coordinate(is_mail)
        logger.debug("判断是否有全部领取")
        is_get = ImageService.exists(Onmyoji.reward_YXQBLQ, wait=3)
        if is_get:
            logger.debug("点击全部领取")
            ImageService.touch_coordinate(is_get)
            logger.debug("点击确定")
            ImageService.touch(Onmyoji.reward_QD, wait=3)
            logger.debug("获得奖励，退出")
            is_reward = ImageService.exists(Onmyoji.reward_HDJL, wait=3)
            if is_reward:
                ImageService.touch_coordinate((1 / 2 * is_reward[0], 1 / 2 * is_reward[1]))
        logger.debug("返回首页")
        ImageService.touch(Onmyoji.comm_FH_YSJZDHBSCH, wait=3)
    else:
        ComplexService.refuse_reward()
    logger.debug("确认返回首页")
    impl_initialization.return_home(game_task)

    logger.debug("2.礼包屋奖励")
    is_store = ImageService.exists(Onmyoji.store_SDTB)
    if is_store:
        logger.debug("点击商店图标")
        ImageService.touch_coordinate(is_store)
        logger.debug("判断是否有右上角返回")
        is_right = ImageService.exists(Onmyoji.comm_FH_YSJHDBSCH)
        if is_right:
            ImageService.touch_coordinate(is_right)
        logger.debug("点击礼包屋")
        ImageService.touch(Onmyoji.store_LBW)
        logger.debug("点击推荐")
        ImageService.touch(Onmyoji.store_TJ)
        logger.debug("判断是否有每日领取")
        is_day = ImageService.exists(Onmyoji.store_MRLQ, wait=2)
        if is_day:
            ImageService.touch_coordinate(is_day)
            logger.debug("获得每日免费奖励，退出")
            is_reward = ImageService.exists(Onmyoji.store_HDJL, wait=3)
            if is_reward:
                ImageService.touch_coordinate((1 / 2 * is_reward[0], 1 / 2 * is_reward[1]))
        else:
            logger.debug("无每日免费奖励")
        logger.debug("返回首页")
        ImageService.touch(Onmyoji.comm_FH_ZSJHKHSXYH)
        ImageService.touch(Onmyoji.comm_FH_ZSJHKHSXYH)
        ImageService.touch(Onmyoji.comm_FH_ZSJLDYXBSXYH)
    else:
        ComplexService.refuse_reward()
    logger.debug("确认返回首页")
    impl_initialization.return_home(game_task)
    logger.debug("3.花合战奖励")
    is_flower_battle = ImageService.exists(Onmyoji.reward_HHZTB, is_click=True)
    if is_flower_battle:
        logger.debug("点击空白")
        ImageService.touch(Onmyoji.reward_DJKB)
        ComplexService.get_reward(Onmyoji.reward_DJKB)
        logger.debug("点击右侧任务")
        ImageService.touch(Onmyoji.reward_YCRW)
        logger.debug("点击全部领取")
        ImageService.exists(Onmyoji.reward_HHZQBLQ, is_click=True)
        logger.debug("获得奖励")
        ComplexService.get_reward(Onmyoji.reward_HDJL)
        logger.debug("返回首页")
        ImageService.touch(Onmyoji.comm_FH_ZSJLDBKBSXYH)
    else:
        ComplexService.refuse_reward()
    logger.debug("4.首页小纸人奖励")
    logger.debug("判断是否有签到小纸人")
    is_sign_in = ImageService.exists(Onmyoji.reward_QDXZR, timeouts=2)
    if is_sign_in:
        logger.debug("有签到小纸人")
        ImageService.touch_coordinate(is_sign_in)
        logger.debug("点击每日一签")
        ImageService.touch(Onmyoji.reward_MRYQ)
        logger.debug("点击退出挑战")
        ImageService.touch(Onmyoji.reward_TCTZ, wait=5)
        logger.debug("返回首页")
        ImageService.touch(Onmyoji.comm_FH_YSJHDBSCH)
    else:
        ComplexService.refuse_reward()
    logger.debug("判断是否有体力小纸人")
    is_strength = ImageService.exists(Onmyoji.reward_TLXZR, timeouts=2, wait=3)
    if is_strength:
        logger.debug("有体力小纸人")
        ImageService.touch_coordinate(is_strength)
        logger.debug("获得体力奖励，退出")
        is_reward = ImageService.exists(Onmyoji.reward_HDJL, wait=3)
        if is_reward:
            ImageService.touch_coordinate((1 / 2 * is_reward[0], 1 / 2 * is_reward[1]))
        logger.debug("点击可能存在的返回")
        ImageService.touch(Onmyoji.comm_FH_YSJHDBSCH)
    else:
        ComplexService.refuse_reward()
    logger.debug("判断是否有勾玉小纸人")
    is_jade = ImageService.exists(Onmyoji.reward_GYXZR, timeouts=2, wait=3)
    if is_jade:
        logger.debug("有勾玉小纸人")
        ImageService.touch_coordinate(is_jade)
        logger.debug("获取勾玉奖励")
        is_reward = ImageService.exists(Onmyoji.reward_HDJL, wait=3)
        if is_reward:
            logger.debug("有勾玉奖励")
            ImageService.touch_coordinate((1 / 2 * is_reward[0], 1 / 2 * is_reward[1]))
        logger.debug("检查返回")
        ImageService.touch(Onmyoji.comm_FH_YSJHDBSCH)
    else:
        ComplexService.refuse_reward()
    logger.debug("判断是否有御魂觉醒加成小纸人")
    is_soul_addition = ImageService.exists(Onmyoji.reward_YHJXJCXZR, timeouts=2, wait=3)
    if is_soul_addition:
        logger.debug("有御魂觉醒加成小纸人")
        ImageService.touch_coordinate(is_soul_addition)
        logger.debug("获得奖励，退出")
        is_reward = ImageService.exists(Onmyoji.reward_HDJL, wait=3)
        if is_reward:
            ImageService.touch_coordinate((1 / 2 * is_reward[0], 1 / 2 * is_reward[1]))
        logger.debug("检查返回")
        ImageService.touch(Onmyoji.comm_FH_YSJHDBSCH)
    logger.debug("确认返回首页")
    impl_initialization.return_home(game_task)
    time_all = time.time() - time_start
    # 记录项目执行结果
    game_project_log = GameProjectLog(project_id=game_project.id, role_id=game_account.id, devices_id=game_devices.id,
                                      result='每日奖励完成', cost_time=int(time_all))
    Mapper.save_game_project_log(game_project_log)
    logger.debug("每日奖励,用时{}秒", round(time_all))


def soul_arrange(game_task: []):
    """
    御魂整理
    :param game_task: 任务信息
    :return:
    """
    resolution = ImageService.resolution_ratio()
    # 开始时间
    time_start = time.time()
    # 项目信息
    (game_projects_relation, game_account,
     game_project, game_devices) = (GameProjectsRelation(game_task[1]), GameAccount(game_task[2]),
                                    GameProject(game_task[3]), GameDevices(game_task[4]))
    for i in range(2):
        ComplexService.refuse_reward()
        logger.debug("点击式神录")
        ImageService.touch(Onmyoji.arrange_SSLTB)
        logger.debug("点击右侧详细")
        ImageService.touch_coordinate((resolution[0], 0.5 * resolution[1]), wait=3)
        logger.debug("点击右侧御魂")
        ImageService.touch(Onmyoji.arrange_YCYH)
        logger.debug("点击更换")
        ImageService.touch(Onmyoji.arrange_GH)
        logger.debug("1.贪吃鬼，清理待吃御魂1-4星")
        ImageService.touch(Onmyoji.arrange_TCG)
        logger.debug("点击进食习惯")
        ImageService.touch(Onmyoji.arrange_JSXG)
        logger.debug("点击立即进食")
        ImageService.touch(Onmyoji.arrange_LJJS)
        logger.debug("点击不再提示")
        ImageService.touch(Onmyoji.arrange_JRBZTS)
        logger.debug("点击吞噬确定")
        ImageService.touch(Onmyoji.arrange_TSQD)
        logger.debug("点击吞噬确定")
        ImageService.touch(Onmyoji.arrange_TSQD)
        logger.debug("退出贪吃鬼小屋")
        ComplexService.get_reward(Onmyoji.arrange_TCGXW)
        logger.debug("点击右上角返回")
        ImageService.touch(Onmyoji.comm_FH_YSJHDBSCH)
        logger.debug("2.点击右侧奉纳")
        ImageService.touch(Onmyoji.arrange_YCFN)
        logger.debug("点击左上角已弃置")
        ImageService.touch(Onmyoji.arrange_ZSJYQZ)
        for i_offering in range(5):
            logger.debug("奉纳{}次，长按弃置标志", i_offering + 1)
            ImageService.touch(Onmyoji.arrange_QZBZ, cvstrategy=Cvstrategy.default, duration=2)
            logger.debug("判断是否弃置满额，200个")
            is_full_amount = ImageService.touch(Onmyoji.arrange_QZME)
            if is_full_amount:
                logger.debug("奉纳")
                ImageService.touch(Onmyoji.arrange_FN)
                logger.debug("点击获得奖励")
                ComplexService.get_reward(Onmyoji.arrange_HDJL)
                logger.debug("点击神赐")
                ComplexService.get_reward(Onmyoji.arrange_SC)
            else:
                logger.debug("不满200")
                break
        logger.debug("返回首页,3次")
        ImageService.touch(Onmyoji.comm_FH_ZSJHKZDHSXYH)
        ImageService.touch(Onmyoji.comm_FH_ZSJHKZDHSXYH)
        ImageService.touch(Onmyoji.comm_FH_ZSJHKZDHSXYH)
    time.sleep(5)
    logger.debug("确认返回首页")
    impl_initialization.return_home(game_task)
    time_end = time.time()
    time_all = time_end - time_start
    # 记录项目执行结果
    game_project_log = GameProjectLog(project_id=game_project.id, role_id=game_account.id, devices_id=game_devices.id,
                                      result='御魂整理', cost_time=int(time_all))
    Mapper.save_game_project_log(game_project_log)
    logger.debug("御魂整理总用时{}", UtilsTime.convert_seconds(time_all))
