from time import *

class Skill:

    def __init__(self, start, train_time, name, **kwargs):

        self.start = start
        self.train_time = train_time
        self.finish = self.start + self.train_time
        self.__name__ = name





    
        
