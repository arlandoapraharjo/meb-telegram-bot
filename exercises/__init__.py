"""
Modular Exercise Banks for English Buddy Bot.
Provides 1,000 curated, bite-sized offline exercises across 5 learning tracks and 3 levels.
"""

from exercises.conversation import CONVERSATION_EXERCISES
from exercises.vocabulary import VOCABULARY_EXERCISES
from exercises.grammar import GRAMMAR_EXERCISES
from exercises.reading import READING_EXERCISES
from exercises.challenge import CHALLENGE_EXERCISES

__all__ = [
    "CONVERSATION_EXERCISES",
    "VOCABULARY_EXERCISES",
    "GRAMMAR_EXERCISES",
    "READING_EXERCISES",
    "CHALLENGE_EXERCISES",
]
