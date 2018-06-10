from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal
from goods.Good import *

app = Flask(__name__, static_url_path="")
api = Api(app)

goods = {}

goods_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'manufacturer': fields.String,
    'price': fields.Float,
    'amount': fields.Integer,
    'goods_colour': fields.String,
    'goods_type': fields.String
}


class Goods(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('manufacturer', type=str, location='json')
        self.reqparse.add_argument('price', type=float, location='json')
        self.reqparse.add_argument('amount', type=int, location='json')
        self.reqparse.add_argument('goods_colour', type=str, location='json')
        self.reqparse.add_argument('goods_type', type=str, location='json')
        super(Goods, self).__init__()  # super().__init__() / Good.__init__(self)

    @app.route('/goods')
    def put(self):
        args = self.reqparse.parse_args()
        good = {
            'id': args['id'],
            'name': args['name'],
            'manufacturer': args['manufacturer'],
            'price': args['price'],
            'amount': args['amount'],
            'goods_colour': args['goods_colour'],
            'goods_type': args['goods_type']
        }
        goods.update(good)
        return marshal(good, goods_fields), 201

    @app.route('/goods')
    def post(self):
        args = self.reqparse.parse_args()
        good = [good for good in goods if goods.get('id') == args['id']]
        if len(good) == 0:
            abort(404)
        goods.pop(good[0])
        new_good = {
            'id': args['id'],
            'name': args['name'],
            'manufacturer': args['manufacturer'],
            'price': args['price'],
            'amount': args['amount'],
            'goods_colour': args['goods_colour'],
            'goods_type': args['goods_type']
        }
        goods.update(new_good)
        return marshal(new_good, goods_fields)

    @app.route('/goods/<int:id>')
    def get(self, id):
        good = [good for good in goods if goods.get('id') == id]
        if len(good) == 0:
            abort(404)
        return marshal(good[0], goods_fields)

    @app.route('/goods/<int:id>')
    def delete(self, id):
        good = [good for good in goods if goods.get('id') == id]
        if len(good) == 0:
            abort(404)
        goods.pop(good[0])
        return {'result': True}


api.add_resource(Goods, '/goods', endpoint='goods')
api.add_resource(Goods, '/goods/<int:id>', endpoint='good')

if __name__ == '__main__':
    app.run(debug=True)
