from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class ReconPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel("Recon Module")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)