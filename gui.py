import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import chatbot

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Chatbot")
        self.root.geometry("850x550")
        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', background='#4CAF50', foreground='white', font=('Arial', 12))
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        self.style.configure('TEntry', padding=5)

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Greeting Label
        self.greeting_label = ttk.Label(self.main_frame, text="Hello! Welcome to AI Chatbot!", font=("Arial", 16, 'bold'))
        self.greeting_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Name Frame
        self.name_label = ttk.Label(self.main_frame, text="Enter your name: ", font=("Arial", 14))
        self.name_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(self.main_frame, width=30, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, pady=5)
        self.name_entry.bind("<Return>", lambda event: self.returnname())
        self.name_button = ttk.Button(self.main_frame, text="Submit", command=self.returnname)
        self.name_button.grid(row=1, column=2, padx=5, pady=5)

        # Instructions Label
        self.instructions_label = ttk.Label(self.main_frame, text="What do you want to do?", font=("Arial", 14))
        self.instructions_label.grid(row=2, column=0, columnspan=3, pady=10)

        # Buttons Frame
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.grid(row=3, column=0, columnspan=3, pady=10)
        self.info_button = ttk.Button(self.buttons_frame, text="Get Information", command=self.wikichat)
        self.info_button.grid(row=0, column=0, padx=10)
        self.chat_button = ttk.Button(self.buttons_frame, text="Chat with Bot", command=self.chat_with_bot)
        self.chat_button.grid(row=0, column=1, padx=10)

        # Output Text Box
        self.output_text = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, width=90, height=15, font=("Arial", 12))
        self.output_text.grid(row=4, column=0, columnspan=3, pady=10)

        # Input Frame (hidden initially)
        self.input_frame = ttk.Frame(self.main_frame)
        self.input_frame.grid(row=5, column=0, columnspan=3, pady=5)
        self.input_entry = ttk.Entry(self.input_frame, width=60, font=("Arial", 12))
        self.input_entry.grid(row=0, column=0, pady=5)
        self.input_entry.bind("<Return>", lambda event: self.submit_input())
        self.input_button = ttk.Button(self.input_frame, text="Submit", command=self.submit_input)
        self.input_button.grid(row=0, column=1, padx=5, pady=5)

        # Status Bar
        self.status_bar = ttk.Label(self.root, text="Welcome to the AI Chatbot!", relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 10))
        self.status_bar.grid(row=1, column=0, sticky=(tk.W, tk.E))

        # Menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Instructions", command=self.show_instructions)

        # Hide input frame initially
        self.input_frame.grid_remove()

    def returnname(self):
        name = self.name_entry.get()
        response = chatbot.returnname(name)
        self.output_text.insert(tk.END, response + "\n")
        self.output_text.insert(tk.END, chatbot.instructions() + "\n")
        self.name_entry.delete(0, tk.END)  # Clear the name entry
        self.status_bar.config(text=f"Hello {name}! What would you like to do?")

    def wikichat(self):
        self.clear_output()
        self.output_text.insert(tk.END, "What do you want to learn about? \n")
        self.show_input_box(self.get_wiki_article)

    def get_wiki_article(self):
        article_name = self.input_entry.get()
        result = chatbot.get_wiki_article(article_name)
        self.output_text.insert(tk.END, result + "\n")
        self.input_entry.delete(0, tk.END)  # Clear the query entry
        self.status_bar.config(text="Article retrieved successfully!")

    def chat_with_bot(self):
        self.clear_output()
        self.output_text.insert(tk.END, "You are now chatting with the AI chatbot. Type 'exit' to return to the main menu.\n")
        self.show_input_box(self.get_bot_response)

    def get_bot_response(self):
        user_input = self.input_entry.get().strip().lower()
        if user_input == 'exit':
            self.output_text.insert(tk.END, "Bot: Goodbye!\n")
            self.input_entry.delete(0, tk.END)
            self.input_frame.grid_remove()
            self.status_bar.config(text="Exited chat mode. What would you like to do?")
            return
        response = chatbot.chat_with_bot(user_input)
        self.output_text.insert(tk.END, f"You: {user_input}\nBot: {response}\n")
        self.input_entry.delete(0, tk.END)  # Clear the chat entry

    def show_input_box(self, submit_command):
        self.input_entry.bind("<Return>", lambda event: submit_command())
        self.input_button.config(command=submit_command)
        self.input_frame.grid()

    def submit_input(self):
        self.input_button.invoke()

    def clear_output(self):
        self.output_text.delete(1.0, tk.END)
        self.input_frame.grid_remove()

    def show_instructions(self):
        messagebox.showinfo("Instructions", chatbot.instructions())

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
