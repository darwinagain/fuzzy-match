# Fuzzy-Match
Fuzzy string matching in Python. By default it uses [Trigrams](https://en.wikipedia.org/wiki/Trigram) to calculate a similarity score and find matches by splitting strings into ngrams with a length of 3. The length of the ngram can be altered if desired. Also, [Cosine](https://en.wikipedia.org/wiki/Cosine_similarity), [Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance), and [Jaro-Winkler Distance](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance) algorithims are also available as alternatives.

# Usage
```python
>>> from fuzzy_match import match
>>> from fuzzy_match import algorithims
```
### Trigram
```python
>>> algorithims.trigram("this is a test string", "this is another test string")
    0.703704
```
### Cosine
```python
>>> algorithims.cosine("this is a test string", "this is another test string")
    0.7999999999999998
```
### Levenshtein
```python
>>> algorithims.levenshtein("this is a test string", "this is another test string")
    0.7777777777777778
```
### Jaro-Winkler
```python
>>> algorithims.jaro_winkler("this is a test string", "this is another test string")
    0.798941798941799
```
### Match
```python
>>> choices = ["simple strings", "strings are simple", "sim string", "string to match", "matching simple strings", "matching strings again"]
>>> match.extract("simple string", choices, limit=2)
    [('simple strings', 0.8), ('sim string', 0.642857)]
>>> match.extractOne("simple string", choices)
    ('simple strings', 0.8)
```
You can also pass additional arguments to `extract` and `extractOne` to set a score cutoff value or use one of the other algorithims mentioned above. Here is an example:
```python
>>> match.extract("simple string", choices, match_type='levenshtein', score_cutoff=0.7)
    [('simple strings', 0.9285714285714286), ('sim string', 0.7692307692307693)]
```
`match_type` options include `trigram`, `cosine`, `levenshtein`, `jaro_winkler`