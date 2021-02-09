import sys
sys.path.append('.')
from flask_restful import fields, marshal_with
from dao.city_dao import CityDao
from models.city import City 
from resources.base_resource import BaseResource


class CityResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "description": fields.String,
        "id_state": fields.Integer
    }

    def __init__(self):
        self.__dao = CityDao()
        self.__model_type = City

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