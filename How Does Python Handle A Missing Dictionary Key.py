# https://www.youtube.com/watch?v=6H5RDXmcjZM
# How Does Python Handle A Missing Dictionary Key?
# Custom dictionary class.
# The __missing__ method is invoked when
#  a key is not found in the dictionary.
class DefaultDict(dict):
    def __missing__(self, key):
        return f"***Missing: {key}"
# Here's how we use 
#  our DefaultDict class:
d = DefaultDict()
# Missing key: apple
print(d['apple'])
# What if we just use a regular dictionary
#  and try to access a missing key?
myDict = dict() # Empty dictionary
try:
#   This will raise a KeyError
    print(myDict['banana']) 
except KeyError as e:
    print(f"KeyError: {e}")
