import sys
import PyQt5.QtWidgets as qtWidget
import PyQt5.QtGui as qtGui
from PyQt5 import QtCore
import functions
import stylesheet
import dialogues
import os
# import threading


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


class MainWindow(qtWidget.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windows = []
        self.setWindowTitle("OOPS")
        self.setFixedWidth(1000)
        # window.move(2700, 200)
        self.setStyleSheet("background: #FFFFFF;")

        btnGrid = qtWidget.QGridLayout()
        pathLayout = qtWidget.QHBoxLayout()
        # window.setLayout(grid)
        mainLayout = qtWidget.QVBoxLayout()

        self.setLayout(mainLayout)

        # LOGO & PROJECT NAME
        image = qtGui.QPixmap("logo.jpg")
        logo = qtWidget.QLabel()
        logo.setStyleSheet("margin-top: 20px; margin-bottom: 0px;")
        logo.setPixmap(image)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        mainLayout.addWidget(logo)

        brandName = qtWidget.QLabel()
        brandName.setText("Our Own Operating System")
        brandName.setStyleSheet(
            "font-size: 20px; font-family: Copperplate; margin-bottom: 30px")
        brandName.setAlignment(QtCore.Qt.AlignCenter)
        mainLayout.addWidget(brandName)
        # Current Path and Directory
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

        # Functions Btn

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

        moveContentFileBtn = qtWidget.QPushButton()
        moveContentFileBtn.setCursor(
            qtGui.QCursor(QtCore.Qt.PointingHandCursor))
        moveContentFileBtn.setIcon(qtGui.QIcon("closeFile.png"))
        moveContentFileBtn.setText(" Move Content Within File")
        moveContentFileBtn.clicked.connect(dialogues.moveContentFile)
        moveContentFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
        btnGrid.addWidget(moveContentFileBtn, 2, 1)

        readFileBtn = qtWidget.QPushButton()
        readFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
        readFileBtn.setIcon(qtGui.QIcon("read.png"))
        readFileBtn.setText(" Read from File")
        readFileBtn.clicked.connect(dialogues.readFileDlg)
        readFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
        btnGrid.addWidget(readFileBtn, 3, 0)

        writeFileBtn = qtWidget.QPushButton()
        writeFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
        writeFileBtn.setIcon(qtGui.QIcon("write.png"))
        writeFileBtn.setText(" Write to File")
        writeFileBtn.clicked.connect(dialogues.writeToFileDlg)
        writeFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
        btnGrid.addWidget(writeFileBtn, 3, 1)

        moveFileBtn = qtWidget.QPushButton()
        moveFileBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
        moveFileBtn.setIcon(qtGui.QIcon("memory.png"))
        moveFileBtn.setText(" Move File")
        moveFileBtn.clicked.connect(dialogues.showMoveFileDlg)
        moveFileBtn.setStyleSheet(stylesheet.funcBtnStyle)
        btnGrid.addWidget(moveFileBtn, 4, 0)

        memoryMapBtn = qtWidget.QPushButton()
        memoryMapBtn.setCursor(qtGui.QCursor(QtCore.Qt.PointingHandCursor))
        memoryMapBtn.setIcon(qtGui.QIcon("memory.png"))
        memoryMapBtn.setText(" Show Memory Map")
        memoryMapBtn.clicked.connect(self.show_new_window)
        memoryMapBtn.setStyleSheet(stylesheet.funcBtnStyle)
        btnGrid.addWidget(memoryMapBtn, 4, 1)

        mainLayout.addLayout(btnGrid)

    def show_new_window(self):
        self.windows.append(MainWindow())
        self.windows[len(self.windows) - 1].show()


app = qtWidget.QApplication(sys.argv)
window = MainWindow()
# window.setWindowTitle("OOPS")
# window.setFixedWidth(1000)
# # window.move(2700, 200)
# window.setStyleSheet("background: #FFFFFF;")
# mainLayout = qtWidget.QVBoxLayout()
# window.setLayout(mainLayout)


window.show()
sys.exit(app.exec_())


# try:
#     t1 = threading.Thread(target=startProgram)
#     t1.start()
# except Exception as e:
#     print(e)

# startProgram()


def getcwd():
    return os.getcwd()
