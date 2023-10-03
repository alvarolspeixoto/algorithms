from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size += 1

    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __len__(self): 
            # retorna o tamanho da lista
            return self._size
        
    def __getitem__(self, index):
            # a = lista[x]
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        # lista[x] = a
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
        
        
    def index(self, elem):
        # retorna o índice de elem na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        return -1
    
    def insert(self, index, elem):
        # insere elem na posição index
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
        # remove elem da lista
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size -= 1
                    return True
                ancestor = pointer
                pointer = pointer.next
            raise ValueError("{} is not in list".format(elem))
        
    def __repr__(self):
        if self.head == None:
            return ""
        r = str(self.head.data)
        pointer = self.head.next
        while pointer:
            r += " -> " + str(pointer.data)
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()