import os


class Change(object):
    changeInfo = None
    conn = None
    changeURL = None

    def __init__(self, conn, changeId):
        self.conn = conn
        self.changeInfo = self.conn.GET(os.path.join("a/changes/", changeId))
        self.changeURL = os.path.join("a/changes/", self.changeInfo.id)

    def rebase(self):
        address = os.path.join(self.changeURL, "rebase")
        return self.conn.POST(address)
