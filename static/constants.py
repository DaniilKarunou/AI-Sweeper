models = "static/sprites/"
temp = "./temporaryFiles/"
tree_path = "./AI/DT/"
grass = "grass_new.jpg"
rock = "sand.jpg"
big_rock = "bigrock.jpg"
water = "water.jpg"
bomb_to_int = { "grass": 1,
                "rock": 2,
                "water": 4
                }
bombid_to_img = {0: "mine.png",
                 1: "grenade.png",
                 2: "water_mine.png",
                 3: "air_bomb.png",
                 4: "c4.png",
                 5: "fake_bomb.png",
                 6: "hand_bomb.png",
                 7: "molotov.png",
                 8: "nuke_bomb.png",
                 9: "tnt.png"}

walls = [(3,2),
         (6,3),
         (2,1),
         (8,8),
         (3,3),
         (7,0),
         (1,7),
         (0,9),
         (9,7),
         (6,2),
         (2,0),
         (9,0),
         (8,5),
         (6,4),
         (0,3),
         (1,5),
         (10,9),
         (11,8),
         (6,13),
         (12,7),
         (13,1),
         (12,0)]
bombs = {"Mine": "mine.png",
         "Grenade": "grenade.png",
         "WaterMine": "water_mine.png",
         "AirBomb": "air_bomb.png",
         "C4": "c4.png",
         "FakeBomb": "fake_bomb.png",
         "HandBomb": "hand_bomb.png",
         "Molotov": "molotov.png",
         "NukeBomb": "nuke_bomb.png",
         "TNT": "tnt.png"}
