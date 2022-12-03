if __name__ == "__main__":
    with open("data.txt") as f:
        data = f.read().split("\n")
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        points_exercise_1 = 0
        points_exercise_2 = 0

        for sack in data:
            median = int(len(sack) / 2)
            sack1 = set(sack[:median])
            sack2 = set(sack[median:])
            matching = sack1.intersection(sack2)
            for char in matching:
                points_exercise_1 += chars.index(char) + 1

        for batch in range(0, len(data), 3):
            sack1 = set(data[batch])
            sack2 = set(data[batch + 1])
            sack3 = set(data[batch + 2])
            sack_inter = sack2.intersection(sack1)
            matching = sack_inter.intersection(sack3)
            for char in matching:
                points_exercise_2 += chars.index(char) + 1
        print(f"First exercice : {points_exercise_1}")
        print(f"Second exercice : {points_exercise_2}")
