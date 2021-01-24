import base64

txt = 'base64 encoded string'
txt = txt.encode("UTF-8")
encoded = base64.b64encode(txt)
print(encoded)
# 'YmFzZTY0IGVuY29kZWQgc3RyaW5n'