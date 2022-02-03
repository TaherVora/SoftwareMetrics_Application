from PyQt5.QtGui import QStandardItem, QFont, QColor


class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=16, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()
        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)
