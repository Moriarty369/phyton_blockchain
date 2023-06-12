#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:40:01 2023

@author: Abelardo Acosta Cracco
"""
import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:  
    def __init__(self): 
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
      
    def create_block(self, proof, previous_hash):
        #se crea el bloque como diccionario para facilitar el jsonify
        block = {
            'index' : len(self.chain)+1,
            # para que no haya conflicto de datos entre datetime y jsonify lo convertimos a string
            'timestamp' : str(datetime.datetime.now()),
            'proof' : proof,
            'previous_hash' : previous_hash
            }
        self.chain.append(block)
        return block
    
    def get_previous_block (self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
           new_proof = 1
           check_proof = False
           while check_proof is False:
              #la operacion entre new y previous proof no puede ser simétrica(o conmutativa). Esto ayuda a evitar que los mineros encuentren soluciones demasiado rápido mediante la simple adición o sustracción de valores pequeños(subimos la dificultad del nonce).
              #Al restar new_proof - previous_proof, se crea una relación de dependencia entre el valor actual de prueba (new_proof) y el valor de prueba del bloque anterior (previous_proof). 
              # OJO para lanzarlo podemos optimizar la operacion entre previous y new (añadir polinomio de mayor grado)
              hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
              if hash_operation[:4] == '0000':
                  check_proof = True
              else:
                  new_proof +=1
           return new_proof
  
   
    def hash(self, block):
        #codificamos el diccionario a string con json organizando los elementos por su key (la función json  es dump)
        encode_block = json.dumps(block, sort_keys = True ).encode()
        return hashlib.sha256(encode_block).hexdigest()
    
    #Validar si la cadena es "correcta" comprobando el previous_hash y verificando la proof
    def is_chain_valid (self, chain,):
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

#Creamos una appweb con Flask
app  = Flask(__name__)
# para evitar el Internal error 5000 ejecutamos la siguiente línea
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


#instanciamos nuestra clase blockchain
blockchain = Blockchain()

#Minando un nuevo bloque configurando el Flask
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message' : '¡Enhorabuena has minado un bloque!',
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash']}
    #200 es el código http para indicar OK
    return jsonify(response), 200      

#obtener la cadena de bloques completa 
@app.route('/get_chain', methods = ['GET'])   
def get_chain():
    response = {'chain' : blockchain.chain,
                'length' : len(blockchain.chain)}
    return jsonify(response), 200
#comprobamos si la cadena de bloques es valida 
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'La cadena de bloques es válida.'}
    else:
        response = {'message': 'La cadena de bloques no es válida.'}
    return jsonify(response), 200


# Ejecutamos la app
app.run(host = '0.0.0.0', port = 5000)


