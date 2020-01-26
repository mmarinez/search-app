import os


def main():
    search_app_welcome()
    folder = get_user_folder()
    if not folder:
        print("Sorry we can't search that location")
        return

    text = get_text_from_user()
    if not text:
        print("Sorry we can't search for nothing!")
        return

    matches = search_folders(folder, text)

    for match in matches:
        print(match)


def search_app_welcome():
    print("--------------------------")
    print("        SEARCH APP")
    print("--------------------------")


def get_user_folder():
    folder = input("What folder do you want to search on? ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_text_from_user():
    text = input("What text do you want to search? ")
    return text


def search_folders(folder, text):
    all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            matches = search_folders(full_item, text)
            all_matches.extend(matches)
        else:
            matches = search_file(full_item, text)
            all_matches.extend(matches)

    return all_matches


def search_file(filename, search_text):
    matches = []
    with open(filename, 'r', encoding='utf-8') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = search_folders()
                matches.append(line)

        return matches


if __name__ == "__main__":
    main()