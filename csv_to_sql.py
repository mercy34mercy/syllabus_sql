
import psycopg2
import csv

DATABASE_URL = "postgres://hdskofuyufyqgx:18d75e06e7fd23852717b2f3903245d1b0691c56d8d5746fa66258e167f0019b@ec2-3-209-234-80.compute-1.amazonaws.com:5432/de5lc85kl2p0o"
DATABASE_URL2 = "postgres://qshfwxsvugxznm:8ad876169c16e56bc21620af32927b7710ae4623e5563c5e38ac28e157950a1b@ec2-34-206-245-175.compute-1.amazonaws.com:5432/dfk2litiovki4b"


def to_DB():
    url = "aki1.csv"

    con = psycopg2.connect(DATABASE_URL2, sslmode='require')
    cur = con.cursor()

    csvfile = open("aki2.csv")
    csv_data = csv.reader(csvfile) # Read the csv
    i = 0

    for rows in csv_data: # Iterate through csv
        cur.execute("INSERT INTO syllabus2(gakubu,url,number,gakki,yobi,campus,pro,lang,tani) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",rows)
        print(i)
        i+=1
    con.commit()

to_DB()