import sys
sys.path.append('model')
sys.path.append('dao')
sys.path.append('resource')
from flask_restful import fields, marshal_with
from city_dao import CityDao
from city_model import City
from resource.base_resource import BaseResource


class CityResource(BaseResource):
    fields = {
        "id": fields.Integer,
        "description": fields.String,
    }

    def __init__(self):
        self.__dao = CityDao()
        self.__model_type = City
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id = None):
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
