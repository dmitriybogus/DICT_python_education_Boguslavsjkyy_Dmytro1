class MarkdownEditor:

    def __init__(self):
        self.selected_format = None
        self.content = ""

    test_string = """
# Simple Editor


## About the project

Hi, this App will help you add Markdown markup through the console. 

## Usage example

```if option == "ordered-list":```   
1. plain  
2. bold  
3. italic  
4. header  
5. link  
6. inline-code  
7. ordered-list  
8. unordered-list  
9. new-line  

```if option == "unordered-list":```  
* !help  
* !done  

```if option == "bold":```  

**bold**

```if option == "italic":```  

*italic*"""

    reserved_characters = ("*", "**", "```", "#")

    available_formatters = ("plain", "bold", "italic", "header",
                            "link", "inline-code", "ordered-list",
                            "unordered-list", "new-line")

    special_commands = "!help", "!done"

    all_commands = (*available_formatters, *special_commands)

    def show_help(self):
        print("Available formatters:", *self.available_formatters)
        print("Special commands:", *self.special_commands)

    def correctly_input_command(self, string):
        user_input = input(string)
        while user_input not in self.all_commands:
            if not user_input:
                print("If you do not know what to do write command !help")
                user_input = input(string)
                continue
            print("Unknown formatting type or command")
            user_input = input(string)
        return user_input

    def menu_options(self):
        option = self.correctly_input_command("Choose a formatter: > ")
        if option == "!help":
            self.show_help()
            self.menu_options()

        elif option == "!done":

            return

        elif option == "plain":
            user_input = self.correct_input("Text: > ")
            self.content += f"{user_input} "

        elif option == "bold":
            user_input = self.correct_input("Text: > ")
            self.content += f"**{user_input}** "

        elif option == "italic":
            user_input = self.correct_input("Text: > ")
            self.content += f"*{user_input}* "

        elif option == "header":
            level = self.correct_input_level("Level: > ")
            user_input = self.correct_input("Text: > ")

            if not self.selected_format:
                self.content += f"\n"
                self.selected_format = option
            else:
                self.content += f"\n\n"

            self.content += f"{level * '#'} {user_input}\n\n"

        elif option == "link":
            label = self.correct_input("Label: > ")
            url = self.correct_input("URL: > ")
            self.content += f"[{label}]({url}) "

        elif option == "inline-code":
            user_input = self.correct_input("Text: > ")
            self.content += f"```{user_input}``` "

        elif option == "ordered-list":
            number_rows = self.input_number_rows("Number of rows: > ")
            for row in range(1, number_rows + 1):
                user_input = self.correct_input(f"Row #{row}: > ")
                self.content += f"{row}. {user_input}  \n"

        elif option == "unordered-list":
            number_rows = self.input_number_rows("Number of rows: > ")
            for row in range(1, number_rows + 1):
                user_input = self.correct_input(f"Row #{row}: > ")
                self.content += f"* {user_input}  \n"

        elif option == "new-line":
            self.content += "  \n"

        print(self.content)
        self.menu_options()

    def correct_input(self, string):
        user_input = input(string)
        while not set(self.reserved_characters).isdisjoint(user_input):
            print("Sorry, these characters are not allowed here:",
                  *self.reserved_characters)
            user_input = input(string)
        return user_input

    @staticmethod
    def correct_input_level(string):
        user_input = input(string)
        while user_input:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please input number")
                user_input = input(string)
                continue

            else:
                user_input = int(user_input)
                if not 0 < user_input <= 6:
                    print("The level should be within the range of 1 to 6.")
                    user_input = input(string)
                    continue
                break

        return user_input

    @staticmethod
    def input_number_rows(string):
        user_input = input(string)
        while user_input:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please input number")
                user_input = input(string)
                continue

            else:
                user_input = int(user_input)
                if not 0 < user_input:
                    print("Number rows cannot be negative")
                    user_input = input(string)
                    continue
                break

        return user_input


mde = MarkdownEditor()
# mde.menu_options()
