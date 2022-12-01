# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(data)
result = {row.letter: row.code for (index, row) in df.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_code = input('enter: ').upper()
res = [result.get(i[0]) for i in user_code.split() if i[0] in result.keys()]
print(res)
