import pymysql

from fastapi import FastAPI

conn = pymysql.connect(host="127.0.0.1", db="aadhaar_project", user="root", port=3306)
cur = conn.cursor()

# new_reg("784512326599", "9874561230", "XYZ LMN", "2012-04-30", "M", "PHOTO", "Solapur", "Biometrics")

app = FastAPI()


@app.get("/new_reg")
def new_reg(Aadhaar_Card_Number, Phone_Number, Name, DOB, Gender, Photo, Address, Fingerprint):
    try:
        if len(Aadhaar_Card_Number) == 12 and Aadhaar_Card_Number.isdigit() and Phone_Number.isdigit() and len(
                Phone_Number) == 10:
            stmt = "INSERT INTO userdb VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            vals = (Aadhaar_Card_Number, Phone_Number, Name, DOB, Gender, Photo, Address, Fingerprint)
            cur.execute(stmt, vals)
            conn.commit()
            # return {"Code": 201}  # Data Accepted
            return 201  # Data Accepted
        else:
            # return {"Code": 400}  # Bad Request
            return 400  # Bad Request
    except Exception as e:
        msg = str(e)
        return {"Error": msg}


@app.get("/check")
def check(search):
    try:
        cur.execute("SELECT Aadhaar_Card_Number FROM userdb")
        data = cur.fetchall()
        for i in range(len(data)):
            if search == data[i][0]:
                return True
        return False
    except Exception as e:
        msg = str(e)
        return {"Error": msg}


@app.get("/update")
def update(Phone_No, Name, DOB, Gender, Photo, Address, Fingerprint, Aadhaar_Card_Number):
    try:
        stmt = "UPDATE userdb set Phone_No=%s,Name=%s,DOB=%s,Gender=%s,Photo=%s,Address=%s,Fingerprint=%s WHERE " \
               "Aadhaar_Card_Number=%s"
        val = (Phone_No, Name, DOB, Gender, Photo, Address, Fingerprint, Aadhaar_Card_Number)
        cur.execute(stmt, val)
        conn.commit()
        if cur.rowcount > 0:
            return 201
        else:
            return 500
    except Exception as e:
        msg = str(e)
        return {"Error": msg}


# @app.get("/get_data")
# def select(search):
#     try:
#         cur.execute("SELECT * FROM userdb WHERE Aadhaar_Card_Number=%s", (search,))
#         data = cur.fetchall()
#         if len(data) > 0:
#             data2 = data[0][1:]
#             datadict = {}
#             datadict[data[0][0]] = {x for x in data2}
#             return str(datadict)
#         else:
#             return 500
#     except Exception as e:
#         msg = str(e)
#         return {"Error": msg}
