# Name: Juan Pablo Duque Ochoa
# OSU Email: duqueocj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: (6) Portfolio Project - HashMap Implementation
# Due Date: 06/05/2022
# Description: Implementation of HashMap class with chaining for collision resolution.


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(LinkedList())

        self._capacity = capacity
        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Update the key / value pair in the hash map. If the key exists in
        the hash map, its associated value is replaced with the new value.
        If the key is not in the hash map, a key / value pair is added.
        """
        index = self.get_index(key)
        link_list: LinkedList = self._buckets[index]
        node = link_list.contains(key)
        if node:
            node.value = value
        else:
            link_list.insert(key, value)
            self._size += 1

    def empty_buckets(self) -> int:
        """
        Return the number of empty buckets in the hash table.
        """
        count = 0
        for index in range(self._capacity):
            if self._buckets[index].length() == 0:
                count += 1
        return count

    def table_load(self) -> float:
        """
        Return the current hash table load factor.
        """
        count = 0
        for index in range(self._capacity):
            count += self._buckets[index].length()
        return count / self._capacity

    def clear(self) -> None:
        """
        Clear the contents of the hash map without changing the underlying
        hash table capacity.
        """
        self.__init__(self._capacity, self._hash_function)

    def resize_table(self, new_capacity: int) -> None:
        """
        Change the capacity of the internal hash table. All existing
        key / value pairs remain in the new hash map, and all
        hash table links are rehashed.
        """
        if new_capacity < 1:
            return
        buckets = self._buckets
        capacity = self._capacity
        self._capacity = new_capacity
        self.clear()
        for index in range(capacity):
            for node in buckets[index]:
                self.put(node.key, node.value)

    def get(self, key: str) -> object:
        """
        Return the value associated with the given key or None if the key
        is not in the hash.
        """
        index = self.get_index(key)
        node = self._buckets[index].contains(key)
        return None if not node else node.value

    def contains_key(self, key: str) -> bool:
        """
        Return True if the given key is in the hash map and False otherwise.
        """
        index = self.get_index(key)
        node = self._buckets[index].contains(key)
        return node is not None

    def remove(self, key: str) -> None:
        """
        Remove the given key and its associated value from the hash map.
        """
        index = self.get_index(key)
        removed = self._buckets[index].remove(key)
        if removed:
            self._size -= 1
        return

    def get_keys(self) -> DynamicArray:
        """
        Return a DynamicArray that contains all the keys stored in the hash map.
        """
        arr = DynamicArray()
        for index in range(self._capacity):
            for node in self._buckets[index]:
                arr.append(node.key)
        return arr

    def get_index(self, key) -> int:
        """
        Return hashed index.
        """
        return self._hash_function(key) % self._capacity


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    Receive a DynamicArray and return a tuple containing a DynamicArray comprising
    the mode (most occurring) value/s of the array, and an integer that represents
    the highest frequency (how many times they appear). O(N).
    """
    # Separate instance of Chaining HashMap
    map = HashMap(da.length() // 3, hash_function_1)
    arr_freq = DynamicArray()
    size = da.length()
    # Populate hash map with elements and their frequency values
    for index in range(size):
        if not map.contains_key(da[index]):
            map.put(da[index], 1)
        else:
            value = map.get(da[index])
            value += 1
            map.put(da[index], value)
    # Create keys array
    arr_key = map.get_keys()
    freq = 0
    # Populate array with elements of highest frequency
    for idx in range(arr_key.length()):
        # Get the frequency value
        val: int = int(map.get(arr_key[idx]))
        # Get the key
        key = arr_key[idx]
        if val > freq:
            arr_freq = DynamicArray()
            arr_freq.append(key)
            freq = val
        elif val == freq:
            arr_freq.append(arr_key[idx])
    return arr_freq, freq


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "melon", "peach"])
    map = HashMap(da.length() // 3, hash_function_1)
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        map = HashMap(da.length() // 3, hash_function_2)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}\n")
