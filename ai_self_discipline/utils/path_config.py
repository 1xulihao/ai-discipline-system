# utils/path_config.py

import os

# 获取项目根目录（即 ai_self_discipline 所在目录的上一级）
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# 常用路径定义
ASSETS_DIR = os.path.join(PROJECT_ROOT, "ai_self_discipline", "assets")
TASK_FILE = os.path.join(ASSETS_DIR, "tasks.json")
LOG_FILE = os.path.join(ASSETS_DIR, "logs.txt")
AI_CACHE_PATH = os.path.join(ASSETS_DIR, "ai_cache.json")  # 可用于AI对话缓存或生成信息

# 确保相关目录存在（初始化）
os.makedirs(ASSETS_DIR, exist_ok=True)

# 你可以在其他模块中这样引用：
# from utils.path_config import TASK_FILE