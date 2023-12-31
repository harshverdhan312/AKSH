# importing necessary modules
from tkinter import *
from tkinter import simpledialog
import pygame
from PIL import ImageTk, Image
from connect import *
import smtplib
import random
import ssl
from email.message import EmailMessage
from aunthentication import password
# authentication


def mail():
    global otp
    send_email = "sinovationtechnologies@gmail.com"
    otp = random.randrange(1001, 9999)
    subject = "Your OTP authentication mail!"
    body = f"""
Thanks for signing up with AKSH!!
We wish you all the best for this journey ! 
your OTP to verify is {otp}
Do not share with anyone.

Best wishes!
Sinovation Technologies 
"""
    em = EmailMessage()
    em['From'] = send_email
    em['To'] = usermail
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib. SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(send_email, password)
        smtp.sendmail(send_email, usermail, em.as_string())

# screen_guis
# login_gui


def login():
    a = Tk()
    a.title("LOG-IN")
    a.geometry("500x500")
    a.resizable(False, False)
    a.configure(bg="gray")
    ea = Label(a, text="Email-Address", bg="gray")
    ea.place(x=100, y=150)
    pds = Label(a, text="Password", bg="gray")
    pds.place(x=100, y=250)
    var1 = StringVar()
    var2 = StringVar()
    Font_tuple = ("Comic Sans MS", 50, "bold")

    title = Label(a, text="AKSH", font=Font_tuple,
                  bg='gray').place(x=100, y=50)
    ent = Entry(a, bd=5, textvariable=var1, font=(
        "Arial", "20", "normal"), width=10)
    ent.place(x=200, y=150)
    ent2 = Entry(a, bd=5, textvariable=var2, font=(
        "Arial", "20", "normal"), width=10)
    ent2.place(x=200, y=250)

    def login_mech():
        un = str(ent.get())
        pd = str(ent2.get())

        query = "select * from info ;"
        cursor.execute(query)
        l = cursor.fetchall()
        for i in l:
            if un == i[1] and pd == i[-1]:
                a.destroy()
                root.destroy()
                homescreen()
        else:
            ea.config(bg="red")
            pds.config(bg="red")

    btn = Button(a, text="login", bd=5, command=login_mech).place(x=250, y=310)
    Label(a, text="New to AKSH ? ", bg="gray").place(x=100, y=400)
    Button(a, text="Sign-up", bd=5, command=signup).place(x=300, y=400)

    a.mainloop()
# signup_gui


def signup():
    a = Tk()
    a.title("Sign-UP")
    a.geometry("500x600")
    a.resizable(False, False)
    a.config(bg="gray")
    Font_tuple = ("Comic Sans MS", 50, "bold")
    title = Label(a, text="AKSH", font=Font_tuple,
                  bg='gray').place(x=100, y=50)
    Label(a, text="Name", bg="gray").place(x=100, y=150)
    Label(a, text="E-Mail Address", bg="gray").place(x=100, y=200)
    Label(a, text="Gender", bg="gray").place(x=100, y=250)
    Label(a, text="DOB", bg="gray").place(x=100, y=300)
    Label(a, text="Password", bg="gray").place(x=100, y=350)

    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()

    var5 = StringVar()
    var = IntVar()
    nent = Entry(a, bd=5, textvariable=var1)
    nent.place(x=200, y=150)
    emlent = Entry(a, bd=5, textvariable=var2)
    emlent.place(x=200, y=200)
    gen = ""

    def female():
        global gen
        gen = "Female"
        radio2.config(state="disabled")
        radio3.config(state="disabled")

    def male():
        global gen
        gen = "Male"
        radio1.config(state="disabled")
        radio3.config(state="disabled")

    def others():
        global gen
        gen = "Others"
        radio1.config(state="disabled")
        radio2.config(state="disabled")

    radio1 = Button(a, text="Female", command=female)
    radio1.place(x=200, y=250)
    radio2 = Button(a, text="Male", command=male)
    radio2.place(x=260, y=250)
    radio3 = Button(a, text="Others", command=others)
    radio3.place(x=310, y=250)
    datent = Entry(a, bd=5, textvariable=var5)
    datent.insert(0, "YYYY-MM-DD")
    datent.place(x=200, y=300)

    pdent = Entry(a, bd=5, textvariable=var3)
    pdent.place(x=200, y=350)

    def signup_mech():
        global gen
        global usermail
        name = nent.get()
        usermail = emlent.get()
        passwd = pdent.get()
        date = datent.get()
        query = "insert into info values('{}','{}','{}','{}','{}')".format(
            name, usermail, gen, date, passwd)
        cursor.execute(query)
        con.commit()
        mail()
        a.destroy()
        root.destroy()
        homescreen()

    btn = Button(a, text="Sign-Up", bd=5, command=signup_mech)
    btn.place(x=250, y=450)
    Label(a, text="Have an account , Login instead -->",
          bg="gray").place(x=100, y=500)
    Button(a, text="Login", bd=5, command=login).place(x=300, y=500)

    a.mainloop()

# homescreen_gui


def homescreen():

    a = Tk()
    a.title("AKSH-MAIN")
    a.geometry("1000x800")
    a.resizable("0", '0')
    a.config(bg="gray")
    global obj_frame
    Font_tuple_time = ("Arial", 100, "bold")

    def meditation():
        b2.config(state='disabled')
        b3.config(state='disabled')

        def music():
            pygame.init()
            pygame.mixer.music.load("song.wav")
            pygame.mixer.music.play()
        time = Button(a, text="Start Meditating", bd=5,
                      font=Font_tuple, bg='white', command=music)
        time.place(x=150, y=300)

    def journaling():
        b1.config(state='disabled')
        b3.config(state='disabled')
        global story
        var1 = StringVar()
        st = Entry(obj_frame, textvariable=var1, bg='pink', width=100)
        st.config(width=100)
        st.place(x=30, y=250)
        Label(obj_frame, textvariable=var1, bg='pink', font=(
            "Arial", "20", "bold"), wraplength=650).place(x=30, y=300)
        f = open("Journal.txt", 'a')

        def workdone():
            story = var1.get()
            print(story)
            f.write(story+"\n")
            f.flush()

        Button(main_frame, text='done', bd=5,
               command=workdone).place(x=50, y=710)

    def reading():
        b1.config(state='disabled')
        b2.config(state='disabled')
        f = open("story.txt")
        a = f.read()
        Label(obj_frame, text=a, height=28, width=87, font=(
            "Arial", "10", "bold")).place(x=30, y=250)

    Font_tuple = ("Comic Sans MS", 40, "bold")
    Font_tuple2 = ("Comic Sans MS", 20, "bold")
    Label(a, text="AKSH", font=Font_tuple, bg='gray').place(x=400, y=10)
    main_frame = Frame(a, bg='yellow', height=1000,
                       width=1000).place(x=0, y=100)
    detail_frame = Frame(main_frame, bg='#30D5C8',
                         height=100, width=1000).place(x=0, y=100)
    Label(detail_frame, text="Select an Activity and keep growing !!",
          bg='#30D5C8', font=Font_tuple2).place(x=250, y=100)
    b1 = Button(detail_frame, text='meditation',
                bd=5, width=30, command=meditation)
    b1.place(x=100, y=150)
    b2 = Button(detail_frame, text='journaling',
                bd=5, width=30, command=journaling)
    b2.place(x=400, y=150)
    b3 = Button(detail_frame, text='reading', bd=5, width=30, command=reading)
    b3.place(x=700, y=150)
    obj_frame = Frame(main_frame, bg='white', height=450,
                      width=700).place(x=30, y=250)
    side_frame = Frame(main_frame, bg='red', height=500,
                       width=250).place(x=740, y=250)

    quote = "Whatever the mind of \n man can conceive and believe, it can achieve.\n -Napoleon Hill"
    Label(side_frame, text=quote, wraplength=270, font=("Sans Serif",
          "25", "normal"), bg='red', fg='yellow').place(x=740, y=250)

    a.mainloop()
# intro_gui


def mainpage():
    global cursor
    global root
    root = Tk()
    root.title("AKSH")

    root.geometry("1000x1000")
    root.resizable("0", "0")
    root.configure(bg='gray')

    check_database()
    cursor = cur
    print("connected")

    main_frame1 = Frame(root, bg='gray').pack()

    Font_tuple = ("Comic Sans MS", 100, "bold")
    Font_tuple2 = ("Comic Sans MS", 20, "bold")
    title = Label(main_frame1, text="AKSH", font=Font_tuple,
                  bg='gray').place(x=300, y=50)

    def Exit():
        root.destroy()

    lbtn = Button(main_frame1, text="LOG-IN", bd='5',
                  command=login).place(x=200, y=600)
    sbtn = Button(main_frame1, text="SIGN-UP", bd='5',
                  command=signup).place(x=800, y=600)
    ebtn = Button(main_frame1, text="EXIT", bd='5',
                  command=Exit).place(x=500, y=600)
    Label(main_frame1, bg='yellow', width=1000, height=20).place(x=0, y=700)
    Label(main_frame1, text="By--> HARSH VERDHAN SINGH and AKHIL GUPTA",
          font=Font_tuple2, bg='yellow').place(x=150, y=730)

    img = ImageTk.PhotoImage(Image.open("20221225_163936.jpg"))
    Label(main_frame1, image=img, height=250, width=240).place(x=350, y=300)
    root.mainloop()


# starting program
mainpage()
