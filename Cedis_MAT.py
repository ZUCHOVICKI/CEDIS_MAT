
import openpyxl
from pathlib import Path
from datetime import datetime
from openpyxl.styles import Color, PatternFill, Font, Border

##CENTRAL FILE WHERE OPERATIONS AND DATA IS STORED
xlsx_file = Path('.', 'CEDIS_MAT.xlsx')

wb_obj = openpyxl.load_workbook(xlsx_file)

## mAIN FUCNTION FOR ADDING ORDERS TO AND COMPONENTS ( DATE = "DATE WHEN THE ORDER IS DUE" 
#  DATA = ITEMS THAT MUST BE LOADED TO THE ORDER FILE) 
# ++IMPORTANT ADDORDER MUST BE CALLED AFTER EVERY NEW COMPONENT IS ADDED TO THE ORDER
def ADDORDER(Data,Date):


    ## USED TO LOEADING NEW COMPONENTS ON EXISTING ORDERS WHITHOUT DELETING EXISITING COMPONENTS
    try:
        dataDict =  finishedOrders[Date] 
    except:
        dataDict = {}

    ## GETS THE EXCEL SHEET WHERE INFORMATIÓN IS LOCATED AND THE NUMBER OF TIMES IT NEEDS TO BE CALLED 
    for key in Data:
        sheetnom = key
        num = Data.get(key)
        
        
    ##SEARCHS FOR THE WORKSHEET AND TAKES ALL COMPONENTS NEEDED FOR THE ORDER 
    for sheet in wb_obj.worksheets:
        
        if sheet.title != sheetnom:
            continue
        
        for row in sheet.iter_rows(max_row=sheet.max_row):

            if row[1].value == None:
                continue
            if row[3].value == None:
                continue

            if row[1].value in dataDict:
                
                dataDict[row[1].value] += (row[3].value)*num

            else:
                dataDict[row[1].value] = (row[3].value)*num

    ##ADDORDER LOADS DATA ON THE GLOBAL VARIABLE finishedOrders
    finishedOrders[Date] = dataDict
    
##GETS ALL THE INVENTAROY COMPONETS AND THE NUMBER ONHAND FROM A SPECIFIC EXCEL PAGE
##**TODO ADD THE OPTION OF FILTERING INVENTORY ACCORDING TO LOCATION ON ENTERPRISE
def GetInventario():
    inventario = {}

    onHand = wb_obj["ON-HAND"]
    HojasInventario =[onHand]



    for sheet in HojasInventario:
        
        for row in sheet.iter_rows(max_row=sheet.max_row):
                
                if row[0].value == None:
                    continue
                if row[1].value == None:
                    continue

                if row[0].value in inventario:
                    
                    inventario[row[0].value] += (row[1].value)

                else:
                    inventario[row[0].value] = (row[1].value)
    ##GETINVENTARIO LOADS THE AVAILABLE MATERIALS ON GLOBAL VARIABLE inventario
    return inventario


## CHECKS FOR THE TOTAL NUMBER OF MATERIALS AFTER THE ORDER HAS BEEN FINALIZED ( Orders = finished orders and date
#  Inventary = inventory details order = dates ordered from closest to furthest)
def CheckAvailable(Orders,Inventary,order):
    Actualdate = ""
    warningsProduct = {}
    
    for date in order:
       Actualdate =date
       
       data =  Orders[date]
       
      
       for product in data:
           
           if product not in Inventary:
               
               if product not in warningsProduct:
                
                warningsProduct[product]= 0 - data[product]
               else:
                warningsProduct[product] -= (data[product])
               continue
           
           Inventary[product] -= data[product]
           
           
           
           if(Inventary[product]<=0):
               
               
               if product not in warningsProduct:
                
                warningsProduct[product] = (Inventary[product] - data[product])

            
           
       newOrders = warningsProduct.copy()
       
       
       dateWarnings[Actualdate]=newOrders
       newOrders= {}
    #    print("Guardado")
    
    return dateWarnings


 ##Function for display of all loaded Bills of Materials on the interfaze   
def getAllBills():
    MATBills = {}
    count = 1
    for sheet in wb_obj.worksheets:
        if sheet.title in ["ON-HAND","Ordenes"]:
            continue
        MATBills[count] = sheet.title
        count+=1  
    count = 1     
    # for x in MATBills:
    #             print("{0} ---- {1}".format(count,MATBills.get(x)))
    #             count+=1
    return MATBills





    ##Function for ordering dates after the creatión of an order      
def OrderDate(date):
    dateOrder.append(date)
    str(date)
    dateOrder.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))
    # print(finishedOrders)
    
##Function for adding onlly one subcomponent from a bill and not the whole bill
def AgregarIndividual(Item,Date,Amount):
   

    
    try:
        finishedOrders[Date][Item] += Amount
    except:
        finishedOrders[Date] = {Item:Amount}
    

##Final function that generates an Excel file using the Availability of the materials
def GenerarReporte(Warnings,FirstDate,Orders,DateOrder,inventario):
    
    items =  ItemMaster()
    today = datetime.today().strftime('%Y-%m-%d')
    wb_obj.create_sheet(title="Reporte")
    sheet = wb_obj["Reporte"]

    redFill = PatternFill(start_color='FFFF0000',
                   end_color='FFFF0000',
                   fill_type='solid')
    greenfill = PatternFill(start_color='00FF00',
                   end_color='00FF00',
                   fill_type='solid')

    for s in wb_obj.worksheets:

        if s.title != 'Reporte':
            sheet_name = wb_obj[s.title]
            wb_obj.remove_sheet(sheet_name)

    
    sheet.cell(column=1, row=1, value="Fecha de Generación de Reporte")
    sheet.cell(column=2, row=1, value=today)


    sheet.cell(column=10, row=1, value="Fecha Maxima de Materiales")
    sheet.cell(column=11, row=1, value=FirstDate)

    currentRow = 3
    # print(Warnings)
    for Date in DateOrder:

        sheet.cell(column=1, row=currentRow, value="Orden")
        sheet.cell(column=2, row=currentRow, value=Date)
        currentRow+=1
        sheet.cell(column=1, row=currentRow, value="Material")
        sheet.cell(column=2, row=currentRow, value="# Necesitado")        
        sheet.cell(column=3, row=currentRow, value="Total")
        sheet.cell(column=4, row=currentRow, value="Status")
        currentRow+=1
        for item in Orders[Date]:
            itemStr = str(item)
            # print(itemStr)
            # print(type(itemStr))

            
            try:
                if items[itemStr] == "M":
                    # print("Manufactura")
                    continue
                
            except:
                
                
                print("Not In Item Master")

            
            sheet.cell(column=1, row=currentRow, value=item)
            sheet.cell(column=2, row=currentRow, value=Orders[Date][item])
            if item in Warnings[Date]:
                sheet.cell(column=3, row=currentRow, value=Warnings[Date][item])
                
                sheet.cell(column=4, row=currentRow).fill=redFill
            else:
                sheet.cell(column=3, row=currentRow, value=inventario[item])
                sheet.cell(column=4, row=currentRow).fill=greenfill
            currentRow+=1

# report is saved with the keyword "Reporte" + the date it was generated
    wb_obj.save('Reporte'+today+'.xlsx')

##Loads a Central DB where information about all materials is stored
def ItemMaster():
    ItemS = {}
    xlsx_file = Path('.', 'Item master.xlsx')
    Item_Master = openpyxl.load_workbook(xlsx_file)

    sheet = Item_Master["Data"]
    for row in sheet.iter_rows(max_row=sheet.max_row):
            
            ItemS[row[1].value] = row[10].value
    
    return ItemS

## loads all the components in a selected Bill of materials and siplays it on the interface
def GetIndividualComponents(Item):
    allItem = []
    for sheet in wb_obj.worksheets:
        
        if sheet.title != Item:
            continue
        
        for row in sheet.iter_rows(max_row=sheet.max_row):
            if row[1].value == None:
                continue
            if row[3].value == None:
                continue
            allItem.append(row[1].value)
        
    return allItem
MATBills = getAllBills()


## Global variables that can be read from all the aplication 
finishedOrders = {} ##Orders that have been submitted
dateOrder = [] # Orders submitted but in chronological order
dateWarnings = {} # Orders that have one or more materials close or under 0 available units
ActualOrder = {} #Private Variable used in functions for temporary storage of order info
dataDict = {} #Private Variable used in functions for temporary storage of componets info
inventario = GetInventario() # Current inventory loaded on separate file


