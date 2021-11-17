import json
import os
from PyQt5.QtWidgets import QMessageBox
from treelib import Node, Tree

tree = Tree()
cwd = os.getcwd()
tree.create_node(cwd, cwd)
# tree.create_node("Harry", 1, data={
#                  "name": "dsa", "createdAt": 12, "size": 12})  # root node
# tree.create_node("Hdarry", "harry", 1)  # root node
# tree.create_node("arry", "arry", "harry")  # root node
# print(tree.to_json(with_data=True))


def getcwd():
    return os.getcwd()


def goback():
    os.chdir("../")
    cwd = os.getcwd()
    print(cwd)


def changeWD(pathValue):
    print(pathValue)
    os.chdir(pathValue)


def createErrorBox(msg, icon):
    msgBox = QMessageBox()
    msgBox.setIcon(icon)
    msgBox.setText(msg)
    msgBox.setWindowTitle("Error")
    msgBox.exec_()


def createInfoBox(msg):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(msg)
    msgBox.setWindowTitle("Info")
    msgBox.exec_()


def createFile(fileName):
    try:
        cwd = os.getcwd()
        filePath = os.path.join(cwd, fileName)
        if not os.path.exists(filePath):
            with open(fileName, 'w') as fp:
                fp.write("New File Created")
                fp.close()
            tree.create_node(filePath, filePath, cwd, {"isDir": False})
            createInfoBox(fileName+" created")
        else:
            createErrorBox("File already exists", QMessageBox.Critical)
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def deleteFile(fileName):
    try:
        os.remove(fileName)
        createInfoBox(fileName+" deleted")
        filePath = os.path.join(cwd, fileName)
        tree.remove_node(filePath)
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def createDirectory(dirName):
    try:
        os.mkdir(dirName)
        createInfoBox(dirName+" created")
        cwd = os.getcwd()
        dirPath = os.path.join(cwd, dirName)
        tree.create_node(dirPath, dirPath, cwd, {"isDir": True})
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def deleteDirectory(dirName):
    try:
        os.rmdir(dirName)
        createInfoBox(dirName+" created")
        dirPath = os.path.join(cwd, dirName)
        tree.remove_node(dirPath)
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def openFile(fileName):
    try:
        os.startfile(fileName)
        createInfoBox(fileName+" opened")
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def closeFile(fileName):
    try:
        os.close(fileName)
        createInfoBox(fileName+" closed")
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def writeToFile(fileName, pos, text, appMode):
    if bool(fileName) and bool(text):
        if appMode:
            try:
                print("APPEND MODE")
                if os.path.exists(fileName):
                    file_object = open(fileName, 'a')
                    file_object.write(text)
                    file_object.close()
                    createInfoBox(fileName+" modified")
                else:
                    createErrorBox(
                        "File Specified does not exist", QMessageBox.Critical)

            except Exception as e:
                createErrorBox(str(e), QMessageBox.Critical)
        else:
            try:
                if os.path.exists(fileName):
                    with open(fileName, "w") as f:
                        f.seek(int(pos), 0)
                        f.write(text)
                    createInfoBox(fileName+" modified")
                else:
                    createErrorBox(
                        "File Specified does not exist", QMessageBox.Critical)
            except Exception as e:
                createErrorBox(str(e), QMessageBox.Critical)
    else:
        createErrorBox("Please Fill All the Fields", QMessageBox.Warning)


def recurseDirHandle(dir):
    for contentWithin in dir.values():
        for child in contentWithin["children"]:
            for name in child:
                if child[name]["data"]["isDir"]:
                    if child[name]["children"]:
                        recurseDirHandle(child[name]["children"])
                else:
                    stat = os.stat(name)
                    child[name]["data"] = {"isDir": False, "file_mode": stat.st_mode, "inode": stat.st_ino, "num_of_hard_links": stat.st_nlink, "user_id": stat.st_uid,
                                           "group_id": stat.st_gid, "size": stat.st_size, "last_access_time": stat.st_atime, "last_modified": stat.st_mtime}


def showMemMap():
    memMap = json.loads(tree.to_json(with_data=True))
    recurseDirHandle(memMap)
    # print(memMap)
    # for node in tree.expand_tree(mode=Tree.DEPTH):
    #     print(memMap[tree[node].tag])
    print(memMap)
