from PySide6.QtWidgets import QVBoxLayout, QWidget

from .buttons_widget import ButtonsWidget
from .fields_widget import FieldsWidget


class InnerWidget(QWidget):
    """Inner widget containing the fields and buttons widgets"""
    def __init__(self, main_window):
        super().__init__()

        self.inner_widget_layout = QVBoxLayout()

        self.fields_widget = FieldsWidget()
        self.buttons_widget = ButtonsWidget(main_window)

        self.inner_widget_layout.addWidget(self.fields_widget)
        self.inner_widget_layout.addWidget(self.buttons_widget)

        self.setLayout(self.inner_widget_layout)