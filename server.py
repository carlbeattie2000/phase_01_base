import Pyro4
from mysql_connection import connect_to_mysql

config = {
        "host": "127.0.0.1",
        "port": "1234",
        "user": "root",
        "password": "mypasssword",
        "database": "phase_01"
}

cnx = connect_to_mysql(config, attempts=3)


@Pyro4.expose
class TaxPayers(object):
    def get_tax_payer(self, name):
        with cnx.cursor() as cursor:
            query = ("SELECT * FROM tax_payers WHERE first_name = %s")
            cursor.execute(
                    query,
                    [name])
            row = cursor.fetchone()
            cursor.close()
            return row


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(TaxPayers)
ns.register("example.tax_payers", uri)

print("Ready.")
daemon.requestLoop()
