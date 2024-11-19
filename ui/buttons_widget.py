from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget

from src import submit_form


class ButtonsWidget(QWidget):
    """Buttons widget containing the cancel and create buttons"""
    def __init__(self, main_window):
        super().__init__()

        self.buttons_widget_layout = QHBoxLayout()

        self.create_button = QPushButton('Create')
        self.create_button.clicked.connect(lambda: submit_form(main_window))
        self.create_button.setDisabled(True)

        self.buttons_widget_layout.addWidget(self.create_button)

        self.setLayout(self.buttons_widget_layout)