import tkinter as tk
import pyttsx3
import HomeView as Home
import xlrd

LARGE_FONT= ("Verdana", 15)
DaTa = "comming soon "


class Items(tk.Frame):
    
    #when click on item, get text from db and convert to voice     
    def Entery_Text_To_Voice(self,message,imagedestination):
        m= message
        engine = pyttsx3.init()
        engine.say(m)
        engine.runAndWait()
        if Home.r1_v.get()=='enable':
            self.cc.Edit_page_create(imagedestination)
        
    #render items button
    def create_button(self,bottomframe,imagedestination,Speech_sentence):
        photo = tk.PhotoImage(file = r"image/"+imagedestination)
        label = tk.Label(image=photo)
        label.image = photo
        bb=tk.Button(bottomframe, 
                   image = photo,text='Convert to voice',
                  command=lambda:self.Entery_Text_To_Voice(Speech_sentence,imagedestination))
        return bb

    def show_print(self):
        print("self print ",self.wow,"\n ")
    
    #render items from db
    def __init__(self, parent,wow, controller):
        
        self.wow = wow

        wb = xlrd.open_workbook("db/listofdatatable.xlsx")
        sheet = wb.sheet_by_index(0)

        excelname = sheet.cell_value(wow,0)
        
        wb = xlrd.open_workbook("db/"+excelname+".xlsx")
        sheet = wb.sheet_by_index(0)
        Emotion ={}
        
        for x in range(sheet.nrows):
            if sheet.cell_value(x,0)!='':
                Emotion[sheet.cell_value(x,0)]=sheet.cell_value(x, 1)
            
        self.cc = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=excelname.upper(), font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        photo = tk.PhotoImage(file = r"image/back.png")
        label = tk.Label(image=photo)
        label.image = photo
        button1 = tk.Button(self, text="Back to Home",image = photo,
                            command=lambda: controller.show_frame(Home.Home))
        button1.pack()
        
        i =1
        bottomframe = tk.Frame(self)
        bottomframe.pack()
        for x in Emotion:
            
            b = self.create_button(bottomframe,x,Emotion[x])
            if i > 5:
                bottomframe = tk.Frame(self)
                bottomframe.pack()
                b.pack(side=tk.LEFT)
                i = 0
            else:
                b.pack(side=tk.LEFT)
                
            i=i+1
        
