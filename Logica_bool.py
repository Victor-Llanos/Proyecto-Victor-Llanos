from Game import Game
from Player import Player
import random
import requests

api = requests.get("https://api-escapamet.vercel.app")

class Logica_bool(Game):
    def __init__(self,cuarto,juego):
        super().__init__(cuarto,juego)
        number = self.number
        self.question = self.juego["game"]["questions"][number]["question"]
        self.answer = self.juego["game"]["questions"][number]["answer"]
        

    def game(self,players):

        martillo = True

        #if "martillo" in players[0].invetario: 
        if martillo:
            
            print(self.name,"\n")
            print("Reglas:",self.rules,"\n")

            print(self.question)
            resp = input("> ")

            if resp == self.answer:
                print("Correcto!!")
                print("Has conseguido:",self.award)
                #players[0].inventario.append(self.award)

            else:
                print("Incorrecto!!")
                #players[0].vidas -= 0.5
                
        if not martillo:
            print(api.json()[3]["objects"][0]["game"]["message_requirement"])

logica_bool = Logica_bool(cuarto = 3, juego = 0)