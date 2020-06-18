import xlsxwriter
import psycopg2

wb = xlsxwriter.Workbook('test.xlsx') #создание книги
ws = wb.add_worksheet() # создание листа в книге

db = psycopg2.connect(
    database = 'rainbow_database',
    user = "unicorn_user",
    password = 'magical_password',
    host = '5.101.50.80',
    port = '5432'
)

print("The database is open!")

cur = db.cursor() #создание курсора
cur.execute(
"SELECT * FROM fssp FULL JOIN persons ON fssp.exe = persons.firstname")
res = cur.fetchall()

row = 0 # строка
col = 0 #столбец

for n in range(len(res)):
    for item in res[n]:
        ws.write(row, col, item)
        col += 1
        if col == len(res[n]):
            col = 0
            row += 1

print('The file is written!')

wb.close() # закрытие книги
db.close() # закрытие базы данных
