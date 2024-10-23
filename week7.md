## Parsing, PCFGS, and Machine Translation

Section I: Introduction to Parsing
----    

Parsing:
    - The process of analyzing the syntactic structure of a sentence based on a grammar. 

    Types - Constituency Parsing - Breaks sentences into constituent parts (noun pharases, ver phrases, etc)

    Dependancy Parsing - Focuses on grammatical relationships between individual words. Similar to how an object connects to its action.

ex. "the cat chased the mouse"

    Dependancy Parsing (Chased is the main verb and cat is the subject and mouse is the object)

Constituency Trees vs Dependency Trees

    Constituency Tree - shows sentence structure based on phrases
    Dependency Tree - Maps grammatical relationships between individual words.

Real-world Parsing Example

    - "Can you schedule a meeting for tomorrow?" 

    -Constituency Parsing - Identifies large phrases like noun phrases, verb phrases and prepositional phrases.

    - Dependency Parsing - maps word relationships (who is doing what to whom)


Sextion II Probabilistic Context-Free Grammars (PCFG's)

    Defintion: A formal grammar consisting of a set of rules that define the structure of valid sentences in a language.

    Derivation Trees : Show how CFG break down sentences into smaller components

    Rule: S -> NP Vp (A sentence consitis of a noun phrase followed by a verb phrase)

    PCFG - A proablisitic extension of CFGs that assigns probabilities to grammar rules
    purpose : Helps resolve syntactic ambiguity in sentences

    Excample : Parsing the ambiguous sentence ' Saw the man with the telescope'
    - The system uses the probabilities associated with each potential parse to determine whether its more common to interpret with the telescope as modifying saw or man.

    Ambiguity in real-world Parsing 

    - Ambiguity - Multiple valid interpretations for a sentence. PCFGs help resolve ambiguity by selecting the most likely interpretation based on proababilities.

    Chart Parsing the CKY Algorithm

    - CKY ALGO : a dynamic programming approach used in chart parsing
        - Benefits : Efficient parsing that avoid recalculating sub-parses
    - Bottom up Approach - Builds the parse tree from the smallest units upward.
    -Steps : Creating a parse Chart, (visual representation of how the sentence is broken down), Cky Algorithim (Parsing the sentence), Final Tree (creates S -> NP VP)

    Section 4: Machine Translation:

    - MT - automatically converting text from one language to another.
    - Parsing's role - Parsing helps understand and translate sentence structure from the source language to the target language.
    - Challenges - Handling ambiguity, idiomatic expressions, and different word orders across languages.

    How Parsing Supports MT

    - using Constituency parsing (Identifies large-scale sentence structures, helping to preserve meaning across translations), dependency Parsing (Maps grammatical relationships to ensure accurate word positioning in the targer language) and PCFGs (Help handle ambiguity during translation by selecting the most likely interpretation)

    chase as verb cat as subject
    mouse as object

    
Question 2		0 / 4 points
What is probability in the context of NLP?

Question options:

A way to categorize words.


A measure of how likely an event is to occur.


A method for generating new text.


A rule for translating text.

Question 5		0 / 4 points
How does Bayesian Rule update probabilities in chatbot systems?

Question options:

By assigning fixed probabilities based on grammar rules.


By generating random responses based on word order.


By updating the probability of user intent based on new user inputs.


By predicting the next response based on the previous sentence.

Question 6		0 / 6 points
In a chatbot system, how would you calculate the posterior probability if the prior is 0.6 and the likelihood is 0.9?

Answer:	P(B/A)P(A) / P(B)	
Question 7		0 / 4 points
What is the main advantage of using a ChatbotHandler in a chatbot system?

Question options:

It focuses on individual word frequencies rather than entire sentences.


It simplifies chatbot logic by ignoring user context.


It centralizes input processing, intent recognition, and response generation, making the system scalable and maintainable.


It predicts the next word in a sentence based on grammar rules.

Question 8		0 / 4 points
How do n-gram models differ from Bayesian inference in chatbot systems?

Question options:

N-gram models are more accurate than Bayesian inference.


N-gram models focus on sentence structure, while Bayesian inference ignores context.


N-gram models predict word sequences, while Bayesian inference updates probabilities based on user input.


N-gram models are deterministic, while Bayesian inference is probabilistic.

Question 12		0 / 4 points
Which of the following describes the role of POS tagging in word-sense disambiguation?

Question options:

POS tagging predicts the next word in a sentence based on its grammatical role.


POS tagging resolves ambiguity by analyzing the structure of sentences.


POS tagging prioritizes the likelihood of specific word combinations.


POS tagging provides grammatical context, helping clarify ambiguous word meanings.