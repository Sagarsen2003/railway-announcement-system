import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=True)
    myobj.save(filename)

# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio=AudioSegment.from_mp3('Railway Announcement Software/railway.mp3')
    #1- Generate "Kripiya dheyan dijiye"
    start=18000
    finish=21200
    audioProcessed= audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    #2- Train No.

    #3- Train Name.

    #4 is from-city

    #5 Generate "ke raste"
    start=131200
    finish=131800
    audioProcessed= audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")

    #6 to city

    #7 Generate "ko janewali"
    start=28800
    finish=29800
    audioProcessed= audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")

    #8 Generate "Apne nirdharet samay"
    start=29900
    finish=31800
    audioProcessed= audio[start:finish]
    audioProcessed.export("8_hindi.mp3",format="mp3")
    
    #9 time

    #10 Generate "platform number"(announcement)
    start=35000
    finish=36000
    audioProcessed= audio[start:finish]
    audioProcessed.export("10_hindi.mp3",format="mp3")

    #11 platform number


    #12 Generate "se jayegi"
    start=97200
    finish=98000
    audioProcessed= audio[start:finish]
    audioProcessed.export("12_hindi.mp3",format="mp3")

        
def generateAnnouncement(filename):
    df =pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        #2-Generate Train No.
        textToSpeech(item['train_no'], '2_hindi.mp3') 
        #3-Generate Train Name.
        textToSpeech(item['train_name'], '3_hindi.mp3')
        #4-Generate from-city
        textToSpeech(item['from'], '4_hindi.mp3')
        #6-Generate to city
        textToSpeech(item['to'], '6_hindi.mp3')
        #9-Generate time
        textToSpeech(item['time'], '9_hindi.mp3')
        #10-Generate platform number
        textToSpeech(item['platform_no'], '11_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,13)]

        announcement = mergeAudios(audios)
        announcement.export(f'anouncement_{item['train_no']}_{index+1}.mp3',format="mp3")
    

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement.....")
    generateAnnouncement("Railway Announcement Software/Announcement_list.xlsx") 



