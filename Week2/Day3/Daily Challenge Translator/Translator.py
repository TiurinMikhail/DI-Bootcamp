import googletrans

print(googletrans.LANGUAGES)

stroke = 'Hello'

from googletrans import Translator

translator = Translator()

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translated_words = {}
for word in french_words:
    translated_words[word] = translator.translate(word, src='fr', dest='en').text

print(translated_words)
