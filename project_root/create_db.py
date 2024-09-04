from app import app, db, User

with app.app_context():
    db.create_all()
    
    # Verifique se o usuário admin já existe
    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        # Cria o usuário admin com a senha 'admin'
        admin_user = User(username='admin', password='admin')
        db.session.add(admin_user)
        db.session.commit()
        print("Usuário admin criado com sucesso.")
    else:
        print("Usuário admin já existe.")
