class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
    
    def __str__(self):
        return self.__repr__()