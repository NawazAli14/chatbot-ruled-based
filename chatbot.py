import wikipediaapi
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from responses import get_random_response

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('en')

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

def returnname(name):
    return f"Wow! Cool name, {name}!"

def instructions():
    instructions_text = (
        "I am a robot with a wide feature set!\n"
        "First off, I returned your name at the beginning of the program!\n"
        "Furthermore, I can:\n"
        "- Find Information about something you want to learn (Powered by Wikipedia)\n"
        "- Chat with me (Rule-based responses)\n"
        "Operating me is very simple, from the main menu, type the button that corresponds to the action.\n"
        "Then, you can follow the on-screen prompts to tell me what to do.\n"
    )
    return instructions_text

def get_wiki_article(article_name):
    page_py = wiki_wiki.page(article_name)
    if page_py.exists():
        return f"Page - Title: {page_py.title}\nPage - Summary: {page_py.summary}\n"
    else:
        return "Article not found. Please try again."

def chat_with_bot(user_input):
    if not user_input:
        return "Please enter something meaningful."
    if user_input == 'exit':
        return "Goodbye!"
    else:
        response = get_random_response(user_input)
        return response
