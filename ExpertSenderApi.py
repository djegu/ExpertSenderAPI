import requests
import xml.etree.ElementTree as ET
import pandas as pd
import lxml.etree
import json 
from datetime import timedelta
from datetime import date

"""***************************************************
Output
***************************************************"""
version = 'v1'
folderName = r'C:\Users\15148\Documents\01 - Mediazur\API Data'
currentYear = 2022
currentDate = date.today().strftime('%Y-%m-%d')
reportDate = currentDate
exportFileName = '\Export data - ' + version + ' - ' + reportDate


'''***************************************************
Og link & Var method API
***************************************************'''

#https://api.esv2.com/v2/Api/Messages?apiKey=YOUR_API_KEY_HERE
#https://api.esv2.com/v2/Api/Messages/893?apiKey=YOUR_API_KEY_HERE
#https://api.esv2.com/v2/Api/MessageStatistics/123?apiKey=YOUR_API_KEY_HERE 
#https://api.esv2.com/v2/Api/SmsMmsMessages?apiKey=YOUR_API_KEY_HERE

mtd_eml = 'Api/Messages'
mtd_eml2 = 'Api/Messages/'
mtd_stats = 'Api/MessageStatistics/'
mtd_api = '?apiKey='
mtd_sms = 'Api/SmsMmsMessages/'


'''***************************************************
Test Pandas
***************************************************'''

df_xl = pd.read_excel(r"C:\Users\15148\Documents\01 - Mediazur\API Data.xlsx")

for index, row in df_xl.iterrows():
    #r = requests.get(f"{row['SERVEUR']}{mtd_eml}{mtd_api}{row['CLE API']}")
    r = requests.get('https://api5.esv2.com/v2/Api/Messages?apiKey=XNBsZQVSnDOQfTTFnktE')
    json_data = r.text
    #tree = ET.parse(r.text)
    root = ET.fromstring(json_data)
    for child in root.iter():
        message = child.find('Id')
        if message is not None:
            id_message = message.text
            msg_stats = requests.get(f'https://api5.esv2.com/v2/Api/MessageStatistics/{id_message}?apiKey=XNBsZQVSnDOQfTTFnktE')
            each_data = ET.fromstring(msg_stats.text)
            for c in each_data.iter():
                sent = c.find('Sent') 
                bounced = c.find('Bounced')
                data = sent + bounced
                print (data)
            
    '''for elem in r.iter():
        print (elem)
    
    
    json_data = r.text
    root = ET.fromstring(json_data)
    textelem = root.find('Message/Id')
    print  (textelem)
    '''
  
    #dfxml = pd.read_xml(r.content)
    #print (dfxml)
    #root = ET.fromstring(json)
    #ET.dump(root)
    

'''OLD TEST'''

#root = lxml.etree.fromstring(xmlstr)
#textelem = root.find('result/field/value/text')
#print textelem.text
    #data =[]
    #testid = root.find('Id')
    #for id in root.iter('Message'):
        #print (id.text)
        #for child in id.findall('Id'):
            #ID = child.text
            #print (ID)
            #v1 = dict(tag = child.tag, text = child.text)



#MsgId = []

#for child in root.iter('Id'):
    #print(child.tag, child.text)

#SentDate = []

#for child in root.iter('SentDate'):
 #   SentDate.append(child.text)
