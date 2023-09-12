from bs4 import BeautifulSoup
import threading
import requests
import re


def save_proxies():
    with open('proxies.txt', 'w') as f:
        url = "https://spys.me/proxy.txt"
        req = requests.get(url=url)
        pattern = re.compile("\\d{1,3}(?:\\.\\d{1,3}){3}(?::\\d{1,5})?")
        matcher = re.findall(pattern, req.text)
        for i in matcher:
            f.write(i + '\n')

        pubproxy_url = 'http://pubproxy.com/api/proxy'
        pubproxy_response = requests.get(pubproxy_url)
        src = pubproxy_response.json()
        a = src['data']
        for l in a:
            pub = l['ipPort']
            f.write(pub + '\n')

        spys_url = "https://spys.me/proxy.txt"
        req_spys = requests.get(url=spys_url)
        pattern = re.compile("\\d{1,3}(?:\\.\\d{1,3}){3}(?::\\d{1,5})?")
        matcher = re.findall(pattern, req_spys.text)
        for i in matcher:
            f.write(i + '\n')

        url = 'http://www.httptunnel.ge/ProxyListForFree.aspx'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        ter = soup.find_all("tr")
        for k in ter:
            pattern = re.compile("\\d{1,3}(?:\\.\\d{1,3}){3}(?::\\d{1,5})?")
            matcher1 = re.findall(pattern, k.text)
            for j in matcher1:
                f.write(j + '\n')

        static_url = 'http://static.fatezero.org/tmp/proxy.txt'
        static_response = requests.get(static_url)
        f.write(static_response.text)

        github_url = 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt'
        github_response = requests.get(github_url)
        f.write(github_response.text)

        github2_url = 'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt'
        github2_response = requests.get(github2_url)
        f.write(github2_response.text)

        multiproxy_url = 'https://multiproxy.org/txt_all/proxy.txt'
        multiproxy_response = requests.get(multiproxy_url)
        f.write(multiproxy_response.text)

        rootjazz_url = 'http://rootjazz.com/proxies/proxies.txt'
        rootjazz_response = requests.get(rootjazz_url)
        f.write(rootjazz_response.text)


def validate_proxy(proxy):
    proxies = {
        "http": f'http://{proxy}',
        "https": f'https://{proxy}',
    }

    try:
        r = requests.get('http://icanhazip.com/', proxies=proxies)
        if r.status_code == 200:
            print(proxy, 'ВАЛИДНЫЙ СУКА!')
    except:
        print(proxy, 'НИХУЯ НЕ НЕВАЛИДНЫЙ!')


def validation_proxy():
    file = open('proxies.txt', 'r')
    proxies = ''.join(file.readlines()).strip().split('\n')

    threads = []
    for proxy in proxies:
        t = threading.Thread(target=validate_proxy, args=(proxy,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def main():
    validation_proxy()


if __name__ == '__main__':
    main()