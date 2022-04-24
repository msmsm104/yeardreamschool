class Node():
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable():
    def __init__(self, bucket_size = 1024):
        self.bucket_size = bucket_size
        self.buckets = [[]] * self.bucket_size
        self.size = 0
    
    def put(self, key, value):
        idx = hash(key) % self.bucket_size
        bucket = self.buckets[idx]
        for node in bucket:
            if node.key == key:
                node.data = value
                return
        new_node = Node(key, value)
        bucket.append(new_node)
        self.size += 1
    
    def get(self, key):
        idx = hash(key) % self.bucket_size
        bucket = self.buckets[idx]
        for node in bucket:
            if node.key == key:
                return node.data
        return None
    
    def delete(self, key):
        idx = hash(key) % self.bucket_size
        bucket = self.buckets[idx]
        for node in bucket:
            if node.key == key:
                bucket.remove(node)
                self.size -= 1
                
    def contains(self, key):
        idx = hash(key) % self.bucket_size
        bucket = self.buckets[idx]
        for node in bucket:
            if node.key == key:
                return True
        return False
