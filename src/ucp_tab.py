from PyQt5 import QtWidgets

from pyui.tab_calculate_ucp import Ui_Form
from pyui.new_ucp_tab_dialog import Ui_Dialog
from src.utils import StandardItem
from src.tcf_dialog import TcfDialog
from src.ecf_dialog import EcfDialog
from src.uucw_dialog import UucwDialog
from src.uaw_dialog import UawDialog


class NewUcpTabDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(NewUcpTabDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.ucp_filename = ""
        self.ui.buttonBox.accepted.connect(self.btn_clicked)

    def execute(self):
        self.exec_()

    def btn_clicked(self, restore=False):
        if not restore:
            self.ucp_filename = self.ui.lineEdit.text()
        list(self.parent.project_heirarchy_dict.values())[0].appendRow(
            StandardItem(self.ucp_filename, 12))
        self.parent.add_new_ucp_tab()

    def save(self):
        pass


class UcpTabWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UcpTabWidget, self).__init__()
        # uic.loadUi('gui/tab_calculate_ucp.ui', self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.parent = parent
        self.ucp_filename = self.parent.ucp_filename
        self.tcf_dialog = None
        self.ecf_dialog = None
        self.uucw_dialog = None
        self.uaw_dialog = None
        self.estimates = self.estimates = {
            "pf": 20,
            "loc_per_pm": 700,
            "loc_per_ucp": 100
        }
        self.setup_actions()

    def setup_actions(self):
        self.tcf_dialog = TcfDialog(parent=self)
        self.ecf_dialog = EcfDialog(parent=self)
        self.uucw_dialog = UucwDialog(parent=self)
        self.uaw_dialog = UawDialog(parent=self)
        self.ui.btn_calc_tcp.clicked.connect(self.tcf_dialog.execute)
        self.ui.btn_calc_ecf.clicked.connect(self.ecf_dialog.execute)
        self.ui.btn_calc_uucw.clicked.connect(self.uucw_dialog.execute)
        self.ui.btn_calc_uaw.clicked.connect(self.uaw_dialog.execute)
        self.ui.btn_calc_metrics.clicked.connect(self.calculate_metrics)

    def calculate_metrics(self):
        try:
            # UUCP
            self.ui.label_uucp_result.setText(
                str(float(self.ui.label_uucw_result.text()) + float(self.ui.label_uaw_result.text())))
            # UCP
            self.ui.label_ucp_result.setText(
                str(float(self.ui.label_tcp_result.text()) * float(self.ui.label_ecf_result.text()) *
                    float(self.ui.label_uucp_result.text()) * float(self.ui.inp_pf.text())))
            # LOC
            self.ui.label_est_loc.setText(
                str(float(self.ui.label_ucp_result.text()) * float(self.ui.inp_loc_ucp.text())))
            # PM
            self.ui.label_est_pm.setText(
                str(float(self.ui.label_est_loc.text()) / float(self.ui.inp_loc_pm.text())))
            # Hours
            self.ui.label_est_hours.setText(
                str(float(self.ui.label_est_pm.text()) + float(160)))
        except:
            pass
        self.estimates = {
            "pf": self.ui.inp_pf.text(),
            "loc_per_pm": self.ui.inp_loc_pm.text(),
            "loc_per_ucp": self.ui.inp_loc_ucp.text()
        }
        self.save()

    def restore_values(self):
        self.ui.inp_pf.setText(self.estimates["pf"])
        self.ui.inp_loc_pm.setText(self.estimates["loc_per_pm"])
        self.ui.inp_loc_ucp.setText(self.estimates["loc_per_ucp"])

    def save(self):
        self.parent.project_data_dict[self.parent.file_new_project_dialog.project_name]["UCP"][
            self.parent.ucp_filename]["estimates"] = self.estimates
        print(self.parent.project_data_dict)
