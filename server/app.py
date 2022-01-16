from pickle import FALSE
from unittest import result
from flask import Flask, jsonify, request
from functions import *
app = Flask(__name__)

lockedFiles = []


def isFileLocked(fileName):
    found = False
    for lockedFile in lockedFiles:
        if lockedFile == fileName:
            found = True
            break
    return found


@app.post("/add_file")
def add_file():
    fileName = request.args.get('fileName', '')
    return jsonify(createFile(fileName))


@app.delete("/del_file")
def del_file():
    fileName = request.args.get('fileName', '')
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    lockedFiles.append(fileName)
    result = jsonify(deleteFile(fileName))
    lockedFiles.remove(fileName)
    return result


@app.post("/add_dir")
def add_dir():
    dirName = request.args.get('dirName', '')
    return jsonify(createDirectory(dirName))


@app.delete("/del_dir")
def del_dir():
    dirName = request.args.get('dirName', '')
    if isFileLocked(dirName):
        return jsonify({"error": "Directory already in use"})
    lockedFiles.append(dirName)
    result = jsonify(deleteFile(dirName))
    lockedFiles.remove(dirName)
    return result


@app.get("/open_file")
def open_file():
    fileName = request.args.get('fileName', '')
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    lockedFiles.append(fileName)
    result = jsonify(deleteFile(fileName))
    lockedFiles.remove(fileName)
    return result


@app.patch("/move_file_content")
def move_file_content():
    fileName = request.args.get('fileName', '')
    start = request.args.get("start", "")
    size = request.args.get("size", "")
    target = request.args.get("target", "")
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    lockedFiles.append(fileName)
    result = jsonify(moveContentWithinFile(fileName, start, size, target))
    lockedFiles.remove(fileName)
    return result


@app.get("/read_file")
def read_file():
    fileName = request.args.get('fileName', '')
    pos = request.args.get("pos", "")
    size = request.args.get("size", "")
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    lockedFiles.append(fileName)
    result = jsonify(readFromFile(fileName, pos, size))
    lockedFiles.remove(fileName)
    return result


@app.patch("/write_file")
def write_file():
    fileName = request.args.get('fileName', '')
    pos = request.args.get("pos", "")
    text = request.args.get("text", "")
    appMode = request.args.get("appMode", "")
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    lockedFiles.append(fileName)
    result = jsonify(writeToFile(fileName, pos, text, appMode))
    lockedFiles.remove(fileName)
    return result


@app.patch("/move_file")
def move_file():
    fileName = request.args.get('fileName', '')
    newDir = request.args.get('newDir', '')
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
    lockedFiles.append(fileName)
    result = jsonify(moveFile(fileName, newDir))
    lockedFiles.remove(fileName)
    return result


@app.patch("/truncate_file")
def truncate_file():
    fileName = request.args.get('fileName', '')
    size = request.args.get("size", "")
    if isFileLocked(fileName):
        return jsonify({"error": "File already in use"})
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
