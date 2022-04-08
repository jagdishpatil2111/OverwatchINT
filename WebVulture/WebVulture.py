from tkinter import *
import ttk
import socket
from datetime import datetime
import subprocess
from tkinter import messagebox


class Scanning_port:

    def __init__(self, master):
        master.title('Infosecplatform Presents nikto with python PFv1.0')
        master.resizable(False, False)
        master.configure(background="#e1d8b9")

        self.style = ttk.Style()
        self.style.configure('TFrame', background="#e1d8b9")
        self.style.configure('TButton', background="#e1d8b9")
        self.style.configure('TLabel', background="#e1d8b9")
        self.style.configure('TSeparator', background="#e1d8b9")
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        ## Frame 1 ##
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, text="Nikto with Python Framework v 1.0", style='Header.TLabel').grid(row=0,
                                                                                                           column=1,
                                                                                                           padx=5,
                                                                                                           pady=5,
                                                                                                           sticky='sw')
        ttk.Label(self.frame_header, wraplength=295, text="Nikto Scanning tool (cmd:Nikto -h target)").grid(row=1,
                                                                                                            column=1,
                                                                                                            padx=5,
                                                                                                            sticky='sw')
        ttk.Label(self.frame_header, wraplength=295,
                  text="(Make sure, nikto is already installed on your machine)").grid(row=2, column=1, padx=5, pady=5,
                                                                                       sticky='sw')
        ttk.Separator(self.frame_header, orient=HORIZONTAL).grid(row=3, columnspan=5, sticky="ew", padx=5, pady=10)
        ## END ##
        ## Frame 2 ##

        self.frame_content = ttk.Frame(master)
        self.frame_content.config(height=200, width=400)
        # self.frame_content.config(relief = GROOVE)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text="Enter Target URL Address: ").grid(row=2, column=0, padx=5, pady=10)

        self.entry_name = ttk.Entry(self.frame_content, textvariable="server")
        self.entry_name.setvar(name="server", value="127.0.0.1")
        self.entry_name.grid(row=3, column=0, padx=5)

        ttk.Button(self.frame_content, text="Scan", command=self.dscan).grid(row=3, column=1, padx=5, pady=10,
                                                                             sticky='se')
        ttk.Button(self.frame_content, text="Clear", command=self.Clear).grid(row=3, column=2, padx=5, pady=10,
                                                                              sticky='se')

        ## END ##
        ## Frame 3 ##

        self.frame_report = ttk.Frame(master)
        self.frame_content.config(height=400, width=400)
        self.frame_report.pack()

        self.txt = Text(self.frame_report, width=60, height=15)
        self.txt.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txt.insert(0.0, 'Nikto Scanning Report will appear here...')

    def dscan(self):
        self.txt.delete(0.0, END)
        subprocess.call('clear', shell=True)
        t1 = datetime.now()
        remoteServer = self.entry_name.get()
        remoteServerIP = socket.gethostbyname(remoteServer)
        nik = subprocess.Popen(["nikto +host http://" + remoteServerIP], stdout=subprocess.PIPE, shell=True)
        (output, error) = nik.communicate()
        # output = nik.communicate()
        msg1 = str(output)
        self.txt.insert(0.0, msg1)
        t2 = datetime.now()
        total = t2 - t1
        print
        "Scanning Completed in: ", total
        messagebox.showinfo(title="Report Status!", message="Scaning Process Completed ")

    def Clear(self):
        self.entry_name.delete(0, 'end')
        self.txt.delete(0.0, 'end')


def main():
    root = Tk()
    scan = Scanning_port(root)
    menubar = Menu(root, background="#e1d8b9")
    filemenu = Menu(menubar, tearoff=0, background="#e1d8b9")
    filemenu.add_command(label="Scan", command=scan.dscan)
    filemenu.add_command(label="Clear", command=scan.Clear)

    filemenu.add_separator()

    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu, background="#e1d8b9")

    helpmenu = Menu(menubar, tearoff=0, background="#e1d8b9")
    helpmenu.add_command(label="Help", command=index0)
    helpmenu.add_command(label="About...", command=index)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar, background="#e1d8b9")
    root.mainloop()


def index():
    filewin = Toplevel()
    labelframe = LabelFrame(filewin, text="About", background="#e1d8b9")
    labelframe.pack(fill="both", expand="yes")

    left1 = Label(labelframe, background="#e1d8b9",
                  text="Infosecplatform presents Python Framework v 1.0\n", font="Verdana 10 bold").pack()

    left7 = Label(labelframe, background="#e1d8b9", text="Got Questions ?", font="Verdana 10 bold").pack()
    left8 = Label(labelframe, wraplength=325, background="#e1d8b9",
                  text="Please Submit your questions, comments and requests to niraj007m@gmail.com\n https://about.me/niraj.mohite\n https://infosecplatform.wordpress.com/").pack()
    left9 = Label(labelframe, wraplength=325, background="#e1d8b9",
                  text="This Tool is only for learning purpose, "
                       "We are not responsible if you misuse it !\n", font="Verdana 7").pack()

    left10 = Label(labelframe, wraplength=300, background="#e1d8b9",
                   text="Nikto is already licensed under GNU, I designed just GUI which runs only the nikto tools. visit nikto https://github.com/sullo/nikto",
                   font="Verdana 7").pack()

    filewin.mainloop()


def index0():
    filewin1 = Toplevel()
    labelframe = LabelFrame(filewin1, text="Help", background="#e1d8b9")
    labelframe.pack(fill="both", expand="yes")

    left1 = Label(labelframe, background="#e1d8b9",
                  text="Infosecplatform presents Python Framework with Nikto v 1.0\n", font="Verdana 10 bold").pack()
    left2 = Label(labelframe, background="#e1d8b9",
                  text="What is Nikto with Python Framework v 1.0 ?", font="Verdana 10 bold").pack()
    left3 = Label(labelframe, background="#e1d8b9",
                  text="niktopy Provides:").pack()
    left4 = Label(labelframe, background="#e1d8b9",
                  text="Simply GUI - Python based Tool used for").pack()
    left5 = Label(labelframe, background="#e1d8b9", text="Nikto scanning.").pack()
    filewin1.mainloop()


if __name__ == "__main__":
    main()
