import json

def main():
    a = [{'name':'PC', 'cost':500, 'detail':{'a':'True', 'b':[1,2,3,4]}},{'name':'Screen','cost':250, 'detail':{'a':'False', 'b':[9,8,7,6]}}]
    # convert this Python structure to JSON
    a_j = json.dumps(a) # this will iteratively convet any hierarchichal structure into a JSON text string
    print(type(a))
    print(type(a_j))
    # we can covnert back
    b = json.loads(a_j)
    print(b)

# we can use JSON to encode a class
class Item: # this implicitlyy inherists from 'object'
    '''
    this class encapsulated items that have a name and a cost
    Name is a string, cost is a positive float'''
    def __init__(self, name, cost):
        self.name = name #this will call the property setter methods
        self.cost = cost
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            self.__name = 'default'
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost):
        if type(cost) == float and cost >= 0:
            self.__cost = cost
        else:
            self.__cost = 0.00

class ItemEncoder(json.JSONEncoder): # we inherit fro mthe built-in JSON encoder
    def default(self, obj): # here we override the built-in 'default' of JSONEncoder
        # check wer are dealing with an 'Item' instance
        if isinstance(obj, Item):
            return obj.__dict__ # return whatever we wish to encode
        else:
            # if it is NOT an Item instance, just use the default ecoding
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    main()
    z = Item('Zoe', 28.00) # expects a string and a float
    # can we JSON encode the class instance?
    # z_j = json.dumps(z) # fail
    z_j = json.dumps(z, cls=ItemEncoder) # usee our encoder to encodee an instance of an Item
    print(z_j)
    # we coan just serializee the __dict__ of ANY class
    x = json.dumps(z.__dict__)
    print(x)