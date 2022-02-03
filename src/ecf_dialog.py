from PyQt5 import QtWidgets
import traceback

from pyui.ecf_dialog import Ui_Dialog


class EcfDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(EcfDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ucp_filename = ""
        self.adj_value_dict = {
            "2": dict(),
            "3": dict()
        }
        self.widget_dict = {
            "2": dict(),
            "3": dict(),
            "4": dict()
        }
        self.setup_actions()

    def setup_actions(self):
        for i in range(1, self.ui.gridLayout.rowCount()):
            for j in [2, 3, 4]:
                try:
                    widget = self.ui.gridLayout.itemAtPosition(i, j).widget()
                    if j == 2 and isinstance(widget, QtWidgets.QLineEdit):
                        self.widget_dict[str(j)][str(i)] = widget
                        self.widget_dict[str(j)][str(i)].textChanged.connect(self.update_adjustment_values)
                    if j == 3 and isinstance(widget, QtWidgets.QComboBox):
                        self.widget_dict[str(j)][str(i)] = widget
                        self.widget_dict[str(j)][str(i)].currentIndexChanged.connect(self.update_adjustment_values)
                    if j == 4 and isinstance(widget, QtWidgets.QLabel):
                        self.widget_dict[str(j)][str(i)] = widget
                except:
                    pass
        self.ui.buttonBox.accepted.connect(self.btn_accept_clicked)
        self.ui.buttonBox.rejected.connect(self.close)

    def restore_values(self):
        for i in range(1, self.ui.gridLayout.rowCount()-1):
            for j in [2, 3]:
                if str(j) in self.widget_dict and str(i) in self.widget_dict[str(j)]:
                    widget = self.widget_dict[str(j)][str(i)]
                    if j == 2 and isinstance(widget, QtWidgets.QLineEdit):
                        if str(i) in self.adj_value_dict[str(j)]:
                            widget.setText(self.adj_value_dict[str(j)][str(i)])
                    if j == 3 and isinstance(widget, QtWidgets.QComboBox):
                        if str(i) in self.adj_value_dict[str(j)]:
                            widget.setCurrentText(self.adj_value_dict[str(j)][str(i)])
        self.update_adjustment_values()
        self.save()

    def update_adjustment_values(self):
        for i in range(1, self.ui.gridLayout.rowCount() - 1):
            widget_weight = self.widget_dict[str(2)][str(i)]
            widget_input = self.widget_dict[str(3)][str(i)]
            widget_result = self.widget_dict[str(4)][str(i)]
            if isinstance(widget_result, QtWidgets.QLabel):
                try:
                    widget_result.setText(
                        str(float(widget_weight.text()) * float(widget_input.currentText()))
                    )
                except:
                    pass
        try:
            total_sum = 0
            for i in range(1, self.ui.gridLayout.rowCount()-1):
                try:
                    total_sum += float(self.widget_dict[str(4)][str(i)].text())
                except:
                    pass
            # self.VAF = total_sum
            self.parent.ui.label_ecf_result.setText(str(total_sum))
            self.ui.label_7.setText(str(total_sum))
        except:
            pass

    def execute(self):
        self.ucp_filename = self.parent.parent.ucp_filename
        self.exec_()

    def btn_accept_clicked(self):
        self.update_adjustment_values()
        self.save()
        self.close()

    def save(self):
        for i in range(1, self.ui.gridLayout.rowCount()-1):
            for j in [2, 3, 4]:
                if str(j) in self.widget_dict and str(i) in self.widget_dict[str(j)]:
                    widget = self.widget_dict[str(j)][str(i)]
                    if j == 2 and isinstance(widget, QtWidgets.QLineEdit):
                        self.adj_value_dict[str(j)][str(i)] = widget.text()
                    if j == 3 and isinstance(widget, QtWidgets.QComboBox):
                        self.adj_value_dict[str(j)][str(i)] = widget.currentText()
        self.parent.parent.project_data_dict[self.parent.parent.file_new_project_dialog.project_name]["UCP"][
            self.parent.ucp_filename]["ecf"] = self.adj_value_dict
        print(self.parent.parent.project_data_dict)
