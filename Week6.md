## Parts of Speech (POS Tagging)

- Pos tagging assings parts of speech (nouns and verbs) to each word.
    - Importance cruical for syntactic understanding and downstream NLP tasks
    - Applications - Machine Translation, search engines, sentiment analysis

Types of tagging
    - Standardized Tagging - Penn Treebank Tageset.

        - This is a standard for consistency tagging across NLP's
        - Helps with reducing ambuiguity in words
        - NN (Noun), VB(verb), JJ(Adjective), RB(Adverb)

Evaulation Metrics for POS Tagging
    
    - Accuracy - percentage of correctly tagged words
    - Confusion Matrix - Analyzes tagging errors (True/False positve True/False Negative) Shows how often the system makes a misrepentive mistake.
    - Common Tagging Errors- Mislabeling nouns as verbs and etc (adjective to verb  ex:  I run every morning. run vs ran same meaning but different tenses)

Hidden Markov Models (HMMs) in POS tagging

    - Definition: A probabilistic model used for sequence prediction. (ex:A type of predictive model that predicts hidden states.)
    - How? Predicts POS tags based on context (ex: The parts of speech that is being tagged is influenced based on the following words)
    - Transition probability - The likelihood of one tag following another. (ex: if a word is a noun it might tag that the next word would likely be a verb)

Conditional random fields CRF's in POS tagging

    - Definition : A proababilisitic model that considers entire sequences.
    - Advantage over HMMS - considered the entire sentence, not just adjacent words.
    - POS Tagging Application - CRFS improve accuracy by modeling context more effectively.

Section II: Understanding Natural Language Understanding (NLU)
----

From POS tAGGING TO nlu

    - NLU - A process of Moving from syntax to semantics (Which means moving from indiviudal words to understanding the meaning of the sentences)
    - Importance Extracting Meaning and context from text

Syntax Vs Semantics 

- Syntax - sentence structure, word order (Grammer) (HOW a sentence is made)
- Semantics - Meaning behind the words. (What does this sentence mean)
- POS Tagging Role - Helps establish syntax but doesnt fully capture meaning


Word-sense Disambiguation in NLU

-   Resolving ambiguities in word meanings (bOOK A FLIGHT VS READ A BOOK)
-   POS Tagging's role - helps disambiguate based on context

Context Awareness in NLU

- Understanding Context - beyond single sentence, broader conversation matters

- Pragmatics in NLU - How context shapes meaning (Ex. responding based on previous user input) heavily based on intention
- System must understand the flow of a conversation between the user. ex "what is the weather today? what about tomorrow?" Tomorrow should be related to the weather and nothing else

From Syntax to NLU - applications in chatbot

    - pragmatic response - conversational bots adapt based on previous dialouge.
    - NlU in sentiment analysis -Understanding user emotions
    - Question-Answer Sytems - Extracting meaning to give accurate answers

Section III : Introduction to Collocations and their importance in NLP
--- 

Collocation
    - Defintion : Words that frewuenctly appear together in a language.
    - Types - Lexical collocations ('make a decision', context words (noun verb adjective) where the verb and noun commonly are together) grammatical collocations ('depend on' context words being paired with grammactical words )
    - Significance - improves natural language flow in systems.

How Collocations improve NLP systems?

    - Natural Language flow - Recognizing common word pairings enhances fluency.
    - Disambiguation - Helps systems understand meaning based on frequent combinations.
    - Response Gneration - Collocations improve the relevance and naturalness of responses

Collocations and Language models

- Probabilistic Models - Use N-grams to capture word pair frequency
- Training Language Models - Collocations help generate more fluent responses
- NLP Improvements - recognizing collocations makes responses sound more natural
