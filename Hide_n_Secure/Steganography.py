from tkinter import *
from tkinter import messagebox
from argparse import FileType
# from stegano import lsb
from tkinter.filedialog import *
from PIL import ImageTk, Image
# from  stegano.lsbset import generators
from stegano import lsb
from tkinter import font as tkFont
from stegano import exifHeader as aaa
import os
from subprocess import Popen

def main():

    def encode():
        main.destroy()
        enc = Tk()
        enc.attributes("-fullscreen", True)
        enc.wm_attributes('-transparentcolor')
        img = ImageTk.PhotoImage(Image.open("bg2.jpg"))
        fontl = tkFont.Font(family='Algerian', size=32)
        label1 = Label(enc, image=img)
        label1.pack()

        LabelTitle = Label(text="ENCODE", bg="red", fg="white", width=20)
        LabelTitle['font'] = fontl
        LabelTitle.place(relx=0.6, rely=0.1)

        def openfile():
            global fileopen
            global imagee

            fileopen = StringVar()
            fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg,png files", "*jpg *png"), ("all files", "*.*")))
            imagee = ImageTk.PhotoImage(Image.open(fileopen))

            Labelpath = Label(text=fileopen)
            Labelpath.place(relx=0.6, rely=0.25, height=21, width=450)

            Labeling = Label(image=imagee)
            Labeling.place(relx=0.7, rely=0.3, height=200, width=200)

        Button2 = Button(text="Openfile", command=openfile)
        Button2.place(relx=0.7, rely=0.2, height=31, width=94)

        secimg = StringVar()
        radio1 = Radiobutton(text='jpeg', value='jpeg', variable=secimg)
        radio1.place(relx=0.7, rely=0.57)

        radio2 = Radiobutton(text='png', value='png', variable=secimg)
        radio2.place(relx=0.8, rely=0.57)

        Label1 = Label(text="Enter message")
        Label1.place(relx=0.6, rely=0.6, height=21, width=104)
        entrysecmes = Entry()
        entrysecmes.place(relx=0.7, rely=0.6, relheight=0.05, relwidth=0.200)

        Label2 = Label(text="File Name")
        Label2.place(relx=0.6, rely=0.70, height=21, width=104)

        entrysave = Entry()
        entrysave.place(relx=0.7, rely=0.70, relheight=0.05, relwidth=0.200)

        def encode():
            if secimg.get() == "jpeg":
                inimage = fileopen
                response = messagebox.askyesno("popup", "do you want to encode")
                if response == 1:
                    aaa.hide(inimage, entrysave.get() + '.jpg', entrysecmes.get())
                    messagebox.showinfo("popup", "successfully encode" + entrysave.get() + ".jpeg")
                else:
                    messagebox.showwarning("popup", "unsuccessful")

            if secimg.get() == "png":
                inimage = fileopen
                response = messagebox.askyesno("popup", "do you want to encode")
                if response == 1:
                    lsb.hide(inimage, message=entrysecmes.get()).save(entrysave.get() + '.png')
                    messagebox.showinfo("popup", "successfully encode to " + entrysave.get() + ".png")
                else:
                    messagebox.showwarning("popup", "unsuccessful")

        def back():
            enc.destroy()
            # execfile('image steganography using lsb.py')
            # os.system('python imagesteganographyusinglsb.py')
            Popen('python steganography.py')

        Button2 = Button(text="ENCODE", command=encode)
        Button2.place(relx=0.7, rely=0.8, height=31, width=94)

        Buttonback = Button(text="Back", command=back)
        Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)

        enc.mainloop()


    def decode():
        main.destroy()
        dec = Tk()
        dec.attributes("-fullscreen", True)
        dec.wm_attributes('-transparentcolor')
        img = ImageTk.PhotoImage(Image.open("bg2.jpg"))
        fontl = tkFont.Font(family='Algerian', size=32)
        label1 = Label(dec, image=img)
        label1.pack()

        LabelTitle = Label(text="DECODE", bg="blue", fg="white", width=20)
        LabelTitle['font'] = fontl
        LabelTitle.place(relx=0.6, rely=0.1)

        secimg = StringVar()
        radio1 = Radiobutton(text='jpeg', value='jpeg', variable=secimg)
        radio1.place(relx=0.7, rely=0.57)

        radio2 = Radiobutton(text='png', value='png', variable=secimg)
        radio2.place(relx=0.8, rely=0.57)

        def openfile():
            global fileopen
            global imagee
            fileopen = StringVar()
            fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files, png file", "*jpg *png"), ("all files", "*.*")))

            imagee = ImageTk.PhotoImage(Image.open(fileopen))
            Labelpath = Label(text=fileopen)
            Labelpath.place(relx=0.6, rely=0.25, height=21, width=450)

            Labelimg = Label(image=imagee)
            Labelimg.place(relx=0.7, rely=0.3, height=200, width=200)

        def deimg():
            if secimg.get() == "png":
                messag = lsb.reveal(fileopen)

            if secimg.get() == "jpeg":
                messag = aaa.reveal(fileopen)

            Label2 = Label(text=messag)
            Label2.place(relx=0.7, rely=0.7, height=21, width=204)

        Button2 = Button(text="Openfile", command=openfile)
        Button2.place(relx=0.7, rely=0.2, height=31, width=94)

        Button2 = Button(text="DECODE", command=deimg)
        Button2.place(relx=0.7, rely=0.8, height=31, width=94)

        def back():
            dec.destroy()
        # execfile('image steganography using lsb.py')
        # os.system('python imagesteganographyusinglsb.py')
            Popen('python steganography.py')

        Buttonback = Button(text="Back", command=back)
        Buttonback.place(relx=0.7, rely=0.85, height=31, width=94)

        dec.mainloop()


# main program
    main = Tk()
    main.title('Enc & Dec Panel ')
# main.geometry("1300x750")
    main.attributes("-fullscreen", True)
    fontl = tkFont.Font(family='Algerian', size=32)

    global image1
    image1 = ImageTk.PhotoImage(Image.open("bg1.jpg"))
    label = Label(main, text="lalal", image=image1)
    label.pack()

    encbutton = Button(text='Encode', fg="white", bg="black", width=20, command=encode)
    encbutton['font'] = fontl
    encbutton.place(relx=0.6, rely=0.3)

    decbutton = Button(text='Decode', fg="white", bg="black", width=20, command=decode)
    decbutton['font'] = fontl
    decbutton.place(relx=0.6, rely=0.5)

    closebutton = Button(text='EXIT', fg="white", bg="red", width=20, command=exit)
    closebutton['font'] = fontl
    closebutton.place(relx=0.6, rely=0.7)
    main.mainloop()


def exit():
    main.destroy()
