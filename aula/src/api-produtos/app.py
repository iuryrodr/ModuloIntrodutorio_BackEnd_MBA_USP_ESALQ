from fastapi import FastAPI
from models.product import Product

app = FastAPI()

products = [
    Product(id=1,name='Coca-cola',description='Uma bebida mundialmente conhecuida', price=9.98),
    Product(id=2,name='Iphone',description='Celular Top',price= 5524.22),
    Product(id=3,name='Tenis Air Max',description='tenizao zika',price= 650.00),
]

@app.get('/api/products')
def get_products():
    return products


@app.get('/api/products/sale')
def get_sale():
    """
    Endpoint que exibe o produto com maior desconto, não passa nenhum parâmetro
    """
    return products[1]