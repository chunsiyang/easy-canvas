from app.tools.db_tools import get_connection, get_collection
from app.tools.init_requirement_tools import app_config
from app.tools.sha1_tools import sha1_encode


def init_database():
    """
        init database creat database if no exist
    :return: mongo database object
    """
    connection = get_connection()
    database = None
    db_list = connection.list_database_names()
    if not app_config['DB']['DBNAME'] in db_list:
        database = connection[app_config['DB']['DBNAME']]
        database.add_user(app_config['DB']['USER'], app_config['DB']['PWD'])
    return database


def init_data():
    """
        init data (insert user admin if no exist)
    :return:
    """
    collection = get_collection('user')
    if collection.find_one({"name": "admin"}) is None:
        admin_user = app_config["ADMIN"]
        admin_user["password"] = sha1_encode(admin_user["name"] + admin_user["password"])
        admin_user["roles"] = "admin"
        collection.insert(admin_user)


def init_db_and_data():
    init_database()
    init_data()
