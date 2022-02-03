from PyQt5 import QtWidgets

from pyui.new_tab_dialog import Ui_Dialog
from pyui.tab_widget_function_pts import Ui_Form
from src.language_dialog import LanguagePreferenceDialog
from src.utils import StandardItem
from src.val_adjustment_dialog import ValueAdjustmentsDialog


class NewTabDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(NewTabDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.metrics_filename = ""
        self.ui.buttonBox.accepted.connect(self.btn_clicked)

    def execute(self):
        self.exec_()

    def btn_clicked(self, restore=False):
        if not restore:
            self.metrics_filename = self.ui.lineEdit.text()
        list(self.parent.project_heirarchy_dict.values())[0].appendRow(
            StandardItem(self.metrics_filename, 12, set_bold=False))
        self.parent.add_new_fp_tab()

    def save(self):
        pass


class FunctionPtsTabWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(FunctionPtsTabWidget, self).__init__()
        # uic.loadUi('gui/tab_widget_function_pts.ui', self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.selected_language = self.parent.selected_language
        self.metrics_filename = self.parent.metrics_filename
        self.language_dialog = LanguagePreferenceDialog(parent=self)
        self.val_adj_dialog = ValueAdjustmentsDialog(parent=self)
        self.ui.pushButton_2.clicked.connect(self.val_adj_dialog.execute)
        self.ui.pushButton_4.clicked.connect(self.language_dialog.execute)
        self.ui.pushButton.clicked.connect(self.update_weights)
        self.ui.pushButton_3.clicked.connect(self.compute_code_size)
        self.total_count = 0
        self.weights = dict()

    def restore_weights(self):
        for i in range(5):
            widget = self.ui.gridLayout.itemAtPosition(i, 1).widget()
            if isinstance(widget, QtWidgets.QLineEdit):
                widget.setText(str(self.weights["1"][i]))
        for i in range(5):
            for j in range(2, 5):
                widget = self.ui.gridLayout.itemAtPosition(i, j).widget()
                if isinstance(widget, QtWidgets.QRadioButton) and widget.text() == str(self.weights["2"][i]):
                    widget.setChecked(True)
        self.update_weights()
        self.compute_code_size()

    def update_weights(self):
        self.weights = dict()
        for i in range(5):
            widget = self.ui.gridLayout.itemAtPosition(i, 1).widget()
            if isinstance(widget, QtWidgets.QLineEdit):
                if 1 not in self.weights:
                    self.weights[1] = [widget.text()]
                else:
                    self.weights[1].append(widget.text())
        for i in range(5):
            for j in range(2, 5):
                widget = self.ui.gridLayout.itemAtPosition(i, j).widget()
                if isinstance(widget, QtWidgets.QRadioButton):
                    if widget.isChecked():
                        if 2 not in self.weights:
                            self.weights[2] = [widget.text()]
                        else:
                            self.weights[2].append(widget.text())
        self.total_count = 0
        for i in range(5):
            widget = self.ui.gridLayout.itemAtPosition(i, 5).widget()
            if isinstance(widget, QtWidgets.QLabel):
                count = int(self.weights[1][i]) * int(self.weights[2][i])
                widget.setText(str(count))
                self.total_count += count
        self.ui.gridLayout.itemAtPosition(5, 5).widget().setText(str(self.total_count))
        self.compute_fp()

    def compute_fp(self):
        self.ui.gridLayout.itemAtPosition(6, 5).widget().setText(
            str(self.total_count * (0.65 + 0.01 * int(self.val_adj_dialog.VAF))))
        self.save()

    def compute_code_size(self):
        if not self.language_dialog.selected_widget:
            self.ui.gridLayout.itemAtPosition(8, 5).widget().setText(str(0))
        else:
            self.ui.gridLayout.itemAtPosition(8, 5).widget().setText(
                str(self.total_count * int(self.language_dialog.selected_widget.property("score"))))
        self.save()

    def save(self):
        self.parent.project_data_dict[self.parent.file_new_project_dialog.project_name]["FP"][
            self.metrics_filename]["weights"] = self.weights
        print(self.parent.project_data_dict)
