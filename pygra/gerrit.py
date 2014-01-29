from change import Change
from connectionhelper import ConnectionHelper


class Gerrit(object):
    conn = None

    def __init__(self, user, password, url):
        self.conn = ConnectionHelper(user, password, url)

    def testConnection(self):
        return self.conn.GET("a/changes/?q=status:open&n=1")

    def getChange(self, changeId):
        return Change(self.conn, changeId)



def main(argv):
    from netrc import netrc
    from urlparse import urlparse
    import json

    url = argv[1]
    changeId = argv[2]

    n = netrc()
    user, account, password = n.authenticators(urlparse(url).netloc)

    gerrit = Gerrit(user, password, url);


    change = gerrit.getChange(changeId)
    print json.dumps(change.changeInfo, sort_keys=True, indent=4)

    # r = change.rebase()
    # print r

if __name__ == "__main__":
    import sys
    main(sys.argv)
