from app import app, db
from app import User
from werkzeug.security import generate_password_hash

def add_admin_user():
    with app.app_context():
        admin_username = 'daniel'
        admin_password = '123'
        hashed_password = generate_password_hash(admin_password, method='pbkdf2:sha256')

        # Verifica se o usuário já existe
        user = User.query.filter_by(username=admin_username).first()
        if user:
            print(f"Usuário {admin_username} já existe.")
        else:
            # Cria um novo usuário admin
            new_user = User(username=admin_username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            print(f"Usuário {admin_username} criado com sucesso.")

if __name__ == '__main__':
    add_admin_user()
