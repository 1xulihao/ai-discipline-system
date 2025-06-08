# storage/json_store.py
import json
import os
from core.models.task import Task
from utils.path_config import TASK_FILE

def load_tasks():
    """从本地 JSON 文件中读取任务列表"""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("📂 读取任务：", len(data))
    return [Task.from_dict(t) for t in data]

def save_tasks(task_list):
    """将任务列表写入 JSON 文件"""
    print("💾 保存路径：", TASK_FILE)
    print("💾 保存数据：", [t.to_dict() for t in task_list])
    os.makedirs(os.path.dirname(TASK_FILE), exist_ok=True)
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in task_list], f, indent=2, ensure_ascii=False)