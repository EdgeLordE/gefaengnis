import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute("select * from Gefaengnis"))
  return res
  