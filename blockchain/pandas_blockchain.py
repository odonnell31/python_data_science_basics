'''
Author: Michael O'Donnell
Date: 10/19/19

A mock blockchain built with Pandas dataframes

This blockchain consists of three components:
    1. python Class called PandasChain
        1.1 This is the entire blockchain where the blocks live
    2. python Class called Block
        2.1 Each block holds transactions between blockchain users
        2.2 Each block can hold 10 transaction maximum
        2.3 A block is "uncommitted" until it has 10 transactions, then it's "committed"
        2.4 each block has a block hash
    3. method called add_transaction (within PandasChain class)
        3.1 this functions adds a transaction between users to the blockchain
        3.2 each transaction has a Sender, Receiver, Value, Timestamp, and Transaction Hash
'''        

import datetime as dt
import hashlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import unittest
import uuid

# a class to define the blockchain, with many methods
class PandasChain:
    def __init__(self, name): 
        self.__name = name.upper()
        self.__chain = []
        self.__id = hashlib.sha256(str(str(uuid.uuid4())+self.__name+str(dt.datetime.now())).encode('utf-8')).hexdigest()
        self.__seq_id = 0
        self.__prev_hash = None
        self.__current_block = Block(len(self._PandasChain__chain), self._PandasChain__prev_hash)
        print(self.__name,'PandasChain created with ID',self.__id,'chain started.')
    
    # loop through all committed and uncommitted blocks and display all transactions
    def display_chain(self): 
        for i in self._PandasChain__chain:
            for j in self._PandasChain__chain[i]:
                print(['transactions'])
    
    # This method accepts a new transaction and adds it to current block if block is not full. 
    # If block is full, it will delegate the committing and creation of a new current block 
    def add_transaction(self,s,r,v): 
        if self.__current_block.get_size() >= 10:
            self.__commit_block(self.__current_block)
        self.__current_block.add_transaction(s,r,v)
    
    # this method is called by add_transaction if a block is full (>=10 transactions)
    def __commit_block(self,block):
        # change block status to committed
        block._Block__status = "COMMITTED"
        
        # obtain the merkle root hash
        merk_concat = ""
        for i in block._Block__transactions:
            merk_concat = merk_concat + str(i)
        block._Block__merkle_tx_hash = hashlib.sha256(str(merk_concat).encode('utf-8')).hexdigest()
        
        # generate the block's hash
        block_concat = str(block._Block__prev_hash) + str(block._Block__seq_id) + str(dt.datetime.now()) + str(block._Block__seq_id) + str(block._Block__merkle_tx_hash)
        block._Block__block_hash = hashlib.sha256(str(block_concat).encode('utf-8')).hexdigest()
        
        # set the prev_hash to the previous Block's hash
        block._Block__prev_hash = self._PandasChain__prev_hash
        
        # append this block to the chain list
        self._PandasChain__chain.append(block)
        
        # increment the seq_id
        self._PandasChain__seq_id = self._PandasChain__seq_id + 1
        
        # create a new block as the current block
        self._PandasChain__current_block = Block(len(self._PandasChain__chain), self._PandasChain__prev_hash)
        
        # let the user know the block is committed
        #print('Block committed')
 
    # Display just the metadata of all blocks (committed or uncommitted), one block per line.  
    # sequence Id, status, block hash, previous block's hash, merkle hash and count of transactions in the block
    def display_block_headers(self): 
        for b in self._PandasChain__chain:
            print(b._Block__seq_id, b._Block__status, b._Block__block_hash,
                  b._Block__prev_hash, b._Block__merkle_tx_hash,
                  len(b._Block__transactions))
    
    # returns number of blocks on the chain
    def get_number_of_blocks(self): 
        return(len(self._PandasChain__chain) + 1)
    
    # returns all of the values of all transactions from every block as a single list
    def get_values(self):
        # create blank list (to append all transaction values to)
        pandas_coin_list = [] 

        # loop through all transactions of all blocks
        for b in self._PandasChain__chain:
            for t in b._Block__transactions['Value']:
                # append each transaction to the list
                pandas_coin_list.append(t)
                
        return(pandas_coin_list)
    
# a class to define a block, with many methods        
class Block:
    def __init__(self,seq_id,prev_hash): 
        self.__seq_id = seq_id
        self.__prev_hash = prev_hash
        self.__col_names = ['Timestamp','Sender','Receiver','Value','TxHash']
        self.__transactions = pd.DataFrame(columns=['Timestamp','Sender','Receiver','Value','TxHash'])
        self.__status = "UNCOMMITTED"
        self.__block_hash = None
        self.__merkle_tx_hash = None
        
    # a single line the metadata of this block
    # sequence Id, status, block hash, previous block's hash, merkle hash and count of transactions
    def display_header(self):
        return(self._Block__seq_id, self._Block__status,
               self._Block__block_hash, self._Block__merkle_tx_hash,
               self._Block__seq_id, "transactions:",
               len(self._Block__transactions))
    
    # method to add a transaction
    # this method takes sender, receiver, and value as s, r, and v
    def add_transaction(self,s,r,v):
        ts = str(dt.datetime.now())
        # Hash of timestamp, sender, receiver, value
        tx_hash = hashlib.sha256((str(ts)+str(s)+str(r)+str(v)).encode('utf-8')).hexdigest()
        
        # dict of transaction data to pass into single lined dataframe
        data = {'Timestamp': ts, 'Sender': s, 'Receiver': r, 'Value': v, 'TxHash': tx_hash}
        new_transaction = pd.DataFrame(data = data, index =[0])
        
        # Append transaction to the block's dataframe of transactions
        self._Block__transactions = self._Block__transactions.append(new_transaction) 
        
    # print all transactions contained by this block
    def display_transactions(self): 
        for t in self._Block__transactions:
            print(t)
    
    # return the number of transactions contained by this block
    def get_size(self): 
        return(len(self._Block__transactions))
    
    # setter for status - Allow for the change of status (only two statuses exist - COMMITTED or UNCOMMITTED).
    def set_status(self,status):
        self._Block__status = status
    
    # setter for block hash
    def set_block_hash(self,hash):
        self._Block__block_hash = hash
    
    # return merkle hash by taking all transaction hashes, concatenate them into one string
    # hash that string producing a "merkle root"
    def get_simple_merkle_root(self): 
        merk_concat = ""
        for i in self._Block__transactions:
            merk_concat = merk_concat + str(i)
        return(hashlib.sha256(str(merk_concat)).hexdigest())


# Testing the blockchain...
block = Block(1,"test")
block.add_transaction("Bob","Alice",50)
pandas_chain = PandasChain('testnet')
pandas_chain.add_transaction("Bob","Alice",20)
pandas_chain.add_transaction("Bob","Alice",51)
pandas_chain.add_transaction("Bob","Sam",45)
pandas_chain.add_transaction("Bob","George",102)
pandas_chain.add_transaction("George","Grace",65)
pandas_chain.add_transaction("Sunny","Lilly",7)
pandas_chain.add_transaction("Bob","Brixton",123)
pandas_chain.add_transaction("Sam","Sunny",45)
pandas_chain.add_transaction("Edward","Sunny",53)
pandas_chain.add_transaction("Johnny","Lonnie",78)
pandas_chain.add_transaction("Jimmy","Alice",64)
pandas_chain.add_transaction("Kelly","Lonnie",89)
pandas_chain.add_transaction("Kelsey","Jim",100)
pandas_chain.add_transaction("Cam","Bob",102)
pandas_chain.add_transaction("Mike","Sunny",56)
pandas_chain.add_transaction("Jim","Cam",13)
pandas_chain.add_transaction("Isaac","Jimmy",20)
pandas_chain.add_transaction("Vinny","Alice",76)
pandas_chain.add_transaction("Nick","Kyle",65)
pandas_chain.add_transaction("Kyle","Jim",84)
pandas_chain.add_transaction("Lonnie","Luke",45)
pandas_chain.add_transaction("Luke","Jason",91)
pandas_chain.add_transaction("Holly","Erick",76)
pandas_chain.add_transaction("Nancy","Erick",26)
pandas_chain.add_transaction("Carolyn","Erick",80)
pandas_chain.add_transaction("Erick","Paisley",95)
pandas_chain.add_transaction("Brittany","Edgar",106)
pandas_chain.add_transaction("Benny","Edward",131)
pandas_chain.add_transaction("Paisley","Cam",11)
pandas_chain.add_transaction("Lilly","George",19)
pandas_chain.add_transaction("Benji","Paisley",29)
pandas_chain.add_transaction("Ulysses","Benny",25)

print("number of blocks:", pandas_chain.get_number_of_blocks())

x_vals = list(range(1, len(pandas_chain.get_values())+1))
y_vals = pandas_chain.get_values()

plt.figure(figsize=(7,4))
plt.scatter(x_vals, y_vals)
plt.xticks(np.arange(min(x_vals), max(x_vals)+1, 1))
plt.title('All Transactions in pandaschain')
plt.xlabel('transaction number')
plt.ylabel('transaction value')
plt.show()