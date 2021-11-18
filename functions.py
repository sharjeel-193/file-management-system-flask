import json
import os
from PyQt5.QtWidgets import QMessageBox
from treelib import  Tree
import json2tree

tree = Tree()
cwd = os.getcwd()
tree.create_node(cwd, cwd)

class Node(object):
    def __init__(self, name, path_to_file=None):
        self.name = name
        self.path_to_file = path_to_file
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

    def dump(self, indent=0):
        """dump tree to string"""
        tab = '    '*(indent-1) + ' |- ' if indent > 0 else ''
        print('%s%s' % (tab, self.name))
        for obj in self.children:
            obj.dump(indent + 1)

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
            tree.create_node(fileName, filePath, cwd, {"isDir": False})
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
        tree.create_node(dirName, dirPath, cwd, {"isDir": True})
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
    print(fileName)
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
                    with open(fileName, "r") as f:
                        fileData = f.read()
                        f.close()

                    with open(fileName, "w") as f:
                        fileData = fileData[:int(
                            pos)] + text + fileData[int(pos):]
                        f.write(fileData)
                    createInfoBox(fileName+" modified")
                else:
                    createErrorBox(
                        "File Specified does not exist", QMessageBox.Critical)
            except Exception as e:
                createErrorBox(str(e), QMessageBox.Critical)
    else:
        createErrorBox("Please Fill All the Fields", QMessageBox.Warning)

def readFromFile (fileName, pos, size):
    try:
        x=int(pos)+int(size)
        f = open(fileName, "r")
        data = f.read()
        f.close()
        return data[int(pos):int(x)]
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)

def moveContentWithinFile(fileName, start, size, target):
    try:
        x=int(start)+int(size)
        f = open(fileName, "r")
        data = f.read()
        f.close()
        f = open(fileName, "w")
        moveData=data[int(start):x]
        data=data[:int(target)] + moveData+data[int(target):]
        removedData=""
        data=data[:int(start)]+removedData+data[x:]
        f.write(data) 
        f.close()
        createInfoBox(fileName + " Content Modified")
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)

def moveFile(fileName,newDir):
    try:
        cwd = os.getcwd()
        os.rename(cwd+"/"+fileName, newDir+"/"+fileName)
        createInfoBox("File Moved")
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)



def recurseDirHandle(dir):
    for contentWithin in dir.values():
        if "children" in contentWithin:
            for child in contentWithin["children"]:
                for name in child:
                    if child[name]["data"]["isDir"]:
                        if "children" in child[name]:
                            recurseDirHandle(child)
                    else:
                        stat = os.stat(name)
                        child[name]["data"] = {"isDir": False, "file_mode": stat.st_mode, "inode": stat.st_ino, "num_of_hard_links": stat.st_nlink, "user_id": stat.st_uid,
                                               "group_id": stat.st_gid, "size": stat.st_size, "last_access_time": stat.st_atime, "last_modified": stat.st_mtime}


def showMemMap():
    memMap = json.loads(tree.to_json(with_data=True))
    # recurseDirHandle(memMap)
    # os.remove('tree.txt')
    # tree.save2file('tree.txt')
    # print(json2tree(json.dumps(memMap)))

    # with open('tree.txt') as file:
    #     lines = file.readlines()
    #     lines = [line.rstrip() for line in lines]

    # print (lines)
    # print(memMap)
    # for entry in memMap:
    #     treeText = f"{entry}\n|_ "
    # mapToText(memMap,treeText)
    # print(treeText)
    return tree

def mapToText(memMap,treeText):
    # rootName = 'F:\BSCS\BSCS-Sem-5\CS 330 - Operating Systems\LABS\Lab 6'
    # info = memMap[rootName]
    # # print(info)
    # for child in info['children']:
    #     if child:
    #         root.add_child(mapToText(child))
    # print (root)
    for contentWithin in memMap.values():
        if "children" in contentWithin:
            for child in contentWithin["children"]:
                for name in child:
                    treeText += name
                    if child[name]["data"]["isDir"]:
                        if "children" in child[name]:
                            treeText += "\n|_ "
                            mapToText(child,treeText)
                    else:
                        pass
    print(treeText)



