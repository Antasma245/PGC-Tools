from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import QToolBar

from src import clear_fields, import_template, show_about, show_help, show_settings


class ToolBar(QToolBar):
    """Toolbar mounted to the app's main window"""
    def __init__(self, main_window, app):
        super().__init__()

        self.setWindowTitle('Toolbar')
        self.setMovable(False)

        default_font_name = QFont().family()
        self.setFont(QFont(default_font_name, 16))

        self.import_template_action = QAction('\N{Inbox Tray}', main_window)
        self.import_template_action.setToolTip('Import template spreadsheet')
        self.import_template_action.triggered.connect(lambda: import_template(self, main_window))
        self.addAction(self.import_template_action)

        self.clear_fields_action = QAction('\N{Wastebasket}', main_window)
        self.clear_fields_action.setToolTip('Clear entry fields')
        self.clear_fields_action.triggered.connect(lambda: clear_fields(main_window, True))
        self.addAction(self.clear_fields_action)

        self.addSeparator()

        self.show_help_action = QAction('\N{Open Book}', main_window)
        self.show_help_action.setToolTip('Help')
        self.show_help_action.triggered.connect(lambda: show_help(self))
        self.addAction(self.show_help_action)

        self.show_about_action = QAction('\N{Information Source}', main_window)
        self.show_about_action.setToolTip('About')
        self.show_about_action.triggered.connect(lambda: show_about(self))
        self.addAction(self.show_about_action)

        self.addSeparator()

        self.show_settings_action = QAction('\N{Gear}', main_window)
        self.show_settings_action.setToolTip('Settings')
        self.show_settings_action.triggered.connect(lambda: show_settings(main_window))
        self.addAction(self.show_settings_action)

        self.quit_action = QAction('\N{Cross Mark}', main_window)
        self.quit_action.setToolTip('Quit')
        self.quit_action.triggered.connect(lambda: app.quit())
        self.addAction(self.quit_action)