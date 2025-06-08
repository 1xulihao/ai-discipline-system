from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal

class TaskCard(QWidget):
    task_deleted = pyqtSignal(object)  # 传出任务对象
    task_edit_requested = pyqtSignal(object)  # 传出任务对象
    
    def __init__(self, task, parent=None):
        super().__init__(parent)
        self.task = task
        
        self.init_ui()
    
    def init_ui(self):
        # 主布局
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(8, 4, 8, 4)
        main_layout.setSpacing(10)
        
        # 任务信息标签
        self.task_label = QLabel(f"🕒 {self.task.start_time_str} · {self.task.title}")
        main_layout.addWidget(self.task_label, 1)
        
        # 按钮区域（默认隐藏）
        self.button_container = QWidget()
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(5)
        
        # 修改按钮
        self.btn_edit = QPushButton("✏️")
        self.btn_edit.setFixedSize(24, 24)
        self.btn_edit.clicked.connect(lambda: self.task_edit_requested.emit(self.task))
        
        # 删除按钮
        self.btn_delete = QPushButton("🗑")
        self.btn_delete.setFixedSize(24, 24)
        self.btn_delete.clicked.connect(lambda: self.task_deleted.emit(self.task))
        
        button_layout.addWidget(self.btn_edit)
        button_layout.addWidget(self.btn_delete)
        self.button_container.setLayout(button_layout)
        
        main_layout.addWidget(self.button_container)
        
        self.setLayout(main_layout)
        
        # 初始状态：隐藏按钮
        self.button_container.setVisible(False)
    
    def enterEvent(self, event):
        """鼠标进入控件"""
        self.button_container.setVisible(True)
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        """鼠标离开控件"""
        self.button_container.setVisible(False)
        super().leaveEvent(event)