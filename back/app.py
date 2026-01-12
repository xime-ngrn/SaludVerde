import os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import MySQLdb.cursors

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

load_dotenv()

# Configuración de la base de datos MySQL
app.config['Host'] = os.environ.get('MYSQL_HOST')
app.config['Username'] = os.environ.get('MYSQL_USER')
app.config['Password'] = os.environ.get('MYSQL_PASSWORD')
app.config['Database'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)
# Inicio de prueba al backend
@app.route('/')
def index():
    # Esto sirve el archivo principal de tu Frontend
    return render_template("index.html")

# Inicio de prueba a la base de datos
@app.route('/db-test')
def test_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        cur.close()
        return jsonify({
            "status": "online",
            "mysql_version": version[0]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Usuario - Login y Registro
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password_candidata = data.get('password')

    if not username or not password_candidata:
        return jsonify({"success": False, "message": "Faltan credenciales"}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT nombres, username, contrasena FROM Usuario WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()

    if user:
        nombres = user[0]
        username_db = user[1]
        password_encriptada_db = user[2]

        if check_password_hash(password_encriptada_db, password_candidata):
            return jsonify({
                "success": True,
                "message": "Login exitoso",
                "user": {"nombres": nombres, "username": username_db}
            }), 200
    
    return jsonify({"success": False, "message": "Usuario o contraseña incorrectos"}), 401

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    required_fields = ['name', 'lastname', 'age', 'username', 'email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    hashed_password = generate_password_hash(data['password'])
    
    try:
        cur = mysql.connection.cursor()
        
        query = """
            INSERT INTO Usuario 
            (nombres, apellidos, edad, vocacion, username, email, contrasena, fecha_registro) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        values = (
            data['name'], 
            data['lastname'], 
            data.get('age'), 
            data.get('vocacion', 'No especificada'),
            data['username'], 
            data['email'], 
            hashed_password, 
            datetime.now()
        )
        
        cur.execute(query, values)
        mysql.connection.commit()
        cur.close()

        return jsonify({"success": True, "message": "Usuario registrado con éxito"}), 201

    except MySQLdb.IntegrityError as e:
        return jsonify({"error": "El usuario o correo ya existe"}), 409
    except Exception as e:
        return jsonify({"error": f"Error en el servidor: {str(e)}"}), 500
    
@app.route('/usuario', methods=['GET'])
def get_usuario():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Falta el parámetro username"}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT nombres, apellidos, edad, vocacion, username, email, fecha_registro FROM Usuario WHERE username = %s", (username,))
    user_data = cur.fetchone()
    cur.close()

    if user_data:
        return jsonify({
            "nombre": user_data[0],
            "apellido": user_data[1],
            "edad": user_data[2],
            "vocacion": user_data[3],
            "username": user_data[4],
            "email": user_data[5],
            "fechaRegistro": user_data[6]
        }), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
@app.route('/update_usuario', methods=['PUT'])
def update_usuario():
    data = request.get_json()
    username = data.get('username')
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    edad = data.get('edad')
    vocacion = data.get('vocacion')
    email = data.get('email')

    try:
        cur = mysql.connection.cursor()
        query = """
            UPDATE Usuario 
            SET nombres=%s, apellidos=%s, edad=%s, vocacion=%s, email=%s 
            WHERE username=%s
        """
        cur.execute(query, (nombre, apellido, edad, vocacion, email, username))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({"success": True, "message": "Actualizado correctamente"}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# REGISTRO CONTABLE - OBTENER CATEGORÍAS
@app.route('/categorias', methods=['GET'])
def categorias():
    tipo = request.args.get('tipo')
    cur = mysql.connection.cursor()
    if tipo == 'ingreso':
        cur.execute("SELECT id_cati, Titulo FROM Cat_Ingresos")
    elif tipo == 'gasto':
        cur.execute("SELECT id_catg, Titulo FROM Cat_Gastos")
    else:
        return jsonify({"success": False, "message": "No se pudieron obtener las categorías"}), 401
    
    categorias = cur.fetchall()
    cur.close()
    return jsonify({"categorias": categorias})

@app.route('/obtenerReportes', methods=['GET'])
def obtenerReportes():
    username = request.args.get('username')
    cur = mysql.connection.cursor()
    
    # 🔧 Asegúrate de que 'Username' coincida con tu tabla Usuario
    cur.execute("SELECT Id_usuario FROM Usuario WHERE username = %s", (username,))
    usuario = cur.fetchone()
    
    if not usuario:
        cur.close()
        return jsonify({"success": False, "message": "Usuario no encontrado"}), 404
    
    id_usuario = usuario[0]

    # 🔧 Agregamos un try-except para ver errores específicos en la consola de Python
    try:
        query = """
            SELECT 
                R.Id_reporte,
                R.Nombre,
                COALESCE(SUM(CASE WHEN Reg.Tipo_de_movimiento = 0 THEN Reg.Cantidad ELSE 0 END), 0) as total_ingresos,
                COALESCE(SUM(CASE WHEN Reg.Tipo_de_movimiento = 1 THEN Reg.Cantidad ELSE 0 END), 0) as total_gastos
            FROM Reporte R
            LEFT JOIN Registro Reg ON R.Id_reporte = Reg.Id_reporte
            WHERE R.Id_usuario = %s
            GROUP BY R.Id_reporte, R.Nombre
            ORDER BY R.Id_reporte DESC
        """
        cur.execute(query, (id_usuario,))
        reportes = cur.fetchall()
        cur.close()

        reportes_list = [
            {
                "Id_reporte": r[0], 
                "Nombre": r[1],
                "total_ingresos": float(r[2]),
                "total_gastos": float(r[3])
            } for r in reportes
        ]
        return jsonify({"success": True, "reportes": reportes_list}), 200

    except Exception as e:
        print(f"Error en SQL obtenerReportes: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/obtenerDetallesReporte', methods=['GET'])
def obtenerDetallesReporte():
    id_reporte = request.args.get('id')
    
    if not id_reporte:
        return jsonify({"success": False, "message": "Falta el parámetro id"}), 400
    
    try:
        cur = mysql.connection.cursor()
        
        query = """
            SELECT 
                Referencia as titulo,
                CASE WHEN Tipo_de_movimiento = 0 THEN Cantidad ELSE NULL END as ingreso,
                CASE WHEN Tipo_de_movimiento = 1 THEN Cantidad ELSE NULL END as gasto,
                Fecha_de_registro
            FROM Registro
            WHERE Id_reporte = %s
            ORDER BY Fecha_de_registro DESC
        """
        cur.execute(query, (id_reporte,))
        registros = cur.fetchall()
        cur.close()
        
        detalles = [
            {
                "titulo": r[0],
                "ingreso": float(r[1]) if r[1] is not None else None,
                "gasto": float(r[2]) if r[2] is not None else None,
                "fecha": r[3].strftime('%Y-%m-%d') if r[3] else None
            } for r in registros
        ]
        
        return jsonify(detalles), 200
        
    except Exception as e:
        print(f"Error al obtener detalles: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/agregarRegistroContable', methods=['POST'])
def agregarRegistroContable():
    data = request.get_json()
    
    required_fields = ['username', 'fecha', 'tipo', 'monto', 'titulo']
    if not all(field in data for field in required_fields):
        return jsonify({"success": False, "message": "Faltan campos obligatorios"}), 400
    
    try:
        cur = mysql.connection.cursor()
        
        # Obtener ID del usuario
        cur.execute("SELECT Id_usuario FROM Usuario WHERE Username = %s", (data['username'],))
        usuario = cur.fetchone()
        if not usuario:
            return jsonify({"success": False, "message": "Usuario no encontrado"}), 404
        id_usuario = usuario[0]

        # Manejo de Reporte
        id_reporte = data.get('id_reporte')
        if not id_reporte:
            fecha_dt = datetime.strptime(data['fecha'], '%Y-%m-%d')
            nombre_reporte = fecha_dt.strftime('Reporte %m-%Y')
            
            cur.execute("SELECT Id_reporte FROM Reporte WHERE Id_usuario = %s AND Nombre = %s", (id_usuario, nombre_reporte))
            reporte_existente = cur.fetchone()
            
            if reporte_existente:
                id_reporte = reporte_existente[0]
            else:
                cur.execute("INSERT INTO Reporte (Id_usuario, Nombre) VALUES (%s, %s)", (id_usuario, nombre_reporte))
                mysql.connection.commit()
                id_reporte = cur.lastrowid

        id_cat_ingreso = None
        id_cat_gasto = None
        tipo = int(data['tipo'])
        id_cat_seleccionada = data.get('id_categoria')

        if tipo == 0:  # <--- CAMBIO: Si es 0 es INGRESO
            id_cat_ingreso = id_cat_seleccionada
            id_cat_gasto = None
        else:          # <--- Si es 1 es GASTO
            id_cat_gasto = id_cat_seleccionada
            id_cat_ingreso = None

        # La inserción usa el 'tipo' tal cual llega de Vue
        query_registro = """
            INSERT INTO Registro 
            (Id_reporte, Fecha_de_registro, Tipo_de_movimiento, Cantidad, Referencia, Descripcion, Id_cat_ingreso, Id_cat_gasto) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
        values_registro = (
            id_reporte, data['fecha'], tipo, float(data['monto']),
            data['titulo'], data.get('descripcion', ''), id_cat_ingreso, id_cat_gasto
        )
        
        cur.execute(query_registro, values_registro)
        mysql.connection.commit()
        cur.close()

        return jsonify({"success": True, "message": "Registro guardado correctamente"}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route('/crearReporte', methods=['POST'])
def crearReporte():
    data = request.get_json()
    
    if not data.get('username') or not data.get('nombre'):
        return jsonify({"success": False, "message": "Faltan campos obligatorios"}), 400
    
    try:
        cur = mysql.connection.cursor()
        
        # Obtener ID del usuario
        cur.execute("SELECT Id_usuario FROM Usuario WHERE Username = %s", (data['username'],))
        usuario = cur.fetchone()
        if not usuario:
            return jsonify({"success": False, "message": "Usuario no encontrado"}), 404
        id_usuario = usuario[0]
        
        # Verificar si ya existe un reporte con ese nombre
        cur.execute("SELECT Id_reporte FROM Reporte WHERE Id_usuario = %s AND Nombre = %s", 
                   (id_usuario, data['nombre']))
        if cur.fetchone():
            return jsonify({"success": False, "message": "Ya existe un reporte con ese nombre"}), 409
        
        # Crear el reporte
        cur.execute("INSERT INTO Reporte (Id_usuario, Nombre) VALUES (%s, %s)", 
                   (id_usuario, data['nombre']))
        mysql.connection.commit()
        id_reporte = cur.lastrowid
        cur.close()
        
        return jsonify({
            "success": True, 
            "message": "Reporte creado exitosamente",
            "id_reporte": id_reporte
        }), 201
        
    except Exception as e:
        print(f"Error al crear reporte: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500
    
# Metas de Ahorro
@app.route('/agregarMeta', methods=['POST'])
def agregar_meta():
    data = request.get_json()
    try:
        cur = mysql.connection.cursor()
        # Obtener ID de usuario
        cur.execute("SELECT Id_usuario FROM Usuario WHERE Username = %s", (data['username'],))
        id_usuario = cur.fetchone()[0]

        query = """
            INSERT INTO Metas (Id_usuario, Objetivo, Monto_final, Fecha_de_inicio, 
                              Fecha_de_conclusion, Cantidades_periodicas, Monto_actual, Progreso)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        # Calculamos una cantidad periódica sugerida (opcional)
        valores = (
            id_usuario, data['title'], data['ahorro'], data['inicio'], 
            data['fin'], 0, 0, 0
        )
        cur.execute(query, valores)
        mysql.connection.commit()
        cur.close()
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/obtenerMetas', methods=['GET'])
def obtener_metas():
    username = request.args.get('username')
    cur = mysql.connection.cursor()
    # Importante: Usamos alias (AS) para que el JSON sea fácil de leer en Vue
    query = """
        SELECT Id_meta, Objetivo, Monto_final, Fecha_de_inicio, 
               Fecha_de_conclusion, Monto_actual, Progreso
        FROM Metas m
        JOIN Usuario u ON m.Id_usuario = u.Id_usuario
        WHERE u.Username = %s
    """
    cur.execute(query, (username,))
    rows = cur.fetchall()
    metas = []
    for r in rows:
        metas.append({
            "idMeta": r[0],
            "title": r[1],
            "ahorro": float(r[2]),
            "inicio": r[3].strftime('%Y-%m-%d'),
            "fin": r[4].strftime('%Y-%m-%d'),
            "progreso": float(r[5] or 0) # Monto_actual
        })
    cur.close()
    return jsonify(metas)

@app.route('/depositarMeta', methods=['POST'])
def depositar_meta():
    data = request.get_json()
    id_meta = data.get('id_meta')
    monto = data.get('monto')
    
    if not id_meta or not monto:
        return jsonify({"success": False, "error": "Datos incompletos"}), 400

    try:
        cur = mysql.connection.cursor()
        # 1. Registrar depósito
        cur.execute("INSERT INTO Depositos (Id_meta, Fecha, Monto) VALUES (%s, %s, %s)", 
                   (id_meta, datetime.now(), monto))
        
        # 2. Actualizar Meta
        cur.execute("SELECT Monto_final, Monto_actual FROM Metas WHERE Id_meta = %s", (id_meta,))
        meta = cur.fetchone()
        nuevo_monto = float(meta[1] or 0) + float(monto)
        nuevo_progreso = int((nuevo_monto / float(meta[0])) * 100)
        
        cur.execute("UPDATE Metas SET Monto_actual = %s, Progreso = %s WHERE Id_meta = %s",
                   (nuevo_monto, nuevo_progreso, id_meta))
        
        mysql.connection.commit()
        cur.close()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    
@app.route('/obtenerEstadisticas')
def obtener_estadisticas():
    username = request.args.get('username')
    try:
        cur = mysql.connection.cursor()

        # 1. INGRESOS POR CATEGORÍA (Usando relación directa)
        query_ingresos = """
            SELECT ci.Titulo, SUM(r.Cantidad)
            FROM Registro r
            JOIN Cat_Ingresos ci ON r.Id_cat_ingreso = ci.Id_cati
            JOIN Reporte rep ON r.Id_reporte = rep.Id_reporte
            JOIN Usuario u ON rep.Id_usuario = u.Id_usuario
            WHERE u.Username = %s AND r.Tipo_de_movimiento = 0
            GROUP BY ci.Id_cati
        """
        cur.execute(query_ingresos, (username,))
        res_ingresos = cur.fetchall()

        # 2. PROGRESO DE METAS
        query_metas = """
            SELECT Objetivo, IFNULL(Monto_actual, 0), Monto_final 
            FROM Metas m
            JOIN Usuario u ON m.Id_usuario = u.Id_usuario
            WHERE u.Username = %s
        """
        cur.execute(query_metas, (username,))
        res_metas = cur.fetchall()

        # 3. HISTÓRICO DE GASTOS (Últimos 6 meses)
        query_gastos_mes = """
            SELECT DATE_FORMAT(Fecha_de_registro, '%%Y-%%m') as mes, SUM(Cantidad)
            FROM Registro r
            JOIN Reporte rep ON r.Id_reporte = rep.Id_reporte
            JOIN Usuario u ON rep.Id_usuario = u.Id_usuario
            WHERE u.Username = %s AND r.Tipo_de_movimiento = 1
            GROUP BY mes ORDER BY mes ASC LIMIT 6
        """
        cur.execute(query_gastos_mes, (username,))
        res_gastos_mes = cur.fetchall()

        # 4. GASTOS POR CATEGORÍA (Usando relación directa)
        query_gastos_cat = """
            SELECT cg.Titulo, SUM(r.Cantidad)
            FROM Registro r
            JOIN Cat_Gastos cg ON r.Id_cat_gasto = cg.Id_catg
            JOIN Reporte rep ON r.Id_reporte = rep.Id_reporte
            JOIN Usuario u ON rep.Id_usuario = u.Id_usuario
            WHERE u.Username = %s AND r.Tipo_de_movimiento = 1
            GROUP BY cg.Id_catg
        """
        cur.execute(query_gastos_cat, (username,))
        res_gastos_cat = cur.fetchall()

        # 5. COMPARATIVA MENSUAL (Corregido: 0 Ingreso, 1 Gasto)
        query_comparativa = """
            SELECT 
                rep.Nombre,
                SUM(CASE WHEN r.Tipo_de_movimiento = 0 THEN r.Cantidad ELSE 0 END) as ingresos,
                SUM(CASE WHEN r.Tipo_de_movimiento = 1 THEN r.Cantidad ELSE 0 END) as gastos
            FROM Reporte rep
            JOIN Usuario u ON rep.Id_usuario = u.Id_usuario
            LEFT JOIN Registro r ON rep.Id_reporte = r.Id_reporte
            WHERE u.Username = %s
            GROUP BY rep.Id_reporte, rep.Nombre
            ORDER BY rep.Id_reporte DESC LIMIT 5
        """
        cur.execute(query_comparativa, (username,))
        res_comparativa = cur.fetchall()

        cur.close()

        return jsonify({
            "ingresosPorCategoria": {
                "labels": [str(i[0]) for i in res_ingresos],
                "values": [float(i[1]) for i in res_ingresos]
            },
            "progresoMetas": [
                {"objetivo": m[0], "actual": float(m[1]), "faltante": float(max(0, m[2]-m[1]))} 
                for m in res_metas
            ],
            "historicoGastos": {
                "meses": [str(g[0]) for g in res_gastos_mes],
                "montos": [float(g[1]) for g in res_gastos_mes]
            },
            "gastosPorCategoria": {
                "labels": [str(g[0]) for g in res_gastos_cat],
                "values": [float(g[1]) for g in res_gastos_cat]
            },
            "comparativaMensual": {
                "nombres": [str(c[0]) for c in reversed(res_comparativa)],
                "ingresos": [float(c[1]) for c in reversed(res_comparativa)],
                "gastos": [float(c[2]) for c in reversed(res_comparativa)]
            },
            "distribucionRadar": {
            "labels": [str(g[0]) for g in res_gastos_cat],
            "values": [float(g[1]) for g in res_gastos_cat]
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)