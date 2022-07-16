"""sample fastapi project
"""
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fibonacci import fibonacci
from enigma import enigma

app = FastAPI()


class Number(BaseModel):
    x: int


class StockItem(BaseModel):
    name: str
    shares: int
    price: Optional[float] = 1000


class Rotors(BaseModel):
    rotor1: int
    rotor2: int
    rotor3: int


@app.get('/')
def hello_world():
    """hello world api
    """
    return {'message': 'Hello, World!'}


@app.get('/greeting/{name}')
def greeting_user(name: str):
    """greeting to user with name
    """
    return {'message': f'Hello, {name}'}


@app.post('/power')
def power_of_number(data: Number):
    """return power of number
    """
    x = data.x
    return {'result': x*x}


@app.get('/stock/{id}')
def get_stock_detail(id: int):
    """get details of stock with id
    """
    return {'stock_id': id}


@app.get('/stock')
def get_stock_with_query_params(id: int = None):
    """get details of stock with id using query params
    """
    if id is None:
        return [
            {'stock_id': stock_id} for stock_id in range(10)
        ]
    if id == 1:
        return {
            'stock_id': id,
            'stock': '∞'
        }
    return {
        'stock_id': id
    }


@app.post('/stock/buy')
def buy_stock(item: StockItem):
    """buy stock
    """
    return {
        'stock_name': item.name,
        'shares': item.shares,
        'price': item.price,
        'total_price': item.shares * item.price
    }


@app.get('/fib/{number}')
def fib(number: int):
    """return list of fibonacci numbers
    """
    return {
        'number': number,
        'result': fibonacci(number)
    }


@app.get('/enigma')
def enigma_(text: str, rotors: Rotors = None):
    """code and decode text using enigma machine
    """
    if rotors is not None:
        rotors = (rotors.rotor1, rotors.rotor2, rotors.rotor3)
    return {
        'input_text': text,
        'rotors': rotors,
        'result': enigma(text, rotors)
    }
