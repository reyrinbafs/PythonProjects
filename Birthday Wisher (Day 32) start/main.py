import smtplib

my_email = "reyrinbaf@gmail.com"
password = "@Nik1411"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email ,to_addrs="tiwarinikhil808@gmail.com", msg="wassssup")
connection.close()

