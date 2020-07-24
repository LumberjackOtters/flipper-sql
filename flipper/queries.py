def databases():
    query = """
        SELECT `SCHEMA_NAME` from `INFORMATION_SCHEMA`.`SCHEMATA` WHERE `SCHEMA_NAME` NOT IN ( "mysql", "information_schema", "performance_schema");
    """
    return query

def create_database(db):
    query = """
        SHOW CREATE DATABASE %s;
    """ % (db)
    return query

def tables(db):
    query = """
        SHOW TABLES FROM %s;
    """ % (db)
    return query

def create_table(db, table):
    query = """
        SHOW CREATE TABLE %s.%s;
    """ % (db, table)
    return query