class Hashtable():
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def first_hash(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def insert(self, key, value):
        first_hashed = self.first_hash(key)
        if not self.keys[first_hashed]:
            self.keys[first_hashed] = key
            self.values[first_hashed] = value
        else:
            rehashed = self.rehash(first_hashed)
            while not self.keys[rehashed] and \
                    self.keys[rehashed] != key:  # 如果键已经存在就覆盖
                rehashed = self.rehash(key)

            # 跳出循环时，可能是self.keys[rehashed]为空，也可能是发现存在key
            self.keys[rehashed] = key
            self.values[rehashed] = value

    def get(self, key):
        first_hashed = self.first_hash(key)
        if self.keys[first_hashed] == key:
            return self.values[first_hashed]
        else:
            rehashed = self.rehash(first_hashed)
            while self.keys[rehashed] != key:
                if rehashed == first_hashed:
                    break
                rehashed = self.rehash(rehashed)
            if self.keys[rehashed] == key:
                return self.values[rehashed]
            else:
                raise ValueError('key {} not found'.format(key))

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.insert(key, value)
