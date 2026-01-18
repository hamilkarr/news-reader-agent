from crewai.tools import tool


@tool
def count_letters(sentence: str):
    """this function is to count the amount of letters in a sentence. the input is a `sentence` string and the output is the number of letters in the sentence"""
    return len(sentence)
