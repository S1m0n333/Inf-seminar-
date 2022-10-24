# utocne sily 2 ,1, 0,5 ,0
# {"normal": {"normal":1,......}}
#1 jason ktory mam - dostat do pythonu a  nacitat do rozumnej struktury
#2 tuto strukturu transformovat na to čo potrebujem - utok["atacker"]["defender"]
# kniznice -  requests,urllyb
import requests
import json

translator = {"super effective": 2, "normal effective": 1, "not very effective": 0.5, "no effect": 0}
attacks = {}
data = requests.get("https://raw.githubusercontent.com/yorkcshub/Miscellanous/master/effectiveness.json")
data_json = json.loads(data.text)


for power in data_json:
    for attacker in data_json[power]:
        temp = attacks.get(attacker, {})
        for defender in data_json[power][attacker]:
            temp[defender] = translator[power]
        attacks[attacker]=temp

def attack(at1, at2, pokemons):
    pokemons = pokemons.split(",")
    team_1 = []
    team1point = 0
    team_2 = []
    team2point = 0

    for i in range(0,at1):
        team_1.append(pokemons[i])
    for j in range(0,at2):
        team_2.append(pokemons[j+at1])
    #print(list_pok)
    #print(team_1)
    #print(team_2)
    for x in team_1:
        for y in team_2:
            x_1 = x.split()
            y_2= y.split()
            zoz = []
            for z in x_1:
                zoz2 = []
                for l in y_2:
                    zoz2.append(attacks[z][l])
                result = 1
                for m in zoz2:
                    result = result * m
                zoz.append(result)
            team1point += max(zoz)
    for i in team_2:
        for j in team_1:
            i2 = i.split()
            j2 = j.split()
            zoz3 = []
            for x in i2:
                zoz4 = []
                for y in j2:
                    zoz4.append(attacks[x][y])
                result = 1
                for n in zoz4:
                    result = result * n
                zoz3.append(result)
            team2point += max(zoz3)
    if team1point > team2point:
        return team1point, team2point, "ME"
    elif team1point < team2point:
        return team1point, team2point, "FOE"
    else:
        return team1point, team2point, "EQUAL"

print(attack(2,6,"Psychic Dark,Fire,Ghost Ice,Fairy Electric,Normal Steel,Ghost,Poison Fire,Dark Bug"))


