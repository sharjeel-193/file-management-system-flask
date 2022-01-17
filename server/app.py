from flask import Flask, jsonify, request
from functions import *
app = Flask(__name__)

# locked file name in format -> "username-filename"
lockedFiles = []


def isFileLocked(fileName):
    for lockedFile in lockedFiles:
        lFileName = lockedFile.split("-")[1]
        if lFileName == fileName:
            return True
    return False


def isUserAccess3File(username):
    fileAccessCount = 0
    for lockedFile in lockedFiles:
        fileUsername = lockedFile.split("-")[0]
        if fileUsername == username:
            fileAccessCount += 1
            if fileAccessCount >= 3:
                return True
    return False


@app.post("/add_file")
def add_file():
    fileName = request.args.get('fileName', '')
    return jsonify(createFile(fileName))


@app.delete("/del_file")
def del_file():
    fileName = request.args.get('fileName', '')
    userName = request.args.get('userName', '')
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    if isUserAccess3File(userName):
        return jsonify({"error": "You already have access to 3 files"})
    lFileName = f"${userName}-${fileName}"
    lockedFiles.append(lFileName)
    result = jsonify(deleteFile(fileName))
    lockedFiles.remove(lFileName)
    return result


@app.post("/add_dir")
def add_dir():
    dirName = request.args.get('dirName', '')
    return jsonify(createDirectory(dirName))


@app.delete("/del_dir")
def del_dir():
    dirName = request.args.get('dirName', '')
    userName = request.args.get('userName', '')
    if isFileLocked(dirName):
        return jsonify({"error": "Directory already in use"})
    if isUserAccess3File(userName):
        return jsonify({"error": "You already have access to 3 files"})
    lFileName = f"${userName}-${dirName}"
    lockedFiles.append(lFileName)
    result = jsonify(deleteFile(dirName))
    lockedFiles.remove(lFileName)
    return result


@app.get("/open_file")
def open_file():
    fileName = request.args.get('fileName', '')
    userName = request.args.get('userName', '')
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    if isUserAccess3File(userName):
        return jsonify({"error": "You already have access to 3 files"})
    lFileName = f"${userName}-${fileName}"
    lockedFiles.append(lFileName)
    result = jsonify(deleteFile(fileName))
    lockedFiles.remove(lFileName)
    return result


@app.patch("/move_file_content")
def move_file_content():
    fileName = request.args.get('fileName', '')
    userName = request.args.get('userName', '')
    start = request.args.get("start", "")
    size = request.args.get("size", "")
    target = request.args.get("target", "")
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    if isUserAccess3File(userName):
        return jsonify({"error": "You already have access to 3 files"})
    lFileName = f"${userName}-${fileName}"
    lockedFiles.append(lFileName)
    result = jsonify(moveContentWithinFile(fileName, start, size, target))
    lockedFiles.remove(lFileName)
    return result


@app.get("/read_file")
def read_file():
    fileName = request.args.get('fileName', '')
    userName = request.args.get('userName', '')
    pos = request.args.get("pos", "")
    size = request.args.get("size", "")
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    if isUserAccess3File(userName):
        return jsonify({"error": "You already have access to 3 files"})
    lFileName = f"${userName}-${fileName}"
    lockedFiles.append(lFileName)
    result = jsonify(readFromFile(fileName, pos, size))
    lockedFiles.remove(lFileName)
    return result


@app.patch("/write_file")
def write_file():
    fileName = request.args.get('fileName', '')
    userName = request.args.get('userName', '')
    pos = request.args.get("pos", "")
    text = request.args.get("text", "")
    appMode = request.args.get("appMode", "")
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    if isUserAccess3File(userName):
        return jsonify({"error": "You already have access to 3 files"})
    lFileName = f"${userName}-${fileName}"
    lockedFiles.append(lFileName)
    result = jsonify(writeToFile(fileName, pos, text, appMode))
    lockedFiles.remove(lFileName)
    return result


@app.patch("/move_file")
def move_file():
    fileName = request.args.get('fileName', '')
    userName = request.args.get('userName', '')
    newDir = request.args.get('newDir', '')
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    if isUserAccess3File(userName):
        return jsonify({"error": "You already have access to 3 files"})
    lFileName = f"${userName}-${fileName}"
    lockedFiles.append(lFileName)
    result = jsonify(moveFile(fileName, newDir))
    lockedFiles.remove(lFileName)
    return result


@app.patch("/truncate_file")
def truncate_file():
    fileName = request.args.get('fileName', '')
    userName = request.args.get('userName', '')
    size = request.args.get("size", "")
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    if isUserAccess3File(userName):
        return jsonify({"error": "You already have access to 3 files"})
    return jsonify(truncateFile(fileName, size))


@app.get("/show_mem_map")
def show_mem_map():
    return jsonify(showMemMap())


@app.get("/cwd")
def cwd():
    return jsonify({"content": os.getcwd()})


@app.patch("/change_cwd")
def change_cwd():
    newPath = request.args.get("newPath", "")
    return jsonify(changeWD(newPath))


if __name__ == "__main__":
    makeMemMap()
    app.run(port=95)
