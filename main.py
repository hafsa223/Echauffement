import datetime

def is_palindrome(text):
    return text == text[::-1]

def greeting_based_on_time(language="fr"):
    now = datetime.datetime.now()
    if 5 <= now.hour < 12:
        return "Bonjour" if language == "fr" else "Good Morning"
    elif 12 <= now.hour < 18:
        return "Bon après-midi" if language == "fr" else "Good Afternoon"
    elif 18 <= now.hour < 22:
        return "Bonsoir" if language == "fr" else "Good Evening"
    else:
        return "Bonne nuit" if language == "fr" else "Good Night"

def farewell_based_on_time(language="fr"):
    now = datetime.datetime.now()
    if 5 <= now.hour < 12:
        return "Au revoir et bonne journée" if language == "fr" else "Goodbye and have a great day"
    elif 12 <= now.hour < 18:
        return "Au revoir et bon après-midi" if language == "fr" else "Goodbye and have a great afternoon"
    elif 18 <= now.hour < 22:
        return "Au revoir et bonne soirée" if language == "fr" else "Goodbye and have a great evening"
    else:
        return "Au revoir et bonne nuit" if language == "fr" else "Goodbye and have a great night"

def main():
    language = input("Choose your language (fr/en) : ").strip().lower()
    if language not in ["fr", "en"]:
        print("Invalid language. Defaulting to French (fr).")
        language = "fr"
        
    print(greeting_based_on_time(language))
    while True:
        user_input = input("Écrivez quelque chose (ou tapez 'exit' pour quitter) : ")
        if user_input.lower() == "exit":
            print(farewell_based_on_time(language))
            break
        elif is_palindrome(user_input):
            print("Bien dit !" if language == "fr" else "Well said!")
        else:
            print("En miroir : " if language == "fr" else "Mirrored: ", user_input[::-1])

if __name__ == "__main__":
    main()
