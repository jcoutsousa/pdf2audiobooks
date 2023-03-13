import pyttsx3
import PyPDF2
import numpy


def tts(speaker):
    """ RATE"""
    rate = speaker.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    speaker.setProperty('rate', 160)  # setting up new voice rate
    return speaker


def visitor_body(text, cm, tm, fontDict, fontSize):
    parts = []
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)
        #print(parts)
    text_body = "".join(parts)
    #print(text_body)
    return text_body


def pdf2text2audio(pages):
    text = []
    for num in range(0, pages):
        page = pdfReader.pages[num]
        text_1 = page.extract_text(visitor_text=visitor_body)
        text.append(text_1)

    return text


if __name__ == '__main__':
    book = open('sw-transcripts.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    text = pdf2text2audio(1)
    print(text)
    numpy.savetxt('Extract_text.txt', text, fmt= '%s')
    file = open("/Users/jcsousa/PycharmProjects/pdf2audiobooks/Extract_text.txt", "r")

    read_content = file.read().split("\n")

    print(read_content)

    speaker = pyttsx3.init()
    speaker = tts(speaker)

    speaker.say(str(read_content))

    speaker.runAndWait()


