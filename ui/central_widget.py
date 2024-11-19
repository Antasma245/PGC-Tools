from PySide6.QtWidgets import QHBoxLayout, QWidget

from .scroll_area import ScrollArea


class CentralWidget(QWidget):
    """Central widget of the main window containing the scrollable area"""
    def __init__(self, main_window):
        super().__init__()

        self.scroll_area = ScrollArea(main_window)

        self.central_widget_layout= QHBoxLayout()
        self.central_widget_layout.addStretch()
        self.central_widget_layout.addWidget(self.scroll_area)
        self.central_widget_layout.addStretch()
        
        self.setLayout(self.central_widget_layout)