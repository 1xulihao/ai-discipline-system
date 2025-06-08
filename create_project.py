import os

# 定义目录结构
project_structure = {
    "ai_self_discipline": {
        "main.py": None,
        "core": {
            "models": {
                "task.py": None
            },
            "logic": {
                "task_manager.py": None
            },
            "scheduler": {
                "timer.py": None
            }
        },
        "storage": {
            "json_store.py": None,
            "api_adapter.py": None
        },
        "ui": {
            "window.py": None,
            "task_card.py": None,
            "add_task_dialog.py": None
        },
        "ai": {
            "nlp_parser.py": None,
            "tone_generator.py": None,
            "planner.py": None
        },
        "api_server": {
            "main.py": None,
            "routes": {
                "tasks.py": None,
                "stats.py": None,
                "ai.py": None
            }
        },
        "assets": {
            "tasks.json": None
        },
        "utils": {
            "time_utils.py": None
        },
        "screenshots": {},
        "README.md": None,
        "requirements.txt": None
    }
}

# 递归创建目录和文件
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w', encoding='utf-8') as f:
                if content is not None:
                    f.write(content)

# 执行生成
create_structure('.', project_structure)