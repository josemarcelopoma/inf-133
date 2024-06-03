from app.database import db


# Define la clase `Animal` que hereda de `db.Model`
# `Animal` representa la tabla `animals` en la base de datos
class Product(db.Model):
    __tablename__ = "products"

    # Define las columnas de la tabla `animals`
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    # Inicializa la clase `Animal`
    def __init__(self, name, description, price,stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    # Guarda un animal en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los animales de la base de datos
    @staticmethod
    def get_all():
        return Product.query.all()

    # Obtiene un animal por su ID
    @staticmethod
    def get_by_id(id):
        return Product.query.get(id)

    # Actualiza un animal en la base de datos
    def update(self, name=None, description=None, price=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        db.session.commit()

    # Elimina un animal de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()