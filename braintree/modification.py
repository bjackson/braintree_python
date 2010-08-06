from decimal import Decimal
from braintree.resource import Resource

class Modification(Resource):
    def __init__(self, attributes):
        Resource.__init__(self, attributes)
        self.amount = Decimal(self.amount)
