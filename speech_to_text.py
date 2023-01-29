import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
    # with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
        r.adjust_for_ambient_noise(source)
        print("Please say your query...")
        audio = r.listen(source = source, timeout=3,phrase_time_limit=10)
        try:
            print("Recognizing Now .... ")
            text  = r.recognize_google(audio_data = audio,language='en', with_confidence= True, show_all=False)
            # print(text)
            # print("Audio Recorded Successfully \n ")

            # write audio
            with open("static/audios/audio.wav", "wb") as f:
                f.write(audio.get_wav_data())

            #Write text
            with open("static/texts/audio.txt", "w") as f:
                f.write(text[0])
                f.close()

        except Exception as e:
            print("Error :  " + str(e))



if __name__ == "__main__":
    speech_to_text()