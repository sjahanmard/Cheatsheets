import xlrd
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from xlwt import Workbook
wb = Workbook()



file = 'file.xls'
wb = xlrd.open_workbook(file)
sh = wb.sheet_by_index(0)
name=[]
price=[]
uid=[]
for i in range(sh.nrows-1):
      uid.append(sh.cell_value(i+1,0))
      name.append(sh.cell_value(i+1,1))
      price.append(sh.cell_value (i+1,2))
for i in range(sh.nrows-1):
    uid[i] = int (uid[i])
    price[i] = int (price[i])


web = webdriver.Chrome()
c = '/Comments'
#C is really the uid list which will be put dynamically in he link
web.get(f'https://60e81f8ef6ac33a382dcb1c7--angry-gates-6a167a.netlify.app{c}')
# this part is to give time to log in, the link doesn't really matter it just opens up chrome
time.sleep(5)

esme_file = 'log.txt'

for i in range(len(uid)):
    try:

        web.get(f'https://60e81f8ef6ac33a382dcb1c7--angry-gates-6a167a.netlify.app{c}')

    
        
        bname = web.find_element_by_xpath('//*[@id="root"]/div/html/body/form/input[1]')
        bname.send_keys(name[i])
    
        bprice = web.find_element_by_xpath('//*[@id="root"]/div/html/body/form/textarea')
        bprice.send_keys(price[i])
    
    
    
        Submit = web.find_element_by_xpath('//*[@id="root"]/div/html/body/form/input[2]')
        Submit.click()
        
        with open(esme_file, 'a') as f:
            f.write(f'{uid[i]}     ')
            f.write('Successful\n')
    


    except NoSuchElementException:
        with open(esme_file, 'a') as f:
            f.write(f'{uid[i]}     ')
            f.write('f\n')
    
    
