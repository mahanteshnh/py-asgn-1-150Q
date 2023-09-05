import urllib.request


def print_url_content(url):
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    print(content)


# URL to access
url = 'https://www.example.com'

# print the URL Content
print_url_content(url)
