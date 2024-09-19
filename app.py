from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import MySQLdb
import bcrypt
from datetime import timedelta
# pip install Flask-SQLAlchemyd
# pip install Flask Flask-JWT-Extended Flask-MySQLdb

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'repaso_web'

# Configuración de JWT
app.config['JWT_SECRET_KEY'] = 'super-secret' 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)

# Inicializar JWT y MySQL
jwt = JWTManager(app)

# Conexión a MySQL
db = MySQLdb.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    passwd=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)
cursor = db.cursor()
#Ruta para registrar
@app.route('/register', methods=['POST'])
def register():
    name = request.json.get('name')  # Recibir el nombre del usuario
    email = request.json.get('email')
    password = request.json.get('password')

    # Encriptar la contraseña
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        # Insertar el nuevo usuario con nombre, email y la contraseña encriptada
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_password))
        db.commit()
        return jsonify({"msg": "Usuario registrado exitosamente"}), 201
    except MySQLdb.IntegrityError as e:
        # Mostrar el error exacto si ocurre
        return jsonify({"msg": "Error al registrar el usuario", "error": str(e)}), 400


# Login del usuario
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    
    # Consulta para obtener el usuario
    cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
        # Generar un token JWT
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Credenciales incorrectas"}), 401

# Ruta protegida
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    # Obtener identidad del JWT
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)


# middleware = archivos filtrar peticiones
# rol, permisos, puerto, ip, dominio