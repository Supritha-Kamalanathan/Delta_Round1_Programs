# Tried out 2 modules, langdetect and lang-detector. Though both are not 100 % reliable, langdetect seems to be more accurate comparitively

from langdetect import detect
from langcodes import *

string = input("Enter your sentence: ")
lang = detect(string)

print("This sentence is in: ", Language.make(language=lang).display_name())


