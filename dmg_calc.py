import time
import ast


def calc_damage(attack_stats):
    attacker_stat = attack_stats[0]
    attacker_buff = attack_stats[1]
    defense = attack_stats[2]
    defense_buff = attack_stats[3]
    total_attack = 0
    total_defense = 0
    damage_taken = 0
    if attacker_buff is None:
        total_attack = attacker_stat
    else:
        total_attack = (attacker_stat * (1 + attacker_buff))
    if defense_buff is None:
        total_defense = defense
    else:
        total_defense = (defense * (1 + defense_buff))
    damage_taken = round(total_attack - total_defense)
    return damage_taken


while True:
    print("Waiting for Request...")
    time.sleep(2)
    attack_nums = []
    attacked = False

    with open('calc_damage.txt') as f:
        attack = f.read()
        if len(attack) > 2:
            attacked = True
            attack_stats = ast.literal_eval(attack)
            for value in attack_stats.values():
                attack_nums.append(value)
            attack_damage = calc_damage(attack_nums)
            print(f"Damage Calculated: {attack_damage}")
    if attacked:
        f = open('calc_damage.txt', 'w')
        f.writelines(str(attack_damage))
        print("Damage Written to Text File. Ready for next attack.")
        attacked = False
        f.close()

