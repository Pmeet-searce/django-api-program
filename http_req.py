import requests
import json

def my_get():
    x = requests.get("http://localhost:8000/employees/")
    print(x.json())

my_get()
y = requests.post("http://localhost:8000/employees/",json={ "first_name":"searce", "last_name":"rajkot" })
print(y)
my_get()

z = requests.put("http://localhost:8000/employees/5/",json = { "first_name":"searce1", "last_name":"rajkot1" })
print(z)
my_get()

w = requests.delete("http://localhost:8000/employees/5/")
print(w)
my_get()
