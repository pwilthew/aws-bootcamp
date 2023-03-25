from psycopg_pool import ConnectionPool
import os

class Db:
  def __init__(self):
    self.init_pool()

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

  # Commit data such as an insert
  def query_commit(self):
    try:
      conn = self.pool.connection()
      cur =  conn.cursor()
      cur.execute(sql)
      conn.commit() 
    except Exception as err:
      self.print_sql_err(err)
      #conn.rollback()

  # Return a json object
  def query_array_json(self,sql):
    print("SQL STATEMENT-[array]------")
    print(sql + "\n")
    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        json = cur.fetchone()
        return json[0]
  
  # Return an array of json objects
  def query_object_json(self,sql):
    print("SQL STATEMENT-[object]-----")
    print(sql + "\n")
    wrapped_sql = self.query_wrap_object(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        json = cur.fetchone()
        return json[0]

  def query_wrap_object(self,template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql

  def query_wrap_array(self,template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql

  def print_sql_err(self,err):
    # Get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # Get the line number where exception occured
    line_num = traceback.tb_lineno

    # Print the connect() error
    print("\npsycopg error:", err, "on line number:", line_num)
    print("psycopg traceback:", traceback, "-- type:", err_type)

    # psycopg2 extensions.Diagnostics object attribute
    print("\nextensions.Diagnostics:", err.diag)

    # print the pgcode and pgerror exceptions
    print("pgerror:", err.pgerror)
    print("pgcode:", err.pgcode, "\n")

db = Db()