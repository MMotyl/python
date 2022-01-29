import json

event = {}
event['code'] = 'Test'

print (event)

txt = json.dumps(event, ensure_ascii=False, indent=4)

print (txt)