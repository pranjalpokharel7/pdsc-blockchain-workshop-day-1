import time
import hashlib
from typing import List

from transaction import Transaction

# block holds transactions i.e. list assignment details
# a block is created when there are pending transactions in the transaction pool
class Block:
    def __init__(self, pending_transactions: List[Transaction]) -> None:
        self.timestamp = time.time() # time a block was created
        self.transactions = pending_transactions
        self.hash = None 
        self.previous_hash = None
        
    def calculate_hash(self) -> str:
        block_string = str(self.timestamp) + str(self.previous_hash) 
        for transaction in self.transactions:
            block_string += str(transaction)
        self.hash = hashlib.sha256(block_string.encode('utf-8')).hexdigest()
        return self.hash
    
    def to_dict(self):
        return {
            "hash": self.hash,
            "timestamp": self.timestamp,
            "transactions": [transaction.to_dict() for transaction in self.transactions],
            "hash": self.hash
        }
