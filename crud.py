"""CRUD operations"""

from model import db, Inventory, Warehouse, connect_to_db

def create_item(item_name, item_location=unassigned):
    """Create and return a new item added to inventory."""

    item = Inventory(item_name = item_name, item_location=item_location)

    db.session.add(item)
    db.session.commit()

    return item

def create_warehouse(warehouse_city):
    """Create and return a newly created warehouse location."""

    warehouse = Warehouse(warehouse_city)

    db.session.add(warehouse)
    db.session.commit()

    return warehouse

#TODO Edit inventory

#TODO Assign inventory to warehouse/location

def get_inventory():
    """Get all the items in inventory."""

    return Inventory.query.all()

def delete_item(item_id):
    """Delete an item from inventory."""

    deleted_item = Inventory.query.filter(Inventory.item_id == item_id).first()
    db.session.delete(deleted_item)
    db.session.commit()

    if __name__ == '__main__':
        from server import app
        connect_to_db(app)
