#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 18:40:01 2023

@author: sibarita
"""

#Módulo 1 - Crear Blockchain
import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    def __init__(self): 
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {
            'index' : len(self.chain)+1,
            'timestamp' : str(datetime.datetime.now()),
            'proof' : proof,
            'previous_hash' : previous_hash
            }
        self.chain.append(block)
        return block
    
    def get_previous_block (self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
           new_proof = 1,
           check_proof = False
           while check_proof is False:
              hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
              if hash_operation[:4] == '0000':
                  check_proof = True
              else:
                  new_proof +=1
           return new_proof
  
    #Hash function
    def hash(self, block):
        #codificamos el diccionario a string con json organizando los elementos por su key (la función jsno es dump)
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
            # Mining blocks