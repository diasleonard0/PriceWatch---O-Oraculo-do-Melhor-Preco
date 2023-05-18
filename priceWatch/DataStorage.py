import sqlite3

class DataStorage():

    def __init__(self):
        self.__db = None

    def connectToDatabase(self):
        self.__db = sqlite3.connect('data.db')

    def createTheTable(self):
        cursor = self.__db.cursor()

        cursor.execute('CREATE TABLE historico (name TEXT PRIMARY KEY, url TEXT, price TEXT)')

        self.__db.commit()
        self.__db.close()

    def enterData(self, nome, url, price):
        self.connectToDatabase()
        cursor = self.__db.cursor()
        cursor.execute('INSERT INTO historico (name, url, price) VALUES (?, ?, ?)', (nome, url, price))
