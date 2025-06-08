import os
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QApplication
from ui.add_task_dialog import AddTaskDialog
from core.models.task import Task
import json
from storage.json_store import save_tasks, load_tasks  
from core.logic.task_manager import TaskManager
from core.scheduler.timer import TaskScheduler
from ui.task_card import TaskCard


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自律管理系统")
        self.tasks = load_tasks()               # ✅ 直接加载任务
        print("📂 加载任务数量：", len(self.tasks))
        self.task_manager = TaskManager(self.tasks)
        self.task_scheduler = TaskScheduler(self.task_manager)
        self.init_ui()                          # ✅ 初始化 UI（渲染任务）
        for task in self.tasks:
            self.add_task_to_ui(task)           # ✅ 将已加载的任务展示到界面

    def init_ui(self):
        layout = QVBoxLayout()

        self.add_task_button = QPushButton("添加任务")
        self.add_task_button.clicked.connect(self.show_add_task_dialog)

        layout.addWidget(self.add_task_button)

        # 用于显示任务的容器
        self.task_list_container = QVBoxLayout()
        self.task_list_container.addStretch()

        layout.addLayout(self.task_list_container)

        self.setLayout(layout)

    def show_add_task_dialog(self):
        dialog = AddTaskDialog(self)
        if dialog.exec_() == AddTaskDialog.Accepted:
            task_data = dialog.get_task_data()
            new_task = Task(**task_data)
            self.tasks.append(new_task)
            self.add_task_to_ui(new_task)
            save_tasks(self.tasks)
            print("✅ 已保存任务：", len(self.tasks))

    def add_task_to_ui(self, task):
        card = TaskCard(task)
        card.task_deleted.connect(self.handle_task_deleted)
        card.task_edit_requested.connect(self.handle_task_edit)
        self.task_list_container.insertWidget(self.task_list_container.count() - 1, card)


    def handle_task_deleted(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            save_tasks(self.tasks)
            print("✅ 已保存任务：", len(self.tasks))
            self.refresh_task_list()

    def handle_task_edit(self, task):
        from ui.add_task_dialog import AddTaskDialog
        dialog = AddTaskDialog(self)
        dialog.title_edit.setText(task.title)
        dialog.start_time_edit.setTime(task.start_time)
        dialog.duration_spinbox.setValue(task.duration_minutes)
        dialog.start_mode_combo.setCurrentText(task.start_mode)
        dialog.complete_mode_combo.setCurrentText(task.complete_mode)
        dialog.repeat_mode_combo.setCurrentText(task.repeat_mode)
        dialog.track_mode_combo.setCurrentText(task.track_mode)

        if dialog.exec_():
            updated = dialog.get_task_data()
            for k, v in updated.items():
                setattr(task, k, v)
            save_tasks(self.tasks)
            print("✅ 已保存任务：", len(self.tasks))
            self.refresh_task_list()
    def refresh_task_list(self):
        # 清空旧任务卡片
        while self.task_list_container.count() > 1:
            item = self.task_list_container.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        # 重新添加
        for task in self.tasks:
            self.add_task_to_ui(task)