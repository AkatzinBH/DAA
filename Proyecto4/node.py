class Node:
    def __init__(self,id):
        self.id = id
        self.attrs = dict()
    
    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return repr(self.id)

    def __str__(self):
        return str(self.id)