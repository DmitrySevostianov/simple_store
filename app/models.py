from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(64), index=True, unique=True)
    
    #Метод __repr__ сообщает Python, как печатать объекты этого класса,
    # это полезно для отладки
    def __repr__(self):
        return '<Product {}>'.format(self.productname) 
