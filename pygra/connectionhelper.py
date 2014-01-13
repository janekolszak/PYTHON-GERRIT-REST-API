import os
import requests
import json

from collections import namedtuple
from requests.auth import HTTPDigestAuth


class ConnectionHelper(object):
    url = None
    user = None
    password = None

    def __str__(self):
        return self.user + ":" + self.password + " " + self.url

    def __init__(self, user, password, url):
        self.url = url
        self.user = user
        self.password = password

    def POST(self, address, data=None):
        return self.send(address, "POST", data)

    def GET(self, address):
        return self.send(address, "GET")

    def PUT(self, address, data):
        return self.send(address, "PUT", data)

    def send(self, addr, method, data="{}"):
        address = os.path.join(self.url, addr)
        headers = {'Content-Type': 'application/json;charset=UTF-8',
                   'Accept': 'application/json'
                   }
        if method == "GET":
            response = requests.get(url=address,
                                    headers=headers,
                                    auth=HTTPDigestAuth(self.user, self.password))

        elif method == "PUT":
            response = requests.put(url=address,
                                    headers=headers,
                                    auth=HTTPDigestAuth(self.user, self.password),
                                    data=data)

        elif method == "POST":
            response = requests.post(url=address,
                                     headers=headers,
                                     auth=HTTPDigestAuth(self.user, self.password),
                                     data=json.dumps(None))

        responseJSON = response.content.replace(')]}\'', '', 1)

        def filterKeys(keys):
            # Field names can't start with '_'
            newKeys = []
            for k in keys:
                if k[0] == '_':
                    newKeys.append(k[1:])
                else:
                    newKeys.append(k)

            return newKeys
        try:
            return json.loads(responseJSON, object_hook=lambda d: namedtuple('GerritEntity', filterKeys(d.keys()))(*d.values()))

        except:
            return responseJSON

