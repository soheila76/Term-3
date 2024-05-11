from tkinter import*
from tkinter import ttk
import pymysql

class Game ():
    def __init__(self,mooz,color,width,height):
        self.mooz=mooz
        self.color=color
        self.width=width
        self.height=height
        self.lll=[]

    def check(self):
        
        start_o=["o","x","o","x","o","x","o","x","o"]
        x,y=self.btn_1.grid_location(0,0)

        print(self.btn_2.grid_location(0,0))

    def man_badbakh_shodam(self):
        import page2


    def man_badbakh_shodam2(self):
        import page3


    def Tom(self):
        tom=Toplevel()
        tom.geometry("300x300")
        tom.config(bg="gold")
        lbl_win=Label(tom,text="Win=",font=("",14),bg="medium sea green")
        lbl_lose=Label(tom,text="Lose=",font=("",14),bg="red")
        lbl_equals=Label(tom,text="Equals=",font=("",14),bg="dim gray")

        btn_sql=Button(tom,text=" (: Save To SQL :) ",width=12,height=3,bg="royal blue",command=self.alaki)
        btn_sql.grid(row=8,column=2)

        lbl_win.grid(row=2,column=0,pady=10,padx=10)
        lbl_lose.grid(row=4,column=0,pady=10,padx=10)
        lbl_equals.grid(row=6,column=0,pady=10,padx=10)

        self.spin_win=Spinbox(tom,from_=0,to=100,font=('','10'))
        self.spin_lose=Spinbox(tom,from_=0,to=100,font=('','10'))
        self.spin_equals=Spinbox(tom,from_=0,to=100,font=('','10'))

        self.spin_win.grid(row=2,column=2,pady=10)
        self.spin_lose.grid(row=4,column=2,pady=10)
        self.spin_equals.grid(row=6,column=2,pady=10)

    def alaki(self):
        win=self.spin_win.get()
        lose=self.spin_lose.get()
        equals=self.spin_equals.get()

        if win !="" and lose!="" and equals!="":
            try:
                connect=pymysql.connect(host="localhost",user="root",password="root",database="oandx")
                cursor=connect.cursor()
                score=f"insert into socres(win,lose,equals) values('{win}','{lose}','{equals}')"
                cursor.execute(score)
                connect.commit()
                print("Yes")
            except:
                print("No")

        else:
            print("sorry there is an Error?!")

    def create_label(self):
        lbl_xando=Label(mooz,text="X  and  O",font=("",14),bg="cyan2")
        lbl_help=Label(mooz,text="Choose Your Shape Pls",font=("",14),bg="deep sky blue")
        lbl_x=Label(mooz,text="❌",font=("",14),bg="brown1")
        lbl_o=Label(mooz,text="🔵",font=("",14),bg="cornflower blue")
        lbl_welcome=Label(mooz,text="Welcome To My Game",font=("",14),bg="cyan2")

        lbl_xando.grid(row=0,column=4,pady=10,padx=10)
        lbl_help.grid(row=1,column=4,pady=10,padx=10)
        lbl_o.grid(row=5,column=0,pady=10,padx=10)
        lbl_x.grid(row=5,column=6,pady=10,padx=10)
        lbl_welcome.grid(row=7,column=4,pady=30,padx=10)

    def create_btn(self):
        btn_x=Button(mooz,text="X",width=10,height=3,bg="brown1",fg="white",command=self.man_badbakh_shodam)
        btn_x.grid(row=6,column=6)

        btn_o=Button(mooz,text="O",width=10,height=3,bg="royal blue",fg="white",command=self.man_badbakh_shodam2)
        btn_o.grid(row=6,column=0)
        
        btn_score=Button(mooz,text="[: Your Score :]",width=10,height=3,bg="red",command=self.Tom)
        btn_score.grid(row=8,column=4)
        btn_quit=Button(mooz,text="]: QUIT :[",width=11,height=4,bg="blue2",fg="white",command=mooz.destroy)
        btn_quit.grid(row=6,column=4)


mooz=Tk()
mooz.config(bg="light gray")
g=Game(mooz,"gold",500,500)
g.create_label()
g.create_btn()


mooz.mainloop()