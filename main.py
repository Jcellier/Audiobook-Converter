import pyttsx3
import PyPDF2

want_to_read = ""

book = open("demo.pdf", "rb")               #  Open the pdf file you want to read
pdf_reader = PyPDF2.PdfFileReader(book)     # initialize the pdf_reader
num_pages = pdf_reader.numPages             # Count the number of pages for later use

play = pyttsx3.init()                       # Initialize the text to speech module as "play"
print("Playing Audio Book")

voices = play.getProperty("voices")         # Creates a variable containing the voice property
play.setProperty("voice", voices[1].id)     # Change the voice property to a female voice

rate = play.getProperty("rate")             # Creates a variable containing the rate property
play.setProperty("rate", 150)               # Changed the rate to "150" (default=200) to slow down the speech a bit


for num in range(5, num_pages):         # Create a for loop to read all the pages in the pdf file. range should be = range(0, num_pages)
    page = pdf_reader.getPage(num)      # Gets the page of the pdf for each iteration

    data = page.extractText()           # Creates a variable in which the text will be converted to text

    play.say(data)                      # Play the audio from the data extracted

    play.runAndWait()
