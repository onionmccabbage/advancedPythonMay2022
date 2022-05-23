# requests can make get, post, put , delete etc. calls
import requests

def makePost():
    url = 'https://httpbin.org/post' # a free echo service - echoes anythbnig we might send to it
    payload = {'item':'Ocelot', 'status':'admin'}
    try:
        res = requests.post(url, data=payload) # send our payload as a 'post' request
        # did we rececive a response?
        print(res.text)
    except Exception as err:
        print( err )

if __name__ == '__main__':
    makePost()