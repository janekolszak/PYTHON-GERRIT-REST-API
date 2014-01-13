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



def main():
    gerrit = Gerrit("", "", "")

    changeId = ""

    change = gerrit.getChange(changeId)
    print change.changeInfo.id

    r = change.rebase()

    print r

if __name__ == "__main__":
    main()