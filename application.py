from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import messagebox
from tkVideoPlayer import TkinterVideo
import time
import datetime
# create root

root=  Tk()
root.geometry("580x450")
root.title("Applicationo Form")
root.iconbitmap(r'form.ico')
# frame
main_frame=Frame(root)
main_frame.pack(fill="both",expand=True)
global second_frame
global image1
global image2
global image3
global image4
global image5
global image6
global c1
global c2
global c3
global c4
global lb
global lb1
global lb2
global lb3
global var1
global var2
global var3
global var4
global n_entry
global s_combo
global r_entry
global d_combo
# splash screen
def splach_screen():
    global image_frame
    image_frame=Frame(main_frame)
    image_frame.pack(fill="both",expand=True)
    splash=TkinterVideo(image_frame)
    splash.load("APPLICATION FORMD_2.mp4")
    splash.pack(fill="both",expand=True)
    splash.play()
def destory_splash():
     image_frame.destroy()
def next_p():

    next_frame.destroy()
    new_frame=ttk.Frame(main_frame)
    new_frame.pack(fill="both",expand=True)
    def on_scroll(*args):
        canvas.yview(*args)

    canvas = Canvas(new_frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(new_frame, orient="vertical",bootstyle="success", command=on_scroll)
    scrollbar.pack(side="right", fill="y")

    canvas.config(yscrollcommand=scrollbar.set)

    # Create a frame to hold the widgets
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    det_label=Label(frame,text=f"Minimum marks % of BS computer science",font="Garamond 15 bold",fg="white",bg="black")
    det_label.pack(padx=70)
    cs_meter = ttk.Meter(frame,
        metersize=130,
        padding=8,
        amountused=60,
        metertype="full",
        interactive= False,
        bootstyle='success',
        stripethickness=5,
        textright='%')
    cs_meter.pack()
    det_label1=Label(frame,text=f"Minimum marks % of BS software engineering",font="Garamond 15 bold",fg="white",bg="black")
    det_label1.pack()
    cs_meter = ttk.Meter(frame,
        metersize=130,
        padding=8,
        interactive= False,
        amountused=50,
        metertype="full",
        bootstyle='success',
        stripethickness=5,
        textright='%')
    cs_meter.pack()
    det_label2=Label(frame,text=f"Minimum marks %  of BS math",font="Garamond 15 bold",fg="white",bg="black")
    det_label2.pack()
    cm_meter = ttk.Meter(frame,
    metersize=130,
    padding=8,
    amountused=65,
    metertype="full",
    interactive= False,
    bootstyle='success',
    stripethickness=5,
    textright='%')
    cm_meter.pack()
    det_label3=Label(frame,text=f"Minimum marks %  of BS chemistry",font="Garamond 15 bold",fg="white",bg="black")
    det_label3.pack()
    m_meter = ttk.Meter(frame,
    metersize=130,
    padding=8,
    interactive= False,
    amountused=45,
    metertype="full",
    bootstyle='success',
    stripethickness=5,
    textright='%')
    m_meter.pack()
    def configure_canvas(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", configure_canvas)
    b4= ttk.Button(new_frame, text="Exit", bootstyle="success",command=quit)
    b4.pack()
def eny(e):
    # 
    global next_frame
    nm=n_entry.get()
    rn=r_entry.get()
    if (d_combo.get()=="Select Department"):
        messagebox.showwarning("Warning", "Complete the form")
    elif (r_entry.get()==""):
        messagebox.showwarning("Warning", "Complete the form")
    elif (n_entry.get()==""):
        messagebox.showwarning("Warning", "Complete the form")
    elif (s_combo.get()=="Select Semester"):
        messagebox.showwarning("Warning", "Complete the form")
    elif(n_entry.get()==nm) and (r_entry.get()==int(rn)) and (d_combo.get()=="BS physics") or(d_combo.get()=="BS Math")or(d_combo.get()=="BS Computer Science") or (d_combo.get()=="BS Chemistry") or (s_combo.get()=="1")or (s_combo.get()=="2")or (s_combo.get()=="3")or (s_combo.get()=="4")or (s_combo.get()=="5")or (s_combo.get()=="6")or (s_combo.get()=="7")or (s_combo.get()=="8"):
        lb.config(image=image1)
        lb1.config(image=image2)
        lb2.config(image=image3)
        lb3.config(image=image4)
        c1.config(text="verified")
        c2.config(text="verified")
        c3.config(text="verified")
        c4.config(text="verified")
        time.sleep(1)
        messagebox.showinfo("verification message", "Verification Done") 
        time.sleep(1)
        second_frame.destroy()
        next_frame=Frame(main_frame)
        next_frame.pack(fill="both",expand=True)
        image7=Image.open("verify.jpg")
        image7=image7.resize((100,100), resample=Image.Resampling.LANCZOS)
        image7=ImageTk.PhotoImage(image7)
        fg1=ttk.Floodgauge(next_frame,bootstyle="success",font="Garamond 20 bold",mask='Successfully Complete ' + '{}%', value=99,maximum=100, length=400)
        fg1.grid(column=0,row=0,padx=100,pady=50)
        lb6=Label(next_frame,image=image1)
        lb6.grid(column=0,row=1,columnspan=2,padx=90,pady=20)
        lb5=Label(next_frame,text="You verfication is complete",font="Garamond 23 bold" )
        lb5.grid(column=0,row=2,columnspan=2,padx=90,pady=10)
        lb7=Label(next_frame, text='For More Details Click Next!',)
        lb7.grid(column=0,row=3,columnspan=2,pady=10)
        b2= ttk.Button(next_frame, text="Next", bootstyle="success",command=next_p)
        b2.grid(row=4, column=0, padx=10, pady=10)
        b3= ttk.Button(next_frame, text="Exit", bootstyle="success",command=quit)
        b3.grid(row=5, column=0, padx=10, pady=10)
    else:
        pass
def home():
    global second_frame
    global image1
    global image2
    global image3
    global image4
    global image5
    global image6
    global c1
    global c2
    global c3
    global c4
    global lb
    global lb1
    global lb2
    global lb3
    global var1
    global var2
    global var3
    global var4
    global n_entry
    global s_combo
    global r_entry
    global d_combo
    global p1
    # frame
    second_frame=Frame(main_frame)
    second_frame.pack(fill="both",expand=True)
    # images
    image6=Image.open("waiting.png")
    image6=image6.resize((50,50), resample=Image.Resampling.LANCZOS)
    image6=ImageTk.PhotoImage(image6)
    image5=Image.open("rej.webp")
    image5=image5.resize((50,50), resample=Image.Resampling.LANCZOS)
    image5=ImageTk.PhotoImage(image5)
    image1=Image.open("verify.jpg")
    image1=image1.resize((50,50), resample=Image.Resampling.LANCZOS)
    image1=ImageTk.PhotoImage(image1)
    image2=Image.open("verify.jpg")
    image2=image2.resize((50,50), resample=Image.Resampling.LANCZOS)
    image2=ImageTk.PhotoImage(image2)
    image3=Image.open("verify.jpg")
    image3=image3.resize((50,50), resample=Image.Resampling.LANCZOS)
    image3=ImageTk.PhotoImage(image3)
    image4=Image.open("verify.jpg")
    image4=image4.resize((50,50), resample=Image.Resampling.LANCZOS)
    image4=ImageTk.PhotoImage(image4)
    # image label
    lb=Label(second_frame,image=image5)
    lb.grid(column=3,row=1,padx=15,pady=5)
    lb1=Label(second_frame,image=image5)
    lb1.grid(column=3,row=2,padx=15,pady=5)
    lb2=Label(second_frame,image=image5)
    lb2.grid(column=3,row=3,padx=15,pady=5)
    lb3=Label(second_frame,image=image5)
    lb3.grid(column=3,row=4,padx=15,pady=5)
    #  date entry
    current_date = datetime.date.today()
    d_entRy=ttk.DateEntry(second_frame,bootstyle="success",dateformat='%Y-%m-%d',firstweekday=2,startdate=current_date)
    d_entRy.grid(column=0,row=0,padx=200,columnspan=4)
    # label
    name_label=Label(second_frame,text="Name",font="Garamond 15 bold",fg="white",bg="black")
    name_label.grid(column=0,row=1,pady=15)
    roll_label=Label(second_frame,text="Roll No",font="Garamond 15 bold",fg="white",bg="black")
    roll_label.grid(column=0,row=2,pady=15)
    dept_label=Label(second_frame,text="Department",font="Garamond 15 bold",fg="white",bg="black")
    dept_label.grid(column=0,row=3,pady=15)
    sem_label=Label(second_frame,text="Semester",font="Garamond 15 bold",fg="white",bg="black")
    sem_label.grid(column=0,row=4,pady=15)

    # check button
    var1=ttk.BooleanVar()
    var2=ttk.BooleanVar()
    var3=ttk.BooleanVar()
    var4=ttk.BooleanVar()
    def pp1(e):
        var1.set(True)
        lb.config(image=image6)
        c1.config(text="waiting")
        r_entry.focus_set()
    def pp2(e):
        var2.set(True)
        lb1.config(image=image6)
        c2.config(text="waiting")
        d_combo.focus_set()
    def pp3(e):
        var3.set(True)
        lb2.config(image=image6)
        c3.config(text="waiting")
        s_combo.focus_set()
    def pp4(e):
        var4.set(True)
        lb3.config(image=image6)
        c4.config(text="waiting")
        b1.focus_set()
    c1=ttk.Checkbutton(second_frame,text="click to verify ",variable=var1,onvalue=True,offvalue=False, bootstyle="success-round-toggle")
    c1.grid(column=2,row=1,pady=15)
    c2=ttk.Checkbutton(second_frame,text="click to verify ",variable=var2,onvalue=True,offvalue=False, bootstyle="success-round-toggle")
    c2.grid(column=2,row=2,pady=15)
    c3=ttk.Checkbutton(second_frame,text="click to verify ",variable=var3,onvalue=True,offvalue=False, bootstyle="success-round-toggle")
    c3.grid(column=2,row=3,pady=15)
    c4=ttk.Checkbutton(second_frame,text="click to verify ",variable=var4,onvalue=True,offvalue=False, bootstyle="success-round-toggle")
    c4.grid(column=2,row=4,pady=15)
    # entry 
    n_entry=ttk.Entry(second_frame,width=25,bootstyle="success")
    n_entry.grid(row=1,column=1,pady=15)
    # n_entry.bind('<Return>',p1)
    n_entry.bind('<Return>',pp1)
    r_entry=ttk.Entry(second_frame,width=25,bootstyle="success")
    r_entry.grid(row=2,column=1,pady=15)
    r_entry.bind('<Return>',pp2)
    d_list=["BS physics","BS Chemistry","BS Math","BS Computer Science"]
    d_combo=ttk.Combobox(second_frame,values=d_list,bootstyle="success")
    d_combo.set("Select Department")
    d_combo.configure(state="readonly")
    d_combo.grid(column=1,row=3,pady=15)
    d_combo.bind('<Return>',pp3)
    s_list=["1","2","3","4","5","6","7","8"]
    s_combo=ttk.Combobox(second_frame,values=s_list,bootstyle="success")
    s_combo.set("Select Semester")
    s_combo.configure(state="readonly")
    s_combo.grid(column=1,row=4,pady=15)
    s_combo.bind('<Return>',pp4)
    # button
    b1= ttk.Button(second_frame, text="Click To Verify", bootstyle="success",command=eny)
    b1.grid(row=5, column=1, padx=30, pady=30)
    b1.bind('<Return>',eny)
splach_screen()
root.after(4000,destory_splash)
root.after(4000,home)
root.mainloop()