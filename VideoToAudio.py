from youtube_dl import YoutubeDL
import speech_recognition as sr
from flask import Flask, render_template,request
app = Flask(__name__)

audio_downloader = YoutubeDL({'format':'bestaudio',
                              'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'wav',
                                'preferredquality': '192',
                              }]})
@app.route("/")
def form():
    return render_template('index.html')

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        txt = request.form.get('vid')
        URL=txt
        print("extracting...")

        audio_downloader.extract_info(URL)

        print("converting to summarized text.....")

        sound = "But what is a Neural Network _ Deep learning, chapter 1-aircAruvnKk.wav"
        r = sr.Recognizer()
        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            print(r.recognize_google(audio))

    return render_template("index.html")


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response



if __name__ == "__main__":
    app.run(debug=True)



