import requests as rq 
result = rq.post("http://165.227.106.113/post.php",data= {"username": "admin", "password": "71urlkufpsdnlkadsf"})
print(result.text)
