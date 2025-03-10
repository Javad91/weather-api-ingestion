import requests
import json
import boto3


s3 = boto3.client('s3')

api_key = 'Your API key'  # Replace with your OpenWeather API key: https://home.openweathermap.org/api_keys
city = 'Melbourne'  # You can change this to any city you like
country = "AU"

def fetch_weather_data():
    # Step 1: Get Geolocation (Latitude & Longitude)
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={api_key}"
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()

    if not geo_data:
        return {"error": "City not found!"}

    lat = geo_data[0]['lat']
    lon = geo_data[0]['lon']

    # Step 2: Get Weather Data using Latitude & Longitude
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    return weather_data

# resource1: https://openweathermap.org/api/geocoding-api#direct
# resource2: https://openweathermap.org/current

weather_data = fetch_weather_data()
print(weather_data)

def upload_data_to_s3(data):
    bucket_name = 'weather-api-ingestion-aws-bucket'  # Replace with your bucket name
    file_name = 'weather-data.json'  # File name in S3
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data),
        ContentType='application/json'
    )
    print('Data uploaded successfully to S3')

# Lambda handler function
def lambda_handler(event, context):
    try:
        # Fetch the weather data for the city
        weather_data = fetch_weather_data()
        
        # Write the fetched data to S3
        upload_data_to_s3(weather_data)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"Successfully fetched weather data for Melbourne and uploaded to S3")
        }

    except Exception as e:
        # Handle any error and return a failure response
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }