import requests

#asking user to enter the location
print("Which city you want to see the weather")
city = input()

#creating full URL with user's credentials
params = {
  'access_key': '02aee7fd5aed7f3acf3f6b9e15d883b0',
  'query': city
}

api_result = requests.get('http://api.weatherstack.com/current', params)
api_response = api_result.json()
print("In {} there is {}°C\n".format(api_response['location']['name'],api_response['current']['temperature']))

# check if user wants to see extra details
extra = input("Do you want to see extra details? (y/n): ")

# print categorized data based on user input
if extra.lower() == "y":
    print("\nWeather Data:")
    print("Temperature:", api_response['current']['temperature'], "C")
    print("Weather Description:", api_response['current']['weather_descriptions'][0])
    print("Wind Speed:", api_response['current']['wind_speed'], "km/h")
    print("Humidity:", api_response['current']['humidity'], "%")
    print("Cloud Cover:", api_response['current']['cloudcover'], "%")

    print("\nLocation Data:")
    print("Name:", api_response['location']['name'])
    print("Country:", api_response['location']['country'])
    print("Region:", api_response['location']['region'])
    print("Latitude:", api_response['location']['lat'])
    print("Longitude:", api_response['location']['lon'])

    print("\nTime Data:")
    print("Timezone ID:", api_response['location']['timezone_id'])
    print("Local Time:", api_response['location']['localtime'])
    print("UTC Offset:", api_response['location']['utc_offset'])
else:
    print("Temperature:", api_response['current']['temperature'], "C")
    print("Weather Description:", api_response['current']['weather_descriptions'][0])
