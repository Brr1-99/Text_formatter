import pyautogui

languages = {
    "Hex": "x",
    "Binary": "b",
    "Octal": "o",
}

numbers = {
    "Hex": 6,
    "Binary": 2,
    "Octal": 8,
}

def encript(message: str, language: str) -> str:
    return " ".join(format(ord(char), language) for char in message)

def decript(text: str, language: int) -> str:
    return "".join(chr(int(char, language)) for char in text)

option = pyautogui.confirm(text="Do you want to encript or decript(D) a message?", buttons=["Encript", "Decript"])

if option == 'Encript':

    text = input("Write the text you want to encript: ")

    formatt = pyautogui.confirm(text="To what format do you want to encript it?", buttons=["Hex", "Binary", "Octal"])

    print(f"Here is your encripted text: {encript(text, languages.get(formatt))}")

elif option == 'Decript':

    text = input("Write the text you want to decript: ")

    formatt = pyautogui.confirm(text="From which format do you want to decript it?", buttons=["Hex", "Binary", "Octal"])

    print(f"Here is your decripted text: {encript(text, numbers.get(formatt))}")