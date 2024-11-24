import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class FieldsWidget(QWidget):
    """Fields widget containing the labels and text edit zones of the PGC modules"""
    def __init__(self):
        super().__init__()

        self.fields_widget_layout = QVBoxLayout()

        self.add_logo()

        self.setLayout(self.fields_widget_layout)

    
    def add_logo(self):
        """Add the application logo to the widget as a placeholder"""
        self.logo_label = QLabel()
        
        self_path = os.path.dirname(__file__)
        logo_path = os.path.join(self_path, '..', 'assets', 'pgc_tools_logo.png')
        logo_path = os.path.normpath(logo_path)

        logo_pixmap = QPixmap(logo_path)
        self.logo_label.setPixmap(logo_pixmap)

        self.fields_widget_layout.addWidget(self.logo_label)