# Regular Expressions
Often abbreviated as regex or regexp, are powerful sequences of characters used to define search patterns.

![Regular expression joke](https://www.explainxkcd.com/wiki/images/1/10/perl_problems.png)

## Description
Regular expressions, often abbreviated as regex or regexp, are powerful sequences of characters used to define search patterns. They are used to match, search, and manipulate text in strings or files. Regular expressions provide a flexible and concise way to perform complex search and replace operations. In regular expressions, you define a pattern that describes a set of strings you want to find or manipulate. These patterns can include literal characters, metacharacters, and quantifiers. 

## Features
 * **Literal Characters:** Any regular character in a regex matches itself in the text. For example, the regex cat will match the word "cat" in the text.
 * **Metacharacters:** Special characters with a predefined meaning in regex. Examples of metacharacters include:
	* . (Dot): Matches any single character, except a newline.
	* * (Asterisk): Matches zero or more occurrences of the preceding character.
	* + (Plus): Matches one or more occurrences of the preceding character.
	* ? (Question Mark): Matches zero or one occurrence of the preceding character.
	* | (Pipe or Alternation): Matches either the expression before or after the pipe.
	* [] (Character Class): Matches any character inside the square brackets.
	* () (Grouping): Groups multiple characters or expressions together.
 * **Quantifiers:** Define the number of occurrences of the preceding character or group. Examples include \*, +, ?, {n}, {n,}, and {n,m}.
 * **Anchors:** Used to match the position, not the characters. Examples include ^ (start of line) and $ (end of line).
 * **Escape Sequence:** The backslash \ is used as an escape character to treat metacharacters as literal characters. For example, \., \*, or \( will match a literal dot, asterisk, or opening parenthesis, respectively. 

## Examples
```rb
# Match words starting with "cat":
cat\w*

# Match phone numbers with the format "(123) 456-7890":
\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}

# Match email addresses:
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

# Match URLs:
https?://\S+

# Match integers (positive and negative):
-?\d+

# Match dates in the format "YYYY-MM-DD":
^\d{4}-\d{2}-\d{2}$
```

## Overview
Regular expressions are supported by many programming languages and text editors. They provide a powerful and compact way to perform text pattern matching, validation, and manipulation tasks. However, they can also be complex and challenging to read, especially for more intricate patterns. Learning regular expressions takes time and practice, but it's a valuable skill for anyone working with text processing and data manipulation.

## Credits
 * [Introduction to Regular Expressions](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
 * [Advanced Regular Expressions](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
 * [Rubular](https://rubular.com/)
 * [Regular Expressions: Now You Have Two Problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
 * [RegexBuddy](https://www.regexbuddy.com/)
 * [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)
 * [CS50P - Lecture 7 - Regular Expressions](https://www.youtube.com/watch?v=hy3sd9MOAcc)
 * [LoneStarRuby Conf 2013 - Beneath the Surface: Regular Expressions in Ruby](https://www.youtube.com/watch?v=cZW-Y37R4B0)
 
## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
