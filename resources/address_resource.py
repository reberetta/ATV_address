import sys
sys.path.append('.')
from flask_restful import fields, marshal_with
from dao.address_dao import AddressDao
from models.address import Address 
from resources.base_resource import BaseResource


class AddressResource(BaseResource):
    fields = {
        "id": fields.Integer,
        "description": fields.String,
        "number": fields.Integer,
        "cep": fields.String,
        "id_district": fields.Integer
    }

    def __init__(self):
        self.__dao = AddressDao()
        self.__model_type = Address

        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)