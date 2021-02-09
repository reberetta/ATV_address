from flask import Flask
from flask_restful import Api

from resources.address_resource import AddressResource
from resources.city_resource import CityResource
from resources.country_resource import CountryResource
from resources.district_resource import DistrictResource
from resources.state_resource import StateResource

app = Flask(__name__)
api = Api(app)

api.add_resource(AddressResource, '/api/address/<int:id>', endpoint='addresses')
api.add_resource(AddressResource, '/api/address', endpoint='address')

api.add_resource(CityResource, '/api/city/<int:id>', endpoint='city')
api.add_resource(CityResource, '/api/city', endpoint='cities')

api.add_resource(CountryResource, '/api/country/<int:id>', endpoint='country')
api.add_resource(CountryResource, '/api/country', endpoint='countries')

api.add_resource(DistrictResource, '/api/district/<int:id>', endpoint='district')
api.add_resource(DistrictResource, '/api/dstrict', endpoint='districts')

api.add_resource(StateResource, '/api/state/<int:id>', endpoint='state')
api.add_resource(StateResource, '/api/state', endpoint='states')

app.run(debug=True)