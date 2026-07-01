from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class LogsPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("Logs Module")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)