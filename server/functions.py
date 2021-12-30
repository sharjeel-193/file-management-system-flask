import json
import os
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


def makeMemMap():
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
            return {"data": fileName+" created"}
        else:
            return {"error": "File already exists"}
    except Exception as e:
        return {"error": str(e)}


def deleteFile(fileName):
    try:
        os.remove(fileName)
        filePath = os.path.join(os.getcwd(), fileName)
        tree.remove_node(filePath)
        persistMemMap()
        return {"data": fileName + " deleted"}
    except Exception as e:
        return {"error": str(e)}


def createDirectory(dirName):
    try:
        os.mkdir(dirName)
        cwd = os.getcwd()
        dirPath = os.path.join(cwd, dirName)
        print(tree.create_node(dirName, dirPath, cwd, {"isDir": True}))
        persistMemMap()
        return {"data": dirName + " created"}
    except Exception as e:
        return {"error": str(e)}


def deleteDirectory(dirName):
    try:
        os.rmdir(dirName)
        dirPath = os.path.join(os.getcwd(), dirName)
        tree.remove_node(dirPath)
        persistMemMap()
        return {"data": dirName + " deleted"}
    except Exception as e:
        return {"error": str(e)}


def openFile(fileName):
    try:
        os.startfile(fileName)
        return {"data": fileName + " opened"}
    except Exception as e:
        return {"error": str(e)}


def closeFile(fileName):
    print(fileName)
    try:
        os.close(fileName)
        return {"data": fileName + " closed"}
    except Exception as e:
        return {"error": str(e)}


def writeToFile(fileName, pos, text, appMode):
    if bool(fileName) and bool(text):
        if appMode:
            try:
                print("APPEND MODE")
                if os.path.exists(fileName):
                    file_object = open(fileName, 'a')
                    file_object.write(text)
                    file_object.close()
                    return {"data": fileName + " modified"}
                else:
                    return {"data": "File Specified does not exist"}
            except Exception as e:
                return {"error": str(e)}
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
                        return {"data": fileName + " modified"}
                else:
                    return {"data": "File Specified does not exist"}
            except Exception as e:
                return {"error": str(e)}
    else:
        {"error": "Please Fill All the Fields"}


def readFromFile(fileName, pos, size):
    try:
        x = int(pos)+int(size)
        f = open(fileName, "r")
        data = f.read()
        f.close()
        return {"content": data[int(pos):int(x)]}
    except Exception as e:
        return {"error": str(e)}


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
        return {"data": fileName + " Content Modified"}
    except Exception as e:
        return {"error": str(e)}


def moveFile(fileName, newDir):
    try:
        cwd = os.getcwd()
        oldPath = os.path.join(cwd, fileName)
        newPath = os.path.join(cwd, newDir, fileName)
        os.rename(oldPath, newPath)
        node = tree.get_node(oldPath)
        nodeData = node.data
        tree.remove_node(oldPath)
        print(tree.create_node(fileName, newPath,
                               os.path.join(cwd, newDir), nodeData))
        persistMemMap()
        return {"data": " File moved"}
    except Exception as e:
        return {"error": str(e)}


def getDirInfo(filePath):
    stat = os.stat(filePath)
    return {"data": {"isDir": True, "num_of_files_and_dirs": sum([len(files) for r, d, files in os.walk(filePath)]), "size": sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(filePath) for filename in filenames), "file_mode": stat.st_mode, "inode": stat.st_ino, "num_of_hard_links": stat.st_nlink, "user_id": stat.st_uid,
            "group_id": stat.st_gid, "last_access_time": stat.st_atime, "last_modified": stat.st_mtime}}


def recurseDirHandle(dir, root):
    for entryName, contentWithin in dir.items():
        if "children" in contentWithin:
            for child in contentWithin["children"]:
                for name in child:
                    parent = os.path.join(
                        root, entryName) if not root == "" else entryName

                    if child[name]["data"]["isDir"]:
                        child[name] = getDirInfo(os.path.join(
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
    return {"content": memMap}


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
            return {"data": fileName + " Truncated"}
        else:
            return{"error": 'File Specified does not exist'}

    except Exception as e:
        return {"error": str(e)}
