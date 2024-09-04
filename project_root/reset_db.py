import os
from app import app, db

def reset_database():
    # Remover o banco de dados existente se ele existir
    db_path = 'site.db'
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Banco de dados {db_path} removido com sucesso.")

    # Criar um novo banco de dados
    with app.app_context():
        db.create_all()
        print("Novo banco de dados criado com sucesso.")

if __name__ == '__main__':
    reset_database()
