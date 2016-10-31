import requests

api_token = "ed59e6df342decc4ebbd71aa60e6e23d"
end_point1 = "http://challenge.code2040.org/api/haystack"
end_point2 =  "http://challenge.code2040.org/api/haystack/validate"

def haystack_needle(jsonData):
	haystack = jsonData['haystack']
	needle = jsonData['needle']
	index = 0
	count = 0
	for item in haystack:
		if needle == item:
			index = count
		else:
			count = count + 1
	return index

def send_needle(jsonData):
	index = haystack_needle(jsonData)
	data = {"token" : api_token, "needle" : index}
	content = requests.post(end_point2, json = data)
	print content.content   



def main():
	token = {"token": api_token}
	content = requests.post(end_point1, json = token)
	jsonData = content.json()
	send_needle(jsonData)

    
if __name__  == "__main__":
    main()