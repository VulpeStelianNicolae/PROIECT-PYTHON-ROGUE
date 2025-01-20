import random

WIDTH = 10
HEIGHT = 10


MAP = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
player_position = [5,5]
player_health = 100
player_symbol = '@'
monster_health = 20
monster_symbol = 'M'
monsters = []


def spawn_monsters(num_monsters):
    for _ in range(num_monsters):
        monster_pos = [random.randint(0, HEIGHT-1), random.randint(0, WIDTH-1)]
        monsters.append({'position': monster_pos, 'health': monster_health})



def draw_map():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [y, x] == player_position:
                print(player_symbol, end=' ')
            elif any(monster['position'] == [y, x] for monster in monsters):
                print(monster_symbol, end=' ')
            else:
                print('.', end=' ')
        print()


def move_player(direction):
    global player_position
    if direction == 'w' and player_position[0] > 0:
        player_position[0] -= 1
    elif direction == 's' and player_position[0] < HEIGHT - 1:
        player_position[0] += 1
    elif direction == 'a' and player_position[1] > 0:
        player_position[1] -= 1
    elif direction == 'd' and player_position[1] < WIDTH - 1:
        player_position[1] += 1


def fight(monster):
    global player_health
    print(f"Te-ai întâlnit cu un monstru! Lupta începe...")
    while player_health > 0 and monster['health'] > 0:
        print(f"Sănătatea ta: {player_health}, Sănătatea monstru: {monster['health']}")
        action = input("Ce vrei să faci? (atac): ").lower()
        if action == 'atac':
            damage = random.randint(5, 10)
            monster['health'] -= damage
            print(f"Îi provoci {damage} daune monstrului!")
        if monster['health'] <= 0:
            print("Ai învins monstrul!")
            break
        damage = random.randint(1, 5)
        player_health -= damage
        print(f"Monstrul iți provoaca {damage} daune.")
        if player_health <= 0:
            print("Ai murit!")
            break


def check_win():
    if len(monsters) == 0:
        print("Ai câștigat! Ai învins toți monștrii!")
        return True
    return False


def game_loop():
    global player_health, player_position, monsters
    spawn_monsters(3)  
    while player_health > 0:
        draw_map()
        print(f"Sănătatea ta: {player_health}")
        move = input("Mișcă-te (w - sus, s - jos, a - stânga, d - dreapta, p - luptă): ").lower()
        if move in ['w', 'a', 's', 'd']:
            move_player(move)
        elif move == 'p':
           
            monster = next((m for m in monsters if m['position'] == player_position), None)
            if monster:
                fight(monster)
                
                monsters = [m for m in monsters if m['health'] > 0]
            else:
                print("Nu există niciun monstru pe această poziție!")
        else:
            print("Comandă invalidă!")

        if check_win():
            break

    print("Jocul s-a terminat!")

game_loop()
