# PortfolioProject2

#1. HashMap class with chaining for collision resolution: 
Implementation of a HashMap class using a Dynamic Array (implemented in a6_include.py) to store the hash table. Chaining is implemented for collision resolution using singly linked lists. Chains of key/value pairs are stored in the linked lists nodes. Includes the following methods: 

put(self, key: str, value: object) -> None:
This method updates the key / value pair in the hash map. If the given key already exists in the hash map, its associated value must be replaced with the new value. If the given key is not in the hash map, a key / value pair must be added.

empty_buckets(self) -> int:
This method returns the number of empty buckets in the hash table.

table_load(self) -> float:
This method returns the current hash table load factor.

clear(self) -> None:
This method clears the contents of the hash map. It does not change the underlying hash table capacity.

resize_table(self, new_capacity: int) -> None:
This method changes the capacity of the internal hash table. All existing key / value pairs must remain in the new hash map, and all hash table links must be rehashed. If new_capacity is less than 1, the method does nothing.

get(self, key: str) -> object:
This method returns the value associated with the given key. If the key is not in the hash map, the method returns None.

contains_key(self, key: str) -> bool:
This method returns True if the given key is in the hash map, otherwise it returns False. An empty hash map does not contain any keys.

remove(self, key: str) -> None:
This method removes the given key and its associated value from the hash map. If the key is not in the hash map, the method does nothing (no exception needs to be raised).

get_keys(self) -> DynamicArray:
This method returns a DynamicArray that contains all the keys stored in the hash map. The order of the keys in the DA does not matter.

find_mode(arr: DynamicArray) -> (DynamicArray, int):
Write a standalone function outside of the HashMap class that receives a DynamicArray (that is not guaranteed to be sorted). This function will return a tuple containing, in this order, a DynamicArray comprising the mode (most occurring) value/s of the array, and an integer that represents the highest frequency (how many times they appear).
If there is more than one value with the highest frequency, all values at that frequency should be included in the array being returned (the order does not matter). If there is only one mode, return a DynamicArray comprised of only that value.
You may assume that the input array will contain at least one element, and that all values stored in the array will be strings. You do not need to write checks for these conditions.
For full credit, the function must be implemented with O(N) time complexity. For best results, we recommend using the separate chaining HashMap provided for you in the function’s skeleton code.

#2. HashMap class with open addressing for collision resolution:
Implementation of a HashMap class using a Dynamic Array (implemented in a6_include.py) to store the hash table. Open Addressing with Quadratic Probing is implemented for collision resolution inside the Dynamic Array. Key/value pairs are stored in the array. Includes the following methods: 

put(self, key: str, value: object) -> None:
This method updates the key / value pair in the hash map. If the given key already exists in the hash map, its associated value must be replaced with the new value. If the given key is not in the hash map, a key / value pair must be added. For this hash map implementation, the table must be resized to double its current
capacity when this method is called and the current load factor of the table is greater than or equal to 0.5.

table_load(self) -> float:
This method returns the current hash table load factor.

empty_buckets(self) -> int:
This method returns the number of empty buckets in the hash table.

resize_table(self, new_capacity: int) -> None:
This method changes the capacity of the internal hash table. All existing key / value pairs must remain in the new hash map, and all hash table links must be rehashed. If new_capacity is less than 1, or less than the current number of elements in the map, the method does nothing.

get(self, key: str) -> object:
This method returns the value associated with the given key. If the key is not in the hash map, the method returns None.

contains_key(self, key: str) -> bool:
This method returns True if the given key is in the hash map, otherwise it returns False. An empty hash map does not contain any keys.

remove(self, key: str) -> None:
This method removes the given key and its associated value from the hash map. If the key is not in the hash map, the method does nothing (no exception needs to be raised).

clear(self) -> None:
This method clears the contents of the hash map. It does not change the underlying hash table capacity.

get_keys(self) -> DynamicArray:
This method returns a DynamicArray that contains all the keys stored in the hash map. The order of the keys in the DA does not matter.



* No built-in Python data structures or methods were used in this project.
