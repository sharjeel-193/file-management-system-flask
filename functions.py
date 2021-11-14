import os
from PyQt5.QtWidgets import QMessageBox

cwd = os.getcwd()

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
        with open(fileName, 'w') as fp:
            pass
            fp.write("New File Created")
        createInfoBox(fileName+" created")
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)

def deleteFile(fileName):
    try:
        os.remove(fileName)
        createInfoBox(fileName+" deleted")
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)

def createDirectory(dirName):
    try:
        os.mkdir(dirName)
        createInfoBox(dirName+" created")
    except Exception as e:
        createErrorBox(str(e), QMessageBox.Critical)

def deleteDirectory(dirName):
    try:
        os.rmdir(dirName)
        createInfoBox(dirName+" created")
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
                    createErrorBox("File Specified does not exist", QMessageBox.Critical)

            except Exception as e:
                createErrorBox(str(e), QMessageBox.Critical)
        else:
            try:
                if os.path.exists(fileName):
                    with open(fileName,"w") as f:
                        f.seek(int(pos), 0)
                        f.write(text)
                    createInfoBox(fileName+" modified")
                else:
                    createErrorBox("File Specified does not exist", QMessageBox.Critical)
            except Exception as e:
                createErrorBox(str(e), QMessageBox.Critical)
    else:
        createErrorBox("Please Fill All the Fields", QMessageBox.Warning)
    