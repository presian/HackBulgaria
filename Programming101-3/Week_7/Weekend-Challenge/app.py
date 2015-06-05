import json
import requests
from bs4 import BeautifulSoup
from histogram import Histogram


def getHtml():
    return requests.get("http://register.start.bg/").text


def makeSoup(html):
    return BeautifulSoup(html)


def getBoxWithBoxLinks(soup):
    return soup.select("#boxes")[0]


def getLinkBoxes(box):
    return[x.get('href') for x in box.find_all('a')]


def getAllValidLinks(links):
    return [x[12:] for x in links if (x is not None) and (len(x) > 10 and x[:12] == 'link.php?id=')]


def chekForRedirection(headers):
    return 'location' in headers


def makeRequestTo(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    try:
        r = requests.head(url, headers=headers, timeout=2, allow_redirects=True)
        server = r.headers['server']
        return server
    except Exception:
        return None


def makeUrl(link_number):
    return "http://register.start.bg/link.php?id={}".format(link_number)


def getRowSeversData(valid_links):
    return [makeRequestTo(makeUrl(x)) for x in valid_links if x is not None]


def getServersDict(all_servers):
    h = Histogram()
    for server in all_servers:
        if server is not None:
            if 'apache' in server.lower():
                h.add('Apache')
            if 'nginx' in server.lower():
                h.add('nginx')
            if 'IIS' in server.upper():
                h.add('IIS')
    return h


def writeToFile(histogram):
    histogram_file = open("servers.json", "w")
    histogram_file.write(json.dumps(histogram, sort_keys=True, indent=4, separators=(',', ': ')))
    histogram_file.close()


def main():
    html = getHtml()
    soup = makeSoup(html)
    box = getBoxWithBoxLinks(soup)
    links = getLinkBoxes(box)
    valid_links = getAllValidLinks(links)
    all_servers = getRowSeversData(valid_links)
    histogram = getServersDict(all_servers)
    writeToFile(histogram.get_dict())
    print(histogram.get_dict())

    # print (all_servers)
    # print(all_valid_redirected_links)


if __name__ == '__main__':
    main()
