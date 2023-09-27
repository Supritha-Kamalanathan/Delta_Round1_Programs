# Have installed googletrans==3.0.0a0. The other versions dont seem to support this operation.

from googletrans import Translator
translator = Translator()

string = input("Enter your sentence: ")
code = input("Enter the language code of preferred language: ")

transtring = translator.translate(string, dest = code)

print("This sentence translates to: ", transtring.text)
