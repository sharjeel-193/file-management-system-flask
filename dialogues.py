import stylesheet
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QPlainTextEdit, QTextEdit, QCheckBox
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QValidator, QIntValidator
import functions
import os


def createFileDlg():
    dlg = QDialog()
    grid = QGridLayout()
    # dlg.width(500)
    dlg.setLayout(grid)
    dlg.setWindowTitle("Create File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    addBtn = QPushButton()
    addBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    addBtn.setText("Add")
    addBtn.setStyleSheet(stylesheet.formBtnStyle)
    addBtn.clicked.connect(lambda: functions.createFile(nameBox.text()))
    grid.addWidget(addBtn, 1, 1)

    dlg.exec()


def deleteFileDlg():
    dlg = QDialog()
    grid = QGridLayout()
    # dlg.width(500)
    dlg.setLayout(grid)
    dlg.setWindowTitle("Delete File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    delBtn = QPushButton()
    delBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    delBtn.setText("Delete")
    delBtn.setStyleSheet(stylesheet.formBtnStyle)
    delBtn.clicked.connect(lambda: functions.deleteFile(nameBox.text()))
    grid.addWidget(delBtn, 1, 1)

    dlg.exec()


def addDirDlg():
    dlg = QDialog()
    grid = QGridLayout()
    # dlg.width(500)
    dlg.setLayout(grid)
    dlg.setWindowTitle("Add Directory")

    label = QLabel()
    label.setText("Directory Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    addBtn = QPushButton()
    addBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    addBtn.setText("Add")
    addBtn.setStyleSheet(stylesheet.formBtnStyle)
    addBtn.clicked.connect(lambda: functions.createDirectory(nameBox.text()))
    grid.addWidget(addBtn, 1, 1)

    dlg.exec()


def delDirDlg():
    dlg = QDialog()
    grid = QGridLayout()
    # dlg.width(500)
    dlg.setLayout(grid)
    dlg.setWindowTitle("Delete Directory")

    label = QLabel()
    label.setText("Directory Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    delBtn = QPushButton()
    delBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    delBtn.setText("Delete")
    delBtn.setStyleSheet(stylesheet.formBtnStyle)
    delBtn.clicked.connect(lambda: functions.deleteDirectory(nameBox.text()))
    grid.addWidget(delBtn, 1, 1)

    dlg.exec()


def openFileDlg():
    dlg = QDialog()
    grid = QGridLayout()
    # dlg.width(500)
    dlg.setLayout(grid)
    dlg.setWindowTitle("Open File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    openBtn = QPushButton()
    openBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    openBtn.setText("Open")
    openBtn.setStyleSheet(stylesheet.formBtnStyle)
    openBtn.clicked.connect(lambda: functions.openFile(nameBox.text()))
    grid.addWidget(openBtn, 1, 1)

    dlg.exec()


def closeFileDlg():
    dlg = QDialog()
    grid = QGridLayout()
    # dlg.width(500)
    dlg.setLayout(grid)
    dlg.setWindowTitle("Close File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    closeBtn = QPushButton()
    closeBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    closeBtn.setText("Close")
    closeBtn.setStyleSheet(stylesheet.formBtnStyle)
    closeBtn.clicked.connect(lambda: functions.closeFile(nameBox.text()))
    grid.addWidget(closeBtn, 1, 1)

    dlg.exec()


def writeToFileDlg():
    dlg = QDialog()
    grid = QGridLayout()
    dlg.setLayout(grid)
    dlg.setWindowTitle("Write to File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    label = QLabel()
    label.setText("Append")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 2, 0)

    checkAppend = QCheckBox()
    checkAppend.stateChanged.connect(
        lambda: posBox.setEnabled(not (checkAppend.isChecked())))
    grid.addWidget(checkAppend, 2, 1)

    label = QLabel()
    label.setText("Position")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 3, 0)

    posBox = QLineEdit()
    posBox.setValidator(QIntValidator())
    posBox.setText(str(1))
    posBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(posBox, 3, 1)

    label = QLabel()
    label.setText("Text")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 4, 0)

    textBox = QPlainTextEdit()
    textBox.setStyleSheet(stylesheet.formInputStyle)
    textBox.resize(300, 200)
    grid.addWidget(textBox, 4, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 5, 0)

    writeBtn = QPushButton()
    writeBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    writeBtn.setText("Write to File")
    writeBtn.setStyleSheet(stylesheet.formBtnStyle)
    writeBtn.clicked.connect(lambda: functions.writeToFile(
        nameBox.text(), posBox.text(), textBox.toPlainText(), checkAppend.isChecked()))
    grid.addWidget(writeBtn, 5, 1)

    dlg.exec()


def readFileDlg():
    dlg = QDialog()
    grid = QGridLayout()
    dlg.setLayout(grid)
    dlg.setWindowTitle("Read File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    label = QLabel()
    label.setText("Position")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 2, 0)

    posBox = QLineEdit()
    posBox.setValidator(QIntValidator())
    posBox.setText(str(1))
    posBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(posBox, 2, 1)

    label = QLabel()
    label.setText("Size")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 3, 0)

    sizeBox = QLineEdit()
    sizeBox.setValidator(QIntValidator())
    sizeBox.setText(str(1))
    sizeBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(sizeBox, 3, 1)

    label = QLabel()
    label.setText("Text")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 4, 0)

    textBox = QPlainTextEdit()
    textBox.setStyleSheet(stylesheet.formInputStyle)
    textBox.resize(300, 200)
    grid.addWidget(textBox, 4, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 5, 0)

    writeBtn = QPushButton()
    writeBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    writeBtn.setText("Read from File")
    writeBtn.setStyleSheet(stylesheet.formBtnStyle)
    writeBtn.clicked.connect(lambda: textBox.setPlainText(
        functions.readFromFile(nameBox.text(), posBox.text(), sizeBox.text())))
    grid.addWidget(writeBtn, 5, 1)

    dlg.exec()


def moveContentFile():
    dlg = QDialog()
    grid = QGridLayout()
    dlg.setLayout(grid)
    dlg.setWindowTitle("Move Content Within File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    label = QLabel()
    label.setText("Start")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 1, 0)

    startBox = QLineEdit()
    startBox.setValidator(QIntValidator())
    startBox.setText(str(1))
    startBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(startBox, 1, 1)

    label = QLabel()
    label.setText("Size")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 2, 0)

    sizeBox = QLineEdit()
    sizeBox.setValidator(QIntValidator())
    sizeBox.setText(str(1))
    sizeBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(sizeBox, 2, 1)

    label = QLabel()
    label.setText("Target")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 3, 0)

    targetBox = QLineEdit()
    targetBox.setValidator(QIntValidator())
    targetBox.setText(str(1))
    targetBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(targetBox, 3, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 4, 0)

    moveBtn = QPushButton()
    moveBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    moveBtn.setText("Move Content within File")
    moveBtn.setStyleSheet(stylesheet.formBtnStyle)
    moveBtn.clicked.connect(lambda: functions.moveContentWithinFile(
        nameBox.text(), startBox.text(), sizeBox.text(), targetBox.text()))
    grid.addWidget(moveBtn, 4, 1)

    dlg.exec()


def showMoveFileDlg():
    dlg = QDialog()
    grid = QGridLayout()
    dlg.setLayout(grid)
    dlg.setWindowTitle("Move File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

    label = QLabel()
    label.setText("Target Directory")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 1, 0)

    dirName = QLineEdit()
    # startBox.setValidator(QIntValidator())
    # startBox.setText(str(1))
    dirName.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(dirName, 1, 1)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 2, 0)

    moveBtn = QPushButton()
    moveBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    moveBtn.setText("Move File")
    moveBtn.setStyleSheet(stylesheet.formBtnStyle)
    moveBtn.clicked.connect(lambda: functions.moveFile(
        nameBox.text(), dirName.text()))
    grid.addWidget(moveBtn, 2, 1)

    dlg.exec()


def showMemMapDlg():
    tree = functions.showMemMap()
    str1 = ''
    # print(tree)
    dlg = QDialog()
    grid = QGridLayout()
    dlg.setLayout(grid)
    dlg.setWindowTitle("Write to File")

    textBox = QPlainTextEdit()
    textBox.setStyleSheet(stylesheet.formInputStyle)
    textBox.resize(300, 200)
    textBox.setPlainText(str(tree))
    grid.addWidget(textBox, 0, 0)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    dlg.exec()

    # mapStrings(lines)
    # print(mapStrings(lines))


def mapStrings(mapTree):
    for line in mapTree:
        line = os.path.basename(line)
        print(line)
    return mapTree
