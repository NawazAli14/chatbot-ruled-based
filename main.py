import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')

import time
import sys

answer_A = ["A", "a", "A.", "a."]
answer_B = ["B", "b", "B.", "b."]
answer_C = ["C", "c", "C.", "c."]
yes = ["Y", "y", "Yes", "yes", "YES"]
no = ["N", "n", "No", "no", "NO"]

# ----- Return Name -----
def returnname():
    print("What's your name? (Enter your name only)")
    global name
    name = input(">>> ")
    if name == "exit":
        print("Goodbye!")
        sys.exit()
    elif name == "help":
        instructions()
    elif name == "return":
        mainmenu()
    else:
        print("Wow! Cool name,", name, "!")


# ----- Instructions -----
def instructions():
    """Prints instructions on how to operate the chatbot."""
    print(
        "I am a robot with a wide feature set!\nFirst off, I returned your name at the beginning of the program!\nFurthermore, I can:"
    )
    print(
        "- Find Information about something you want to learn (Powered by Wikipedia)"
    )
    print(
        'Operating me is very simple, from the main menu, type the number that corresponds to the action.\nThen, you can follow the on-screen prompts to tell me what to do.'
    )


# ---------- Main Menu  ----------
def main_menu_validate(x):
    """Input validation for mainmenu() function"""
    if x == "1":
        wikichat()
    elif x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
        time.sleep(1)
        mainmenu()
    elif x == "return":
        mainmenu()
    else:
        return False


def mainmenu():  # Main Function
    """Asks the user what they want to do and redirects accordingly"""
    print(
        "\nWhat do you want to do? Type the number that corresponds to the action."
    )
    time.sleep(1)
    print(
        "\n\n[1] Find Information about something you want to learn (Powered by Wikipedia)"
    )
    x = input(">>> ")
    main_menu_result = main_menu_validate(x)
    if main_menu_result == False:
        while main_menu_result == False:
            print("Please enter a valid input:")
            x = input(">>> ")
            main_menu_result = main_menu_validate(x)


# -- Return to Main Menu (Kapilesh Pennichetty) --
def wiki_return_validate(x):
    """Validates input for wiki_return() function."""
    if x in yes:
        mainmenu()
    elif x in no:
        wikichat()
    else:
        return False


def wiki_return():
    """Returns to the mainmenu() function from the wikichat() function"""
    print("Do you want to return to the main menu?")
    x = input(">>> ")
    if x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        wiki_validation_result = wiki_return_validate(x)
        if wiki_validation_result == False:
            while wiki_validation_result == False:
                print("Please enter a valid input (yes or no):")
                x = input(">>> ")
                wiki_validation_result = wiki_return_validate(x)


# ----- Retrieve Summary of Wikipedia Article  -----
def wiki_article_validate(articlename):
    """Validates the input for the wikichat() function"""
    page_py = wiki_wiki.page(articlename)
    if page_py.exists() == True:
        print("Here you go,", name, ":")
        print(
            "Page - Title: %s" % page_py.title
        ) 
        print(
            "Page - Summary: %s" % page_py.summary
        )  
    else:
        return False
    return page_py


def wikichat():  # Main Function
    """Prompts the user to enter the name of a Wikipedia article to retrieve the summary of said article."""
    print("What do you want to learn about? (Powered by Wikipedia)")
    x = input(">>> ")
    if x == "exit":
        print("Thank you! Goodbye!")
        sys.exit()
    elif x == "help":
        instructions()
    elif x == "return":
        mainmenu()
    else:
        wiki_validation_result = wiki_article_validate(x)
        if wiki_validation_result == False:
            while wiki_validation_result == False:
                print("Please enter a valid input:")
                x = input(">>> ")
                wiki_validation_result = wiki_article_validate(x)
        wiki_return()


# ----- Main Function -----
def main():
    print("Hello! Welcome to my Python Chatbot!")
    returnname()
    instructions()
    mainmenu()


if __name__ == "__main__":
    main()
