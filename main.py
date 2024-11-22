import sys

from PySide6.QtWidgets import QApplication

from ui import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Show the main window of the application
    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())