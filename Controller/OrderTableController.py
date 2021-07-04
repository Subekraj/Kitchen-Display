import re
from config import api
from Service.OrderTableService import GetOrderTableData
from flask_restplus import Resource
from Model.OrderModel import getOrderTable
from flask import render_template

name_space=api.namespace('OrderTable','Get All Order Table')
@name_space.route('/')
class GetAllOrderTable(Resource):
    @api.marshal_with(getOrderTable)
    def get(self):
        return render_template(GetOrderTableData())


