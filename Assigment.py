from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("600x250")
window.title("Efik Dictionary")

label = Label( text="Hello World", font=("Forte", 20))
label.pack(padx=20, pady=20)

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

Efik_dict = {
    'good morning':'emesire',
    'please':'daiya',
    'sorry':'kpe',
    'dog' : 'ewa',
    'thankyou':'sosono',
    'goat': 'ebot',
    'bread': 'uyo',
    'God':'Abasi',
    'bye':'kaadi',
    'sleep':'daiya',
    'five':'ition',
    'witch':'ifot',
    'water':'mmoon',
    'seven':'itiaba',
    'love': 'ima',
    'joy':'idara',
    'grace':'mfon',
    'lion':'ekpe',
    'door':'usun',
    'war':'ekon',
}


def search():
    word = entry_text.get()
    print(word)
    if word in Efik_dict:
        result.set(Efik_dict[word])
        print(Efik_dict[word])
    else:
        result.set("Not found")
        print("Not found")

search_btn = Button(window, text="Search", command=search)
search_btn.pack()

window.mainloop()
