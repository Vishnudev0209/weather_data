import pymysql
import pandas as pd
import matplotlib.pyplot as plt
mydb=pymysql.connect(
    user="root",
    host="localhost",
    password="123456",
    port=3306)
print("connected",mydb)