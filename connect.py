import requests
import pprint
import pandas as pd

api_key = " "
api_key_v4 = " "

# HTTP request METHODS
"""
GET -> grab data
POST -> add/update data

PATCH
PUT
DELETE
"""

# what's the endpoint (or a url)

# what's the HTTP method needed

"""
Endpoint:
GET /movie/{movie_id}

Example API request:
https://api.themoviedb.org/3/movie/550?api_key=0e6720adc41d2a3b9a0e4610032e69e6
"""

# Using v4
"""
headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
}
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
r = requests.get(endpoint, headers= headers) # json={"api_key":api_key}
print(r.status_code)
print(r.text)
"""

# Using v3
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
# r = requests.get(endpoint) # json={"api_key":api_key}
# print(r.status_code)
# print(r.text)

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "Your Name"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
#print(endpoint)
r = requests.get(endpoint)
#pprint.pprint(r.json())

if r.status_code in range(200,299):
    data = r.json()
    results = data['results']
    #results[0].keys() gives out key-value pairs
    if len(results) > 0:
        print(results[0].keys())
        movie_ids = set()
        for i in results:
            _id = i['id']
            #print(i['title'], _id)
            movie_ids.add(_id)
        #print(list(movie_ids))

output = 'movies.csv'
movies_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200,299):
        data = r.json()
        movies_data.append(data)
        
df = pd.DataFrame(movies_data)
print(df.head())
df.to_csv(output, index=False)