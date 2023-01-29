
from gtts import gTTS
import os


def text_to_speech(text):
    audio_bot_file = "static/audios/bot/bot_audio.mp3"

    with open(text, 'r') as f:
        mytext = f.read()
        f.close()
    myobj = gTTS(text=mytext, lang='en-in', slow=False)
    myobj.save(audio_bot_file)
    os.system("mpg123 "+audio_bot_file)

text_file_path = "static/texts/audio.txt"
text_to_speech(text_file_path)