import sys
from PyQt5.QtWidgets import (
    QDialog, QApplication, QFormLayout, QLineEdit,
    QTimeEdit, QSpinBox, QDialogButtonBox, QVBoxLayout, QMessageBox,
    QComboBox
)
from PyQt5.QtCore import QTime


class AddTaskDialog(QDialog):
    """
    添加任务的弹窗对话框类

    功能：
    - 输入任务标题
    - 选择开始时间（默认当前时间）
    - 设置任务时长（单位：分钟）
    - 选择任务模式（开始方式、完成标准、重复模式、追踪方式）
    - 点击“确定”返回输入数据或验证失败提示
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("添加任务")
        
        # 初始化界面组件
        self.title_edit = None
        self.start_time_edit = None
        self.duration_spinbox = None
        
        # 新增的下拉框
        self.start_mode_combo = None
        self.complete_mode_combo = None
        self.repeat_mode_combo = None
        self.track_mode_combo = None
        
        self.init_ui()

    def init_ui(self):
        """初始化界面布局和控件"""
        layout = QFormLayout()

        # 任务标题输入
        self.title_edit = QLineEdit()
        layout.addRow("任务标题:", self.title_edit)

        # 开始时间输入，默认为当前时间
        self.start_time_edit = QTimeEdit()
        self.start_time_edit.setTime(QTime.currentTime())
        layout.addRow("开始时间:", self.start_time_edit)

        # 任务时长输入
        self.duration_spinbox = QSpinBox()
        self.duration_spinbox.setRange(5, 180)  # 设置范围
        self.duration_spinbox.setSuffix(" 分钟")  # 显示单位
        layout.addRow("任务时长:", self.duration_spinbox)

        # start_mode 下拉选择
        self.start_mode_combo = QComboBox()
        self.start_mode_combo.addItems(["fixed_start", "flexible", "point"])
        layout.addRow("开始方式:", self.start_mode_combo)

        # complete_mode 下拉选择
        self.complete_mode_combo = QComboBox()
        self.complete_mode_combo.addItems(["duration_based", "count_based", "binary"])
        layout.addRow("完成标准:", self.complete_mode_combo)

        # repeat_mode 下拉选择
        self.repeat_mode_combo = QComboBox()
        self.repeat_mode_combo.addItems(["one_time", "recurring"])
        layout.addRow("重复模式:", self.repeat_mode_combo)

        # track_mode 下拉选择
        self.track_mode_combo = QComboBox()
        self.track_mode_combo.addItems(["user_mark", "auto", "ai_query"])
        layout.addRow("追踪方式:", self.track_mode_combo)

        # 按钮区域
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.validate_and_accept)
        button_box.rejected.connect(self.reject)

        # 使用 QVBoxLayout 包裹表单和按钮
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)
        main_layout.addStretch()  # 防止按钮过紧
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)

    def validate_and_accept(self):
        """验证输入并接受对话框结果"""
        title = self.title_edit.text().strip()

        if not title:
            # 标题为空时弹出提示
            QMessageBox.warning(self, "输入错误", "任务标题不能为空！")
            return

        # 所有验证通过后接受对话框
        self.accept()

    def get_task_data(self):
        """
        获取用户输入的任务信息（匹配 Task 四元模型）
        :return: dict，任务结构
        """
        return {
            "title": self.title_edit.text().strip(),
            "start_time_str": self.start_time_edit.time().toString("HH:mm"),
            "duration_minutes": self.duration_spinbox.value(),
            "start_mode": self.start_mode_combo.currentText(),
            "complete_mode": self.complete_mode_combo.currentText(),
            "repeat_mode": self.repeat_mode_combo.currentText(),
            "track_mode": self.track_mode_combo.currentText()
        }


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = AddTaskDialog()
    if dialog.exec_() == QDialog.Accepted:
        print("任务信息已提交：", dialog.get_task_data())
    else:
        print("任务取消")
    sys.exit(app.exec_())