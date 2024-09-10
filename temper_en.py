# =========================================================================
#  A program to check temperature information by region and recommend clothing
# =========================================================================
# 1) Fetching weather information
import requests
import datetime

# Weather service API URL
weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

# General authentication key (encoded value)
encoding_key = "Cvzl0n5R3aZ7Jtzmam8s6AcplvKGhMhWZxouzD12WqweqwGuLWpmczItRO8cOdT5bhHkmUdKDIb3vh79f7ulmw%3D%3D" 

# Base date (today's date in YYYYMMDD format)
base_date = datetime.datetime.today().strftime("%Y%m%d")  

# Base time (default 0800, 8 AM)
base_time = "0800"   

# Request user input for region selection. Prompt them to enter a valid number.
while True:
    try:
        area = int(input(
            "1  Seoul     2  Busan     3  Daegu     4  Incheon\n"
            "5  Gwangju   6  Daejeon   7  Ulsan     8  Sejong\n"
            "9  Gyeonggi  10 Chungbuk  11 Chungnam  12 Jeonnam\n"
            "13 Jeonbuk   14 Gyeongbuk 15 Gyeongnam 16 Jeju\n"
            "17 Gangwon\n"
            "\nEnter the number corresponding to your region: "
        ))
        print()
        
        # Exit the loop if a number between 1 and 17 is entered
        if 1 <= area <= 17:
            break
        else:
            # Display a message if an invalid number is entered
            print("Please enter a valid number.") 
    except ValueError:
        # Display a message if a non-numeric value is entered
        print("Please enter a valid number.")

# If the area value is valid, set latitude and longitude coordinates corresponding to the region
if area == 1:
    nx = "59"
    ny = "126"  # Latitude and longitude for Seoul
    region = "Seoul"
elif area == 2:
    nx = "98"
    ny = "76"   # Latitude and longitude for Busan
    region = "Busan"
elif area == 3:
    nx = "89"
    ny = "90"   # Latitude and longitude for Daegu
    region = "Daegu"
elif area == 4:
    nx = "55"
    ny = "124"  # Latitude and longitude for Incheon
    region = "Incheon"
elif area == 5:
    nx = "58"
    ny = "74"   # Latitude and longitude for Gwangju
    region = "Gwangju"
elif area == 6:
    nx = "67"
    ny = "100"  # Latitude and longitude for Daejeon
    region = "Daejeon"
elif area == 7:
    nx = "102"
    ny = "84"   # Latitude and longitude for Ulsan
    region = "Ulsan"
elif area == 8:
    nx = "66"
    ny = "103"  # Latitude and longitude for Sejong
    region = "Sejong"
elif area == 9:
    nx = "60"
    ny = "120"  # Latitude and longitude for Gyeonggi-do
    region = "Gyeonggi"
elif area == 10:
    nx = "69"
    ny = "107"  # Latitude and longitude for Chungbuk
    region = "Chungbuk"
elif area == 11:
    nx = "68"
    ny = "100"  # Latitude and longitude for Chungnam
    region = "Chungnam"
elif area == 12:
    nx = "51"
    ny = "67"   # Latitude and longitude for Jeonnam
    region = "Jeonnam"
elif area == 13:
    nx = "63"
    ny = "89"   # Latitude and longitude for Jeonbuk
    region = "Jeonbuk"
elif area == 14:
    nx = "87"
    ny = "106"  # Latitude and longitude for Gyeongbuk
    region = "Gyeongbuk"
elif area == 15:
    nx = "90"
    ny = "77"   # Latitude and longitude for Gyeongnam
    region = "Gyeongnam"
elif area == 16:
    nx = "52"
    ny = "38"   # Latitude and longitude for Jeju
    region = "Jeju"
elif area == 17:
    nx = "73"
    ny = "134"  # Latitude and longitude for Gangwon
    region = "Gangwon"

# Construct the data required for the API request
load_data = "serviceKey=" + encoding_key + "&" + \
          "dataType=json" + "&" + \
          "base_date=" + base_date + "&" + \
          "base_time=" + base_time + "&" + \
          "nx=" + nx + "&" + \
          "ny=" + ny

# Create a dictionary to store the response data
data = dict()
data['date'] = base_date
weather = dict()

# Request weather information
res = requests.get(weather_url + load_data)
# Extract necessary data from the API response
items = res.json().get('response').get('body').get('items')
for item in items['item']:
    # Fetch temperature (TMP) information
    if item['category'] == 'TMP':
        weather['tmp'] = item['fcstValue']

data['weather'] = weather

# Extract current temperature information
items1 = res.json().get('response').get('body').get('items')
items1['item']
for item in items1['item']:
    if item['category'] == 'TMP':
        current_temperature = int(item['fcstValue'])

# ============================================================================================================================================
# Using Naver Shopping Search OpenAPI
# ============================================================================================================================================

# Define a function for Naver shopping search
def naver_shop_search(query, display):
    # Set the authentication headers for the Naver application
    headers = {
        "X-Naver-Client-Id": "3JKKhUYF8FQCQxm0owkD",    # client_id of Naver application
        "X-Naver-Client-Secret": "TPonc2ZJLB"           # client_secret key of Naver application
    }
    # Set the request parameters for Naver shopping search
    params = {
        "query": query,                                 
        "display": display,         
        "sort": "date"
    }
    # Naver Shopping Search API URL
    naver_shop_url = "https://openapi.naver.com/v1/search/shop.json" 
    # Send Naver Shopping search request   
    res = requests.get(naver_shop_url, headers=headers, params=params)   
    if res.status_code == 200:
        # Check the Naver Shopping search results
        items = res.json().get('items')                     
        # Extract only the 'link' field from each item and return as a list
        links = [item['link'] for item in items]
        return links
    return []

# Set clothing recommendations based on temperature and define search terms
if current_temperature >= 23:
    temperature = "Sleeveless, Shorts, T-shirt, Skirt"
elif 20 <= current_temperature < 23:
    temperature = "T-shirt, Light shirt, Shorts, Cotton pants"
elif 17 <= current_temperature < 20:
    temperature = "Light cardigan, Long-sleeved shirt, Cotton pants, Jeans"
elif 12 <= current_temperature < 17:
    temperature = "Light knit, Cardigan, Sweatshirt, Light jacket, Cotton pants, Jeans"    
elif 9 <= current_temperature < 12:
    temperature = "Jacket, Cardigan, Military jacket, Sweatshirt, Knit stockings, Jeans, Cotton pants"
elif 5 <= current_temperature < 9:
    temperature = "Coat, Heattech, Knit, Jeans, Leggings"
else:
    temperature = "Padded jacket, Thick coat, Fleece items, Scarf"

# Split recommended clothing into search terms
search_terms = temperature.split(", ")

# Output: Region, current temperature, recommended clothing, and shopping links
print(f"Region: {region}\n")
print(f"Current temperature: {current_temperature}°C\n")
print(f"Recommended clothing: {temperature}\n")
print("Links to purchase these items are as follows:")
print("----------------------------------------")

# Perform Naver shopping search for each term
for term in search_terms:
    # Get 2 result links for each search term
    result_links = naver_shop_search(term, 2)  
    print(f"Search results for {term}")
    for link in result_links:
        print(link)
    print()
print("----------------------------------------")
