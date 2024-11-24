from PySide6.QtWidgets import QMessageBox


def show_help(toolbar) -> None:
    """Show the 'help' message box"""
    QMessageBox.question(toolbar,
                            'Help',
                            '<p>Please import the template PGC spreadsheet you want to use by clicking on the dedicated button and paste the texts in the generated fields that will appear (for template PGC spreadsheet examples, please refer to your HoYoWiki branch leader).</p>' +
                            '<p>You can include one or many entities (materials, books, ...) that use the same PGC template in your pasted selection. However, do <b>NOT</b> include the language line (CHS CHT DE EN ...) and the TextId column (Name, Desc, ...) unless mentioned.</p>' +
                            '<p>When pasting text data, please make sure that:</p>' +
                            '<ul><li>The data is formatted in TSV (Tab-Separated Values). If you directly copy/paste the texts from a Microsoft Excel or Google Sheets document, they should already be formatted in TSV (see below for an example of a valid text selection).</li>' +
                            '<li>If your selection includes many entities, make sure they are ordered the same across all text sheets (e.g. if your selection contains Mushroom, Sweet Flower and Fowl, the info in each sheet should be in order of Mushroom, Sweet Flower and Fowl).</li>' +
                            '<li>Your selection does not contain any unrelated text.</li>' +
                            '<li>For image URLs, you only need to provide one per entity (as opposed to one per language per entity for normal texts).</li></ul>' +
                            '<p>Valid text selection example (for 3 languages):</p>'
                            '<table><tr><th>TextId</th><th>CHS</th><th>CHT</th><th>DE</th></tr>' +
                            '<tr><th>Book1</th><td style="background-color: DodgerBlue">Story 1</td><td style="background-color: DodgerBlue">Story 1</td><td style="background-color: DodgerBlue">Story 1</td></tr>' +
                            '<tr><th>Book2</th><td style="background-color: DodgerBlue">Story 2</td><td style="background-color: DodgerBlue">Story 2</td><td style="background-color: DodgerBlue">Story 2</td></tr></table><br>',
                            QMessageBox.Ok)