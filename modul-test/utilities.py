from settings import database_folder
import os


def getAbsolutePath(table_name):
    return os.path.join(database_folder, table_name)
