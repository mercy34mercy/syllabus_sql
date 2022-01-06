import psycopg2


DATABASE_URL  = "postgres://hdskofuyufyqgx:18d75e06e7fd23852717b2f3903245d1b0691c56d8d5746fa66258e167f0019b@ec2-3-209-234-80.compute-1.amazonaws.com:5432/de5lc85kl2p0o"
DATABASE_URL2 = "postgres://qshfwxsvugxznm:8ad876169c16e56bc21620af32927b7710ae4623e5563c5e38ac28e157950a1b@ec2-34-206-245-175.compute-1.amazonaws.com:5432/dfk2litiovki4b"


def get_syllabus(data):
    #授業番号or授業名で検索するクエリ作成
    q_data = ""

    q_data += 'number like \'%' + data + "%\'"
    jsonify = ({
          "data":[]
        })
    a = "SELECT * FROM syllabus1 where number like '%" + data + "%'"
    b = "SELECT * FROM syllabus2 where number like '%" + data + "%'"
    jsonify = request_DB(jsonify, a,DATABASE_URL)
    jsonify = request_DB(jsonify,b,DATABASE_URL2)
    return jsonify




def request_DB(jsonify,q_data,DB_url):
    con = psycopg2.connect(DB_url, sslmode='require')
    cur = con.cursor()
    cur.execute(q_data)
    sql_datas = cur.fetchall()
    for sql_data in sql_datas:
        add_data = {
                "gakubu": sql_data[0],
                "url":sql_data[1],
                "number":sql_data[2],
                "gakki":sql_data[3],
                "yobi":sql_data[4],
                "campus":sql_data[5],
                "pro":sql_data[6],
                "lang":sql_data[7],
                "tani":sql_data[8]
        }
        jsonify["data"].append(add_data)
    return jsonify