from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea

from .inner_widget import InnerWidget


class ScrollArea(QScrollArea):
    """Scrollable area containing an inner widget"""
    def __init__(self, main_window):
        super().__init__()

        self.setFixedWidth(650)
        self.setMinimumHeight(700)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.inner_widget = InnerWidget(main_window)
        self.setWidget(self.inner_widget)