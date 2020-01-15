import numpy as np
from math import log
import random
import sys
import os

class Cache:
    def __init__(self, cSize, ways=1, bSize=4):

        self.cacheSize = cSize  # Bytes
        self.ways = ways        # Default: 1 way (i.e., directly mapped)
        self.blockSize = bSize  # Default: 4 bytes (i.e., 1 word block)
        self.setSize = cSize // bSize // ways

        self.blockBits = 0
        self.setBits = 0

        if (self.blockSize != 1):
            self.blockBits = int(log(self.blockSize, 2))

        if (self.setSize != 1):
            self.setBits = int(log(self.setSize, 2))

        self.cache = np.zeros((self.setSize, self.ways, self.blockSize), dtype=int)
        #actually just a 2D array, setSize = y, blockSize = x
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.setSize, self.ways), dtype=int)
        self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0
        self.hitlatency = 1 # cycle
        self.misspenalty = 10 # cycle

    def reset(self):
        self.cache = np.zeros((self.setSize, self.ways, self.blockSize), dtype=int)
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.setSize, self.ways), dtype=int)
        self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0

    '''
    Warning: DO NOT EDIT ANYTHING BEFORE THIS LINE
    '''


    '''
    Returns the set number of an address based on the policy discussed in the class
    Do NOT change the function definition and arguments
    '''

    def find_set(self, address):
        words_per_block  = self.blockSize >> 2
        if self.setBits == 0:
            return 0 
        return int(str("{0:08b}".format(address >> (2 + int(log(words_per_block, 2))))[-1:-(self.setBits + 1):-1])[::-1], 2)
        
        
    '''
    Returns the tag of an address based on the policy discussed in the class
    Do NOT change the function definition and arguments
    '''

    def find_tag(self, address):
        y, words_per_block = address >> 2, self.blockSize >> 2
        return int(str("{0:08b}".format(y >> (int(log(words_per_block, 2)) + self.setBits))), 2)

    '''Search through cache for address
    return True if found
    otherwise False
    Do NOT change the function definition and arguments'''

    def find(self, address):
        s = self.find_set(address)
        for i in range(self.ways):
            for j in range(self.blockSize):
                if not (self.find_tag(address) ^ self.find_tag(self.cache[s][i][j])):
                    self.hit += 1
                    self.metaCache[s][i] = np.sum(np.absolute(self.metaCache[s]))
                    return True
        return False
            
    '''
    Load data into the cache.
    Something might need to be evicted from the cache and send back to memory
    Do NOT change the function definition and arguments
    '''

    def load(self, address):
        s = self.find_set(address)
        LRU = np.where(self.metaCache[s] == min(self.metaCache[s]))[0][0]
        self.cache[s][LRU] = np.ravel(list(np.repeat(address - (address % self.blockSize) + i, 1) for i in range(self.blockSize)))
        self.metaCache[s][LRU] = np.sum(np.absolute(self.metaCache[s]))
      

