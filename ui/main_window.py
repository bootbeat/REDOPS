from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout
)

from ui.widgets.sidebar import Sidebar
from ui.pages.dashboard import DashboardPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("REDOPS")
        self.resize(1400, 850)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        self.sidebar = Sidebar()
        self.dashboard = DashboardPage()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.dashboard)