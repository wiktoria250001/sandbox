import requests
    class User:
        def __init__(self, miasto): -> object:
            self.miasto = miasto

        def pogoda_z(self, miasto: str):
            url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
            return requests.get(url).json()

    npc_1=User(miasto="warszawa") #linijki do tworzenia nazwy
    npc_2=User(miasto="zamosc")
    print(npc_1.miasto)
    print(npc_2.miasto)

    print(npc_1.pogoda_z(npc_1.miasto))
    print(npc_2.pogoda_z(npc_2.miasto))

    pogoda_z("warszawa")
