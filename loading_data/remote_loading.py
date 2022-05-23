# we may need to access data from an external API
# here we will access the API at 
# https://jsonplaceholder.typicode.com/
# we can access /users /todos /photos or /albums
import sys # sys is the current system upon which Python is running
import requests # we may need to python -m pip install requests

def makeCall(cat='users', id=0): # set sensible defaults
    url = 'https://jsonplaceholder.typicode.com/'
    # url = 'https://nonsuch.com'
    category = cat
    # if ID is zero, get ALL teh data members
    if id==0:
        id='' # send no parameter for the ID
    else:
        id = id # send a numeric value for the id
    try: # good idea to wrap code in a try-except block
        # the Python 'requests' library lets us 'get' or 'post' etc.
        response = requests.get( '{}{}/{}'.format( url, category, id ) )
        print(type(response))
        print(response) # if we receive 200 that means everyhnig worked out fine. 400 would be a problem!!
        data = response.json() # we just want the JSON returned from the request
        print(data)
    except Exception as err:
        print(err) # we might log this to a file or handle it some other way

if __name__ == '__main__':
    # we can check to see if any system argument values were passed in
    print(sys.argv) # any system aruments will exist in a list.
    if len(sys.argv) > 1:
        category = sys.argv[1] # we realyl ought ot validate this to check it is a non-empty string
        id = sys.argv[2] # ... and this must be a positive integer
    else:
        category = 'photos'
        id = 2
    # makeCall('posts') # call with no id, so we get ALL the values
    makeCall(category, id)