from gtts import gTTS

text = "Hello Dhruv, how are you?"
response = gTTS(text=text, lang='en', slow=False)
response.save("./demo.mp3")