from controllers.base_controller import BaseController
from dao.product_dao import AddressDao


class AddressController(BaseController):
    def __init__(self):
        super().__init__(AddressDao())
