import wget
import os
from zipfile import ZipFile
import shutil
import pandas as pd
import csv



dirlist = os.listdir()
print(dirlist)
dirlist.sort()

if 'query_data.zip' in dirlist:
    os.remove('query_data.zip')
if 'query_data' in dirlist:
    shutil.rmtree('query_data')

url = 'https://api.unhcr.org/population/v1/population/?limit=20&dataset=population&displayType=totals&columns%5B%5D=refugees&columns%5B%5D=asylum_seekers&columns%5B%5D=idps&columns%5B%5D=vda&columns%5B%5D=stateless&columns%5B%5D=hst&columns%5B%5D=ooc&yearFrom=1951&yearTo=2021&coo=UKR&coa_all=true&sort%5Byear%5D=asc&download=true#_ga=2.12817008.611515465.1665032592-1779653406.1664862807'
wget.download(url)

with ZipFile('C:\\Users\Ragavan\OneDrive\Desktop\Capstone project\query_data.zip') as zobject:
    zobject.extract('population.csv',path = 'C:\\Users\Ragavan\OneDrive\Desktop\Capstone project\query_data')
zobject.close()

dirlist = os.listdir()
dirlist.sort()
print(dirlist)

with open('C:\\Users\Ragavan\OneDrive\Desktop\Capstone project\query_data\population.csv', 'r') as file:
    updatedlist = []
    my_reader = csv.reader(file, delimiter=',')
    tempcsv = list(my_reader)
    for i in range(14,len(tempcsv)):
        updatedlist.append(tempcsv[i])
        

with open('C:\\Users\Ragavan\OneDrive\Desktop\Capstone project\query_data\population.csv', 'w') as file:
    Writer = csv.writer(file)
    Writer.writerows(updatedlist)
    
df = pd.read_csv('C:\\Users\Ragavan\OneDrive\Desktop\Capstone project\query_data\population.csv')
print(df)