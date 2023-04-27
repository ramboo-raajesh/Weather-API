import requests

#asking user to enter the location
print("Which city you want to see the weather")
city = input()

#creating full URL with user's creditionals
params = {
  'access_key': '02aee7fd5aed7f3acf3f6b9e15d883b0',
  'query': city
}

api_result = requests.get('http://api.weatherstack.com/current', params)
api_response = api_result.json()

#Printing the short report
print("In {} the tempreature is: {}C".format(api_response['location']['name'],api_response['current']['temperature']))

#prompting for further details
print("Do you wanna see further details...! yes/no")
details =  input()
if details == "yes":
    print(api_response)
else:
    pass
