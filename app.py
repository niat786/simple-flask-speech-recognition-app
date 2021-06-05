from flask import Flask, render_template, request, redirect
import speech_recognition


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():


    transcript = ''

    if request.method == 'POST':

        if 'file' not in request.files:
            return redirect(request.url)


        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file:

            recognizer = speech_recognition.Recognizer()
            audioFile = speech_recognition.AudioFile(file)


            with audioFile as source:
                
                data = recognizer.record(source)
                text = recognizer.recognize_google(data, key=None)
                transcript = text

    return render_template('index.html', transcript = transcript)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)


