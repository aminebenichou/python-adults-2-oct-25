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
    values = tuple([f"{element['value']}" for element in elements])
    print(element_definitions)
    
    print(f"INSERT INTO {table_name} ({element_definitions}) VALUES ({values})")
    
    cursor.execute(f'''
        INSERT INTO {table_name} ({element_definitions}) VALUES {values}
    ''')


    conn.commit()


def retrieve_elements(table_name:str):
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    return data


def update_element(table_name:str, element):
    # element={
    #  'id':1, 'data':[{'name': 'title', 'value':'ashvdas'}, {'name': 'status', 'value':1}]
    # }

    element_id = element["id"]
    # {e['name']} = '{e['value']}'
    element_definitions = ", ".join([f"{f"{e['name']} = {e['value']}" if e['name']=='status' else f"{e['name']} = '{e['value']}'"}" for e in element['data']])
    print(element_definitions)
    cursor.execute(f'''
        UPDATE {table_name} SET {element_definitions} WHERE id={element_id}
        ''')
    
    conn.commit()