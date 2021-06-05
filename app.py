from flask import Flask, render_template, request, redirect
import speech_recognition

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ''
    if request.method == 'POST':
        #if file is not available then redirect
        if 'file' not in request.files:
            return redirect(request.url)

        #get audio file
        file = request.files['file']

        #file name should not be empty
        if file.filename == '':
            return redirect(request.url)

        if file:
            #extract text
            recognizer = speech_recognition.Recognizer()
            audioFile = speech_recognition.AudioFile(file)

            with audioFile as source:
                data = recognizer.record(source)
                text = recognizer.recognize_google(data, key=None)
                transcript = text

    return render_template('index.html', transcript = transcript)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)


