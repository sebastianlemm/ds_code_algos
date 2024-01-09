class OpenAddressingHashtable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size
        self.status = ["Empty"] * self.size

    def __str__(self):
        return str(self.table)

    def _linear_probe(self, start_index):
        index = start_index
        while self.status[index] == "Filled":
            index = (index + 1) % self.size
        return index

    def insert(self, elem):
        hash_index = ord(elem[0]) % self.size
        index = self._linear_probe(hash_index)
        self.table[index] = elem
        self.status[index] = "Filled"

    def member(self, elem):
        hash_index = ord(elem[0]) % self.size
        index = hash_index
        while self.status[index] != "Empty":
            if self.table[index] == elem:
                return True
            index = (index + 1) % self.size
            if index == hash_index:
                break
        return False

    def delete(self, elem):
        hash_index = ord(elem[0]) % self.size
        index = hash_index
        while self.status[index] != "Empty":
            if self.table[index] == elem:
                self.table[index] = None
                self.status[index] = "Deleted"
                return
            index = (index + 1) % self.size
            if index == hash_index:
                break

# Testing the Open Addressing Hashtable
s = OpenAddressingHashtable(10)
s.insert("amy") 
s.insert("chase")
s.insert("chris")
print(s.member("amy"))
print(s.member("chris"))
print(s.member("alyssa"))
s.delete("chase")
print(s.member("chris"))
print(s) 
