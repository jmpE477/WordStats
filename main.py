import wordStats
print("1. Word count:              " + str(wordStats.wordCount("dracula.txt")))
print("2. Paragraph count:         " + str(wordStats.countParagraphs("dracula.txt")))
print("3. Average word length:     " + str(wordStats.avgWordLength("dracula.txt")))
print("4. Average sentence length: " + str(wordStats.avgSentenceLength("dracula.txt")))
print("5. Frequency analysis:\n" + str(wordStats.frequencyAnalysis("dracula.txt")))