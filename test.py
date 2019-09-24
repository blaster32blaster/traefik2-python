import sqlalchemy as db

ip = '172.19.0.4'
trae = 'mysql-database'
alias = 'mysql'

in_port = 4314
out_port = 3306

# specify database configurations
config = {
    'host': alias,
    'port': out_port,
    'user': 'root',
    'password': 'mysql_root_password1',
    'database': 'MYSQL'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')
# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = db.create_engine(connection_str)
connection = engine.connect()
# # pull metadata of a table
# metadata = db.MetaData(bind=engine)
# metadata.reflect(only=['test_table'])

# test_table = metadata.tables['test_table']
print(connection)