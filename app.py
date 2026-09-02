print("Team Directory Tool")

with open("team.txt") as f:
    print(f.read())

    def count_entries():
        with open("team.txt") as f:
            return f.read().count("Name:")