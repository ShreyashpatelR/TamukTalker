import tkinter as tk
import xlrd

LARGE_FONT= ("Verdana", 15)
DaTa = "comming soon "


class Home(tk.Frame):
    
    #render home page     
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="MAIN PAGE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        global r1_v 
        r1_v = tk.StringVar()
        r1_v.set('disable')

        
        bottomframe = tk.Frame(self)
        bottomframe.pack()
        
        button = tk.Button(bottomframe, text="EMERGENCY",
                            command=lambda:controller.Emergency_page())    
        button.config( height = 1, width = 10 )
        button.pack(side=tk.LEFT,padx=5)
        
        
        
        RB = tk.Radiobutton(bottomframe, text = 'Enable Edit',value = 'enable',variable=r1_v) 
        RB.pack(side=tk.LEFT,padx=5)

        RB = tk.Radiobutton(bottomframe, text = 'Disable Edit',value = 'disable',variable=r1_v ) 
        
        RB.pack(side=tk.LEFT,padx=5)
                
        
        button = tk.Button(bottomframe, text="ADD/DELETE",
                            command=lambda:controller.Add_page_create())    
        button.config( height = 1, width = 10 )
        button.pack(pady=10,padx=5)
        
        
        
        k =1
        bottomframe = tk.Frame(self)
        bottomframe.pack()
        wb = xlrd.open_workbook("db/listofdatatable.xlsx")
        sheet = wb.sheet_by_index(0)
        total_row = sheet.nrows
        
        for i in range(total_row):
            if sheet.cell_value(i, 0)!='':
                button = self.create_button(bottomframe,i,sheet.cell_value(i, 0),controller)
    
                if k > 5:
                    bottomframe = tk.Frame(self)
                    bottomframe.pack()
                    button.pack(side=tk.LEFT)
                    k = 0
                else:
                    button.pack(side=tk.LEFT)
                    
                k=k+1
    
    # edit items enable / disable    
    def deselect_radio_button(self):
        print("welcome to radio ",self.r1_v.get())
        if self.r1_v.get():
            self.r1_v.set(10)
        else:
            self.r1_v.set(12)
    
    #render items according to fields    
    def create_button(self,bottomframe,i,tt,controller):
        button = tk.Button(bottomframe, text=tt.upper(),
                            command=lambda:controller.show_frame(i))    
        button.config( height = 5, width = 10 )
        return button

