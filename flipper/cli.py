import click, os, pprint
import subprocess
import flipper.dbconnector
import flipper.queries
import flipper.parser


@click.command()
@click.option('--server', prompt=True,
              default=lambda: 'localhost')
@click.option('--user', prompt=True,
              default=lambda: os.environ.get('USER', ''))
@click.password_option()


def process(server, user, password):
# @click.option("--in", "-i", "in_file", required=True,
#     help="Path to csv file to be processed.",
# )

    tables_statements = {}
    connection = flipper.dbconnector.connect(server, user, password)
    databases = flipper.dbconnector.execute_read_query(connection, flipper.queries.databases())
    for db in databases:
        
        db_name = db['SCHEMA_NAME']
        
        create_database_statement = flipper.dbconnector.execute_read_query(connection, flipper.queries.create_database(db_name))
        
        tables = flipper.dbconnector.execute_read_query(connection, flipper.queries.tables(db_name))
        
        for table in tables:
            
            table_name = table["Tables_in_%s" % (db_name)]
            create_table = flipper.dbconnector.execute_read_query(connection, flipper.queries.create_table(db_name, table_name))
            
            tables_statements[table_name] = flipper.parser.parse_table(create_table[0]["Create Table"])
            flipper.parser.parse_fields_and_constraints(tables_statements[table_name]["fields_and_constraints"])
        # pprint.pprint(tables_statements)