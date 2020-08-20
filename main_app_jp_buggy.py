

# this is a app ,with it you can have words from big string by just pasting


from tkinter import *

from app_jp_buggy import main, Ai_name


# defining a command for a button

# in it we run main()
def start_buggy():
    main(Ai_name)


# declare the window
window = Tk()
# set window title
window.title("Buggy App")
# set window width and height
window.configure(width=400, height=335)
# set window background color
window.configure(bg='gray')

# labal
# inside a pack must be:: -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady,  -side
# side must be top, bottom, left, right

Label1 = Label(window, text="バギーの所へようこそ！",
               fg="black", bg="gray", font="times 20 bold italic underline")
Label1.pack(side="top", padx=30)


# button

# ancor  must be:: n, ne, e, se, s, sw, w, nw, center

button2 = Button(window, text="Start-Buggy", width=11,
                 command=start_buggy, bg="pink")
button2.pack(side="top", padx=50, pady=100, expand=-1)

window.mainloop()
