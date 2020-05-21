
import openpyxl

class UpdateSpeechModel:
    
    #get updated text store into db
    def __init__(self,filedataname,EnterData,editspeechrow):
        xfile = openpyxl.load_workbook(filedataname)
        ws = xfile.active
        ws.cell(row=editspeechrow+1,column=2).value = EnterData
        xfile.save(filedataname)