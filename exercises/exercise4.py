# store file name.
file_name = "romeoandjuliet.txt"

#create variables to store number of lines, words, and character
line_counter = 0
character_with_spaces_counter = 0
word_counter = 0
character_counter = 0

#create an empty dictionary to count occurances of words
empty_dict = {}  

# open the file.
my_file = open( "romeoandjuliet.txt", "r")

# loop over lines in file.
for current_line in my_file:

    # print the line
    print( "current_line:" + current_line )

    #increment counter for each line read and print variable value
    line_counter = line_counter + 1
    print( "incremented line_counter:" + str(line_counter) )

    #count the number of characters in each line with spaces included, increment counter, print value
    stripped_string = current_line.strip()
    print( "current stripped word:" + str(stripped_string) )
    character_with_spaces_counter = character_with_spaces_counter + len(stripped_string)
    print( "individual character length for line:" + str( len( stripped_string) ) )
    print( "incremented character counter:" + str(character_with_spaces_counter) )

    #split each line/string into individual words and print number of words
    word_list = current_line.split()
    print( "line converted to list of words:" + str(word_list) )
    word_counter = word_counter + int(len( word_list )  )
    print( "individual string length:" + str( len( word_list ) ) )
    print( "incremented word counter:" + str(word_counter) )

    #new loop - split each word into characters and print number of characters - doesn't include spaces
    for current_word in word_list: 
        print( "current word:" + str(current_word) )
        print( "individual character length:" + str( len(current_word) ) )
        character_counter = character_counter + len(current_word)
        print( "incremented character counter:" + str(character_counter) )

    #Code for catalog and counts for each word - start with string with extra blank space removed
    word_stripped_list = stripped_string.split()  
    for current_stripped_word in word_stripped_list: 
    	if current_stripped_word != empty_dict:
    	    empty_dict[current_stripped_word] = 0
    	    print(empty_dict)


#-- END loop over words and lines of file --#
my_file.close()

#Final Counter Values
print( "final line counter:" + str(line_counter) )
print( "final word counter:" + str(word_counter) )
print( "final character counter not including spaces:" + str(character_counter) )
print( "final character counter including spaces:" + str(character_with_spaces_counter) )