import os


class Change(object):
    changeInfo = None
    conn = None
    changeURL = None

    def __init__(self, conn, changeId):
        self.conn = conn
	# TODO: introduce "authenticated" boolean filed in the ConnectionHelper
	# and use it to decide whether to add "a/" in the path.
        self.changeInfo = self.conn.GET("/".join(["a/changes", changeId]))
        self.changeURL = "/".join(["a/changes", self.changeInfo.id])

    def rebase(self):
        address = os.path.join(self.changeURL, "rebase")
        return self.conn.POST(address)
