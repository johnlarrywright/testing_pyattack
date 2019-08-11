#!/usr/bin/python3

import argparse
from pyattck import pyattck
attack = pyattck.Attck()
  
def py_attack():
    #for malwares in attack.malwares:
        #print('Description', malwares.description)
        #print('Platform', malwares.platforms)
        #print('ID', malwares.id)
        #print('Name: ', malwares.name)
        #print('actors', malwares.actors)
        #print('Mitgations', attack.mitigations)
        #print(malwares)

        for techniques in attack.techniques:
                print(techniques)

                
if __name__ == "__main__":
    py_attack()
