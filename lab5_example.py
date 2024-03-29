class MyHashtable(object):
    # HashTable ADT with chaining implementation
    # This Hashtable only accepts Strings and hashes based on their
    # ascii value of the first char
    # The constructor takes in the size of the table

    def __init__(self, size):  # Creates an empty hashtable
        self.size = size
        # Create the list (of size) of empty lists (chaining)
        self.table = []
        for i in range(self.size):
            self.table.append([])

    def __str__(self):  # for print
        return str(self.table)

    def insert(self, elem):  # Adds an element into the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].append(elem)

    def member(self, elem):  # Returns if element exists in hashtable
        hash = ord(elem[0]) % self.size
        return elem in self.table[hash]

    def delete(self, elem):  # Removes an element from the hashtable
        hash = ord(elem[0]) % self.size
        self.table[hash].remove(elem)


# Testing code
s = MyHashtable(10)
s.insert("amy")  # 97
s.insert("chase")  # 99
s.insert("chris")  # 99
print(s.member("amy"))
s.delete("chase")
print(s.member("chris"))

# You can use print(s) at anytime to see the contents
# of the table for debugging
# print(s)
