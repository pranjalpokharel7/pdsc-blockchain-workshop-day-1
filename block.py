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
        self.hash = self.calculate_hash() 
        self.previous_hash = None
        
    def calculate_hash(self) -> str:
        block_string = str(self.timestamp) + str(self.miner)
        for transaction in self.transactions:
            block_string += str(transaction)
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()
    
    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "miner": self.miner,
            "transactions": [transaction.to_dict() for transaction in self.transactions],
            "hash": self.hash
        }

tx1 = Transaction(doer='Supriya', copier='Ranju', words=300)
tx2 = Transaction(doer='Newton', copier='Sanskar', words=500)
pending_txs = [tx1, tx2]

blk1 = Block(pending_transactions=pending_txs)
print(blk1.to_dict())