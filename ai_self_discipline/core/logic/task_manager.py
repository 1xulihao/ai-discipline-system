# task_manager.py

class TaskManager:
    def __init__(self, tasks):
        self.tasks = tasks

    def get_due_tasks(self, current_qtime):
        due_tasks = []
        for task in self.tasks:
            if task.should_start(current_qtime):
                task.has_been_notified = True  # 防重复
                due_tasks.append(task)
        return due_tasks