from flask import Flask, render_template, request
import os
import uuid
import baidu

app = Flask(
    __name__,
    static_folder='images',
)


@app.route('/')
def main():
    return render_template('index.html')

# 读取文件


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


@app.route('/getaudio', methods=['POST'])
def getaudio():
    audiofile = request.files.get("audioData")
    if audiofile:
        filepath = "audio/%s.pcm" % uuid.uuid4()
        audiofile.save(filepath)
    r = baidu.client.asr(get_file_content(filepath), 'pcm')
    return r


if __name__ == '__main__':
    app.run(debug=True)
