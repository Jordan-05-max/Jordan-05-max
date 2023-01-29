import pyttsx3
import PyPDF2
from PyPDF2 import PdfReader
link = "C:/Users/jorda/Downloads/LPU YEAR 3_2/INT347-Software Bot/AA_Getting_Started_With_AARIDesktop_StepList.pdf"
f = open(link, "rb")
pdf = PyPDF2.PdfReader(f)
pages = len(pdf.pages)
print(pages)
print("type: ",type(pages))

speaker = pyttsx3.init()
for i in range(1, pages+1):
    page= pdf.pages[i-1]
    text=page.extract_text()
    speaker.say(text)
    speaker.runAndWait()