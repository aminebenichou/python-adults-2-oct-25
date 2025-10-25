import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()


def create_table(table_name:str, columns:list):

    column_definitions = ", ".join([f"{col_name} {col_type}" for col_name, col_type in columns])
    
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            {column_definitions}
        )
    ''')

    conn.commit()


#CRUD: Create, Retreive, Update, Delete
def create_element(table_name:str, elements):

    element_definitions = ", ".join([f"{element['name']}" for element in elements])
    values = ", ".join([f"{element['value']}" for element in elements])
    print(element_definitions)
    
    print(f"INSERT INTO {table_name} ({element_definitions}) VALUES ({values})")
    
    cursor.execute(f'''
        INSERT INTO {table_name} ({element_definitions}) VALUES ({values})
    ''')


    conn.commit()
