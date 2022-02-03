from PyQt5 import QtWidgets
import traceback

from pyui.val_adj_fac import Ui_dialog


class ValueAdjustmentsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ValueAdjustmentsDialog, self).__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.pushButton.clicked.connect(self.btn_done_clicked)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.adj_value_dict = dict()
        self.VAF = 0
        self.parent.ui.label_17.setText(str(0))

    def restore_values(self):
        for i in range(self.ui.gridLayout.rowCount()):
            for j in range(self.ui.gridLayout.columnCount()):
                widget = self.ui.gridLayout.itemAtPosition(i, j).widget()
                if isinstance(widget, QtWidgets.QComboBox):
                    if str(i)+"_"+str(j) in self.adj_value_dict:
                        widget.setCurrentText(self.adj_value_dict[str(i)+"_"+str(j)])
        self.update_adjustment_values()
        self.save()

    def update_adjustment_values(self):
        for i in range(self.ui.gridLayout.rowCount()):
            for j in range(self.ui.gridLayout.columnCount()):
                widget = self.ui.gridLayout.itemAtPosition(i, j).widget()
                if isinstance(widget, QtWidgets.QComboBox):
                    self.adj_value_dict[str(i)+"_"+str(j)] = widget.currentText()
        try:
            total_sum = str(sum(list(map(int, self.adj_value_dict.values()))))
            self.VAF = total_sum
            self.parent.ui.label_17.setText(total_sum)
        except:
            print(traceback.format_exc())

    def execute(self):
        self.exec_()

    def btn_done_clicked(self):
        self.update_adjustment_values()
        self.save()
        self.close()

    def save(self):
        self.parent.parent.project_data_dict[self.parent.parent.file_new_project_dialog.project_name]["FP"][
            self.parent.metrics_filename]["vaf_dict"] = self.adj_value_dict
        print(self.parent.parent.project_data_dict)
