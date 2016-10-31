import requests

api_token = "ed59e6df342decc4ebbd71aa60e6e23d"
end_point1 = "http://challenge.code2040.org/api/reverse"
end_point2 =  "http://challenge.code2040.org/api/reverse/validate"
 

def main():
	token = {"token": api_token}
	content = requests.post(end_point1, json = token)
	send_word(content.content)

def send_word(word):
	#uses the reverse the word and stores in the variable
	reverseWord = word[::-1]
	data = {"token" : api_token, "string" : reverseWord}
	content = requests.post(end_point2,json = data)
	print content.content   

    
if __name__  == "__main__":
    main()