#!/usr/bin/env python
# encoding: utf-8
import configparser
from importlib import resources  # Python 3.7+
import algorithims as al



config = configparser.ConfigParser()
config.read(r'fuzzy-match\fuzzy-match\config.ini')
default_algorithim = config.get('DEFAULT', 'default_algorithim')

if default_algorithim == 'trigram':
    default_algorithim = al.trigram
elif default_algorithim == 'levenshtein':
    default_algorithim = al.levenshtein
elif default_algorithim == 'cosine':
    default_algorithim = al.cosine
elif default_algorithim == 'jaro_winkler':
    default_algorithim = al.jaro_winkler


def extract(query, choices, match_type=default_algorithim, score_cutoff=0):
    """
    Find the similarity between a query item and a list of choices.
    Returns a tuple of all choices and their associated similarity score.

     Arguments:
        query: The string you are wanting to match.
        choices: An iterable or dictionary-like object containing choices
            to be matched against the query.
        score_cutoff: Optional argument for score threshold. If the best
            match is found, but it is not greater than this number, then
            return None anyway ("not a good enough match").  Defaults to 0.

    """
    try:
        try:
            if choices is None or len(choices) == 0:
                return
        except TypeError:
            pass

        results = []
        
        for i in choices:
            score = (match_type(query, i))
            data = (i, score)
            if score >= score_cutoff:
                results.append(data)

        return results

    except:
        return None


def extractOne(query, choices, match_type=default_algorithim, score_cutoff=0):
    """
    Finds the most similar item to query item from a list of choices.
    Returns tuple of best choice and its associated similarity score.

     Arguments:
        query: The string you are wanting to match.
        choices: An iterable or dictionary-like object containing choices
            to be matched against the query.
        score_cutoff: Optional argument for score threshold. If the best
            match is found, but it is not greater than this number, then
            return None anyway ("not a good enough match"). Defaults to 0.

    """

    try:
        best_list = extract(query, choices, match_type, score_cutoff)

        best = max(best_list, key=lambda i: i[1])

        return best

    except:
        return None