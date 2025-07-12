from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

app = Flask(__name__)
load_dotenv()
CORS(app)

password = quote_plus(os.getenv("DB_PASSWORD"))  # encodes special characters
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{password}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define models
class Bank(db.Model):
    __tablename__ = 'banks'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    branches = db.relationship('Branch', backref='bank', lazy=True)

class Branch(db.Model):
    __tablename__ = 'branches'
    ifsc = db.Column(db.String(11), primary_key=True)  # ifsc is now the primary key
    branch = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(195))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(26))
    bank_id = db.Column(db.BigInteger, db.ForeignKey('banks.id'), nullable=False)

# Routes
@app.route('/')
def hello():
    return "<h1>Indian Banks</h1>"

@app.route('/banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    return jsonify({
        'banks': [
            {
                'id': bank.id,
                'name': bank.name,
                'branches': [
                    {
                        'ifsc': branch.ifsc,
                        'branch': branch.branch,
                        'address': branch.address,
                        'city': branch.city,
                        'district': branch.district,
                        'state': branch.state,
                    } for branch in bank.branches
                ]
            } for bank in banks
        ]
    })

@app.route('/branches', methods=['GET'])
def get_branches():
    ifsc = request.args.get('ifsc')
    if ifsc:
        branches = Branch.query.filter_by(ifsc=ifsc).all()
    else:
        branches = Branch.query.all()
    return jsonify({
        'branches': [
            {
                'ifsc': branch.ifsc,
                'branch': branch.branch,
                'address': branch.address,
                'city': branch.city,
                'district': branch.district,
                'state': branch.state,
                'bank_id': branch.bank_id
            } for branch in branches
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
