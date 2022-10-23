import tkinter
from tkinter import*
from tkinter import messagebox
from timeit import default_timer as timer
import random 

root = tkinter.Tk()
root.geometry("500x500")
root.configure(bg="Green")

window = tkinter.Tk()
window.geometry("500x500")
window.withdraw()

x = 0

def game():
    global x
    if x == 0:
        root.withdraw()
        x = x+1
    window.deiconify()
    def check_result():
        j=error=0
        answer=entry.get("1.0",'end-1c')
        end = timer()
        time_taken=end-start
        #len diff
        if len(words[word])>=len(answer):
            error=len(words[word])-len(answer)
            for i in answer:
                if i == words[word][j]:
                    pass
                else:
                    error+=1
                    j+=1
        elif len(words[word])<=len(answer):
            error=len(answer)-len(words[word])
            for i in words[word]:
                if i == answer[j]:
                    pass
                else:
                    error+=1
                j+=1
        wpm = len(answer)/5
        wpm = wpm-error
        wpm=int(wpm/(time_taken/60))
        wpm=(-1)*wpm
        result="Your score is : "+str(wpm)+" WPM !"
        messagebox.showinfo("Score",result)
                     
                                   
    
    def finish():
        window.destroy()
        root.destroy()
        
    words = ["Hello to the world of python language, Python language was invented in 1989 by Guido van Rossum","Python is a object oriented, procedure oriented language and easy to learn language"]
    word = random.randint(0, (len(words)-1))

    x2 = Label(window, text=words[word], bg="black", fg="white", height=7, width=47, font="times 15", wraplength=500) #
    x2.place(x=15, y=10)

    x3= Button(window, text="Submit", font="times 20", bg="#fc2828", command=check_result)
    x3.place(x=220, y=350)

    entry = Text(window)
    entry.place(x=100, y=180, height=150, width=350)

    b2 = Button(window, text="Done", font="times 13", bg='#ffc003', width=12, command=finish)
    b2.place(x=155, y=420)

    b3 = Button(window, text="Retry!", font="times 13", bg='#ffc003', width=12, command=game)
    b3.place(x=265, y=420)

    start = timer()

    window.mainloop()
    
    
x1 = Label(root, text="Let's test your typing speed", bg="orange", fg="white", font="times 20")
x1.place(x=100, y=50)
    
b1 = Button(root, text="Go!", width=12, bg='#fcba03', font="times 20", command=game)
b1.place(x=150, y=120)
        
root.mainloop()
