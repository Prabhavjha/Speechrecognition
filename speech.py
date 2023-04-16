import tkinter as tk
from tkinter import filedialog

import speech_recognition as sr

# Create a Tkinter window
window = tk.Tk()
window.withdraw() # Hide the main window

# Initialize a recognizer
r = sr.Recognizer()
check = 1

while(check):
    opinion = input("You want to speak or you have an audio file ? (write speak or audio respectively in lower case) \n")

    if (opinion == 'audio'):
        # Open a dialog box to select an audio file
        file_path = filedialog.askopenfilename(title="Select an Audio File",filetypes=[("Audio files", "*.mp3;*.wav;*.ogg"),("All files", "*.*")])

        # Check if a file was selected
        if file_path:
        
            # Load the audio file
            with sr.AudioFile(file_path) as source:
                # Record audio from the source
                audio = r.record(source)

            # Use Google's Speech Recognition API to convert speech to text
            try:
                text = r.recognize_google(audio)
                check = 0
            except sr.UnknownValueError:
                print("Unable to recognize speech")
                check = 1
            except sr.RequestError as e:
                print("Request error:", e)
                check = 1
        else:
            print("No file selected.")

    elif (opinion == 'speak'):
        # Initialize recognizer
        #r = sr.Recognizer()

        # Record audio from microphone
        with sr.Microphone() as source:
            print("Speak something...")
            audio = r.listen(source)

        # Recognize speech using Google Speech Recognition
        try:
            text = r.recognize_google(audio)
            check = 0
        except sr.UnknownValueError:
            print("Could not understand audio")
            check = 1
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            check = 1
    
    else:
        print("please select the correct option")

if text:
    
    # Open a dialog box to select a text file
    Text_file = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    # Check if a file was selected
    if Text_file:
        with open(Text_file, 'w') as file:
            file.write(text)

        with open(Text_file, 'r') as f:
            for line in f:
                print(line,end='')

    else:
        print("No file selected.")
        filename = input("Enter the filename: ")
        # check if the filename already has .txt extension, if not add it
        if not filename.endswith('.txt'):
            filename += '.txt'

        with open(filename, 'w') as file:
            file.write(text)

        with open(filename,'r') as f:
            for line in f:
                print(line,end='')
else:
    print("Try Again")