#!/usr/bin/env python
# encoding: utf-8
import math
from math import floor, ceil 
import re
from collections import Counter
import numpy as np

def find_ngrams(string: str, split_num: int=3) -> set:
    """
    Slice string into ngrams.
    Returns array of ngrams for the given string.

    Arguments:
        text: the string to find ngrams for.
        split_num: the length the ngrams should be. Defaults to 3 (trigrams).
    """
    try:
        if not string:
            return set()

        words = [f'  {x} ' for x in re.split(r'\W+', str(string).lower()) if x.strip()]

        ngrams = set()

        for word in words:
            for x in range(0, len(word) - split_num + 1):
                ngrams.add(word[x:x+split_num])

        return ngrams

    except:
        return None


def trigram(string1: str, string2: str, split_num: int=3):
    """
    Find the similarity between two strings using ngrams.
    Returns float score value, 0 being completely different strings and 1 being equal strings.

    Arguments:
        string1: Main string to compare against
        string2: second string to compare to string1.
        split_num: the length the ngrams should be. Defaults to 3 (trigrams).
    """
    try:
        ngrams1 = find_ngrams(string1, split_num)
        ngrams2 = find_ngrams(string2, split_num)

        num_unique = len(ngrams1 | ngrams2)
        num_equal = len(ngrams1 & ngrams2)

        score = round(float(num_equal) / float(num_unique), 6)

        return score

    except:
        return None


def text_to_vector(text):
    words = re.compile(r"\w+").findall(text)
    return Counter(words)


def cosine(text1, text2):

    vec1 = text_to_vector(text1)
    vec2 = text_to_vector(text2)
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def levenshtein(a, b):
    size_x = len(a) + 1
    size_y = len(b) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if a[x-1] == b[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    distance = matrix[size_x - 1, size_y - 1]
    score = (max(len(a), len(b)) - distance) / max(len(a), len(b))
    return float(score)


def jaro_winkler(s1, s2):
      
    # If the s are equal 
    if (s1 == s2): 
        return 1.0
  
    # Length of two s 
    len1 = len(s1) 
    len2 = len(s2) 
  
    # Maximum distance upto which matching 
    # is allowed 
    max_dist = floor(max(len1, len2) / 2) - 1
  
    # Count of matches 
    match = 0
  
    # Hash for matches 
    hash_s1 = [0] * len(s1) 
    hash_s2 = [0] * len(s2) 
  
    # Traverse through the first 
    for i in range(len1): 
  
        # Check if there is any matches 
        for j in range(max(0, i - max_dist),  
                       min(len2, i + max_dist + 1)): 
              
            # If there is a match 
            if (s1[i] == s2[j] and hash_s2[j] == 0): 
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break
  
    # If there is no match 
    if (match == 0): 
        return 0.0
  
    # Number of transpositions 
    t = 0
    point = 0
  
    # Count number of occurances 
    # where two characters match but 
    # there is a third matched character 
    # in between the indices 
    for i in range(len1): 
        if (hash_s1[i]): 
  
            # Find the next matched character 
            # in second 
            while (hash_s2[point] == 0): 
                point += 1
  
            if (s1[i] != s2[point]): 
                point += 1
                t += 1
    t = t//2
  
    # Return the Jaro Similarity 
    return (match/ len1 + match / len2 + 
            (match - t + 1) / match)/ 3.0