import requests

api_token = "ed59e6df342decc4ebbd71aa60e6e23d"
end_point1 = "http://challenge.code2040.org/api/prefix"
end_point2 =  "http://challenge.code2040.org/api/prefix/validate"

def main():
	token = {"token": api_token}
	content = requests.post(end_point1, json = token)
	jsonData = content.json()
	send_prefix(jsonData)

def prefix(jsonData):
	strings = jsonData['array']
	prefix = jsonData['prefix']
	array = [ ]
	for item in strings:
		if prefix  not in item:
			array.append(item)
	return array

def send_prefix(jsonData):
	array = prefix(jsonData)
	data = {"token" : api_token, "array" : array}
	content = requests.post(end_point2, json = data)   
	print content.content




    
if __name__  == "__main__":
    main()