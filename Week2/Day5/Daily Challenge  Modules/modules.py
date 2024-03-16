import requests
import time


def get_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        load_time = end_time - start_time
        return load_time, response.status_code
    except:
        return None, None

websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for website in websites:
    load_time, status_code = get_load_time(website)
    if load_time is not None:
        print(f"Website: {website}, Load Time: {round(load_time,2)} seconds, Status Code: {status_code}")
    else:
        print(f"Website: {website}, Load Time: Error occurred")