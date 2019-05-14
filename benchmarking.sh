echo "naive- Levenshtein:"
time python naive.py which 3 1

echo $'\n'

echo "tries - Levenshtein:"
time python fuzz_complete.py which 3 1
echo $'\n'

echo "tries - Damerau Levenstein:"
time python damerau_levenshtein.py which 3 1
