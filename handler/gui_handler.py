from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow



from ui.main_ui import Ui_MainWindow
import os

class ParvusCalamus(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ParvusCalamus, self).__init__(*args, **kwargs)
        self.setupUi(self)

        formats = ["PDF", "JPEG"]
        for h in formats:
            self.qualityCombo.addItem(h)

        self.qualityCombo.setCurrentIndex(0)
        self.pdfList = []
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

        if os.name == "nt":
            self.outputPath.setText(os.path.expanduser("~") + "\Documents")
            print("RUNS ON WINDOWS MACHINE")
        else:
            self.outputPath.setText(os.path.expanduser("~") + "/Documents")
            print("RUNS ON NON-WINDOWS MACHINE (LINUX, UNIX(MAC OS??)")
        print("inited")