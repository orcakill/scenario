# @Time: 2023年07月21日 08:16
# @Author: orcakill
# @File: test_onmyoji_service.py
# @Description: 服务测试类
import time

from src.dao.mapper import select_game_account
from src.model.models import GameProjects, GameProjectsRelation, GameProject
from src.service.airtest_service import AirtestService
from src.service.onmyoji_service import OnmyojiService
from src.utils.my_logger import logger


def test_initialization():
    # 测试登录功能
    game_projects = GameProjects()
    game_projects_relation = GameProjectsRelation()
    game_account = select_game_account("3")
    game_project = GameProject()
    game_task = [game_projects, game_projects_relation, game_account, game_project]
    logger.debug("开始测试")
    # 初始化设备信息
    AirtestService.auto_setup("0")
    # 当前状态初始化
    OnmyojiService.initialization(game_task)


def test_border_fight():
    # 初始化测试任务信息
    game_projects = GameProjects()
    game_projects_relation = GameProjectsRelation()
    game_account = select_game_account("1")
    game_project = GameProject()
    game_task = [game_projects, game_projects_relation, game_account, game_project]
    logger.debug("开始测试")
    # 初始化设备信息
    AirtestService.auto_setup("0")
    # 当前状态初始化
    OnmyojiService.initialization(game_account)
    # 执行测试任务
    OnmyojiService.border_fight(game_task)
