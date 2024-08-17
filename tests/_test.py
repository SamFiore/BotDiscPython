from spellchecker import SpellChecker
from autocorrect import Speller
from python_spell.checker import SpellChecker as SplCheck

# ----- Text Example ------

testList = 'Significa adios, se utiliza para despedir a lguien, si no lo ves por un largo tiempo'
testList = list(testList)
testList = [x:10+20,y:30+41]
# --------------------------

# ------------------ Spellchecker ------------------

# chkr = SpellChecker(language='es')
# # testList = ['arriva','comenzar','desttruir']

# print(testList)
# checker = SplCheck(testList,'spanish')
# misspelled = checker.get_typos()
# print(misspelled)


# testList = testList.split()
# listknow = chkr.known(testList)
# print(listknow)


# correct_word = []

# for word in testList:
#     if word in listknow:
#         correct_word.append(word)
#     else:
#         correct_word.append(chkr.correction(word))

# print(' '.join(correct_word))

# ------------------ ° ------------------

# ------------------ AutoCorrect ------------------
# spell = Speller('es')

# text = ' '.join(testList)

# spell(text)




