from .models import DatabaseAdapter
import rethinkdb as r

config = json.load(open('config.json'))

RDB_ADDRESS = config['rdb_address']
RDB_PORT = config['rdb_port']
RDB_DB = config['rdb_db']


class Rdb_Provider(DatabaseAdapter):
    def __init__(self):
        super().__init__()
        self.connection = r.connect(RDB_ADDRESS, RDB_PORT, db=RDB_DB)

    def get_key(self, key):
        return r.table('keys').get(key).run(self.connection)

    def get_keys_for(self, user_id):
        return r.table('keys').filter(r.row['owner'] == user_id).run(self.connection)

    def create_application(self, application):
        r.table('applications').insert(application).run(self.connection)

    def create_key(self, key):
        r.table('keys').insert(key).run(self.connection)

    def get_keys_sorted_by(self, order_key, ordering):
        func = r.asc if ordering == 'ascending' else r.desc
        return r.table('keys').order_by(func(order_key)).run(self.connection)

    def get_applications_ordered_by(self, order_key):
        return r.table('applications').order_by(order_key).run(self.connection)

    def get_application(self, application_id):
        return r.table('applications').get(application_id).run(self.connection)

    def delete_application(self, application_id):
        r.table('applications').get(application_id).delete().run(self.connection)

    def delete_key(self, key):
        r.table('keys').get(key).delete().run(self.connection)

    def is_key_valid(self, key):
        return r.table('keys').get(key).coerce_to('bool').default(False).run(self.connection)

    def update_key_data(self, key, data):
        r.table('keys').get(key).update(data).run(self.connection)

    def close(self):
        self.connection.close()
