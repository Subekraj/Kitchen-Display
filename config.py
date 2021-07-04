from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/test'
db=SQLAlchemy(app)




from Model.OrderModel import *
from Service.OrderTableService import *
from DatabaseModel.OrderTabledbModel import *
from Controller.OrderTableController import *

