import tkinter as tk #tkinter is a GUI library. GUI is a graphical user interface
from tkinter import ttk # ttk is a theme for tkinter and it is used to make the GUI look better
import requests # requests library makes web requests easy and it is used to make GET and POST requests to web servers and get the response back

# functions need to be defined before they are called.
# Same way you need to teach dog to sit before you can ask it to sit
def get_clean_text(text):
    url = 'https://www.purgomalum.com/service/plain'
    params = {'text': text}
    response = requests.get(url, params=params)
    return response.text


def clean_text(): # function which is called when the button is clicked
    text = entry.get() # get the text from the entry (look below)
    label2['text'] = get_clean_text(text) # set the text of label2 to the return value of get_clean_text function. It was originally empty


root = tk.Tk() # create a window
root.title("Text cleaner") # set the title of the window
root.geometry("450x300") # set the size of the window
root.resizable(True, True) # make the window resizable

# change the icon in title bar to swearingIcon.ico
root.iconbitmap("swearingIcon.ico")

label = ttk.Label(root, text="Enter some dirty text:") # create a label and add it to the window
# label is a text or an image that is displayed on the window
label.grid(row=0, column=0, padx=10, pady=10) # set the position of the label in the window and add some padding
# padding is space between the widget and the window border
entry = ttk.Entry(root) # create an entry and add it to the window
entry.grid(row=0, column=1, padx=10, pady=10)

button = ttk.Button(root, text="Clean text for me!", command=clean_text) # create a button and add it to the window
button.grid(row=1, column=0, padx=10, pady=10)
label2 = ttk.Label(root, text="") # create a label and add it to the window
# the label is empty at the beginning but it will be filled with the response from the purgomalum service
label2.grid(row=1, column=1, padx=10, pady=10)

# add image to the window (image is in the same folder as the program)
image = tk.PhotoImage(file="swearingIcon.png")
label3 = ttk.Label(root, image=image)
label3.grid(row=2, column=0, columnspan=2, padx=10, pady=10)



root.mainloop()








