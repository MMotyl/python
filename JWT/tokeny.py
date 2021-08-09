import jwt
import json 
from jwt.algorithms import get_default_algorithms

token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJxYzhBOGw0aDlrVWo4UkpUUWFKWUZQVlFvRDdZWmJaX3FYSHg3N2kwTi1jIn0.eyJleHAiOjE2MTYwODUwNDYsImlhdCI6MTYxNjA4NDc0NiwianRpIjoiOGNhODA1OTItYjk0Zi00YzdlLWE5YTktMjQzZTk2YTc5MWY1IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay50ZXN0dW5pcWEucGwva2V5Y2xvYWsvcmVhbG1zL25vbi1wcm9kIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRjNzhkOWU3LTFjYmYtNGYyOC05ZTcxLTgwNzdiMjlmYzcyNSIsInR5cCI6IkJlYXJlciIsImF6cCI6Ind3dy1mb3JtLW9ic2x1Z293ZSIsInNlc3Npb25fc3RhdGUiOiI4YjljNGRhZi01MDIyLTRlN2ItOTVjZi0zYTdlYzMxMzg5NzYiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6InByb2ZpbGUgZW1haWwiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsIm5hbWUiOiJmMDB3d3dmb3Jtb2JzbHVnb3dlIEtleWNsb2FjayIsInByZWZlcnJlZF91c2VybmFtZSI6ImYwMHd3d2Zvcm1vYnNsdWdvd2UiLCJnaXZlbl9uYW1lIjoiZjAwd3d3Zm9ybW9ic2x1Z293ZSIsImZhbWlseV9uYW1lIjoiS2V5Y2xvYWNrIn0.HrkRgvVodTlWRNq7WI3EMbnv3LSrafF_P2cPLp3oz2WtO1K5FKU98aO7HfwOW3aJsgVLemNnmciQ3NnpPJVlxQOXPPAkXUTFoGw24qQX7698ZO_mqSZ9nJGf5mh4Y7rZ4y42k0MD0aNTDHUuPAiqkLqrGJQwqBlxUmoXXtPAREYUwH6IFcpYWDay-3L2cUoMpTPk1pEoNwgj-x8EucbEqWphd70ZXkHG1HE2Tn1ntNh_HT5_golRK1haPyCyzLfe3b6hPYKsh1ctddWlO6MlW78sKlIuMLk-DUaK7mBo9esC6eyWr6XZNu2Xd3dHGsdgTeqOUx_cAGbiWx3itH-2Ew' 
token_decoded  = jwt.decode(token,   options={"verify_signature": False} ) # verify=False, algorithms=["HS256"])
header_decoded = jwt.get_unverified_header(token)

header_decoded.pop('kid', None ) # {'alg': 'HS256', 'typ': 'JWT'}
token_decoded['aud'] = 'TIA-API'

# token_decoded['exp'] = '1616281105' # datetime.datetime.utcnow() 

secret = 'x/6vbIqpa6bdKOAKNOwl3TkpgmM3DriD3i57Spa1vhHUqBWoiEGW0nlJTywZoHts'
encoded_jwt = jwt.encode(token_decoded, secret, algorithm='HS256', headers = header_decoded)

# print(header_encoded)
# print(token_encoded)  
# print( json.dumps(token_decoded, ensure_ascii=False, indent=4) )  

print(encoded_jwt)  

#def_alg = get_default_algorithms()
# token_decoded  = jwt.decode(encoded_jwt, secret, algorithms =def_alg.get('RS256') )
token_decoded  = jwt.decode(encoded_jwt, secret, algorithms = ['HS256','RS256'] )

try:
    token_decoded  = jwt.decode(encoded_jwt, secret, algorithms="sha256")
    print('certyfikat ok')
except:
    print('błąd certyfikatu')
