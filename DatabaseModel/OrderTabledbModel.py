from flask_sqlalchemy import SQLAlchemy
from config import app

db=SQLAlchemy(app)
class OrderTable(db.Model):
    __tablename__='kotdisplay'
    table_no=db.Column(db.String(10),primary_key=True)
    def __init__(self,table_no):
        self.table_no=table_no
