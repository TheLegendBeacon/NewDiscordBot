import sqlite3
import os

df = "Databases/data.db"
backup = "Databases/backup.db"

class DoesNotExist(Exception):
  pass

def start_connection(file):
  conn = sqlite3.connect(file)
  return conn

def close_connection(connection, commit):
  connection.commit()
  connection.close()

def db_set_prefix(guild_id, prefix="!"):
  conn = start_connection(df)
  cursor = conn.cursor()
  cursor.execute("Select `id` from prefixes")
  ids = cursor.fetchall()
  try:
    max_id = ids[-1][0]
  except:
    max_id = 0
  tbw_id = max_id + 1
  arg = f"INSERT INTO Prefixes(id, ServerID, Prefix) Values(?, ?, ?)"
  try:
    cursor.execute(arg, (tbw_id, guild_id, prefix))
  except sqlite3.IntegrityError:
    pass
  close_connection(conn, True)

def db_update_prefix(guild_id, prefix):
  conn = start_connection(df)
  cursor = conn.cursor()
  arg = "UPDATE Prefixes\nSET Prefix = ? WHERE ServerID = ?"
  cursor.execute(arg, (prefix, guild_id))
  close_connection(conn, True)

def db_delete_prefix(guild_id):
  conn = start_connection(df)
  cursor = conn.cursor()
  cursor.execute("DELETE FROM Prefixes WHERE ServerID=?", (guild_id))
  close_connection(conn, True)

def read_all_prefix():
  conn = start_connection(df)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Prefixes")
  returndata = {}
  data = cursor.fetchall()
  for entry in data:
    returndata[entry[1]] = entry[2]
  close_connection(conn, False)
  return returndata 

def db_set_welcome_message(guild_id, message, channelid):
  conn = start_connection(df)
  cursor = conn.cursor()
  cursor.execute("Select `id` from welcome_messages")
  ids = cursor.fetchall()
  try:
    max_id = ids[-1][0]
  except:
    max_id = 0
  tbw_id = max_id + 1
  arg = f"INSERT INTO welcome_messages(id, ServerID, message, channel) Values(?, ?, ?, ?)"
  try:
    cursor.execute(arg, (tbw_id, guild_id, message, channelid))
  except sqlite3.IntegrityError:
    pass
  close_connection(conn, True)

def db_update_welcome_message(guild_id, message, channelid):
  conn = start_connection(df)
  cursor = conn.cursor()
  arg = "UPDATE welcome_messages\nSET message = ?\nSET channel = ? WHERE ServerID = ?"
  cursor.execute(arg, (message, channelid, guild_id))
  close_connection(conn, True)

def db_delete_welcome_message(guild_id):
  conn = start_connection(df)
  cursor = conn.cursor()
  try:
    cursor.execute("DELETE FROM welcome_messages WHERE ServerID=?", (guild_id))
    close_connection(conn, True)
  except:
    close_connection(conn, False)
    raise DoesNotExist


def read_all_welcome_messages():
  conn = start_connection(df)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM welcome_messages")
  returndata = {}
  data = cursor.fetchall()
  for entry in data:
    returndata[entry[1]] = entry[2]
  close_connection(conn, False)
  return returndata 

def get_roles_by_server(guild_id):
  conn = start_connection(df)
  cursor = conn.cursor()  
  returndata = {}
  cursor.execute("select * from ReactionRoles where ServerID=?", (guild_id))
  data = cursor.fetchall()
  for x in data:
    if not returndata[x[2]]:
      returndata[x[2]] = [[x[3], x[4]]]
    else:
      returndata[x[2]].append([x[3], x[4]])
  close_connection(conn, True)
  return returndata

def remove_role(role_id):
  conn = start_connection(df)
  cursor = conn.cursor()
  cursor.execute("DELETE FROM ReactionRoles WHERE RoleID=?", (role_id))
  close_connection(conn, True)



def backup():
  os.remove("Databases/backup.db")
  conn = start_connection(df)
  cursor = conn.cursor()
  cursor.execute(".clone ?", (backup))
  close_connection(conn, True)  