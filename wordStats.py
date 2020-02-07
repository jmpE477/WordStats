def wordCount(filename):
  # Task 1 - Ovi
  fopen = open(filename, "r")
 
  count = 0
 
  for line in fopen:
    for ch in line:
      
      if ((ch == " ") or (ch == "-")):
        count = count + 1
  fopen.close()
  return count

def countParagraphs(filename):
  # Task 2 - Peter
  f = open(filename, "r")   # Open the file, assign its content to the variable f.
  isLineEmpty = False       # Initialise variable, we’ll use it to flag if we’ve seen an empty line.
  paragraphCount = 0        # Initialise variable holding the number of paragraphs.

  for line in f:
    if (line=="\n"):            # Have we just encountered an empty line?
      isLineEmpty = True        # Yes. We want to remember it so we set the isLineEmpty variable.
    else:
      if (isLineEmpty == True):               # Previous line was empty but now it isn't,
        paragraphCount = paragraphCount + 1   # so we assume it's a new paragraphs and count it.
        isLineEmpty = False                   # Finally, we re-initialise the isLineEmpty variable.
  return(paragraphCount)

def avgWordLength(filename):
  # Task 3 - Group
  fopen = open(filename, "r")
  words = 0
  letters = 0

  fopen = open(filename, "r")
  for line in fopen:
    for character in line:
      if (ord(character) in range(65,91) or ord(character) in range (97,123)): # Is it a letter?
        letters = letters + 1                                           # If so, let’s count it.
      elif (character == " " or character == "-"):  # If it's not a letter but space or "-"
        words = words +1                            # let's count it as a word.

  fopen.close()
  return(letters/words)

def avgSentenceLength(filepath):
  # Task 4 - Paul
  # This list contains lists. Each list being a line in the file
  file_by_line = []
  word_count = 0
  sentence_count = 0

  with open(filepath) as fp:
    line = fp.readline()
    while line:
      words = line.split()
      file_by_line.append(words)
      line = fp.readline()
  
  #Counts the words 
  for list in file_by_line:
    for word in list:
      word_count = word_count + 1

      #Counts sentences
      if word.endswith('.') or word.endswith('?') or word.endswith('!') :
        sentence_count = sentence_count + 1
  
  #Divides the words into the sentences
  return word_count/sentence_count

def frequencyAnalysis(filename):
  # Task 5 - Peter
  def drawBar(currentValue,maxValue):     # currentValue: number of occurrences of the actual letter.
                                          # maxValue: the highest number of occurrences.
    bar=""                                # Initialise the variable used for drawing the graph.

    # Due to the width of the output terminal, we assume the max length of 25 characters to be safe,
    # hence one "#" represents maxValue/25 occurences. We’ll get the length we need by dividing
    # the current number of occurrences by that value.
    
    for b in range(0,round(currentValue / (maxValue/25))):    
      bar = bar + "#"                     # Fill the variable bar with the appropriate number of "#"s.
    if (bar=="" and (currentValue > 0 )): # If the number of occurrences is smaller than one "#",
      bar = "#"                           # we still want to show it in the graph.
    return bar

  fopen = open(filename, "r")

  output = ""                             # Output returned by this function.
  letterFreq = [0 for i in range(0,123)]  # List for storing a number of occurrences for each letter.

  for line in fopen:
    for character in line:
      if (ord(character) in range(65,91) or ord(character) in range (97,123)):  # Is it a letter?
	# If so, let’s add its occurrence to the letterFreq list.
        letterFreq[ord(character)] = letterFreq[ord(character)] + 1 
  
  fopen.close()

  maxL = max(letterFreq[65:91])   # Find the max number of occurrences within the lowercase letters.
  maxU = max(letterFreq[97:123])  # Find the max number of occurrences within the uppercase letters.

  for a in range(65,91):
    output = output + "\n" + chr(a) + ": " + "{:<6d}".format(letterFreq[a]) + " " + "{:<25}".format(drawBar((letterFreq[a]),maxL))
    output = output + "  " + chr(a+32) + ": " + "{:<6d}".format(letterFreq[a+32]) + " " + "{:<25}".format(drawBar((letterFreq[a+32]),maxU))

    # Add to the variable output the following: current character, number of its occurrences
    # and a bar filled with "#" characters. 
    # The drawBar function requires two arguments: current number of occurrences 
    # and the maximum occurrence. First time we drew a bar for the lowercase letters so we need
    # to repeat it for the uppercase characters.
      
  return(output)