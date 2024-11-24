# PGC Tools

A desktop application to rapidly create PGC XLSX spreadsheets to be used by HoYoWiki staff members.

![pgc-tools-logo-banner](https://github.com/user-attachments/assets/65304c79-cb71-4752-8c42-8babbed0a04c)

<details>

<summary>UI Preview & Functionalities</summary>

| Light Mode | Dark Mode |
| --- | --- |
| ![ui-light](https://github.com/user-attachments/assets/a15e64dd-1eb8-4229-830b-a4d023ce8362) | ![ui-dark](https://github.com/user-attachments/assets/4bb7a282-6810-4463-a238-d8c0d986075b) |

The Light/Dark Mode of PGC Tools aligns with your system's settings. There is currently no way to manually adjust this setting for the application.

### Buttons explained

* :inbox_tray:: Import the template PGC spreadsheet from which the empty PGC modules will be retrieved
* :wastebasket:: Remove all the generated entry fields
* :open_book:: Show instructions and tips on how to use the application
* :information_source:: Show information about the application
* :gear:: Access the settings menu to configure the following:
    * **Saving directory:** The folder in which to save the generated PGC spreadsheets
    * **Total languages:** The number of languages the application should expect to find in the pasted texts
* :x:: Quit the application

</details>

## Automatic Installation (Windows-only, Recommended)

This section will walk you through installing PGC Tools by using the provided all-in-one release. It comes with its own Python interpreter and pre-installed dependencies, i.e. everything you need. Choose this method if you want an easy and hassle-free installation.

### Step 1: Download and extract the latest release

On the main page of the repository, under Releases, locate the latest release (or click [here](https://github.com/Antasma245/PGC-Tools/releases/latest) for quick access). Then, under the Assets section of the release, click on the `PGC_Tools_BuildXXXXXXXX` hyperlink (NOT `Source code`!) to download the project's ZIP archive.

Finally, extract the downloaded ZIP archive where you want the code to be stored.

### Step 2: Run the `start_application.bat` file

To start the application, simply double-click on the `start_application.bat` file in the main directory of the extracted folder. Two windows should open: the PGC Tools user interface and a terminal.

> [!CAUTION]
> Do NOT close the terminal window while the application is running. It will close by itself once you quit the user interface.

### Step 3 (Optional): Create a shortcut to the `start_application.bat` file

To avoid having to navigate to the extracted folder and locate the start-up file every time you want to use the application, you can create a shortcut to the `start_application.bat` file and place it somewhere convenient.

To do so on Windows 10/11, right-click on the said file, optionally click on *Show more options* if you are on Windows 11 and click on *Create shortcut*. A shortcut to the file should now have appeared in the same folder. You can move it wherever you want, but **make sure you move the shortcut and NOT the original file**.

<details>

<summary>Updating your Installation</summary>

To update your PGC Tools installation, you will have to delete your current installation's folder (and the associated shortcut if you created one) and follow the [installation steps](#automatic-installation-windows-only-recommended) again.

Before doing so, make sure to check the `app/out` folder of the application for generated PGC spreadsheets you would want to keep and save them elsewhere. Note that your modified settings (if any) will not be carried over and you will have to re-edit them after installing the new release.

</details>

## Developer notes

* This application remains fully open-source even after release by using Python's *Windows embeddable package (64-bit)*. This way, even if you choose the automatic installation method, you still have direct access to the source `.py` files. The downside of this approach is that it creates pretty big releases since the entirety of the used libraries are included in it.

* For now, type annotations have only been implemented for built-in Python types.

> [!NOTE]
> This program uses the Qt for Python (or PySide6) library, which is based on the Qt framework and is under the GNU LGPLv3 license. A copy of the aforementioned license documents can be found in the [`appendix`](appendix) folder of the application or on [GNU's website](https://www.gnu.org/licenses/licenses.html).
