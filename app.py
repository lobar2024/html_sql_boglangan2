from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Xodimlar(db.Model):
    __tablename__ = 'xodimlar jadvali'
    id = db.Column(db.Integer, primary_key=True)
    ism = db.Column(db.String(100))
    familiya = db.Column(db.String(100))
    tugilgan = db.Column(db.DateTime, default=datetime.now)
    lavozim = db.Column(db.String(100))
    bolim = db.Column(db.String(40))
    telefon = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    ish_haqi = db.Column(db.Integer)
    ishga_kirgan = db.Column(db.DateTime, default = datetime.now)

class Mahsulotlar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mahsulot_nomi = db.Column(db.String(50))
    kategoriya = db.Column(db.String(100))
    ishlab_chiqaruvchi = db.Column(db.String(100))
    narx = db.Column(db.Integer)
    miqdor = db.Column(db.Integer)
    rang = db.Column(db.String(100))
    ogirlik = db.Column(db.Float)
    kafolat_oy = db.Column(db.Integer)
    kelgan_sana = db.Column(db.DateTime, default = datetime.now)

class Buyurtmalar(db.Model):
    __tablename__ = 'buyurtmalar jadvali'
    id = db.Column(db.Integer, primary_Key=True)
    mijoz_ismi = db.Column(db.String(100))
    mijoz_telefon = db.Column(db.String(100), unique=True)
    mahsulot_nomi = db.Column(db.String(100))
    miqdor = db.Column(db.Integer)
    narx = db.Column(db.Integer)
    jami_summa = db.Column(db.Integer)
    tolov_turi = db.Column(db.String(100))
    buyurtma_sana = db.Column(db.DateTime, default = datetime.now)
    yetkazilgan = db.Column(db.String(10))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

