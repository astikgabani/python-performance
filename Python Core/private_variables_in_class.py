class Vector:

    def __init__(self, **coords):
        private_coords = {'_'+ k: v for k, v in coords.items()}
        self.__dict__.update(private_coords)

    def __delattr__(self, name):
        raise AttributeError("Can't access this variable")

    def __getattr__(self, name):
        raise AttributeError("Can't access this variable")

    def __setattr__(self, name, value):
        raise AttributeError("Can't access this variable")

    def set_attr(self, x, val):
        self.__dict__.update({'_'+x : val})
    
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, ", ".join("{k}={v}".format(k=k[1:], v=self.__dict__[k]) for k in sorted(self.__dict__.keys())))

v = Vector(x=5, y=5)
print(v)
v.set_attr("x", 10)
print(v)
v.x = 10  # will raise the exceptions
v._x = 10  # will also raise the exceptions
