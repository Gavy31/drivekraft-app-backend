from app.database import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    contactNumber = db.Column(db.String(10))
    username = db.Column(db.String(15))
    created = db.Column(db.TIMESTAMP)
    updated = db.Column(db.TIMESTAMP)
    firebaseId = db.Column(db.String(255))
    firebaseName = db.Column(db.String(255))
    firebaseEmail = db.Column(db.String(255))
    firebasePassword = db.Column(db.String(255))
    roleId = db.Column(db.Integer, db.ForeignKey('userRole.id'), nullable=False)
    balance = db.Column(db.DECIMAL(10, 2))
    isBlocked = db.Column(db.Boolean)

    userRole = db.relationship('app.Models.mysql.userRole.UserRole', backref='users')
    