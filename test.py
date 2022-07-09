import pymysql

conn = pymysql.connect(host="127.0.0.1", db="aadhaar_project", user="root", port=3306)
cur = conn.cursor()


#
# def check(search):
#     try:
#         stmt = "SELECT Aadhaar_Card_Number FROM userdb"
#         cur.execute(stmt)
#         data = cur.fetchall()
#         # print(data)
#         # data2 = []
#         # for i in range(len(data)):
#         #     data2.append(data[i][0])
#         # print(data2)
#         for i in range(len(data)):
#             if search == data[i][0]:
#                 print(True)
#                 return
#         print(False)
#     except Exception as e:
#         print(e)


#
#
# check("7845123265980")
#
# def update(Phone_No, Name, DOB, Gender, Photo, Address, Fingerprint, Aadhaar_Card_Number):
#     try:
#         stmt = "UPDATE userdb set Phone_No=%s,Name=%s,DOB=%s,Gender=%s,Photo=%s,Address=%s,Fingerprint=%s WHERE " \
#                "Aadhaar_Card_Number=%s"
#         val = (Phone_No, Name, DOB, Gender, Photo, Address, Fingerprint, Aadhaar_Card_Number)
#         cur.execute(stmt, val)
#         conn.commit()
#         print(cur.rowcount)
#         print("Successful")
#     except Exception as e:
#         print(e)
#
#
# update("9874561230", "Temp Check", "2012-04-30", "M", "PHOTO", "Mumbai", "Biometrics", "784512326599")

def select(search):
    try:
        cur.execute("SELECT * FROM userdb WHERE Aadhaar_Card_Number=%s", (search,))
        data = cur.fetchall()
        if len(data) > 0:
            data2 = data[0][1:]
            datadict = {}
            datadict[data[0][0]] = {x for x in data2}
            print(datadict)
        else:
            print(0)
    except Exception as e:
        print(e)


select("784512326598")
