# DRF
Django Rest Framework

# JWT
- We can generate, verify and refresh the token in urls.py using JWT's built-in view classes
- Implemented JWTAuthentication in API Authentication


```
--------------------------------------------- Testing the JWT Token (below) ---------------------------------------------
########################## Test JWT token in POSTMAN ##########################
Test JWT token in Postman:
Request: POST
url: http://127.0.0.1:8000/api/gettoken/
url: http://127.0.0.1:8000/api/verifytoken/
url: http://127.0.0.1:8000/api/refreshtoken/
Headers: 
    Key: Content-Type
    Value: application/json
Body:
for gettoken:
{
    "username": "admin",
    "password": "admin"
}

for verifytoken:
{
    "token": "put your access token here before it expires",
}

for refreshtoken:
{
    "refresh": "put your refresh token here before it expires",
}

########################## Test JWT token in CMD using httpie ##########################
Install httpie to run the API from cmd: pip install httpie

hit below commands in cmd:

Get/Generate Token: http POST http://127.0.0.1:8000/api/gettoken/ username="admin" password="admin"

Verify Token:       http POST http://127.0.0.1:8000/api/verifytoken/ token="access_token"

Refresh Token:      http POST http://127.0.0.1:8000/api/refreshtoken/ refresh="refresh_token"

Output:
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzMTA1NTkyLCJpYXQiOjE2ODMwOTUyODcsImp0aSI6IjM4NGM4NWJlMTg5NTRkM2ViYmJjYzU3OTM0Zjg3NzU5IiwidXNlcl9pZCI6MX0.U_eyrQJSxkoWEQ-VZNokSCGSxYtwp37IilRrVpqmu48",

    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzE4MTY4NywiaWF0IjoxNjgzMDk1Mjg3LCJqdGkiOiJkYWJjNTk2MzdmMGY0ZmIzOWE5OGM2NjQ0ZGRjYjFkOCIsInVzZXJfaWQiOjF9.MS5e2Vl3d26Iganda8TVZuJLWq2XD5f_Wp6casNDBeo"
}
```
--------------------------------------------- Testing the API (below) ---------------------------------------------
```
########################## Test API in POSTMAN ##########################
Test API in Postman:
Request: GET
url: http://127.0.0.1:8000/api/studentapi/
Authorization:
    - Bearer Token
    - Token: access_token

Request: POST
url: http://127.0.0.1:8000/api/studentapi/
Authorization:
    - Bearer Token
    - Token: access_token
Body: {
    "name": "amitabh",
    "roll": 106,
    "city": "mumbai"
}

Request: PUT
url: http://127.0.0.1:8000/api/studentapi/1/
Authorization:
    - Bearer Token
    - Token: access_token
Body: {
    "name": "amitabh-updated",
    "roll": 107,
    "city": "mumbai"
}

Request: DELETE
url: http://127.0.0.1:8000/api/studentapi/1/
Authorization:
    - Bearer Token
    - Token: access_token

########################## Test API in CMD using httpie ##########################
GET Request:
http http://127.0.0.1:8000/api/studentapi/ 'Authorization:Bearer access_token'

POST Request:
http -f http://127.0.0.1:8000/api/studentapi/ name="amitabh" roll=106 city="mumbai" 'Authorization:Bearer access_token'

PUT Request:
http PUT http://127.0.0.1:8000/api/studentapi/37 name="amitabh-updated" roll=107 city="mumbai" 'Authorization:Bearer access_token'

DELETE Request:
http DELETE http://127.0.0.1:8000/api/studentapi/37/ 'Authorization:Bearer access_token'
 
```