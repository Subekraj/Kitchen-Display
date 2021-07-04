from flask_restplus import Api,fields
from config import api

getOrderTable=api.model("Table",{
                                'table_no':fields.String
                                })