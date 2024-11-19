from PySide6.QtWidgets import QMessageBox


def show_about(toolbar) -> None:
    """Show the 'about' message box"""
    QMessageBox.information(toolbar,
                            'About',
                            '<p>This program uses the Qt for Python (or PySide6) library, which is based on the Qt framework and is under the GNU LGPLv3 license.</p>' +
                            '<p>This application is meant to be used by HoYoWiki collaborators. Nevertheless, it is by no means officially affiliated with HoYoVerse.</p>' +
                            '<p>Useful links:</p>' +
                            '<ul><li>GitHub project page: <a href="https://github.com/Antasma245/PGC-Tools">https://github.com/Antasma245/PGC-Tools</a></li>' +
                            '<li>GNU GPLv3 license: <a href="https://www.gnu.org/licenses/gpl-3.0.txt">https://www.gnu.org/licenses/gpl-3.0.txt</a></li>' +
                            '<li>GNU LGPLv3 license: <a href="https://www.gnu.org/licenses/lgpl-3.0.txt">https://www.gnu.org/licenses/lgpl-3.0.txt</a></li></ul>' +
                            '<p>Should you have any question or think something is not working as intended, feel free to contact Antasma245 or check out the Issues page of the GitHub repository.</p>',
                            QMessageBox.Ok)