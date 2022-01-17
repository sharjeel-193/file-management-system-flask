import stylesheet
from PyQt5.QtWidgets import QDialog, QLabel, QMessageBox, QLineEdit, QListWidget, QPushButton, QGridLayout, QPlainTextEdit, QTextEdit, QCheckBox, QTreeWidget, QTreeWidgetItem
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QIntValidator
import functions
import os
import requests

base_url = ""
userName = ""


def handleReq(reqType, endpoint, showDlg):
    res = ""
    try:
        if reqType == "get":
            res = requests.get(base_url+endpoint)
        elif reqType == "post":
            res = requests.post(base_url+endpoint)
        elif reqType == "patch":
            res = requests.patch(base_url+endpoint)
        else:
            res = requests.delete(base_url+endpoint)
        parseRes = res.json()
        # print({'PARSE RESPONSE': parseRes})
        if "data" in parseRes.keys():
            if showDlg:
                functions.createInfoBox(parseRes["data"])
            if "content" in parseRes.keys():
                return parseRes["content"]
        elif "content" in parseRes.keys():
            # print(parseRes["content"])
            return parseRes["content"]
        else:
            if showDlg:
                functions.createErrorBox(
                    parseRes["error"], QMessageBox.Critical)
            return parseRes["error"]
    except Exception as e:
        functions.createErrorBox(
            "Connection with Server Failed", QMessageBox.Critical)
        return "error"


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
    addBtn.clicked.connect(lambda: handleReq("post",
                                             f"/add_file?fileName={nameBox.text()}&userName=${userName}", True))
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
    delBtn.clicked.connect(lambda: handleReq("delete",
                                             f"/del_file?fileName={nameBox.text()}&userName=${userName}", True))
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
    addBtn.clicked.connect(lambda: handleReq("post",
                                             f"/add_dir?dirName={nameBox.text()}&userName=${userName}", True))
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
    delBtn.clicked.connect(lambda: handleReq("delete",
                                             f"/del_dir?dirName={nameBox.text()}&userName=${userName}", True))
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
    openBtn.clicked.connect(lambda: handleReq("get",
                                              f"/open_file?fileName={nameBox.text()}&userName=${userName}", True))
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
    closeBtn.clicked.connect(lambda: handleReq("get",
                                               f"/close_file?fileName={nameBox.text()}&userName=${userName}", True))
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
    writeBtn.clicked.connect(lambda: handleReq("patch",
                                               f"/write_file?fileName={nameBox.text()}&userName=${userName}&pos={posBox.text()}&text={textBox.toPlainText()}&appMode={checkAppend.isChecked()}", True))
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
    writeBtn.clicked.connect(lambda: textBox.setPlainText(handleReq(
        "get", f"/read_file?fileName={nameBox.text()}&userName=${userName}&pos={posBox.text()}&size={sizeBox.text()}", True)))
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
    moveBtn.clicked.connect(lambda: handleReq("patch",
                                              f"/move_file_content?fileName={nameBox.text()}&userName=${userName}&start={startBox.text()}&size={sizeBox.text()}&target={targetBox.text()}", True))
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
    moveBtn.clicked.connect(lambda: handleReq("patch",
                                              f"/move_file?fileName={nameBox.text()}&userName=${userName}&newDir={dirName.text()}", True))
    grid.addWidget(moveBtn, 2, 1)

    dlg.exec()


def makeTree(tree, root, treeNode):
    for entryName, contentWithin in tree.items():
        if "children" in contentWithin:
            for child in contentWithin["children"]:
                for name in child:
                    # print(child)
                    parent = os.path.join(
                        root, entryName) if not root == "" else entryName
                    branch = QTreeWidgetItem([name])
                    treeNode.addChild(branch)
                    if child[name]["data"]["isDir"]:
                        if "children" in child[name]:
                            makeTree(child, parent, branch)


def searchText(text, tree, root):
    for entryName, contentWithin in tree.items():
        if text == entryName:
            return contentWithin["data"]
        if "children" in contentWithin:
            for child in contentWithin["children"]:
                for name in child:
                    if name == text:
                        return child[name]["data"]
                    parent = os.path.join(
                        root, entryName) if not root == "" else entryName
                    if child[name]["data"]["isDir"]:
                        if "children" in child[name]:
                            output = searchText(text, child, parent)
                            if len(output) > 0:
                                return output

        return {}
    return {}


def handleTreeItemClicked(clickedItem, tree):
    text = clickedItem.text(0)
    info = searchText(text, tree, "")
    outStr = ""
    for key, value in info.items():
        outStr += f"{key}: {value}\n"
    dlg = QDialog()
    grid = QGridLayout()
    dlg.setLayout(grid)
    dlg.setWindowTitle("Memory Map")

    textBox = QLabel()
    textBox.setStyleSheet(stylesheet.formInputStyle)
    textBox.resize(300, 200)
    textBox.setText(outStr)
    grid.addWidget(textBox, 0, 0)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    dlg.exec()


def showMemMapDlg():
    tree = handleReq("get", "/show_mem_map", False)
    # print(tree)
    if tree == "error":
        return
    dlg = QDialog()
    grid = QGridLayout()
    dlg.setLayout(grid)
    dlg.setWindowTitle("Memory Map")

    treeWidget = QTreeWidget()
    for entryName in tree:
        topTreeNode = QTreeWidgetItem([entryName])
        treeWidget.addTopLevelItem(topTreeNode)
    makeTree(tree, "", topTreeNode)
    treeWidget.itemClicked.connect(
        lambda clickedItem: handleTreeItemClicked(clickedItem, tree))
    grid.addWidget(treeWidget, 0, 0)

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 1, 0)

    dlg.exec()


def truncateFileDialog():
    dlg = QDialog()
    grid = QGridLayout()
    dlg.setLayout(grid)
    dlg.setWindowTitle("Truncate File")

    label = QLabel()
    label.setText("File Name")
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet(stylesheet.formLabelStyle)
    grid.addWidget(label, 0, 0)

    nameBox = QLineEdit()
    nameBox.setStyleSheet(stylesheet.formInputStyle)
    grid.addWidget(nameBox, 0, 1)

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

    cancelBtn = QPushButton()
    cancelBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    cancelBtn.setText("Cancel")
    cancelBtn.setStyleSheet(stylesheet.formBtnStyle)
    cancelBtn.clicked.connect(dlg.close)
    grid.addWidget(cancelBtn, 3, 0)

    truncateBtn = QPushButton()
    truncateBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    truncateBtn.setText("Truncate")
    truncateBtn.setStyleSheet(stylesheet.formBtnStyle)
    truncateBtn.clicked.connect(
        lambda: handleReq("patch", f"/truncate_file?fileName={nameBox.text()}&userName=${userName}&size={sizeBox.text()}", True))
    grid.addWidget(truncateBtn, 3, 1)

    dlg.exec()
