import os


def main():
    search_app_welcome()
    folder = get_user_folder()
    text = get_text_from_user()
    search_folders(folder, text)


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
    print("Would search {} for {}".format(folder, text))


if __name__ == "__main__":
    main()