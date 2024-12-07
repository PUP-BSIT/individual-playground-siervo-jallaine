from googletrans import Translator
translator = Translator()

text = input("Enter text: ")
language = input("Enter language: ")
translate_to = input("Translate to: ")

translated = translator.translate(text, dest = translate_to, src = language)

print(f"Translated text: {translated.text}")
