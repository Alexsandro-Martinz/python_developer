
class Person:
    
    def __init__(self) -> None:
        self._name = "default name"

    def get_name(self):
        return self._name
    
    def set_name(self, name) -> None:
        if name:
            self._name = name

    name = property(get_name, set_name, "name property")
    

p = Person()
p.name = None

print(p._name)