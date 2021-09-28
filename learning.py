from tkinter import *

# setting up Tkinter window
w = Tk()
w.title("Learning")
w.option_add("*Font", "Montserrat")
w.geometry("300x425")

def learn():
    #CREATE A FRAME
    learn = Frame()

    #CREATE TEXT TO DISPLAY
    title = Label(learn, text="This is some text")
    title.pack(pady=20)

    #CREATE A ENTRY BOX FOR USER TO ENTER TEXT
    entry = Entry(learn, text=0)
    entry.pack(pady=20)

    #CREATING A WAITING BUTTON
    waitVar = IntVar()
    button = Button(learn, text="This is a button", command=lambda: waitVar.set(1))
    button.pack(pady=20)

    learn.pack()

    button.wait_variable(waitVar)

    #THIS CODE WILL RUN AFTER THE BUTTON IS PRESSED
    
    learn.destroy()

    newFrame = Frame()

    #THIS WILL CREATE A SCALE 
    scale = Scale(newFrame, from_=1, to=6, orient=HORIZONTAL, tickinterval=1, length=200)
    scale.pack()

    #THIS WILL SET UP WHAT IS NEEDED FOR A DROP DOWN BOX
    selectOption = StringVar()
    selectOption.set("Pick an option")

    #CREATES THE DROP DOWN BOX
    dropDown = OptionMenu(newFrame, selectOption, "1", "2", ",3", "4")
    dropDown.pack(pady=20)

    #CREATES A BUTTON THAT WILL EXECUTE THE CODE BELLOW IT ONCE PRESSED
    waitVar = IntVar()
    button = Button(newFrame, text="This is a button", command=lambda: waitVar.set(1))
    button.pack(pady=20)

    newFrame.pack()

    button.wait_variable(waitVar)
    
    #GETS AND DISPLAYS THE VALUE FROM THE DROP DOWN BOX
    scaleValue = selectOption.get()
    title = Label(newFrame, text=scaleValue)
    title.pack(pady=20)

    newFrame.pack()



learn()

w.mainloop()
