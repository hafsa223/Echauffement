import datetime

def is_palindrome(text):
    return text == text[::-1]

def greeting_based_on_time():
    now = datetime.datetime.now()
    if 5 <= now.hour < 12:
        return "Bonjour"
    elif 12 <= now.hour < 18:
        return "Bon après-midi"
    elif 18 <= now.hour < 22:
        return "Bonsoir"
    else:
        return "Bonne nuit"

def farewell_based_on_time():
    now = datetime.datetime.now()
    if 5 <= now.hour < 12:
        return "Au revoir et bonne journée"
    elif 12 <= now.hour < 18:
        return "Au revoir et bon après-midi"
    elif 18 <= now.hour < 22:
        return "Au revoir et bonne soirée"
    else:
        return "Au revoir et bonne nuit"

def main():
    print(greeting_based_on_time())
    while True:
        user_input = input("Écrivez quelque chose (ou tapez 'exit' pour quitter) : ")
        if user_input.lower() == "exit":
            print(farewell_based_on_time())
            break
        elif is_palindrome(user_input):
            print("Bien dit !")
        else:
            print("En miroir : ", user_input[::-1])

if __name__ == "__main__":
    main()
