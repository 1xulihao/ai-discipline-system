# ui/task_reminder_dialog.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class TaskReminderDialog(QDialog):
    def __init__(self, task, parent=None):
        super().__init__(parent)
        self.task = task
        self.setWindowTitle("任务提醒")

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"🕒 现在是该执行任务：{task.title} 的时间啦！"))

        btn_done = QPushButton("完成任务")
        btn_done.clicked.connect(self.mark_done)
        layout.addWidget(btn_done)

        btn_later = QPushButton("推迟 15 分钟")
        btn_later.clicked.connect(self.postpone_task)
        layout.addWidget(btn_later)

        self.setLayout(layout)

    def mark_done(self):
        self.task.mark_as_complete()
        self.accept()

    def postpone_task(self):
        self.task.postpone(15)
        self.reject()
