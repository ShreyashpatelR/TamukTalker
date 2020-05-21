import tkinter as tk
import xlrd
import HomeView as Home
import UpdateSpeechController
from tkinter import filedialog
import UploadImageController
LARGE_FONT= ("Verdana", 15)
DaTa = "comming soon "


class EditItems(tk.Frame):
    
    #render edit page when click on edit items
    def __init__(self, parent,imagedestination, controller):
        tk.Frame.__init__(self,parent)
        bottomframe = tk.Frame(self)
        bottomframe.pack()
        label = tk.Label(bottomframe, text="EDIT PAGE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        photo = tk.PhotoImage(file = r"image/back.png")
        label = tk.Label(image=photo)
        label.image = photo
        button1 = tk.Button(bottomframe, text="Back to Home",image = photo,
                            command=lambda: controller.show_frame(Home.Home))
        button1.pack()

        label = tk.Label(bottomframe, text="Update Image")
        label.pack(pady=10,padx=10)
        
        photo = tk.PhotoImage(file = r"image/"+imagedestination)
        label = tk.Label(image=photo)
        label.image = photo

        button1 = tk.Button(bottomframe, text="Upload New Image",image = photo,
                            command=lambda: self.Upload_Image(imagedestination,bottomframe))
        button1.pack(pady=10,padx=10)
        
        label = tk.Label(bottomframe, text="Update Speech")
        label.pack(pady=10,padx=10)
        
        filename = imagedestination.split('/')
        wb = xlrd.open_workbook("db/"+filename[0]+".xlsx")
        sheet = wb.sheet_by_index(0)

        speechsentence = ''
        editspeechrow = 0
        for x in range(sheet.nrows):
            if sheet.cell_value(x,0)== imagedestination:
                speechsentence = sheet.cell_value(x,1)
                editspeechrow = x

        filedataname = "db/"+filename[0]+".xlsx"
            
        EnterData = tk.Entry(bottomframe)
        EnterData.insert(0, speechsentence)
        EnterData.pack(pady=10,padx=10)

        button = tk.Button(bottomframe, text="EDIT SPEECH",
                            command=lambda:self.Change_Speech_button(EnterData,filedataname,editspeechrow,bottomframe))    
        button.config( height = 2, width = 10 )
        button.pack(pady=10,padx=10)
        
    #upload emoji for individual items
    def Upload_Image(self,imagedestination,bottomframe):
        filename=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
        if filename:
            UploadImageController.UploadImageController(filename,imagedestination)
            label = tk.Label(bottomframe, text="Image is updated!")
            label.pack(pady=2,padx=2)
            
        else:
            print("no image")
            label = tk.Label(bottomframe, text="You have not select Image")
            label.pack(pady=2,padx=2)
        
    #edit speech of items   
    def Change_Speech_button(self,EnterData,filedataname,editspeechrow,bottomframe):
        if EnterData.get()!= '':
            UpdateSpeechController.UpdateSpeechController(filedataname,EnterData.get(),editspeechrow)
            #print("update!")
            label = tk.Label(bottomframe, text="Speech is updated! ")
            label.pack(pady=2,padx=2)
            
        print(EnterData.get())
