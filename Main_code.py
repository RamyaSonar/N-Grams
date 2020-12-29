"""
  N-Grams
"""
run = True

while run:

    #import
    import bs4 as bs # BeautifulSoup 
    import urllib.request
    import re
    import random
    import nltk
    from nltk.tokenize import RegexpTokenizer
    #import string
    #from nltk.tokenize import word_tokenize
    nltk.download('punkt')
    
    #Function to perform web scapping with beautiful soup
    def _scrape_webpage(url): 
      """
      Use BeautifulSoup to scrape the webpage text contents. 
      """
      scraped_textdata = urllib.request.urlopen(url) 
      textdata = scraped_textdata.read()
      parsed_textdata = bs.BeautifulSoup(textdata,'lxml') 
      paragraphs = parsed_textdata.find_all('p') 
      formated_text = ""
      for para in paragraphs: 
        formated_text += para.text
      return formated_text
    
    #Create dictionary to store book title as key and EBook number as value
    #You should *not* hard code file names or the number of files your program is able to process.
    print()
    print()
    #Print out output to the users
    print("This program is developed by Ramya Sonar and Joe Lartey. ")
    print()
    print("This program generates random sentences based on an Ngram model. ")
    print()
    #Number of sentences to be genreated
    number_sentences = input("Please enter the number of sentences you would you like to generate: ")
    number_sentences = number_sentences
    #number of N-Grams to generate
    n = input("Please enter the number of N-grams you would like to generate: ")
    n = int(n)
    #input book title
    number_books = input("Please enter the number of books you would you like to read from (1-3)? ")
    number_books = int(number_books)
    
    #book title and number to search for
    books = {'Crimes and Punishments': '58700',
             'War and Peace': '2600',
             'Anna Karenina': '1399'}
    
    #URL to loop through
    url_template = 'https://www.gutenberg.org/files/%s/%s-h/%s-h.htm'
    for x in range(number_books):
        bookTitle = input("Please enter a book title from the list:'Crimes and Punishments'\n,'War and Peace','Anna Karenina' : ") 
        for title,number in books.items():
            if bookTitle in title:
                mytext = _scrape_webpage(url_template % (number, number, number))
                mytext = mytext + mytext
                
 
   
    
    #Tokenize words using regex
    #convert all text to lower case, and make sure to include punctuation in the n-gram models.
    #Make sure that you separate punctuation marks from text and treat them as tokens. Also treat numeric data as tokens.
    tokenizer = RegexpTokenizer(r"[^\W]+|[\.\?\!]")
    regexp_tokens = tokenizer.tokenize(mytext.lower())
    list_single_words = regexp_tokens
    #create a unigram
    #uniqueWords = set(list_single_words)
    
    #function to loop through frequency
    def weighted_word_choice(choices):
      total = sum(value for key, value in choices.items()) 
      r = random.uniform(0, total)
      upto = 0
      for key, value in choices.items():
        if upto + value > r:
          return(key[1])
        upto += value
        
    #Generate the number of grams needed
    def generateNgram(n=1):
      gram = dict()
      # Some helpers to keep us crashing the PC for now
      assert n > 0 and n < 100
      # Populate N-gram dictionary
      for i in range(len(list_single_words)-(n-1)): 
        key = tuple(list_single_words[i:i+n])
        if key in gram:
          gram[key] += 1
        else:
          gram[key] = 1
      gram = {k: v for k, v in sorted(gram.items(), key=lambda item: item[1], reverse=True)}
      return gram
    
    #Generate sentece at random
    def getGramOfSentenceRandom(number_sentences, gram, word, n = 60):
      words = word + ' '
      limit = number_sentences
      count = 0
      for i in range(n):
        #print(word,)
        if (word == '!') or (word == '.') or (word == '?'):
          count = count +1
        if count == limit:
          break
        # Get all possible elements ((first word, second word), frequency)
        choices = {key : value for key, value in gram.items() if key[0] == word}   
        if not choices:
          break
        # Choose a pair with weighted probability from the choice list
        word = weighted_word_choice(choices)
        words += word + ' '
        if count == limit:
          break
      return words
    
    # Generate ngram list
    print()
    print("Generating",str(n),"-gram list...")
    ngram = generateNgram(n)
    print("Done")
    
    for word in ['and', 'he', 'she', 'when', 'is', 'never', 'i', 'how']:
      print ("Start word: %s" % word)
      words = getGramOfSentenceRandom(number_sentences, ngram, word, 60)
      print("%s-gram sentence: \"" % n, words, "\"" ) 
    
    print()
    print()
    runAnother = input("if you would like to run another N-gram sentence enter 'yes', else enter 'no' : ")
    if runAnother == 'yes':
        run = True
    else:
        run = False
        
    
