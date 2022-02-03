from PyQt5 import QtWidgets


class OpenDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(OpenDialog, self).__init__()
        self.parent = parent
        self.mybutton_clicked()

    def mybutton_clicked(self):
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All files (*)",
                                                            options=options)
        print(filename)
        if filename:
            print(filename)
            # name = filename.split("/")[-1]
            self.parent.open_project_path = filename
        else:
            self.close()

