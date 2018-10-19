import urllib.request

read_page = False
while not read_page:
    try:
        url = input('What URL?')
        page = urllib.request.urlopen(url)
        print('Line 1', page.readline())
        read_page = True
    except:
        print('No such page:', url)