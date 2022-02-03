from PyQt5 import QtWidgets

from pyui.save_exit_dialog import Ui_Dialog


class SaveExitDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SaveExitDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ui.buttonBox.accepted.connect(self.save_and_exit)
        self.ui.buttonBox.rejected.connect(self.close)
        self.ui.btn_close_without_save.clicked.connect(self.discard_and_exit)

    def execute(self):
        if self.parent.project_data_dict:
            self.exec_()
        else:
            self.close()
            self.parent.close()

    def save_and_exit(self):
        self.parent.save()
        self.close()
        self.parent.close()

    def discard_and_exit(self):
        self.close()
        self.parent.close()
