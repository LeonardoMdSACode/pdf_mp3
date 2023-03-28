import pyttsx3
from PyPDF2 import PdfReader

pdfreader = PdfReader('Pandas.pdf')
speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'ResidentSleeper.mp3')
speaker.runAndWait()

speaker.stop()