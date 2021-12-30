from flask import Flask, jsonify, request
from functions import *
app = Flask(__name__)


@app.post("/add_file")
def add_file():
    fileName = request.args.get('fileName', '')
    return jsonify(createFile(fileName))


@app.delete("/del_file")
def del_file():
    fileName = request.args.get('fileName', '')
    print(fileName)
    return jsonify(deleteFile(fileName))


@app.post("/add_dir")
def add_dir():
    dirName = request.args.get('dirName', '')
    return jsonify(createDirectory(dirName))


@app.delete("/del_dir")
def del_dir():
    dirName = request.args.get('dirName', '')
    return jsonify(deleteDirectory(dirName))


@app.get("/open_file")
def open_file():
    fileName = request.args.get('fileName', '')
    return jsonify(openFile(fileName))


@app.patch("/move_file_content")
def move_file_content():
    fileName = request.args.get('fileName', '')
    start = request.args.get("start", "")
    size = request.args.get("size", "")
    target = request.args.get("target", "")
    return jsonify(moveContentWithinFile(fileName, start, size, target))


@app.get("/read_file")
def read_file():
    fileName = request.args.get('fileName', '')
    pos = request.args.get("pos", "")
    size = request.args.get("size", "")
    return jsonify(readFromFile(fileName, pos, size))


@app.patch("/write_file")
def write_file():
    fileName = request.args.get('fileName', '')
    pos = request.args.get("pos", "")
    text = request.args.get("text", "")
    appMode = request.args.get("appMode", "")
    return jsonify(writeToFile(fileName, pos, text, appMode))


@app.patch("/move_file")
def move_file():
    fileName = request.args.get('fileName', '')
    newDir = request.args.get('newDir', '')
    print(fileName, newDir)
    return jsonify(moveFile(fileName, newDir))


@app.patch("/truncate_file")
def truncate_file():
    fileName = request.args.get('fileName', '')
    size = request.args.get("size", "")
    return jsonify(truncateFile(fileName, size))


@app.get("/show_mem_map")
def show_mem_map():
    print(showMemMap())
    return jsonify(showMemMap())


if __name__ == "__main__":
    makeMemMap()
    app.run(port=95)
