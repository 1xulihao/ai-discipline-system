from PyQt5.QtCore import QTimer, QTime
from ui.task_reminder_dialog import TaskReminderDialog

class TaskScheduler:
    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_tasks)
        self.align_to_next_minute()  # ⬅️ 初始化时对齐整分
    def align_to_next_minute(self):
        now = QTime.currentTime()
        msecs_to_next_minute = (60 - now.second()) * 1000 - now.msec()
        # 第一次先单独触发一次（对齐整分）
        QTimer.singleShot(msecs_to_next_minute, self.start_regular_timer)
    def start_regular_timer(self):
        self.check_tasks()  # 立刻执行一次
        self.timer.start(60 * 1000)  # 然后每分钟触发一次
    def check_tasks(self):
        current_qtime = QTime.currentTime()
        due_tasks = self.task_manager.get_due_tasks(current_qtime)
        for task in due_tasks:
            dialog = TaskReminderDialog(task)
            dialog.exec_()