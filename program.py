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
    match_count = 0
    for match in matches:
        match_count += 1
    print(match_count )


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
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)



def search_file(filename, search_text):
    with open(filename, 'r', encoding='utf-8') as fin:

        for line in fin:
            if line.lower().find(search_text) >= 0:
                yield line


if __name__ == "__main__":
    main()