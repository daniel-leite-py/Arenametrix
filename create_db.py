import sqlite3

CreateDataBase = sqlite3.connect('MyDataBase.db')

QueryCurs = CreateDataBase.cursor()


def CreateTable():
    QueryCurs.execute('''CREATE TABLE Peugeots
    (id INTEGER PRIMARY KEY, Nom TEXT,Longitude FLOAT,Latitude FLOAT)''')


def AddEntry(Nom, Longitude, Latitude):
    QueryCurs.execute('''INSERT INTO Peugeots (Nom,Longitude,Latitude)
    VALUES (?,?,?)''', (Nom, Longitude, Latitude))


CreateTable()
