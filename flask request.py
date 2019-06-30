import requests
#r= requests.get('https://api.github.com/user',auth=('mitalshivam1789@gmail.com','@Shivam!12%'))
#print(r.status_code) # returns the status code , 200 status code means get successfully.
# to known more about status code search https status code
#print(r.headers['content-type'])
#print(r.encoding)
#print(r.text) # to get all the context under this api and it will give u  the html code
#print(r.json())
s=requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL')
print(s.text)
r=requests.get('http://api.github.com/')
r= requests.post('http://httpbin.org/post',data={"key":"value"})
r=requests.put("http://httpbin.org/put",data = {"key":"value"})
print(r)
