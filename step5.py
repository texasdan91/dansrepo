import requests
import datetime
import dateutil.parser

api_token = "ed59e6df342decc4ebbd71aa60e6e23d"
end_point1 = "http://challenge.code2040.org/api/dating"
end_point2 =  "http://challenge.code2040.org/api/dating/validate"


def time(time):
	values = {"token" : api_token, "datestamp" :time}
	content = requests.post(end_point2, json = values)
	print content.content   


def main():
	token = {"token": api_token}
	content = requests.post(end_point1, json = token)
	jsonData = content.json()

	datestamp = jsonData['datestamp']
	interval =  jsonData['interval']

	current = dateutil.parser.parse(datestamp, ignoretz = True)
	changeDate = current + datetime.timedelta(hours = 0,seconds = interval)
	laterDate = changeDate.isoformat()+'Z'
	time(laterDate)

    
if __name__  == "__main__":
    main()