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
