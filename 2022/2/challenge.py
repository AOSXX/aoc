if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n")

        points_exercise_1 = 0
        points_exercise_2 = 0

        for games in data:
            ennemy, me = games.split()
            points_exercise_1 += {'X': 1, 'Y': 2, 'Z': 3}[me]
            points_exercise_1 += {
                ('A', 'X'): 3,
                ('A', 'Y'): 6,
                ('A', 'Z'): 0,
                ('B', 'X'): 0,
                ('B', 'Y'): 3,
                ('B', 'Z'): 6,
                ('C', 'X'): 6,
                ('C', 'Y'): 0,
                ('C', 'Z'): 3,
            }[(ennemy, me)]

            points_exercise_2 += {'X': 0, 'Y': 3, 'Z': 6}[me]
            points_exercise_2 += {
                ('A', 'X'): 3,
                ('A', 'Y'): 1,
                ('A', 'Z'): 2,
                ('B', 'X'): 1,
                ('B', 'Y'): 2,
                ('B', 'Z'): 3,
                ('C', 'X'): 2,
                ('C', 'Y'): 3,
                ('C', 'Z'): 1,
            }[(ennemy, me)]
        print(f"First exercice : {points_exercise_1}")
        print(f"First exercice : {points_exercise_2}")
