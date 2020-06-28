import os
import pyodbc

batfile = open("C:\\Users\\asawant\\Documents\\bcp\\bcpout.bat","w+")
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=10.153.26.64;'
                      'Database=aqmbm;'
                      'UID=aqm;'
                      'PWD=Aspect123;')
cursor = conn.cursor()
cursor.execute('select distinct convert(date,starttime) from media_core where [mediastatusid]  between 1 and 3 AND [mediatypeid] IN ( 1, 2, 4, 3,6, 12 ) order by 1')
for row in cursor:
    frdate = row[0]
    todate = row[0] + ' 23:59:59.999'
    filename = 'C:\\Users\\asawant\\Documents\\bcp\\' +  frdate + '.csv'
    str = 'bcp "exec aqmbm.[dbo].[usp_GetAPIInteraction] \''  + frdate + '\' , \'' + todate + '\' " queryout ' + filename + ' -c -t, -U aqm -P Aspect123 -S 10.153.26.64'
    batfile.write(str + '\n')
    print(str)
    os.system(str)
batfile.close()
