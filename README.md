# Strans
Any* to any to language voice translator built in python powered by google translator and google text-to-speech API.

3 core libraries are used.
1) Speech_recognition
2) googletrans
3) gTTS

Speech_recognition is for capturing voice of user by using inbuilt or external microphone of computer. This program has been tested on Windows 10 and there is no problem in using this library but,  it may have little change in code when executing in linux environment. 

googletrans is self-explainatory that it is used for detecting the user's spoken language and then convert it text and then translate it into desired language. gTTS is used for coverting into audio from translated text.

You can also create voice instructions likewise I have created .mp3 files using voice_creator.py.

IMPORTANT NOTE: To get this program working, after installing gTTS library for python replace FILE: Lib/site-packages/gtts_token/gtts_token.py with gtts_token.py given in this repo. This thing should be done because there is a problem in tokenizer of gTTS library and it is not fixed by developer yet. So, this is an un-official fix for that. ;)

*NOTE: Languages which are supported by google translator can only be detected and translated by this program.
