from unittest import result
from PenaKecil.PenaUI import Ui_MainWindow
from PyQt6 import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


from pypdf import PdfReader, PdfWriter

import subprocess
import os
import ntpath
from notifypy import Notify
import sys
import random
import time

from PIL import Image


import subprocess

from pdf2image import convert_from_path

class Pena(Ui_MainWindow):
    def __init__(self):
        # formats = ["Screen (72 dpi)", 
        # "E-Book (150 dpi)", 
        # "Pre-Press (300 dpi)", 
        # "Printer (300 dpi)", 
        # "Default", 
        # "JPEG HIGH", 
        # "JPEG MEDIUM", 
        # "JPEG LOW"]

        self.pdfList = []

        import sys
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        ui = self
        ui.setupUi(self.MainWindow)
        

        self.initialize(self.MainWindow)
        
        self.threadpool = QThreadPool()

        sys.exit(app.exec())

       
    def updateProgressBar(self, percentage):
        self.progressBar.setValue(int(percentage))


    def runOrder(self, command):
        stinfo = subprocess.STARTUPINFO()
        stinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.Popen(command, startupinfo=stinfo, stdout=sys.stdout, stderr=sys.stdout).wait()


    def removeFileList(self):
        self.queueList.clear()
        self.pdfList.clear()

    def fileLoader(self):
        print("Open_FILE")
        fileList = QFileDialog.getOpenFileNames(self.MainWindow, "Select PDF Files", "C:\\", "Portable Document Format (*.pdf);; JPEG Picture (*.jpeg; *.jpg)")
        print(fileList)

        self.pdfList.extend(fileList[0])
        self.queueList.addItems(fileList[0])
        # for x in fileList[0]:
        #     self.queueList.addItem(x)

    def folderBrowser(self):
        print("Select_FOLDER")
        exDir = QFileDialog.getExistingDirectory(self.MainWindow, "Select Directory")
        self.outputPath.setText(exDir)

    def timeThief(self):
        print(f"REEEEEEEEEEEEEEEEE")
        sleep(10)


    def beginProcess(self):
        self.progressBar.setValue(int(0))

        being_process_thing_list = self.pdfList
        quality = self.specifyDPI.value()

        worker = PenaWorker(self.qualityCombo.currentText(), being_process_thing_list, quality, self.progressBar, self.outputPath)
        worker.signal.progress.connect(self.updateProgressBar)
        self.threadpool.start(worker)

        # messages = [
        #     "THIS IS YOUR ORDER!",
        #     "Take Care",
        #     "Successful",
        #     "Any other useful messages here?",
        #     "This is notification",
        #     "hello, anyone here?",
        #     "YAAAAAHOOOOOOOOO",
        #     "Java?",
        #     "just some random messsage here",
        #     "your random message here",
        #     "here you go",
        #     "errrr",
        #     "just open it now",
        # ]

    def PenaNotify(self):
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
        notip.application_name = "PenaKecil"
        notip.icon = "calamus.ico"
        notip.send()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PenaKecil - Optimize!"))
        self.label.setText(_translate("MainWindow", "PenaKecil"))
        self.label_2.setText(_translate("MainWindow", "A Simple Front-End to Optimize Documents Size"))
        self.label_5.setText(_translate("MainWindow", "Files Queue : "))
        self.addPush.setText(_translate("MainWindow", "Add File"))
        self.label_4.setText(_translate("MainWindow", "Output Format : "))
        self.outputPath.setPlaceholderText(_translate("MainWindow", "Output file path goes here...."))
        self.outPush.setText(_translate("MainWindow", "Browse")) 
        self.exportPush.setText(_translate("MainWindow", "Export !"))
        self.label_3.setText(_translate("MainWindow", "PenaKecil 1.2 (c) Read\Write Interactive"))

    def initialize(self, MainWindow):
        #formats = ["PDF", "JPEG", "PNG", "TimeThief"]
        formats = ["PDF", "JPEG"]
        
        for h in formats:
            self.qualityCombo.addItem(h)

        # self.qualityCombo.setCurrentText(_translate("MainWindow", "Select Quality"))
        # self.qualityCombo.setItemText(0, _translate("MainWindow", ""))
        # self.qualityCombo.setItemText(1, _translate("MainWindow", "E-Book (150 dpi)"))
        # self.qualityCombo.setItemText(2, _translate("MainWindow", ))
        # self.qualityCombo.setItemText(3, _translate("MainWindow", )
        # self.qualityCombo.setItemText(4, _translate("MainWindow", ))

        self.retranslateUi(MainWindow)
        self.qualityCombo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addPush.clicked.connect(self.fileLoader)
        self.exportPush.clicked.connect(self.beginProcess)
        self.outPush.clicked.connect(self.folderBrowser)
        self.outputPath.setText(os.path.expanduser("~") + "\Documents")
        self.removeList.clicked.connect(self.removeFileList)

        MainWindow.show()

class PenaSignal(QObject):

    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class PenaWorker(QRunnable):
    def __init__(self, target, inputs, quality, pBarObj, exportDir):
        super(PenaWorker, self).__init__()
        self.inputs = inputs
        self.target = target
        self.quality = quality
        self.progressBar = pBarObj
        self.outputPath = exportDir
        self.signal = PenaSignal()

    def runOrder(self, command):
        stinfo = subprocess.STARTUPINFO()
        stinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.Popen(command, startupinfo=stinfo, stdout=sys.stdout, stderr=sys.stdout).wait()

    @pyqtSlot()
    def run(self):
        quality = self.quality
        being_process_thing_list = self.inputs

        print("mengProses . . .")
        processed = 0

        match self.target:
            case "PDF":
                for c in being_process_thing_list:
                    filename = f"{self.outputPath.text()}\\{ntpath.basename(c)}"
                    name, ext = os.path.splitext(filename)
                    if ext == ".pdf":
                        print(name+ext)                  
                        a = f'gs\\bin\\gswin64c.exe -sDEVICE=pdfwrite -dCompabilityLevel=1.4 -dColorImageResolution={quality} -dPDFSETTINGS=/screen -dOptimize=true -dColorImageDownsampleType=/Average  -dNOPAUSE -dBATCH -sOutputFile="{name}_Q{quality}.pdf" "{c}"'
                        print(a)
                        self.runOrder(a)
                    else:
                        img = Image.open(c)
                        img.save(f"{name}_Q-{quality}.pdf", quality=quality, optimize=True, progressive=True)
                
                    processed = processed + 1
                    percentage = (processed/len(being_process_thing_list))*100
                    self.signal.progress.emit(int(percentage))

                    #self.progressBar.setValue(int(percentage))

            case "PDF (Lossless)":
                for c in being_process_thing_list:
                    filename = f"{self.outputPath.text()}\\{ntpath.basename(c)}"
                    name, ext = os.path.splitext(filename)
                    if ext == ".pdf":
                        print(name+ext)                  
                        #a = f'gs\\gs9.53.3\\bin\\gswin32c.exe -sDEVICE=pdfwrite -dCompabilityLevel=1.4 -dColorImageResolution={quality} -dPDFSETTINGS=/screen -dOptimize=true -dColorImageDownsampleType=/Average  -dNOPAUSE -dBATCH -sOutputFile="{name}_Q{quality}.pdf" "{c}"'
                        #print(a)
                        #self.runOrder(a)

                        pdfRead = PdfReader(c)
                        pdfWrite = PdfWriter()

                        for page in pdfRead.pages:
                            page.compress_content_streams()
                            pdfWrite.add_page(page)
                         
                        with open(f"{name}_Q{quality}.pdf", "wb") as f:
                            pdfWrite.write(f)

                    else:
                        img = Image.open(c)
                        img.save(f"{name}_Q-{quality}.pdf", quality=quality, optimize=True, progressive=True)
                
                    processed = processed + 1
                    percentage = (processed/len(being_process_thing_list))*100
                    self.signal.progress.emit(int(percentage))

                    #self.progressBar.setValue(int(percentage))

            case "JPEG":
                for c in being_process_thing_list:
                    filename = f"{self.outputPath.text()}\\{ntpath.basename(c)}"
                    name, ext = os.path.splitext(filename)
                    # pages = convert_from_path(f"{c}", poppler_path=r"poppler-21.03.0\Library\bin")
                    # print(c)
                    # for x in range(len(pages)):
                    #     outName = f"{self.outputPath.text()}\\{ntpath.basename(c).split('.jp')}_page{str(x+1)}.jpg".replace("[", "").replace("]", "")
                    #     print(str(x))
                    #     pages[x].save(outName, 'JPEG')
                    if ext == ".pdf":
                    # if c[:-4] == ".pdf":

                        a = f'gs\\bin\\gswin64c.exe -sDEVICE=jpeg -dNOPAUSE -dBATCH -r{quality} -sOutputFile="{name}_page-%03d_Q-{quality}.jpeg" "{c}"'
                        print(a)
                        self.runOrder(a)

                    else:
                        print(f"Begin! {name}_Q-{quality}.jpeg")
                        img = Image.open(c, mode='r')
                        print(c)
                        img.save(f"{name}_Q-{quality}.jpeg", quality=quality, optimize=True, progressive=True, format="JPEG")

                    ext == ""

                    processed = processed + 1
                    percentage = (processed/len(being_process_thing_list))*100
                    #self.

                    self.signal.result.emit("{name}_Q-{quality}.jpeg")
                    self.signal.progress.emit(int(percentage))

            case "PNG":
                #initial skeleton for PNG support (untested)

                for c in being_process_thing_list:
                    filename = f"{self.outputPath.text()}\\{ntpath.basename(c)}"
                    name, ext = os.path.splitext(filename)

                    if ext == ".pdf":
                    # if c[:-4] == ".pdf":

                        a = f'gs\\gs9.53.3\\bin\\gswin32c.exe -sDEVICE=png16 -dNOPAUSE -dBATCH -r{quality} -sOutputFile="{name}_page-%03d_Q-{quality}.jpeg" "{c}"'
                        print(a)
                        self.runOrder(a)

                    else:
                        img = Image.open(c)
                        img.save(f"{name}_Q-{quality}.png", quality=quality, optimize=True, progressive=True)
                        img.close()

                    ext == ""

            case "TimeThief":
                pass


            case _:
                print("congrats, you are a developer now :)")