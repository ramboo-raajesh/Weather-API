import os
import requests

city = input("Enter the city: ")

params = {
  'access_key': '02aee7fd5aed7f3acf3f6b9e15d883b0',
  'query': city
}

api_result = requests.get('http://api.weatherstack.com/current', params)

try:
    # Make the API request and parse the response
    response = api_result
    response.raise_for_status()  # raise an exception if the response status code is not 200
    data = response.json()

    # Extract the weather information and print it to the console
    location = data['location']['name']
    temperature = data['current']['temperature']
    print(f"In {location} the temperature is: {temperature} C")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"Response error: {e} key not found in response")
