##Finds the file with all inventory and downloads it to a "ON-HAND" sheet on central Excel

import openpyxl
from pathlib import Path
import os
xlsx_file = Path('.', 'CEDIS_MAT.xlsx')

wb_obj = openpyxl.load_workbook(xlsx_file)

inv = wb_obj["ON-HAND"]

inventario ={}

path = "./inventario"

Folderlenght = len(os.listdir(path))

for i in range(0,Folderlenght):
    path = "./inventario"
    

    if len(os.listdir(path)) == 0:
        print("No hay Archivos en la Carpeta de inventario")
        raise SystemExit(0)

    finalFile = os.listdir(path)[0]

    print(finalFile)
    f= open(path+"/"+finalFile, "r") 

    valores = []
    
    for x in f:
        valores = []
        if x.startswith("MXD"):
            valores = x.split()
        
            if len(valores)>=12:
             valores.pop(3)
            if valores[9] == "Yes":
            
                if valores[2] in inventario:
                    inventario[valores[2]] += float(valores[4].replace(',', ''))
                else:
                    inventario[valores[2]] = float(valores[4].replace(',', ''))
        
        #  print(valores)
        
            else:
                continue
  
    f.close() 
    os.remove(os.path.join(path, finalFile))






    
wb_obj.remove(inv)
wb_obj.create_sheet(title="ON-HAND")
inv = wb_obj["ON-HAND"]

row = 1

for x in inventario:
    inv.cell(column=1, row=row, value=x)
    inv.cell(column=2, row=row, value=inventario[x])
    row +=1

wb_obj.save(filename = "CEDIS_MAT.xlsx")


## POSICIÓN / VALOR 
# 1 = Site 
# 2 =Location 
# 3 =Item Number 
# 4 =UM
# 5 = Qty on Hand
# 6 = Created
# 7 = Expire
# 8 =    Assay % Grade 
# 9 = Status     
# 10 = Avail
# 11 = Net
# 12 = OvrIs