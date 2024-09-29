from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTabWidget,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QLabel,
    QVBoxLayout
)
from sqlite3 import (
    connect
)
import sys

app = QApplication(sys.argv)

picker = QFileDialog(caption='Select Database',filter='Databases (*.sqlite)')
if picker.exec():
    fileNames = picker.selectedFiles()
    if len(fileNames) > 1:
        QMessageBox.critical('Too many database selected')
        sys.exit(1)
    fileName = fileNames[0]
    database = connect(fileName)
    cursor = database.cursor()

    window = QTabWidget()

    addDrug = QWidget()
    vBox = QVBoxLayout()
    intro = QLabel("This is a Program for logging newly created drugs")
    vBox.addWidget(intro)


    addDrug.setLayout(vBox)
    window.addTab(addDrug, 'Add Drug')


    registerPharmacy = QWidget()
    window.addTab(registerPharmacy, "Register Pharmacy")

    window.show()

    sys.exit(app.exec())