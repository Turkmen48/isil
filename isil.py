import time
import os,random
import playsound
from gtts import gTTS
import webbrowser
import speech_recognition as sr
#import snowboydecoder

#----------------------------------------------Sözler Başlangıç---------------------------------------------------------------------------
efkar_sozleri = ["efkar", "aga yak yak", "aga yak", "moralim bozuk", "ışıl moralim bozuk","ışıl damardan bir şeyler çal","efkarlıyım","ışıl bir küçük açalım","bir küçük açalım"]
merhaba_sozleri=["merhaba","selamun aleykum","hey","selam"]
hal_hatır_sozleri=["naber","nasılsın","hayat nasıl","hayat nasıl gidiyor","iyi misin","naber lan","napıyon","ışıl nasılsın"]
hal_hatır_sozleri_plus=["ben de iyiyim","sağol","iyiyim"]
soru_sozleri=["sana bir şey soracağım","sana bir şey sorabilir miyim","sana sormam gereken bir şey var"]
program_indir_sozleri=["program indir","ışıl program indir","ışıl program indirmek istiyorum","program indirmek istiyorum","oyun indirmek istiyorum","oyun indir","ışıl oyun indir","ışıl oyun indirmek istiyorum","film indir","film indirmek istiyorum","ışıl film indir","ışıl film indirmek istiyorum"]
#-----------------------------------------------Sözler Bitiş--------------------------------------------------------------------------
#-----------------------------------------------Cevaplar Başlangıç------------------------------------------------------------------------------
merhaba_cevap_sozleri=["merhaba","aleykum selam","hey","selam"]
hal_hatır_cevap_sozleri=["iyim","iyii","ben her zaman iyiyim","iyiyim seni sormalı"]
hal_hatır_cevap_sozleri_plus=["Allah iyilik versin","İyi olmana sevindim"]
soru_cevap_sozleri=["tabii ki sorabilirsin şimdi sormak istediğin kelimeyi söyle"]
#-----------------------------------------------Cevaplar Bitiş-------------------------------------------------------------------------
def detected_callback():
    print("hotword detected")
def oku():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("konuşabilirsin")
        audio = r.listen(source)
        try:
            global oku_deger
            oku_deger=str(r.recognize_google(audio, lang='tr-tr'))
            print("söylediklerin:{}".format(oku_deger))

        except sr.UnknownValueError:
            konus("Anlayamadım canım?")
        except sr.RequestError as e:
            print("Hata oluştu bu uygulama internet bağlantısı gerektirir; {0}".format(e))


def konus(soz):
    tts = gTTS(text=soz,lang='tr')
    randoms = random.randint(0, 9999999999)
    tts.save(str(randoms)+".mp3")
    playsound.playsound(str(randoms)+".mp3")
    os.remove(str(randoms)+".mp3")
def efkar():
    new = 2  # yeni sekmede aç
    url = "file:///C:/Users/Turkmen/Desktop/isil/spotify.html"
    webbrowser.open(url, new=new)
def program_indir():
    konus("Lütfen indirmek istediğin programın, filimin veya oyunun adını söyle")
    soyle=input("url soyle")
    new=2
    url="https://www.fullprogramlarindir.com/?s="+str(soyle)
    webbrowser.open(url,new=new)
while True:
    try:
        #detector = snowboydecoder.HotwordDetector("ışıl.pmdl", sensitivity=0.5, audio_gain=1)
        #detector.start(detected_callback)
        oku()
        soyle = oku_deger
        if (str(soyle) in efkar_sozleri):
            konus("seni bu hale getirenler utansın reyiz tam sana göre bir çalma listem var.")
            efkar()
        elif (str(soyle) in merhaba_sozleri):
            konus(random.choice(merhaba_cevap_sozleri))
        elif (str(soyle) in hal_hatır_sozleri):
            konus(random.choice(hal_hatır_cevap_sozleri))
        elif (str(soyle) in hal_hatır_sozleri_plus):
            konus(random.choice(hal_hatır_cevap_sozleri_plus))
        elif (str(soyle) in program_indir_sozleri):
            program_indir()
        else:
            konus("Söylediğin şeyi nasıl yapacağımı veya nasıl cevap vereceğimi henüz bilmiyorum")
    except NameError:
        konus("Canım konuşmayacaksan ben gidiyorum")
        break




