class Requester:

    request = 'https://api.github.com/users/'
    
    def __init__(self):
        self._credentials = ''
        self._set_credentials()

    def _set_credentials(self):
        result = []
        file = open('credentials.txt', 'r')
        content = file.read().split()
        result = content
        self._credentials = '?client_id={}&client_secret={}'.format(result[0], result[1])
        file.close()

    def following(self, username):
        Requester.request += '{}/following'.format(username)
        Requester.request += self._credentials
        return Requester.request

    def is_following(self, username, target):
        Requester.request += '{}/following/{}'.format(username, target)
        Requester.request += self._credentials
        return Requester.request

r = Requester()
print(r.following('shosh'))

