import requests

CLIENT_ID = '9e7190b2ea4d0ea70d7e'
CLIENT_SECRET = '74c0cfbeb40c7f40f55c14335019f9dfd30abce1'
QUERY_URL = '?client_id={}&client_secret={}'
URL = 'https://api.github.com/users/{}'


def do_you_follow(user):
    query_str = (URL + QUERY_URL).format(user, CLIENT_ID, CLIENT_SECRET)
    query = requests.get(query_str)
    json = query.json()
    followers_url = json['followers_url']
    print((followers_url + QUERY_URL).format(CLIENT_ID, CLIENT_SECRET))
    followers_response = requests.get((followers_url + QUERY_URL).format(CLIENT_ID, CLIENT_SECRET))
    followers_list = followers_response.json()
    return len([x['login'] for x in followers_list])


def main():
    do_you_follow('presian')

if __name__ == '__main__':
    main()
