import sys
import PyQt5.QtWidgets as qtWidget
import PyQt5.QtGui as qtGui
from PyQt5 import QtCore
import functions
import stylesheet
import dialogues
import os

def goback():
    try:
        os.chdir("../")
        cwd = os.getcwd()
        pathName.setText(cwd)
    except Exception as e:
        pathName.setText(os.getcwd())
        msgBox = qtWidget.QMessageBox()
        msgBox.setIcon(qtWidget.QMessageBox.Critical)
        msgBox.setText(str(e))
        msgBox.setWindowTitle("Error")
        msgBox.exec_()

def changeWD():
    try:
        if os.getcwd() != pathName.text():
            os.chdir(pathName.text())
            msgBox = qtWidget.QMessageBox()
            msgBox.setIcon(qtWidget.QMessageBox.Information)
            msgBox.setText("Current Working Directory Changed")
            msgBox.setWindowTitle("Info")
            msgBox.exec_()
            cwd = os.getcwd()
            pathName.setText(cwd)
    except Exception as e:
        pathName.setText(os.getcwd())
        msgBox = qtWidget.QMessageBox()
        msgBox.setIcon(qtWidget.QMessageBox.Critical)
        msgBox.setText(str(e))
        msgBox.setWindowTitle("Error")
        msgBox.exec_()


app = qtWidget.QApplication(sys.argv)
window = qtWidget.QWidget()
window.setWindowTitle("OOPS")
window.setFixedWidth(1000)
# window.move(2700, 200)
window.setStyleSheet("background: #FFFFFF;")

btnGrid = qtWidget.QGridLayout()
pathLayout = qtWidget.QHBoxLayout()
# window.setLayout(grid)
mainLayout = qtWidget.QVBoxLayout()

window.setLayout(mainLayout)

# LOGO & PROJECT NAME
image = qtGui.QPixmap("logo.jpg")
logo = qtWidget.QLabel()
logo.setStyleSheet("margin-top: 20px; margin-bottom: 0px;")
logo.setPixmap(image)
logo.setAlignment(QtCore.Qt.AlignCenter)
mainLayout.addWidget(logo)

brandName = qtWidget.QLabel()
brandName.setText("Our Own Operating System")
brandName.setStyleSheet("font-size: 20px; font-family: Copperplate; margin-bottom: 30px")
brandName.setAlignment(QtCore.Qt.AlignCenter)
mainLayout.addWidget(brandName)

#Current Path and Directory
backBtn = qtWidget.QPushButton()
backBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
backBtn.setIcon(qtGui.QIcon("backBtn.png"))
backBtn.setToolTip("Go Back")
# backBtn.clicked.connect(functions.goback)
backBtn.clicked.connect(goback)
backBtn.setStyleSheet(stylesheet.backBtnStyle)
# grid.addWidget(backBtn,4,0)
pathLayout.addWidget(backBtn)

pathName = qtWidget.QLineEdit()
pathName.setText(functions.getcwd())
# pathName.textChanged.connect(functions.getcwd())
pathName.setStyleSheet(stylesheet.pathLineStyle)
pathLayout.addWidget(pathName)

goBtn = qtWidget.QPushButton()
goBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
goBtn.setIcon(qtGui.QIcon("goBtn.png"))
goBtn.setToolTip("Go")
goBtn.setStyleSheet(stylesheet.backBtnStyle)
goBtn.clicked.connect(changeWD)
pathLayout.addWidget(goBtn)

mainLayout.addLayout(pathLayout)

#Functions Btn

addFileBtn = qtWidget.QPushButton()
addFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
addFileBtn.setIcon(qtGui.QIcon("addFile.png"))
addFileBtn.setText(" Add File")
addFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
addFileBtn.clicked.connect(dialogues.createFileDlg)
btnGrid.addWidget(addFileBtn, 0, 0)

delFileBtn = qtWidget.QPushButton()
delFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
delFileBtn.setIcon(qtGui.QIcon("delFile.png"))
delFileBtn.setText(" Delete File")
delFileBtn.clicked.connect(dialogues.deleteFileDlg)
delFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
btnGrid.addWidget(delFileBtn, 0, 1)

addDirBtn = qtWidget.QPushButton()
addDirBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
addDirBtn.setIcon(qtGui.QIcon("addDir.png"))
addDirBtn.setText(" Add Directory")
addDirBtn.clicked.connect(dialogues.addDirDlg)
addDirBtn.setStyleSheet(stylesheet.funcBtnStyle)
btnGrid.addWidget(addDirBtn, 1, 0)

delDirBtn = qtWidget.QPushButton()
delDirBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
delDirBtn.setIcon(qtGui.QIcon("delDir.png"))
delDirBtn.setText(" Delete Directory")
delDirBtn.clicked.connect(dialogues.delDirDlg)
delDirBtn.setStyleSheet(stylesheet.funcBtnStyle)
btnGrid.addWidget(delDirBtn, 1, 1)

openFileBtn = qtWidget.QPushButton()
openFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
openFileBtn.setIcon(qtGui.QIcon("openFile.png"))
openFileBtn.setText(" Open File")
openFileBtn.clicked.connect(dialogues.openFileDlg)
openFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
btnGrid.addWidget(openFileBtn, 2, 0)

closeFileBtn = qtWidget.QPushButton()
closeFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
closeFileBtn.setIcon(qtGui.QIcon("closeFile.png"))
closeFileBtn.setText(" Close File")
closeFileBtn.clicked.connect(dialogues.closeFileDlg)
closeFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
btnGrid.addWidget(closeFileBtn, 2, 1)

readFileBtn = qtWidget.QPushButton()
readFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
readFileBtn.setIcon(qtGui.QIcon("read.png"))
readFileBtn.setText(" Read from File")
readFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
btnGrid.addWidget(readFileBtn, 3, 0)

writeFileBtn = qtWidget.QPushButton()
writeFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
writeFileBtn.setIcon(qtGui.QIcon("write.png"))
writeFileBtn.setText(" Write to File")
writeFileBtn.clicked.connect(dialogues.writeToFileDlg)
writeFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
btnGrid.addWidget(writeFileBtn, 3, 1)


memoryMapBtn = qtWidget.QPushButton()
memoryMapBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
memoryMapBtn.setIcon(qtGui.QIcon("memory.png"))
memoryMapBtn.setText(" Show Memory Map")
memoryMapBtn.setStyleSheet(stylesheet.funcBtnStyle)
btnGrid.addWidget(memoryMapBtn, 4, 1)



mainLayout.addLayout(btnGrid)





window.show()
sys.exit(app.exec())

def getcwd():
    return os.getcwd()

