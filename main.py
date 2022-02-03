import json

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel

from pyui.mainwindow import Ui_MainWindow
from src.function_pts_tab import FunctionPtsTabWidget, NewTabDialog
from src.file_open_dialog import OpenDialog
from src.language_dialog import LanguagePreferenceDialog
from src.new_project_dialog import FileNewProjectDialog
from src.ucp_tab import UcpTabWidget, NewUcpTabDialog
from src.smi_tab import SmiTabWidget
from src.save_exit_dialog import SaveExitDialog
from src.utils import StandardItem


class CreateNewTab(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super(CreateNewTab, self).__init__()
        self.parent = parent

    def save(self):
        pass


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.project_data_dict = dict()
        self.open_project_path = ""
        self.project_heirarchy_dict = dict()
        self.treeModel = None
        self.rootNode = None
        self.file_new_project_dialog = None
        self.language_dialog = None
        self.new_file_tab = None
        self.new_tab_dialog = None
        self.open_dialog = None
        self.metrics_filename = None
        self.ucp_filename = None
        self.new_ucp_tab_dialog = None
        self.ucp_tab_widget = None
        self.smi_filename = "SMI"
        self.smi_tab_widget = None
        self.function_pts_tab_widget = None
        self.selected_language = None
        self.save_exit_dialog = None
        self.setup_windows()
        self.setup_actions()

    def setup_windows(self):
        self.project_heirarchy_dict = dict()
        self.treeModel = QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
        self.file_new_project_dialog = FileNewProjectDialog(parent=self)
        self.language_dialog = LanguagePreferenceDialog(parent=self)
        self.new_file_tab = CreateNewTab(parent=self)
        self.new_tab_dialog = NewTabDialog(parent=self)
        self.new_ucp_tab_dialog = NewUcpTabDialog(parent=self)
        self.save_exit_dialog = SaveExitDialog(parent=self)

    def setup_actions(self):
        self.ui.actionLanguage.triggered.connect(self.language_dialog.execute)
        self.ui.actionNew.triggered.connect(self.file_new_project_dialog.execute)
        self.ui.actionEnter_FP_Data.triggered.connect(self.new_tab_dialog.execute)
        self.ui.actionEnter_UCP_data.triggered.connect(self.new_ucp_tab_dialog.execute)
        self.ui.actionEnter_SMI_data.triggered.connect(self.add_new_smi_tab)
        self.ui.actionExit.triggered.connect(self.save_exit_dialog.execute)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionOpen.triggered.connect(self.open_project)
        self.ui.menuFunction_Points.setDisabled(True)
        self.ui.menuUse_Case_Points.setDisabled(True)
        self.ui.menuSMI.setDisabled(True)

    def closeEvent(self, event):
        self.save_exit_dialog.execute()

    def exit_window(self):
        self.close()

    def save(self):
        with open(self.file_new_project_dialog.project_name + ".ms", "w+") as f:
            f.write(json.dumps(self.project_data_dict))

    def open_project(self):
        self.open_dialog = OpenDialog(parent=self)
        print(self.open_project_path)
        if self.open_project_path:
            with open(self.open_project_path, "r") as f:
                self.project_data_dict = json.loads(f.read())
            print(self.project_data_dict)
            for project_name, project_data in self.project_data_dict.items():
                self.file_new_project_dialog.project_name = project_name
                self.file_new_project_dialog.buttonBoxEvent(restore=True)
                for metrics_type, metrics in project_data.items():
                    if metrics_type == "FP":
                        for metrics_filename, metrics_data in metrics.items():
                            self.metrics_filename = metrics_filename
                            self.new_tab_dialog.metrics_filename = metrics_filename
                            self.new_tab_dialog.btn_clicked(restore=True)
                            if metrics_data["vaf_dict"]:
                                self.function_pts_tab_widget.val_adj_dialog.adj_value_dict = metrics_data["vaf_dict"]
                                self.function_pts_tab_widget.val_adj_dialog.restore_values()
                            if metrics_data["selected_language"]:
                                self.function_pts_tab_widget.language_dialog.selected_language = metrics_data["selected_language"]
                                self.function_pts_tab_widget.language_dialog.restore()
                            if metrics_data["weights"]:
                                self.function_pts_tab_widget.weights = metrics_data["weights"]
                                self.function_pts_tab_widget.restore_weights()
                            self.ui.menuFunction_Points.setDisabled(False)
                    elif metrics_type == "UCP":
                        for metrics_filename, metrics_data in metrics.items():
                            self.ucp_filename = metrics_filename
                            self.new_ucp_tab_dialog.ucp_filename = metrics_filename
                            self.new_ucp_tab_dialog.btn_clicked(restore=True)
                            if metrics_data["estimates"]:
                                self.ucp_tab_widget.estimates = metrics_data["estimates"]
                                self.ucp_tab_widget.restore_values()
                            if metrics_data["tcf"]:
                                self.ucp_tab_widget.tcf_dialog.adj_value_dict = metrics_data["tcf"]
                                self.ucp_tab_widget.tcf_dialog.restore_values()
                            if metrics_data["ecf"]:
                                self.ucp_tab_widget.ecf_dialog.adj_value_dict = metrics_data["ecf"]
                                self.ucp_tab_widget.ecf_dialog.restore_values()
                            if metrics_data["uucw"]:
                                self.ucp_tab_widget.uucw_dialog.adj_value_dict = metrics_data["uucw"]
                                self.ucp_tab_widget.uucw_dialog.restore_values()
                            if metrics_data["uaw"]:
                                self.ucp_tab_widget.uaw_dialog.adj_value_dict = metrics_data["uaw"]
                                self.ucp_tab_widget.uaw_dialog.restore_values()
                            self.ui.menuUse_Case_Points.setDisabled(False)
                    else:
                        if metrics:
                            self.add_new_smi_tab()
                            self.smi_tab_widget.smi_data = metrics
                            self.smi_tab_widget.restore_values()
                            self.ui.menuSMI.setDisabled(False)

    def add_new_fp_tab(self):
        self.metrics_filename = self.new_tab_dialog.metrics_filename
        self.function_pts_tab_widget = FunctionPtsTabWidget(parent=self)
        self.new_file_tab.addTab(self.function_pts_tab_widget, self.metrics_filename)
        self.project_data_dict[self.file_new_project_dialog.project_name]["FP"][self.metrics_filename] = {
            "weights": {},
            "selected_language": "",
            "vaf_dict": {}
        }
        self.ui.horizontalLayout.addWidget(self.new_file_tab)

    def add_new_ucp_tab(self):
        self.ucp_filename = self.new_ucp_tab_dialog.ucp_filename
        self.ucp_tab_widget = UcpTabWidget(parent=self)
        self.new_file_tab.addTab(self.ucp_tab_widget, self.ucp_filename)
        self.project_data_dict[self.file_new_project_dialog.project_name]["UCP"][self.ucp_filename] = {
            "tcf": {},
            "ecf": {},
            "uucw": {},
            "uaw": {},
            "estimates": {}
        }
        self.ui.horizontalLayout.addWidget(self.new_file_tab)

    def add_new_smi_tab(self):
        self.smi_filename = "SMI"
        list(self.project_heirarchy_dict.values())[0].appendRow(
            StandardItem(self.smi_filename, 12))
        self.smi_tab_widget = SmiTabWidget(parent=self)
        self.new_file_tab.addTab(self.smi_tab_widget, self.smi_filename)
        print(self.project_data_dict)
        self.project_data_dict[self.file_new_project_dialog.project_name]["SMI"] = {}
        self.ui.horizontalLayout.addWidget(self.new_file_tab)
        self.ui.menuSMI.setDisabled(True)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # there's no need to pass args here, usually they're important only to the app
    sys.exit(app.exec_())
