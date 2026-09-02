# Entry point for the team directory tool


def get_entries():
    try:
        with open("team.txt") as f:
            content = f.read()
            return content.strip().split("\n\n")
    except FileNotFoundError:
        print("Error: team.txt not found. Returning an empty team list.")
        return []
    except OSError as e:
        print(f"Error: could not read team.txt ({e}). Returning an empty team list.")
        return []


def count_entries():
    return len(get_entries())


def search_by_name(name):
    entries = get_entries()

    for entry in entries:
        if name.lower() in entry.lower():
            return entry

    return "Not found"


def filter_by_role(role_query):
    entries = get_entries()
    return [entry for entry in entries if role_query.lower() in entry.lower()]


print("Team Directory Tool")
print()

print("Team Members:")
print(open("team.txt").read())

print("Total entries:", count_entries())

print()
print("Search result:")
print(search_by_name("Andiswa"))

print()
print("Filter by role 'Software Developer Trainee':")
for entry in filter_by_role("Software Developer Trainee"):
    print(entry)
    print()