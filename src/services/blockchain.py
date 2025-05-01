
import hashlib
import json



class Blockchain(object):
    difficulty_target = "0000"
    def __init__(self):

        self.chain = []

        self.current_transactions = []


    def hash_block(self, block):
        block_encoded = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()
    

    
        