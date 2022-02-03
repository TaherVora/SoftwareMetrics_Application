from PyQt5 import QtWidgets
from pyui.tab_smi import Ui_Form


class SmiTabWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SmiTabWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.smi_data = dict()
        self.setup_actions()
        self.total_modules = 0

    def setup_actions(self):
        self.ui.btn_add_row.clicked.connect(self.add_row)
        self.ui.btn_compute_idx.clicked.connect(self.compute_index)

    def add_row(self, restore=False, row_data=None):
        rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)
        self.modules_added = QtWidgets.QLineEdit(self)
        self.modules_modified = QtWidgets.QLineEdit(self)
        self.modules_deleted = QtWidgets.QLineEdit(self)
        if not restore:
            numcols = self.ui.tableWidget.columnCount()
            numrows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(numrows)
            self.ui.tableWidget.setColumnCount(numcols)
            self.ui.tableWidget.setCellWidget(numrows - 1, 1, self.modules_added)
            self.ui.tableWidget.setCellWidget(numrows - 1, 2, self.modules_modified)
            self.ui.tableWidget.setCellWidget(numrows - 1, 3, self.modules_deleted)
        else:
            self.modules_added.setText(row_data["1"])
            self.modules_modified.setText(row_data["2"])
            self.modules_deleted.setText(row_data["3"])

    def compute_index(self):
        try:
            self.total_modules = self.total_modules + int(self.modules_added.text()) - int(self.modules_deleted.text())
            smi = (self.total_modules -
                   (int(self.modules_added.text()) +
                    int(self.modules_modified.text()) + int(self.modules_deleted.text()))) / self.total_modules
            numcols = self.ui.tableWidget.columnCount()
            numrows = self.ui.tableWidget.rowCount()

            self.ui.tableWidget.setRowCount(numrows)
            self.ui.tableWidget.setColumnCount(numcols)
            l1 = QtWidgets.QLabel(self)
            l1.setText(str(smi))
            l2 = QtWidgets.QLabel(self)
            l2.setText(self.modules_added.text())
            l3 = QtWidgets.QLabel(self)
            l3.setText(self.modules_modified.text())
            l4 = QtWidgets.QLabel(self)
            l4.setText(self.modules_deleted.text())
            l5 = QtWidgets.QLabel(self)
            l5.setText(str(self.total_modules))
            self.ui.tableWidget.setCellWidget(numrows - 1, 0, l1)
            self.ui.tableWidget.setCellWidget(numrows - 1, 1, l2)
            self.ui.tableWidget.setCellWidget(numrows - 1, 2, l3)
            self.ui.tableWidget.setCellWidget(numrows - 1, 3, l4)
            self.ui.tableWidget.setCellWidget(numrows - 1, 4, l5)
            self.smi_data[numrows - 1] = {
                    1: self.modules_added.text(),
                    2: self.modules_modified.text(),
                    3: self.modules_deleted.text(),
                }
            self.save()
        except:
            pass

    def restore_values(self):
        for row in range(len(self.smi_data)):
            self.add_row(restore=True, row_data=self.smi_data[str(row)])
            self.compute_index()

    def save(self):
        self.parent.project_data_dict[self.parent.file_new_project_dialog.project_name]["SMI"] = self.smi_data
        print(self.parent.project_data_dict)
