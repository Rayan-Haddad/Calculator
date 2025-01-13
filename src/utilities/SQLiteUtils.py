import sqlite3 as sql
from rich import print

# connection = sql.connect("../../database/Definitions.db")
# cursor = connection.cursor()
cursor = "x"
connection = "x"
def recreate():
    cursor.execute("DROP definitions")
    cursor.execute("""CREATE TABEL definitions (
                   Name text
                   Description text
                   Rule text
                   Example text
    )""")
    data = [
        ("Factorial", 
         "A factorial is a mathematical operation that you write like this: n!. It represents the multiplication of all numbers between 1 and n.",
         "n! = n-1 * n-1 * ... * 1",
         "5! = 5 * 4 * 3 * 2 * 1 = 120"),
    ]
    cursor.execute("""
                   INSERT INTO definitions (?,?,?)
                   """, data)
    connection.commit()
    connection.close()

def addDefinition(Def_name: str, Def_description: str, Def_rule: str, Def_example: str):
    cursor.execute(f"INSERT INTO defintions ({Def_name}, {Def_description}, {Def_rule}, {Def_example})")
    print(f"Succesfully added {Def_name} with this info:\n\tDescription: {Def_description}\n\tRule: {Def_rule}\n\tExample: {Def_example}")
    connection.commit()
    connection.close()

def ChangeDefinition(Element_name: str, New_definition: str):
    connection.commit()
    connection.close()

def deleteDefinition(Def_name):
    cursor.execute(f"DELETE FROM defintions WHERE Name = {Def_name}")
    print(f"Succesfully deleted {Def_name}")
    connection.commit()
    connection.close()

def showDefinition(Def_name):

    connection.close()
