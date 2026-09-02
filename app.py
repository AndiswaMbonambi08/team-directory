# Entry point for the team directory tool


def get_entries():
    with open("team.txt") as f:
        content = f.read()
        return content.strip().split("\n\n")


def count_entries():
    return len(get_entries())


def search_by_name(name):
    entries = get_entries()

    for entry in entries:
        if name.lower() in entry.lower():
            return entry

    return "Not found"


print("Team Directory Tool")
print()

print("Team Members:")
print(open("team.txt").read())

print("Total entries:", count_entries())

print()
print("Search result:")
print(search_by_name("Andiswa"))