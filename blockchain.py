from typing import List
from block import Block
from genesis_block import GenesisBlock

class Blockchain:     
    def __init__(self) -> None:
        self.genesis_block = GenesisBlock() # TODO: genesis block
        self.valid_blocks = [self.genesis_block]

    def add_block(self, block: Block) -> None:
        prev_block = self.valid_blocks[-1]
        
        # connect the previous block to the new block to create a chain by their hashes
        block.previous_hash = prev_block.hash
        
        self.valid_blocks.append(block)
    