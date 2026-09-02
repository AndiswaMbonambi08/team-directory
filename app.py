# Entry point for the team directory tool
print("Team Directory Tool")

with open("team.txt") as f:
    print(f.read())

    def count_entries():
        with open("team.txt") as f:
            return f.read().count("Name:")

        print("Total entries:", count_entries())

        def search_by_name(name):
            with open("team.txt") as f:
                content = f.read()
                entries = content.split('\n\n')  
                for entry in entries:
                    if name in entry:
                        return entry
                    return "Not found"

                print(search_by_name("Andiswa"))