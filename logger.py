# -----------------------------------------------+
# TinyDB Based Logger System - Accalina          +
# -----------------------------------------------+

# IMPORT ----------------------------------------+
from tinydb import TinyDB, Query

# INIT ------------------------------------------+
db = TinyDB('db.json')

# CLASS -----------------------------------------+
class logger():
    def __init__(self, logname):
        self.db = TinyDB("{}.log".format(logname))

    def write(self, text):
        self.db.insert(text)

    def selectAll(self):
        return self.db.all()

    def search(self, expression):
        mainlog = Query()
        exec("global result; result = self.db.search(mainlog.{})".format(expression))
        return result

    def update(self, base_expression, target_expression=1):
        mainlog = Query()
        # exec("global result; result = self.db.update({},mainlog.{})".format(base_expression, target_expression))
        # self.db.update({'division':'research'}, mainlog.name == 'liliana')
        result = self.search(base_expression)[0]
        return result

# RUN -------------------------------------------+
if __name__ == "__main__":
    log = logger('log')
    # log.write({'name':'lily','callsign':'shark','division':'research'})
    # print(log.selectAll())
    print(log.update("division == 'research'"))
    print(log.update({'callsign':'shark'},"name == 'liliana'"))

# END -------------------------------------------+
