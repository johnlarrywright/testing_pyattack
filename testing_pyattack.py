#!/usr/bin/python3

import argparse
from pyattck import pyattck
attack = pyattck.Attck()
  
def py_attack(mal):
    for actor in attack.actors:
        print(actor.name)
   # for malware in actor.malware:
    #       print(malware.name)
        #if malware.name == mal:
            #for actor in attack.actors:
             #   print(actor.name)

      
        
    
                
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog= 'Malware',
        description= 'The Malware name that associates with actors'
    )
    parser.add_argument('malware', help= 'Malware actors')

    args = parser.parse_args()

    
    py_attack(args.malware)

          #print('Description', malwares.description)
       # for actor in attack.actors:
            #print(actor.name)
        #    for malware in actor.malware:
        #        print(malware.name)
            
            #print(techniques)
            #for actor in attack.actors:
                #print(actor.name)
                #for malwares in actor.malware
               # print(malwares.name)
            #print(techniques.name)
            #for mitigation in techniques.mitigation:
            #    print(mitigation)
        #for mitigation in malwares.mitigation:
        #    print(mitigation.description)
        #print('Platform', malwares.platforms)
        #print('ID', malwares.id)
        #print('Name: ', malwares.name)
        #print('actors', malwares.actors)
        #print('Mitgations', attack.mitigations)
        #print(malwares)
        
        #for techniques in attack.techniques:
        #        print(techniques.name)
        #        for mitigation in techniques.mitigation:
        #            print(mitigation)