import os, sys
import logging, time
import random
import turtle
from tkinter import messagebox

t = turtle.Pen()

f = open("kelime.txt","r")
kelimeler = f.read().splitlines()    #kelimelerin etrafındaki gereksizleri temizler
f.close()
count =0

screen = turtle.getscreen()
a= random.choice(kelimeler)

LOG_FILE = "dosya.log"         #giriş raporları ve klavyeden veri kaydetme
logging.basicConfig(handlers=[logging.FileHandler(LOG_FILE)], level=logging.INFO,format='%(asctime)s: %(message)s')

logging.info("giriş") 
logging.info("gizli kelime: " + a)

c= list( "_ " * len(a))
b=len(a)

harf = screen.textinput("Oyuna Hoşgeldin", "Harf giriniz:")

hak=7
ind=0

turtle.color('blue')
style = ('Courier', 30, 'italic')

def listToString(s):  
    
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

def adam_ciz(hata):
    
    if (hata == 5):
        t.circle(50)
    if(hata==4):
        t.right(90)
        t.forward(150)
    if(hata==3):
        t.right(90)
        t.left(60)
        t.forward(55)
    if(hata==2):
        t.right(315)
        t.forward(55)
    if(hata==1):
        t.right(15)
        t.forward(150)
        t.right(60)
        t.forward(55)
    if(hata==0):
        t.right(300)
        t.forward(150)
        t.left(60)
        t.forward(55)
        messagebox.showinfo("Title",message= "KAYBETTİNİZ")
        
while hak!=0 and harf is not None:

        harf= harf.lower()
        logging.info(harf)
       
        ind = 0

        t.penup()
        t.setposition(200, 300)
        t.pendown()

        ind = a.find(harf, ind)

        if (ind <0):
            hak -= 1
            adam_ciz(hak)
        
        if "_" not in c:
            cevap= messagebox.askquestion("Oyun bitti","Tekrar oynamak ister misin?",icon="info")
            if cevap=="yes":
                os.execl(sys.executable, os.path.abspath(a), *sys.argv)
            elif cevap=="no":
                break
            
        while ind >= 0:
            c[ind * 2] = harf    
            ind = a.find(harf, ind + 1)
        
        t.penup()
        t.setposition(50, 50)
        t.pendown()
        t.write(listToString(c), font=style, align='right')

        harf = screen.textinput("Oyuna Hoşgeldin", "Harf giriniz:")
       


        
      
            