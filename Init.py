import HomeView as Home
import ItemsView as Items
import AddItemsView as AddItems
import DeleteItemsView
import EmergencyView
import AddFieldsView as AddFields
import EditItemsView as EditItems
import tkinter as tk


class Initialize(tk.Tk):
    
    #product initialize
    def __init__(self):
        
        tk.Tk.__init__(self)
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.ccs = container
        
        self.show_frame(Home.Home)
    
    #build frame 
    def show_frame(self, cont):
            if(isinstance(cont, int)):
                frame = Items.Items(self.ccs,cont,self)
                frame.grid(row=0, column=0, sticky="nsew")
                
            else:
                frame = Home.Home(self.ccs ,self)
                frame.grid(row=0, column=0, sticky="nsew")
                
            
            frame.tkraise()

    #open edit page
    def Edit_page_create(self,imagedestination):
        frame = EditItems.EditItems(self.ccs,imagedestination,self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    #open add field page
    def Add_page_create(self):
        frame = AddFields.AddFields(self.ccs,"hi",self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
    
    #open add items page
    def Add_items(self,selectedField):
        frame = AddItems.AddItems(self.ccs,selectedField,self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        
    def Delete_items(self,cont):
        frame= DeleteItemsView.DeleteItemsView(self.ccs,cont,self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
    
    def Emergency_page(self):
        frame= EmergencyView.EmergencyView(self.ccs,self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

app = Initialize()
app.geometry("500x500")
app.iconphoto(False, tk.PhotoImage(file='image/microphone.png'))
app.title("Tamuk Talker")
app.mainloop()
