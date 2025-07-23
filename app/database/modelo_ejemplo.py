from app.database.db import db

class Ejemplo(db.Model):
    __tablename__ = 'has'
    systemid = db.Column(db.Integer, primary_key=True)
    organizationid = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'systemid': self.systemid,
            'organizationid': self.organizationid
        } 