# main.py

import sys
from PyQt5.QtWidgets import QApplication
from ui.window import MainWindow  # 请确认你的 window.py 路径正确

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())