import requests
import openai
import os

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
    print("Humidity:", api_response['current']['humidity'], "%")
    print("Cloud Cover:", api_response['current']['cloudcover'], "%")
    current = api_response['current']['temperature'],"C","Weather Description:", api_response['current']['weather_descriptions'][0],"Weather Description:", api_response['current']['weather_descriptions'][0],"Humidity:", api_response['current']['humidity'], "%","Cloud Cover:", api_response['current']['cloudcover'], "%"

    print("\nLocation Data:")
    print("Name:", api_response['location']['name'])
    print("Country:", api_response['location']['country'])
    print("Region:", api_response['location']['region'])
    print("Latitude:", api_response['location']['lat'])
    print("Longitude:", api_response['location']['lon'])
    location = "Name:", api_response['location']['name'],"Country:", api_response['location']['country'],"Region:", api_response['location']['region']

    print("\nTime Data:")
    print("Timezone ID:", api_response['location']['timezone_id'])
    print("Local Time:", api_response['location']['localtime'])
    print("UTC Offset:", api_response['location']['utc_offset'])
else:
    print("Temperature:", api_response['current']['temperature'], "C")
    print("Weather Description:", api_response['current']['weather_descriptions'][0])

#making more with ChatGPT API
print("\n\nAsk for any other informations,like...")
choices = ["How do I get warm", "How do I get chill", "Is there any food for this climate"]

for choice in choices:
    print(choice)

   
option = input()

details = 'y'
print("\n\n\nGPT started to run")
while(details =='y'):
   
   # Define the API endpoint
   api_url = 'https://api.openai.com/v1/chat/completions'

# Set up the request headers
   headers = {
       'Authorization': 'Bearer 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',
       'Content-Type': 'application/json'
   }

# Define the payload (input prompt and parameters)
   data = {
       'messages': [
           {'role': 'system', 'content': 'You are'},
           {'role': 'user', 'content': 'The current weather is" {current} "in "{location}" ,{option}'}
       ],
       'model': 'gpt-3.5-turbo'  # Specify the model version
   }


# Send the request
   response = requests.post(api_url, headers=headers, json=data)

# Process the response
   if response.status_code == 200:
    # Get the generated response from the API
       chat_result = response.json()['choices'][0]['message']['content']
       print('ChatGPT:', chat_result)
   else:
       print('Request failed:', response.text)
   print("Wanna more y/n")
   details = input()

if(details == 'n'):
   print("Thank you for using me")
else:
   pass