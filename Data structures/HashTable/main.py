from HashTable import HashTable

ht = HashTable()
ht.add(12, 12)
ht.add(13, 13)
ht.add(14, 14)
ht.add(12, 20)
print(ht.get_value(15))
ht.delete(13)
ht.delete(14)
ht.delete(15)
print(ht.first)
print(ht.last)
