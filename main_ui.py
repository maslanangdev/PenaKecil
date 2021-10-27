import subprocess
import os
import ntpath
from notifypy import Notify
import sys
import random
from mainUI import Ui_MainWindow

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow

import subprocess

# from pdf2image import convert_from_path

class ParvusCalamus(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(ParvusCalamus, self).__init__(*args, **kwargs)
        self.setupUi(self)

        formats = ["PDF", "JPEG"]
        for h in formats:
            self.qualityCombo.addItem(h)
        
        
        self.qualityCombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.removeList.clicked.connect(self.removeFileList)

        self.addPush.clicked.connect(self.fileloader)
        self.exportPush.clicked.connect(self.mainProcess)
        self.outPush.clicked.connect(self.folderbrowser)
        self.outputPath.setText(os.path.expanduser("~") + "\Documents")
        print("inited")
        

        

    def runOrder(self, command):
        stinfo = subprocess.STARTUPINFO()
        stinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.Popen(command, startupinfo=stinfo, stdout=sys.stdout, stderr=sys.stdout).wait()


    def removeFileList(self):
        self.queueList.clear()
        self.pdfList.clear()

    def fileloader(self):
        print("Open_FILE")
        fileList = QFileDialog.getOpenFileNames(MainWindow, "Select PDF Files", "C:\\", "Portable Document Format (*.pdf);; JPEG Picture (*.jpeg; *.jpg)")
        print(fileList)

        self.pdfList.extend(fileList[0])
        self.queueList.addItems(fileList[0])

    def folderbrowser(self):
        print("Select_FOLDER")
        exDir = QFileDialog.getExistingDirectory(MainWindow, "Select Directory")
        self.outputPath.setText(exDir)


    def mainProcess(self):
        if os.name == "nt":
            gsBin = "gs\\gs9.53.3\\bin\\gswin32c.exe"
        else:
            gsBin = "gs"
        being_process_thing_list = self.pdfList
        quality = self.specifyDPI.value()
        print("mengProses . . .")
        processed = 0
        if self.qualityCombo.currentText() == "PDF":
            for c in being_process_thing_list:

                filename = f"{self.outputPath.text()}\\{ntpath.basename(c)}"
                name, ext = os.path.splitext(filename)
                if os.name != "nt":
                    c.replace("\\", "/")
                    name.replace("\\", "/")

                if ext == ".pdf":
                # if c[:-4] == ".pdf":
                    print(name+ext)                    
                    a = f'{gsBin} -sDEVICE=pdfwrite -dCompabilityLevel=1.4 -dColorImageResolution={quality} -dPDFSETTINGS=/screen -dOptimize=true -dColorImageDownsampleType=/Average  -dNOPAUSE -dBATCH -sOutputFile="{name}_Q{quality}.pdf" "{c}"'
                    print(a)
                    # os.system(a)
                    self.runOrder(a)
                else:
                    img = Image.open(c)
                    img.save(f"{name}_Q-{quality}.pdf", quality=quality, optimize=True, progressive=True)
                
                processed = processed + 1
                percentage = (processed/len(being_process_thing_list))*100
                self.progressBar.setValue(percentage)


        if self.qualityCombo.currentText() == "JPEG":
            for c in being_process_thing_list:
                
                filename = f"{self.outputPath.text()}\\{ntpath.basename(c)}"
                # filename = filename.encode("unicode_escape")
                name, ext = os.path.splitext(filename)
                # if os.name != "nt":
                #     name = str(name)
                #     c.replace("\\", "/")
                #     name.replace("\\", "/")

                print(name, "|", c)
                if ext == ".pdf":
                    a = f'{gsBin} -sDEVICE=jpeg -dNOPAUSE -dBATCH -r{quality} -sOutputFile="{name}_page-%03d_Q-{quality}.jpeg" "{c}"'
                    print(a)
                    self.runOrder(a)

                else:
                    img = Image.open(c)
                    img.save(f"{name}_Q-{quality}.jpeg", quality=quality, optimize=True, progressive=True)

                ext == ""

                processed = processed + 1
                percentage = (processed/len(being_process_thing_list))*100
                self.progressBar.setValue(percentage)

        messages = [
            "THIS IS YOUR ORDER!",
            "Successful",
            "Any other useful messages here?",
            "This is a notification",
            "YAAAAAHOOOOOOOOO",
            "just some random messsage here",
            "your random message here",
            "here you go",
        ]

        notip = Notify()
        notip.title = random.choice(messages)
        notip.message = f"Processed {len(being_process_thing_list)} file(s)"
        notip.application_name = "PenaKecil-PreAlpha"
        notip.icon = "Icon.ico"
        notip.send()

# WIP : Threading for progressbar

# class work(QtCore.QThread):
#     _signal = QtCore.pyqtSignal(int)
#     def __init__(self):
#         super(Thread, self).__init__()
    
#     def __del__(self):
#         self.wait()
    
#     def run(self):
#         pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ParvusCalamus()
    ui.show()
    sys.exit(app.exec_())


# placeholder name for this project is CendolBakso

    '''
    Copyright (C) <2021>  <maslanang>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

    '''