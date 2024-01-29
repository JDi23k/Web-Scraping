import requests
url = "https://courses.wscubetech.com/"
response =requests.get(url)
print(response.status_code)  # to get the status code
print(response.text) # to get the whole html of the page