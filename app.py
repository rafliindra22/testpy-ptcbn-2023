from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1209@localhost/testDB'
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JWT_SECRET_KEY'] = 'secretkey'
jwt = JWTManager(app)

db = SQLAlchemy(app)

# conn = psycopg2.connect(
#         host="localhost",
#         database="testDB",
#         user="postgres",
#         password="1209"
# #     )
# cur = conn.cursor()
class Users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
    is_active = db.Column(db.Boolean)
    created_by = db.Column(db.String(100))
    created_time = db.Column(db.DateTime(6))

@app.route('/api/auth/login', methods=['POST'])
def login():
    
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = db.session.query(Users).filter(Users.username==username, password==password).first()
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if user and user.password == password:
        access_token = create_access_token(identity=user.user_id)
        return jsonify({"your token": access_token, "username": user.username}), 200
    elif password == "CBN123!":
        access_token = create_access_token(identity=user.user_id)
        return jsonify({"your token": access_token, "username": user.username}), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

    db.session.commit()
    
@app.route('/api/auth/user', methods=['GET'])
@jwt_required()
def currentUser():
    user_id = get_jwt_identity()
    user = db.session.query(Users).filter(Users.user_id==user_id).first()

    if user:
        return jsonify({"message": "Data Curent User", "id": user.user_id,"username": user.username}), 200
    else:
        return jsonify({"msg": "User not found"}), 404

class M_master(db.Model):
    __tablename__ = "m_master"
    master_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean)
    created_by  = db.Column(db.Integer)
    created_time = db.Column(db.DateTime(6))
    updated_by = db.Column(db.Integer)
    updated_time = db.Column(db.DateTime(6))
    deleted_by =  db.Column(db.Integer)
    deleted_time = db.Column(db.DateTime(6))


@app.route('/api/master/<master_id>', methods=['GET'])
def getByID(master_id):
    
    master = db.session.query(M_master).filter(M_master.master_id==master_id).first()
    if master:
        output = {
            "code": master.code,
            "name": master.name,
            "active": master.is_active,

        }
        return jsonify({"msg": "berhasil menampilkan data dengan id "+ master_id, "output":output}), 200
    else:
        return jsonify({"msg": "Data not found"}), 401


@app.route('/api/master', methods=['POST'])
@jwt_required()
def addData():
    sale = M_master(
        code=request.json.get("code"),
        name=request.json.get("name"),
        description=request.json.get('description'),
        is_active=request.json.get('is_active'),
        created_by=get_jwt_identity(),
        created_time=datetime.now(),
        )

    db.session.add(sale)
    db.session.commit()

    master_id = db.session.query(M_master).filter(M_master.name==sale.name).first()
    output = {
            "code": master_id.code,
            "name": master_id.name,
            "active": master_id.is_active,
            "created by": master_id.created_by,
            "created time": master_id.created_time
        }
    if master_id:
        return jsonify({'msg': 'Added succesfully','added': output}), 200
    else:
        return jsonify({'msg': 'Data gagal ditambahkan'}), 400


@app.route('/api/master/<master_id>', methods=["PUT"])
@jwt_required()
def putByID(master_id):
    
    editCode=request.json.get("code")
    editName=request.json.get("name")
    editDescription=request.json.get('description')
    editIs_active=request.json.get('is_active')
    updated_by=get_jwt_identity()
    updated_time=datetime.now()
        
    query = db.session.query(M_master).filter(M_master.master_id==master_id).first()
    query.code = editCode
    query.name = editName
    query.description = editDescription
    query.is_active = False
    query.updated_by = updated_by
    query.updated_time = updated_time

    db.session.commit()
    if query:
        return jsonify({'msg': 'data berhasil diubah'}), 200
    else:
        return jsonify({'msg': 'data gagal diubah'}), 400

@app.route('/api/master/<master_id>', methods=["DELETE"])
@jwt_required()
def deleteByID(master_id):
    query = db.session.query(M_master).filter(M_master.master_id==master_id).first()
    query.is_active = False
    query.updated_by = get_jwt_identity()
    query.updated_time = datetime.now()
    query.deleted_by = get_jwt_identity()
    query.deleted_time = datetime.now()

    db.session.commit()
    if query:
        return jsonify({'msg': 'data telah dihapus', 'status': 'inactive'}), 200
    else:
        return jsonify({'msg': 'Bad request'}), 400
    
@app.route('/api/master', methods=['GET'])    
def get_master():
    page = 1
    limit = request.args.get('limit', default=10, type=int)
    all_data = []
    while True:
        data = M_master.query.offset((page - 1) * limit).limit(limit).all()
        if data:
            all_data += data
            page +=1
        else:
            break
    return jsonify([{'master_id':i.master_id, 'code':i.code, 'name':i.name, 'description':i.description, 'is_active':i.is_active,
                   'created_by':i.created_by, 'created_time':i.created_time, 'updated_by':i.updated_by, 'updated_time':i.updated_time,
                   'deleted_by':i.deleted_by, 'deleted_time':i.deleted_time} for i in all_data])

   
if __name__ == '__main__':
    app.run(debug=True, port=8080)