import os

from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout

from settings import Settings


def ask_dir(settings_dialog, dir_lineedit) -> None:
    """Ask the user for an existing directory and set the input in the corresponding line edit"""
    root_directory:str = os.path.abspath(os.sep)

    out_dir:str = QFileDialog.getExistingDirectory(settings_dialog, 'Select saving directory', root_directory)

    if not out_dir:
        dir_lineedit.setText('./out')
    else:
        dir_lineedit.setText(out_dir)


def save_settings(settings_dialog, dir_lineedit, language_lineedit) -> None:
    """Save the settings to the appropriate JSON file"""
    out_dir:str = dir_lineedit.text()
    Settings().write('out_dir', out_dir)

    language_amount:str = language_lineedit.text()
    Settings().write('language_amount', int(language_amount))

    settings_dialog.accept()


def show_settings(main_window) -> None:
    """Show the 'settings' box"""
    settings_dialog = QDialog(main_window)
    settings_dialog.setWindowTitle('Settings')
    settings_dialog.setFixedSize(400, 200)

    settings_dialog_layout = QVBoxLayout()

    # Set up the out directory setting
    out_dir:str = Settings().read('out_dir')

    dir_layout = QHBoxLayout()

    dir_label = QLabel('Saving directory:')

    dir_lineedit = QLineEdit()
    dir_lineedit.setText(out_dir)
    dir_lineedit.setDisabled(True)

    dir_button = QPushButton('\N{Open File Folder}')
    dir_button.clicked.connect(lambda: ask_dir(settings_dialog, dir_lineedit))

    dir_layout.addWidget(dir_label)
    dir_layout.addWidget(dir_lineedit)
    dir_layout.addWidget(dir_button)

    # Set up the language amount setting
    language_amount:int = Settings().read('language_amount')

    language_layout = QHBoxLayout()

    language_label = QLabel('Total languages:')

    language_lineedit = QLineEdit()
    language_lineedit.setText(str(language_amount))

    language_lineedit_validator = QIntValidator(1, 50)
    language_lineedit.setValidator(language_lineedit_validator)

    language_layout.addWidget(language_label)
    language_layout.addWidget(language_lineedit)

    # Set up the buttons for the dialog
    button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Abort)

    button_box.rejected.connect(settings_dialog.reject)
    button_box.accepted.connect(lambda: save_settings(settings_dialog, dir_lineedit, language_lineedit))

    # Add all the componenents to the main layout
    settings_dialog_layout.addLayout(dir_layout)
    settings_dialog_layout.addLayout(language_layout)
    settings_dialog_layout.addWidget(button_box)

    settings_dialog.setLayout(settings_dialog_layout)

    settings_dialog.exec()