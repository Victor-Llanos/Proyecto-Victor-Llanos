import requests
from Cuarto import Cuarto
api = requests.get("https://api-escapamet.vercel.app")

class Pasillo(Cuarto):
    def __init__(self,cuarto):
        super().__init__(cuarto)

    pasillo = '''

                                                        _...--""|'-.
                                                _...--"         |   '-.
                                        _...--"                 |      '-.
                                _...--"                         |         '-.
                        _...--"                                 |      |'.   '-.
                _...--"          _..--¨"|                       |      |  '-.   '-.
         ...--"                 |       |                       |      |    |      |
        |                       |      ,|                _...--" '-.   |    |      |
        |                       |     []|        _...--"            '-.|   °|      |
        |                       |       |_...--"                       '.   |      |
        |                       | _...--"                                '-.|      |        
        |     |'-._       _...--"                                            '-.   |     
        |     |    |..--"                                                       '-.|
        |_...-|    |                                                       _...--""            
        '-.   |    |                                               _...--"                   
           '-.|    |                                       _...--"                              
              '-.  |                               _...--"                                       
                 '-|                       _...--"                                     
                   '-.            _...--"                              
                      '-. _...--"                
            
            Te encuentras en los Pasillo de Labs, Si... Ese olor es Sistemas 

        Para inspeccionar la puerta que se encuentra en el centro. Press 1
        
    Inserta R para ir a Biblioteca
    Inserta L para ir a Laboratorios
    '''

    pasillo_2 = '''

                                                        _...--""|'-.
                                                _...--"         |   '-.
                                        _...--"                 |      '-.
                                _...--"                         |         '-.
                        _...--"                                 |      |'.   '-.
                _...--"          _..--¨"|                       |      |  '-.   '-.
         ...--"                 |\      |                       |      |    |      |
        |                       | \     |                _...--" '-.   |    |      |
        |                       |  \    |        _...--"            '-.|   °|      |
        |                       |  |    |_...--"                       '.   |      |
        |                       |  |.--"                                 '-.|      |        
        |     |'-._       _...--\  |                                         '-.   |     
        |     |    |..--"        \ |                                            '-.|
        |_...-|    |          ,   \|                                       _...--""            
        '-.   |    |          []                                   _...--"                   
           '-.|    |                                       _...--"                              
              '-.  |                               _...--"                                       
                 '-|                       _...--"                                     
                   '-.            _...--"                              
                      '-. _...--"                
            
            Te encuentras en los Pasillo de Labs, Si... Ese olor es Sistemas 

        Para inspeccionar la puerta que se encuentra en el centro. Press 1
        
    Inserta R para ir a Biblioteca
    Inserta L para ir a Laboratorios
    ''' 

    def room(self,rooms,players):
        if not api.json()[3]["objects"][0]["game"]["award"] in players[0].inventario:
            print(Pasillo.pasillo)
            rooms.append(self.name)
            return rooms
        else: 
            print(Pasillo.pasillo_2)
            rooms.append(self.name)
            return rooms