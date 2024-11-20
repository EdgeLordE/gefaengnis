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
  res = list(cursor.execute("select name,GID from Gefaengnis"))
  return res

@anvil.server.callable
def get_direktor(GID):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
 
  res = list(cursor.execute(f"select Direktor from Verwaltung where VID={GID}"))
  return res

@anvil.server.callable
def get_freie_zellen(GID):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
 
  res = list(cursor.execute(f"select Anzahl_freie_Zellen from Verwaltung where VID={GID}"))
  return res

@anvil.server.callable
def get_zellennummer_und_anzahl_haeftlinge(GID):
  conn = sqlite3.connect(data_files['gefaengnis.db'])
  cursor = conn.cursor()
  res = list(cursor.execute(f"select zellennummer from Besitzt where GID={GID}"))
  return res



  