# Have installed googletrans==3.0.0a0. The other versions dont seem to support this operation

from googletrans import Translator
translator = Translator()

string = input("Enter your sentence: ")

transtring = translator.translate(string)

print("This sentence translates to: ", transtring.text)

