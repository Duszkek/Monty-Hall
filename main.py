from random import randint


result = []
rounds = 10000


class Door:
    index = -1
    prize = "poop"

    def __init__(self, index):
        self.index = index

    def __str__(self):
        return "Prize in Door[" + str(self.index) + "]: " + str(self.prize)


def print_game_doors(doors):
    for door in doors:
        print(door)


def generate_doors(integer):
    doors = [Door(1), Door(2), Door(3)]
    doors[integer].prize = "1000000$"
    return doors


def remove_one_poop_door(doors, player_door):
    for door in doors:
        if door.index != player_door and door.prize == "poop":
            doors.remove(door)
            return doors

    return doors


def switch_index(doors, player_door_idx):
    for door in doors:
        if door.index != player_door_idx:
            return door.index

    return -1


def get_result(doors, player_door):
    for door in doors:
        if door.index == player_door:
            if door.prize == "poop":
                return False
            return True
    return False


def analyze_results(results):
    won = 0
    lost = 0
    no_of_games = 0

    for res in results:
        no_of_games += 1
        if res:
            won += 1
        else:
            lost += 1

    won_string = "Percentage of games WON: " + str(won / no_of_games)
    lost_string = "Percentage of games LOST: " + str(lost / no_of_games)
    return print(won_string, lost_string)


if __name__ == '__main__':
    iterations = 0

    while iterations < rounds:
        game_doors = generate_doors(randint(0, 2))
        # print_game_doors(game_doors)
        chosen_door = randint(0, 2)
        game_doors = remove_one_poop_door(game_doors, chosen_door)
        # print_game_doors(game_doors)
        chosen_door = switch_index(game_doors, chosen_door)
        result.append(get_result(game_doors, chosen_door))
        iterations += 1

    analyze_results(result)
