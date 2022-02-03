from PyQt5 import QtWidgets
import traceback

from pyui.language_preference import Ui_Dialog

class LanguagePreferenceDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LanguagePreferenceDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.parent = parent
        self.selected_language = self.parent.selected_language
        self.selected_widget = None
        self.ui.pushButton.clicked.connect(self.btn_clicked)
        self.update_language_selection()

    def execute(self):
        self.exec_()

    def restore(self):
        self.items = (self.ui.verticalLayout.itemAt(i) for i in range(self.ui.verticalLayout.count()))
        for item in self.items:
            widget = item.widget()
            if isinstance(widget, QtWidgets.QRadioButton):
                print(self.selected_language)
                if self.selected_language == widget.text():
                    self.selected_widget = widget
                    widget.setChecked(True)
                    try:
                        self.parent.ui.label_19.setText(widget.text())
                    except Exception:
                        print(traceback.format_exc())
        self.save()

    def update_language_selection(self):
        self.items = (self.ui.verticalLayout.itemAt(i) for i in range(self.ui.verticalLayout.count()))
        for item in self.items:
            widget = item.widget()
            if isinstance(widget, QtWidgets.QRadioButton):
                if widget.isChecked():
                    self.selected_language = widget.text()
                    self.selected_widget = widget
                    try:
                        self.parent.ui.label_19.setText(widget.text())
                    except Exception:
                        print(traceback.format_exc())
        if self.selected_widget is None:
            self.items = (self.ui.verticalLayout.itemAt(i) for i in range(self.ui.verticalLayout.count()))
            for item in self.items:
                widget = item.widget()
                if isinstance(widget, QtWidgets.QRadioButton):
                    if self.selected_language == widget.text():
                        self.selected_widget = widget
                        widget.setChecked(True)
                        try:
                            self.parent.ui.label_19.setText(widget.text())
                        except Exception:
                            print(traceback.format_exc())

    def btn_clicked(self):
        self.update_language_selection()
        self.save()
        self.close()

    def save(self):
        self.parent.selected_language = self.selected_language
        try:
            self.parent.parent.project_data_dict[self.parent.parent.file_new_project_dialog.project_name]["FP"][
                self.parent.metrics_filename]["selected_language"] = self.selected_language
            print(self.parent.parent.project_data_dict)
        except:
            pass
