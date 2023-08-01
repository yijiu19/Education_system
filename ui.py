import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Education_system")

        # 创建一个中心小部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建一个按钮和一个输出框
        self.button = QPushButton("Click me", self)
        self.text_box = QTextEdit(self)

        # 将按钮和输出框添加到中心小部件中
        vbox = QVBoxLayout()
        vbox.addWidget(self.button)
        vbox.addWidget(self.text_box)
        central_widget.setLayout(vbox)

        # 设置窗口的初始大小和最小大小
        self.resize(QSize(800, 600))
        self.setMinimumSize(QSize(200, 150))

        # 将按钮与槽函数相连
        self.button.clicked.connect(self.button_clicked)

    # 定义槽函数
    def button_clicked(self):
        self.text_box.append("Button clicked!")


def ui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
