from tkinter import *         # tinker is used for GUI
from tkinter import ttk       # for styling 
from googletrans import Translator, LANGUAGES
from PIL import Image, ImageTk
from gtts import gTTS
import os
# from langcodes import Language
# from pydub import AudioSegment


# main directory
root = Tk()
root.geometry("1100x1100")
root.resizable(200,200)
root["bg"] = "skyblue"
root.title("Language Translator")

# title
Label(root , text="LanguageTranslator" , font="Arial 20 bold").pack()

# input text area
Label(root , text="Enter text" , font="Arial 13 bold", bg="white smoke").place(x=165,y=90)
input_text = Entry(root,width=50)
input_text.place(x=60,y=130)
input_text.get()

# output text area
Label(root , text="Output" , font="Arial 13 bold", bg="white smoke").place(x=780,y=90)
output_text = Text(root,height=5 , width=50, font="Arial 13 ", wrap=WORD, padx=5, pady=5)
output_text.place(x=600,y=130)

# language choice dropdown (107 langs)
language = ['afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu']
dest_lang = ttk.Combobox(root,values=language,width=22)
dest_lang.set("marathi")
dest_lang.place(x=150,y=200)

# function that translates 
def Trans():
    trans = Translator()
    translated = trans.translate(text=input_text.get() , dest=dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)
    return translated.text


# translate button
trans_btn = Button(root, text="Translate", font="arial 12 bold", pady=5, command=Trans, bg="orange", activebackground="green")
trans_btn.place(x=445, y=123)

# audio 
def voice():
    lang_codes = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
    text1 = Trans()
    speech = gTTS(text=text1, lang=lang_codes[dest_lang.get()], slow=False)
    speech.save("out.mp3")
    os.system("start out.mp3")
image_path = "C:\PCL\Aditi College\SE\PBL\Audio.jpg"  
img = Image.open(image_path)
img = img.resize((50,50))
img = ImageTk.PhotoImage(img)
img_btn = Button(root, image=img, pady=5, command=voice, bg="orange", activebackground="green")
img_btn.place(x=600, y=250)

root.lift()

while(True):
    root.mainloop()