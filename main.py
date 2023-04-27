import requests

params = {
  'access_key': '02aee7fd5aed7f3acf3f6b9e15d883b0',
  'query': 'Chennai'
}

api_result = requests.get('http://api.weatherstack.com/current', params)

api_response = api_result.json()

print("In chennai the tempreature is: ", api_response['current']['temperature']," C",api_response['current']['weather_descriptions'],api_response['current']['humidity'],api_response['current']['feelslike'])