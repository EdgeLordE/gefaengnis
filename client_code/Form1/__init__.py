from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.current_gefaengnis_id = self.gefaengnisse_drop_down.selected_value 
    self.current_freie_zellen = int(anvil.server.call(('get_freie_zellen'), self.current_gefaengnis_id)[0][0])
    self.current_direktor = str(anvil.server.call(('get_direktor'), self.current_gefaengnis_id)[0][0])


    
    self.label_direktor.text = self.current_direktor 
    self.label_freie_zellen.text = str(self.current_freie_zellen)

    self.current_zellen_list = anvil.server.call(('get_zellennummer_und_anzahl_haeftlinge'),self.current_gefaengnis_id)
    self.current_haeftling_anzahl = 0
    print(self.current_zellen_list)
    
    self.repeating_zellen.items = [{'zellennummer': int(self.current_zellen_list[0][0]), 'anzahl_häftlinge': '1'}, 
                                   {'zellennummer': int(self.current_zellen_list[1][0]), 'anzahl_häftlinge': '2'},
                                   {'zellennummer': int(self.current_zellen_list[2][0]), 'anzahl_häftlinge': '1'}]

    

  def gefaengnisse_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.current_gefaengnis_id = self.gefaengnisse_drop_down.selected_value 

    self.current_freie_zellen = int(anvil.server.call(('get_freie_zellen'), self.current_gefaengnis_id)[0][0])
    self.current_direktor = str(anvil.server.call(('get_direktor'), self.current_gefaengnis_id)[0][0])
    self.label_direktor.text = self.current_direktor 
    self.label_freie_zellen.text = str(self.current_freie_zellen)

 



  
 
