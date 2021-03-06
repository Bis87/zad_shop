from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            return store.json()
        return{'message': 'Store not found'}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_item_by_name(name):
            return {'message': "Store with '{}' name already exists".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': "An error uccured while createing the store"}, 500
        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_item_by_name(name)
        if store:
            store.delete_from_db()
        return {'messgae': 'Store deleted'}

class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'stores': [i.json() for i in StoreModel.query.all()]}
