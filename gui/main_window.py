import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Doby Test')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel('Hello, PyQt!', self)
        self.layout.addWidget(self.label)

        self.button = QPushButton('Click me', self)
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def on_button_click(self):
        self.label.setText('Button clicked!')