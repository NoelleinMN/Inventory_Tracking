"""Model for Shopify Inventory Tracking Web App"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Inventory(db.Model):
    """Items in the inventory"""

    __tablename__ = 'inventory'

    item_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    item_name = db.Column(db.String)
    item_location = db.Column(db.String)

    def __repr__(self):
        return f"<Inventory ID: {self.item_id}, Name: {self.item_name}, Warehouse: {self.item_location}>"

class Warehouse(db.Model):
    """Association table of warehouses for inventory storage."""

    __tablename__ = 'warehouses'

    warehouse_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    warehouse_city = db.Column(db.String)
    item_id = db.Column(db.Integer, db.ForeignKey('inventory.item_id'))

    item_location = db.relationship('Inventory', backref='item_location')

    # TODO: update this to reflect creation of a warehouse and also the items housed within
    # or, skip items upon return and, instead, make a separate function to get that listing?
    def __repr__(self):
        return f'<Inventory ID: {self.item_id} Warehouse ID: {self.warehouse_id} Warehouse City: {self.warehouse_city}>'

def connect_to_db(flask_app, db_uri='postgresql:///inventory_tracking', echo = True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    # Can execute connect_to_db(app, echo=False) if program output gets too annoying;
    # this will tell SQLAlchemy not to print out every query it executes.

    connect_to_db(app)
