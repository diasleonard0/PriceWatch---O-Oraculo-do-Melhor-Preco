import sqlite3
import os

class DataStorage():

    def __init__(self):
        self.__db = None

    def __connectToDatabase(self):
        self.__db = sqlite3.connect('data.db')

    def createTheTable(self):
        self.__connectToDatabase()
        cursor = self.__db.cursor()

        cursor.execute('CREATE TABLE historico (name TEXT PRIMARY KEY, url TEXT, price TEXT)')

        self.__db.commit()
        self.__db.close()

    def enterData(self, nome, url, price):
        self.__connectToDatabase()
        cursor = self.__db.cursor()
        
        cursor.execute('INSERT INTO historico (name, url, price) VALUES (?, ?, ?)', (nome, url, price))

        self.__db.commit()
        self.__db.close()

    def removeData(self, name):
        self.__connectToDatabase()
        cursor = self.__db.cursor()

        cursor.execute("DELETE FROM historico WHERE name = ?", (name,))

        self.__db.commit()
        self.__db.close()

    def viewData(self, name):
        self.__connectToDatabase()
        cursor = self.__db.cursor()

        cursor.execute("SELECT * FROM historico WHERE name = ?", (name,))

        rows = cursor.fetchall()

        if not rows:
            print("Nenhum dado encontrado.")
        else:
            for row in rows:
                print(f"Nome: {row[0]}\nURL: {row[1]}\nPreço Desejado: {row[2]}")

    def getUrl(self, name):
        self.__connectToDatabase()
        cursor = self.__db.cursor()

        cursor.execute("SELECT * FROM historico WHERE name = ?", (name,))

        row = cursor.fetchone()

        if row is None:
            print("Nenhum dado encontrado!")
        else:
            return row[1]
        
    def getPrice(self, name):
        self.__connectToDatabase()
        cursor = self.__db.cursor()

        cursor.execute("SELECT * FROM historico WHERE name = ?", (name,))

        row = cursor.fetchone()

        if row is None:
            print("Nenhum dado encontrado!")
        else:
            return row[2]

    def checkDatabase(self):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        parentDir = os.path.dirname(currentDir)
        dbPath = os.path.join(parentDir, 'data.db')

        if os.path.isfile(dbPath):
           return True
        else:
            return False
