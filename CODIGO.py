from tkinter import *


def w14():
    w14 = Tk()
    w14.title('Una... ¿Aventura?')
    w14.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w4, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w4, image = img5,command = w15).place(x=752, y=646)
    w14.mainloop()

def w13():
    w13 = Tk()
    w13.title('Una... ¿Aventura?')
    w13.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w4, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w4, image = img5,command = w14).place(x=752, y=646)
    w13.mainloop()
    
def w12():
    w12= Tk()
    w12.title('Una... ¿Aventura?')
    w12.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w12, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w12, image = img5,command = w13).place(x=752, y=646)
    w12.mainloop()
    
def w11():
    w11 = Tk()
    w11.title('Una... ¿Aventura?')
    w11.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w11, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w11, image = img5,command = w12).place(x=752, y=646)
    w11.mainloop()
    
def w10():
    w10 = Tk()
    w10.title('Una... ¿Aventura?')
    w10.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w10, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w10, image = img5,command = w3).place(x=752, y=646)
    w10.mainloop()

def w9():
    w9 = Tk()
    w9.title('Una... ¿Aventura?')
    w9.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w9, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w9, image = img5,command = w10).place(x=752, y=646)
    w9.mainloop()
    
def w8():
    w8 = Tk()
    w8.title('Una... ¿Aventura?')
    w8.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w8, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w8, image = img5,command = w9).place(x=752, y=646)
    w8.mainloop()
    
def w7():
    w7 = Tk()
    w7.title('Una... ¿Aventura?')
    w7.geometry("919x690")
    img4 = PhotoImage(file ='imag7.jgp')
    bgd2 = Label(w7, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w7, image = img5,command = w8).place(x=752, y=646)
    w7.mainloop()
    
def w6():
    w6 = Tk()
    w6.title('Una... ¿Aventura?')
    w6.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w6, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w6, image = img5,command = w7).place(x=752, y=646)
    w6.mainloop()
    
def w5():
    w5 = Tk()
    w5.title('Una... ¿Aventura?')
    w5.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w5, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w5, image = img5,command = w6).place(x=752, y=646)
    w5.mainloop()
    
def w4():
    w4 = Tk()
    w4.title('Una... ¿Aventura?')
    w4.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w4, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w4, image = img5,command = w5).place(x=752, y=646)
    w4.mainloop()

def w3():
    w3 = Tk()
    w3.title('Una... ¿Aventura?')
    w3.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w3, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w3, image = img5,command = w4).place(x=752, y=646)
    w3.mainloop()

def w2():
    w2 = Tk()
    w2.title('Una... ¿Aventura?')
    w2.geometry("919x690")
    img4 = PhotoImage(file ='I2.png')
    bgd2 = Label(w2, image = img4).place(x=0, y=0)
    img5 = PhotoImage(file = 'B4.png')
    but3 = Button(w2, image = img5,command = w3).place(x=752, y=646)
    w2.mainloop()
    but4 = Button(w2, image = img6,command = w3).place(x=752, y=646)
    w2.mainloop()

w1  = Tk()
w1.title('Una... ¿Aventura?')
w1.geometry("919x602")
img = PhotoImage(file ='I1.png')
bgd = Label(w1, image = img).place(x=0, y=0)
img1 = PhotoImage(file = 'B1.png')
but = Button(w1, image = img1, command = w2).place(x=318, y=292)
img2 = PhotoImage(file = 'B2.png')
but1 = Button(w1, image = img2).place(x=318, y=397)
img3 = PhotoImage(file = 'B3.png')
but2= Button(w1, image = img3).place(x=318, y=496)
w1.mainloop()




    
