class map_props:
    def __init__(self):
        self._store = {}

    def put(self, key, values):
        self._store[key] = values

    def get(self, key):
        return self._store.get(key)
    
    def view(self):
        return self._store
    
    def delete(self, key):
        return self._store.pop(key, None)
    
    def clear(self):
        return self._store.clear()

Map=map_props()
Map.put(1,"Python")
Map.put(2,"Java")
print(Map.view())
print(Map.get(1))
print(Map.get(2))
print(Map.delete(2))
print(Map.view())
Map.clear()
print(Map.view())