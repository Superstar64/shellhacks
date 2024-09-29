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
from widgets.AddDrug import AddDrug
from widgets.RegisterPharmacy import RegisterPharmacy

app = QApplication(sys.argv)


picker = QFileDialog(caption='Select Database',filter='Databases (*.sqlite)')
if picker.exec():
    fileNames = picker.selectedFiles()
    if len(fileNames) > 1:
        QMessageBox.critical('Too many database selected')
        sys.exit(1)
    fileName = fileNames[0]
    database = connect(fileName)

    window = QTabWidget()
    window.setWindowTitle("Pharmaceutical Inventory")

    tabs = [
        AddDrug(database),
        RegisterPharmacy(database)
    ]

    for tab in tabs:
        window.addTab(tab, tab.name)

    window.currentChanged.connect(lambda index: tabs[index].update())
    tabs[0].update()

    window.resize(800,600)
    window.show()

    sys.exit(app.exec())