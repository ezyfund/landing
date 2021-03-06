from oauth2client.service_account import ServiceAccountCredentials
import gspread

def get_sheet(sheetname):
    #remember to share sheet with email id in client secret
    print("Looking for",sheetname)
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    print(creds)
    print(type(creds))
    # print(creds)
    client = gspread.authorize(creds)
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    
    status=True
    sheet=None
    try:
        sheet = client.open(sheetname).sheet1
        return status,sheet
    except Exception as e: 
        print("Error is ",e)
        print("An error")
        print(sheet)
        print("An exception occurred") 
        status=False
        return status,sheet

def insert_row(row,sheetname):
    # row is a list of strings
    print("Inserting",row)
    status,sheet=get_sheet(sheetname)
    if not status:
        print("Issue")
        return False
    index = len(sheet.get_all_values())
    print("Index is ",index,"inserting",row)
    # sheet.insert_row([row], index+1)
    sheet.insert_row([row[0],""], index+1)

    return True
