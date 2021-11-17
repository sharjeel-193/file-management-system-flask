import stylesheet
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QPlainTextEdit, QTextEdit, QCheckBox
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QValidator, QIntValidator
import functions


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
    closeBtn.clicked.connect(functions.closeFile)
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


def showMemMapDlg():
    functions.showMemMap()
