import os
import bcp
#C://Users//asawant//Documents//bcp
conn = bcp.Connection(host='10.153.26.64', driver='mssql', username='aqm', password='Aspect123')
my_bcp = bcp.BCP(conn)
root_dir = os.path.dirname(os.path.abspath(__file__))
file = bcp.DataFile(file_path=b'C://Users//asawant//Documents//bcp//file.csv', delimiter=',')
my_bcp.dump(query='select * from sys.tables', output_file=file)
