from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QTabWidget,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QLabel,
    QVBoxLayout,
)
from sqlite3 import connect
import sys
from widgets.AddInventory import AddInventory
from widgets.RegisterPharmacy import RegisterPharmacy
from widgets.ViewDrug import ViewDrug
from widgets.RegisterDrug import RegisterDrug

app = QApplication(sys.argv)


picker = QFileDialog(caption="Select Database", filter="Databases (*.sqlite)")
if picker.exec():
    fileNames = picker.selectedFiles()
    if len(fileNames) > 1:
        QMessageBox.critical("Too many database selected")
        sys.exit(1)
    fileName = fileNames[0]
    database = connect(fileName, autocommit=True)

    window = QTabWidget()
    window.setWindowTitle("Pharmaceutical Inventory")

    tabs = [
        ViewDrug(database),
        AddInventory(database),
        RegisterPharmacy(database),
        RegisterDrug(database),
    ]

    for tab in tabs:
        window.addTab(tab, tab.name)

    window.currentChanged.connect(lambda index: tabs[index].update())
    tabs[0].update()

    window.resize(800, 300)
    window.show()

    sys.exit(app.exec())
