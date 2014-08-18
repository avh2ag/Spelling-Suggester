Acknowledgements:
http://en.wikipedia.org/wiki/Levenshtein_distance
Denotes the general algorithm for determining the number of edits between two strings. 

Runs on python version 2.7.6
Unit testing relies on pytest.py 
to install, pip install pytest

To run all system tests, type py.test to see all unit testing at the root level of the package.

This assumes that both 'word_frequency.csv' and 'mispelled_queries.csv' are in the same directory as run.py. 

To run the Spelling Suggester, use 'python run.py' in the primary Spelling-Suggester directory.

1. How would the code perform if the size of the dictionary were 1 million words?
  The code would slow down tremendously, and would require many more optimizations to be usable. Even now, when I don't check the input word against any word 3 letters longer or shorter, the brute force attempt is making hundreds of calls to the edit distance algorithms. The optimization I currently use, given the size of the dictionary (~11000 words), is to organize all the words of the same length into their own maps. That way, I don't have search all the words each time, as the minimum edit distance of two words of different lengths is the respective difference in length. To handle 1 million words, an approach similar to Peter Norvig's (http://norvig.com/spell-correct.html) is necessary. However, his source code is well discussed and publicly available in python. As a result, I didn't feel comfortable taking his source code line for line.

  2. How would the code perform with an edit distance of 3?
  The code currently takes about 2 seconds per input to find suggestions. Increasing the edit distance that produces an acceptable word does not slow down the code, as it currently is just tossing out those results as unacceptable. The main overhead in the code is the number of words that are being searched for edit-distance. 

  3. How does the code perform on long queries versus short queries and why?
  Short queries take less time. The Levinshtein algorithm used for finding the edit distance runs in proportion to the strings being compared. The shorter the words being queried, the fewer comparisons needed to compute the edit distance. 