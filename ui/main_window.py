from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow

from .central_widget import CentralWidget
from .toolbar import ToolBar


class MainWindow(QMainWindow):
    """Main window of the application"""
    def __init__(self, app):
        super().__init__()

        self.setWindowTitle('PGC Tools')
        self.setWindowIcon(QPixmap('assets/pgc_tools_logo_notext.png'))
        self.setContextMenuPolicy(Qt.PreventContextMenu)

        self.toolbar = ToolBar(self, app)
        self.addToolBar(self.toolbar)

        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)