from PyQt5 import QtWidgets
from src.utils import StandardItem

from pyui.new_project_dialog import Ui_Dialog


class FileNewProjectDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(FileNewProjectDialog, self).__init__(parent=None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.buttonBoxEvent)
        self.parent = parent
        self.project_name = None
        
    def execute(self):
        self.exec_()

    def buttonBoxEvent(self, restore=False):
        if not restore:
            self.project_name = self.ui.projectNameLineEdit.text()
        self.parent.setWindowTitle("CECS 543 Metrics Project - "+self.project_name)
        self.parent.project_data_dict[self.project_name] = {"FP": dict(), "UCP": dict(), "SMI": dict()}
        self.parent.project_heirarchy_dict[self.project_name] = StandardItem(
            self.project_name, 14, set_bold=False)
        self.parent.rootNode.appendRow(self.parent.project_heirarchy_dict[self.project_name])
        self.parent.ui.treeView.setModel(self.parent.treeModel)
        self.parent.ui.menuFunction_Points.setDisabled(False)
        self.parent.ui.menuUse_Case_Points.setDisabled(False)
        self.parent.ui.menuSMI.setDisabled(False)
