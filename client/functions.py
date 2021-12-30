import json
import os
from PyQt5.QtWidgets import QMessageBox
from treelib import Tree

tree = Tree()
root = os.getcwd()
tree.create_node(root, root)
memMapFileName = os.path.join(root, "memMap.txt")


def unravelMemMap(dir, root):
    for entryName, contentWithin in dir.items():
        if "children" in contentWithin:
            for child in contentWithin["children"]:
                for name in child:
                    parent = os.path.join(
                        root, entryName) if not root == "" else entryName
                    if os.path.exists(os.path.join(parent, name)):
                        tree.create_node(
                            name, os.path.join(parent, name), parent, child[name]["data"])
                        print(child)
                        if child[name]["data"]["isDir"]:
                            if "children" in child[name]:
                                unravelMemMap(child, parent)


if os.path.exists(memMapFileName):
    with open(memMapFileName, "r") as f:
        memMap = json.loads(f.read())
        f.close()
    print(memMap)
    unravelMemMap(memMap, "")


def persistMemMap():
    with open(memMapFileName, "w") as f:
        f.write(tree.to_json(with_data=True))
        f.close()


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
            print(tree.create_node(fileName, filePath, cwd, {"isDir": False}))
            persistMemMap()
            createInfoBox(fileName+" created")
        else:
            createErrorBox("File already exists", QMessageBox.Critical)
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def deleteFile(fileName):
    try:
        os.remove(fileName)
        createInfoBox(fileName+" deleted")
        filePath = os.path.join(os.getcwd(), fileName)
        tree.remove_node(filePath)
        persistMemMap()
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def createDirectory(dirName):
    try:
        os.mkdir(dirName)
        createInfoBox(dirName+" created")
        cwd = os.getcwd()
        dirPath = os.path.join(cwd, dirName)
        print(tree.create_node(dirName, dirPath, cwd, {"isDir": True}))
        persistMemMap()
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def deleteDirectory(dirName):
    try:
        os.rmdir(dirName)
        createInfoBox(dirName+" created")
        dirPath = os.path.join(os.getcwd(), dirName)
        tree.remove_node(dirPath)
        persistMemMap()
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


def readFromFile(fileName, pos, size):
    try:
        x = int(pos)+int(size)
        f = open(fileName, "r")
        data = f.read()
        f.close()
        return data[int(pos):int(x)]
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def moveContentWithinFile(fileName, start, size, target):
    try:
        x = int(start)+int(size)
        f = open(fileName, "r")
        data = f.read()
        f.close()
        f = open(fileName, "w")
        moveData = data[int(start):x]
        data = data[:int(target)] + moveData+data[int(target):]
        removedData = ""
        data = data[:int(start)]+removedData+data[x:]
        f.write(data)
        f.close()
        createInfoBox(fileName + " Content Modified")
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def moveFile(fileName, newDir):
    try:
        cwd = os.getcwd()
        oldPath = os.path.join(cwd, fileName)
        newPath = os.path.join(cwd, newDir, fileName)
        os.rename(oldPath, newPath)
        createInfoBox("File Moved")
        node = tree.get_node(oldPath)
        tree.remove_node(oldPath)
        print(tree.create_node(fileName, newPath,
                               os.path.join(cwd, newDir), node.data))
        persistMemMap()
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)


def getDirInfo(filePath):
    stat = os.stat(filePath)
    return {"isDir": True, "num_of_files_and_dirs": sum([len(files) for r, d, files in os.walk(filePath)]), "size": sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(filePath) for filename in filenames), "file_mode": stat.st_mode, "inode": stat.st_ino, "num_of_hard_links": stat.st_nlink, "user_id": stat.st_uid,
            "group_id": stat.st_gid, "last_access_time": stat.st_atime, "last_modified": stat.st_mtime}


def recurseDirHandle(dir, root):
    for entryName, contentWithin in dir.items():
        if "children" in contentWithin:
            for child in contentWithin["children"]:
                for name in child:
                    parent = os.path.join(
                        root, entryName) if not root == "" else entryName

                    if child[name]["data"]["isDir"]:
                        child[name]["data"] = getDirInfo(os.path.join(
                            parent, name))
                        if "children" in child[name]:
                            recurseDirHandle(child, parent)
                    else:
                        stat = os.stat(os.path.join(parent, name))
                        child[name]["data"] = {"isDir": False, "file_mode": stat.st_mode, "inode": stat.st_ino, "num_of_hard_links": stat.st_nlink, "user_id": stat.st_uid,
                                               "group_id": stat.st_gid, "size": stat.st_size, "last_access_time": stat.st_atime, "last_modified": stat.st_mtime}


def showMemMap():
    memMap = json.loads(tree.to_json(with_data=True))
    recurseDirHandle(memMap, "")
    for entryName, contentWithin in memMap.items():
        contentWithin["data"] = getDirInfo(entryName)
    return memMap


def mapToText(memMap, treeText):
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
                            mapToText(child, treeText)
                    else:
                        pass
    # print(treeText)


def truncateFile(fileName, size):
    try:
        if os.path.exists(fileName):
            file_obj = open(fileName, 'a')
            file_obj.truncate(int(size))
            file_obj.close()
            createInfoBox(fileName + " Truncated")
        else:
            createErrorBox('File Specified does not exist',
                           QMessageBox.Critical)

    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)
