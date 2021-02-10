import sys
sys.path.append('.')
from flask_restful import fields, marshal_with
from dao.country_dao import CountryDao
from models.country import Country
from resources.base_resource import BaseResource


class CountryResource(BaseResource):
    fields = {
        "id": fields.Integer,
        "description": fields.String,
    }

    def __init__(self):
        self.__dao = CountryDao()
        self.__model_type = Country
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
