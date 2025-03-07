# instalar con: python3 -m pip install mysql-connector-python
import mysql.connector
from config import DB_CONFIG_SHARD_1
from config import DB_CONFIG_SHARD_2

shard_connections = {
    "shard1": mysql.connector.connect(
        **DB_CONFIG_SHARD_1
    ),
    "shard2": mysql.connector.connect(
        **DB_CONFIG_SHARD_2
    ),
}

def get_shard(user_email):
    return "shard1" if user_email % 2 != 0 else "shard2"

def insert_user(name: str, email: str):
    shard = get_shard(len(email))
    conn = shard_connections[shard]
    cursor = conn.cursor()
    
    query = "INSERT INTO users (name, email) VALUES (%s, %s);"
    cursor.execute(query, (name, email))
    conn.commit()
    print(f"Usuario {name} insertado en {shard}")

def get_user(email):
    shard = get_shard(len(email))
    conn = shard_connections[shard]
    cursor = conn.cursor()
    query = "SELECT id, name, email FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()
    return result

#insert_user("Lucas", "lucas9@example.com")
#insert_user("Paola", "paola12@example.com")

print(get_user("lucas@example.com"))  
print(get_user("lucas6@example.com"))  
print(get_user("lucas9@example.com"))  

