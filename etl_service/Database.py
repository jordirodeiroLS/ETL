import sqlalchemy as db

from Cocktails import Cocktail
from typing import List, Dict

import mysql.connector
import json

class Database:

    def get_information_db_cocktails(self):
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="information"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM cocktails")

        row_headers=[x[0] for x in cursor.description]

        results = cursor.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(row_headers,result)))

        cursor.close()

        return json_data

    def get_information_db_ingredients(self):
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="information"
        )
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM ingredients")

        row_headers=[x[0] for x in cursor.description] #this will extract row headers

        results = cursor.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(row_headers,result)))

        cursor.close()

        return json_data

    def fill_db(self, data: List[Cocktail]) -> None:
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="information"
        )
        cursor = mydb.cursor()

        insert_stmt = (
            "INSERT INTO cocktails (idDrink, strDrink, strCategory, strIBA, strAlcoholic, strGlass, strImage, dateModified) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )

        for cocktail in data:
            data_insert = (cocktail.idDrink,cocktail.strDrink,cocktail.strCategory, cocktail.strIBA, cocktail.strAlcoholic, 
                cocktail.strGlass, cocktail.strImage, cocktail.dateModified)
            cursor.execute(insert_stmt, data_insert)

        mydb.commit()
        
        cursor.close()

        cursor = mydb.cursor()

        insert_stmt = (
            "INSERT INTO ingredients (idDrink, ingredient, quantity) "
            "VALUES (%s, %s, %s)"
        )

        for cocktail in data:
            for key, value in cocktail.ingredients.items():
                data_insert = (cocktail.idDrink,key,value)
                cursor.execute(insert_stmt, data_insert)

        mydb.commit()
        
        cursor.close()

    def first_init(self) -> bool:
        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="password"
        )
        cursor = mydb.cursor()

        cursor.execute("SHOW DATABASES;")
        databases = cursor.fetchall()

        for database in databases:
            if database[0] == "information":
                cursor.close()
                return False

        cursor.close()
        return True

    def connect_db(self) -> None:

        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="password"
        )
        cursor = mydb.cursor()

        #cursor.execute("DROP DATABASE IF EXISTS information")
        cursor.execute("CREATE DATABASE if not exists information")
        cursor.close()

        mydb = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="information"
        )
        cursor = mydb.cursor()

        #cursor.execute("DROP TABLE IF EXISTS cocktails")
        cursor.execute("CREATE TABLE if not exists cocktails (idDrink INT, strDrink VARCHAR(255), strCategory VARCHAR(255), strIBA VARCHAR(255), strAlcoholic VARCHAR(255), strGlass VARCHAR(255), strImage VARCHAR(255), dateModified DATE)")
        #cursor.execute("DROP TABLE IF EXISTS ingredients")
        cursor.execute("CREATE TABLE if not exists ingredients (idDrink INT, ingredient VARCHAR(255), quantity VARCHAR(255))")

        cursor.close()