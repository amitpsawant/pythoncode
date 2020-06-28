import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.;'
                      'Database=aqm;'
                      'UID=aqm;'
                      'PWD=Aspect123;')
cursor = conn.cursor()
cursor.execute('select distinct convert(date,starttime) from media_core ')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\crisilon_Cobro_12_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\crisilon.BACNET.CORP.REDBAC.com\\CobroAqmRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\crisilon_Cobro_12_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm..sg8')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\crisilon_Comercial_8_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\crisilon.BACNET.CORP.REDBAC.com\\ComercialAqmRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\crisilon_Comercial_8_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 3')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\GUALOCUIPQM01_Ventas_3_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\GUALOCUIPQM01\\VentasAQM\\VentasAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\GUALOCUIPQM01_Ventas_3_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 1')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\GUALOCUIPQM01_Cobros_1_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\GUALOCUIPQM01\\CobrosAQM\\CobrosAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\GUALOCUIPQM01_Cobros_1_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 9')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\Hncorisilonuip1_Ventas_9_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\Hncorisilonuip1\\HNCOMUIPQM\\RecordingStorage\\VentasAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\Hncorisilonuip1_Ventas_9_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 10')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\SVCOMUIPQM01_Ventas_10_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\SVCOMUIPQM01\\VentasAQM\\VentasAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\SVCOMUIPQM01_VentasA_10_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 11')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\SVCOMUIPQM01_Cobros_11_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\SVCOMUIPQM01\\CobrosAQM\\CobrosAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\SVCOMUIPQM01_Cobros_11_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 2')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\PANLOCVUIPQMM01_Cobros_2_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\PANLOCVUIPQMM01\\CobrosAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\PANLOCVUIPQMM01_Cobros_2_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 6')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\Hncorisilonuip1_Cobros_6_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\Hncorisilonuip1\\HNCOMUIPQM\\RecordingStorage\\CobrosAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\Hncorisilonuip1_Cobros_6_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 5')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\PANLOCVUIPQMM01_Ventas_5_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\PANLOCVUIPQMM01\\VentasAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\PANLOCVUIPQMM01_Ventas_5_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 4')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\NICLOCUIP126_Cobros_4_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\NICLOCUIP126\\CobrosAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\NICLOCUIP126_Cobros_4_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

cursor.execute('SELECT audiofilename FROM aqm_current..sgother where audiostoragegroupid = 7')
ctr=1
filectr = 2
batfile = open("C:\\Users\\asawant\\Documents\\42584\\NICLOCUIP126_Ventas_7_1.bat","w+")
for row in cursor:
    dayname = row[0]
    batfile.write('del \\\\NICLOCUIP126\\VentasAQMRecordingsArchive\\' + dayname[:9] + dayname +  '\n')
    ctr = ctr + 1
    if ctr % 100000 == 0:
        batfile.close()
        batfile = open('C:\\Users\\asawant\\Documents\\42584\\NICLOCUIP126_Ventas_7_' + str(filectr) + '.bat','w+')
        filectr = filectr + 1
batfile.close()

