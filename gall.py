# GALL - Games Library Lister
# by Patryk Piekarski 2026
#
# A simple Python tool for creating a sorted list of your game collection.
#
# Folder structure:
# Drive\Decades\Years\GameTitleFolder
#
# Example:
# D:\Games\1990-1999\1993\Doom
#
# Output:
# GAME_LIST.txt with sorted list of games.

from pathlib import Path


def scan_library(root):
    """
    Scan game library folder and return dictionary:
    {year: [games]}
    """

    games = {}

    for decade in root.iterdir():

        if decade.is_dir():

            for year in decade.iterdir():

                if year.is_dir() and year.name.isdigit():

                    year_number = int(year.name)
                    game_list = []

                    for game in year.iterdir():

                        if game.is_dir():
                            game_list.append(game.name)

                    game_list.sort()

                    if game_list:
                        games[year_number] = game_list

    return games


def save_list(root, games):
    """
    Save sorted game list to GAME_LIST.txt
    """

    output = root / "GAME_LIST.txt"

    with open(output, "w", encoding="utf-8") as f:

        for year in sorted(games.keys()):

            f.write(f"{year}\n")
            f.write("-" * 30 + "\n")

            for game in games[year]:
                f.write(f"{game}\n")

            f.write("\n")

    return output


def main():

    root = Path(input("Please enter main folder path: "))

    # Check folder
    if not root.exists():
        print("Error: Folder doesn't exist.")
        return

    if not root.is_dir():
        print("Error: Path is not a folder.")
        return


    print("\nScanning library...\n")

    games = scan_library(root)

    if not games:
        print("No games found.")
        return


    output = save_list(root, games)


    # Statistics
    total_games = sum(len(game_list) for game_list in games.values())


    print("\nGame list is ready.")
    print("----------------------")
    print(f"Years scanned: {len(games)}")
    print(f"Games found: {total_games}")
    print(f"Saved to:")
    print(output)
    input("\nPress ENTER to exit...")



if __name__ == "__main__":
    main()