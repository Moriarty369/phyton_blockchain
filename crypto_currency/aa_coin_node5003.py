#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 18:38:13 2023

@author: Abelardo Acosta Cracco
"""

import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse


class Blockchain:  
    def __init__(self): 
        self.chain = []
        # Creamos la lista vacia para las transacciones
        self.transactions = []
        self.create_block(proof = 1, previous_hash = '0')
        """la "lista" de nodos la creamos como un conjunto vacío ya que éstos se encuentran esparcidos y duplicados en la red
            y no consideramos un orden pero evitando su duplicado el nodo se analizará individualmente para encontrar el mas largo ;)"""
        self.nodes = set()
      
    def create_block(self, proof, previous_hash):
        # Creamos el bloque como diccionario para facilitar el jsonify
        block = {
            'index' : len(self.chain)+1,
            # para que no haya conflicto de datos entre datetime y jsonify lo convertimos a string
            'timestamp' : str(datetime.datetime.now()),
            'proof' : proof,
            'previous_hash' : previous_hash,
            'transactions' : self.transactions}
        # Luego de minar el bloque con la transaccion volvemos a vaciar la variable-lista para el siguiente bloque
        self.transactions = []
        self.chain.append(block)
        return block
    
    def get_previous_block (self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
           new_proof = 1
           check_proof = False
           while check_proof is False:
              # La operacion entre new y previous proof no puede ser simétrica(o conmutativa). Esto ayuda a evitar que los mineros encuentren soluciones demasiado rápido mediante la simple adición o sustracción de valores pequeños(subimos la dificultad del nonce).
              # Al restar new_proof - previous_proof, se crea una relación de dependencia entre el valor actual de prueba (new_proof) y el valor de prueba del bloque anterior (previous_proof). 
              # OJO para lanzarlo podemos optimizar la operacion entre previous y new (añadir polinomio de mayor grado)
              hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
              if hash_operation[:4] == '0000':
                  check_proof = True
              else:
                  new_proof +=1
           return new_proof
  
   
    def hash(self, block):
        # Codificamos el diccionario a string con json organizando los elementos por su key (la función json  es dump)
        encode_block = json.dumps(block, sort_keys = True ).encode()
        return hashlib.sha256(encode_block).hexdigest()
    
    # Validar si la cadena es "correcta" comprobando el previous_hash y verificando la proof
    def is_chain_valid (self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            current_block = chain[block_index]
            if current_block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = current_block['proof']
            hash_validation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_validation [:4] != 'oooo':
                return False
            previous_block = current_block
            block_index += 1
        return True    
    
    # Creamos nuestro método para añadir las transacciones
    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'amount': amount})
        # Obtenemos el indice del bloque aplicando la funcion get_previous_block al propio objeto  OJOOOOOOOO
        previous_block = self.get_previous_block()
        # Retornamops el indice donde se retornara nuestra transaccion (el nuevo bloque)
        return previous_block['index'] +1
    
    # Filtramos la url de los nodos para posteriormente analizarlos y buscar el mas largo
    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
    
    # Verificamos individualmente cual es el nodo con la cadena mas largo
    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        # "MI" cadena es la mas larga hasta que detectemos otra más larga 
        # En la red con el bucle for por medio de su url "filtrada"
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                # Comparamos la longitud de la cadena en los otros nodos (verificando si son válidas) 
                # Con la longitud de nuestra cadena
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        # Si es diferente a None (su valor inicial), de lo contrario la cadena mas larga y el nodo elegido es el mío
        if longest_chain:
            self.chain = longest_chain
            return True
        # Si nadie tiene una cadena mas larga retornamos False en la función para mantener nuestra cadena 
        return False
    
# Creamos una appweb con Flask
app  = Flask(__name__)
# para evitar el Internal error 5000 ejecutamos la siguiente línea
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Creamos la dirección del nodo en el puerto 5000 con la libreria uuid
# y lo manipulamos para quitar los guines en el código uuid
node_address = str(uuid4()).replace('-','')

# Instanciamos nuestra clase blockchain
blockchain = Blockchain()

# Minando un nuevo bloque configurando el Flask añadiendo las transacciones y permitirle ser una criptomenda
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    # Añadimos la recompensa del minero
    blockchain.add_transaction(sender = node_address, receiver = "Sebastian", amount = 1)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message' : '¡Enhorabuena has minado un bloque!',
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash'],
                'transactions' : block['transactions']}
    # 200 es el código http para indicar OK
    return jsonify(response), 200      

# Obtener la cadena de bloques completa 
@app.route('/get_chain', methods = ['GET'])   
def get_chain():
    response = {'chain' : blockchain.chain,
                'length' : len(blockchain.chain)}
    return jsonify(response), 200

# Comprobamos si la cadena de bloques es valida 
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'La cadena de bloques es válida.'}
    else:
        response = {'message': 'La cadena de bloques no es válida.'}
    return jsonify(response), 200

# Añadir una nueva transacción en la cadena de bloques con POST
@app.route('/post_transaction', methods = ['POST'])
def post_transaction():  
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    # Analizamos si todas las claves se encuentran dentro de la transacción 
    # (Si para cada clave en transaction_... los 3 keys se encuentra en el json de la transacción)
    if not all(key in json for key in transaction_keys):
        # Incluimos mensaje de error y el error code
        return 'Faltan algunos elementos de la transacción', 400
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message' : f'La transacción será añadida en el bloque número: {index}'}
    return jsonify(response), 201


# Descentralizamos la cadena de bloques!!
# Primero conectamos nuevos nodos con una petición POST
@app.route('/connect_node', methods = ['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes') 
    if nodes is None:
        return 'No hay nodos para añadir', 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'mesage' : 'Todos los nodos han sido conectados, la cadena de AAcoin contiene ahora los siguientes nodos: ', 
                'total_nodes' : list(blockchain.nodes)}
    return jsonify(response), 201

# """ Reemplazamos la cadena en los nodos por la más larga (si es necesario) 
# llamando nuestro metodo en la peticion """
@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'Los nodos tenían diferentes cadenas, que han sido reemplazadas por la más larga',
                    'new_chain' : blockchain.chain}
    else:
        response = {'message' : 'La cadena en todos los nodos ya es la más larga',
                    'actual_chain' : blockchain.chain}
    return jsonify(response), 200 





# Ejecutamos la app
app.run(host = '127.0.0.1', port = 5003)


