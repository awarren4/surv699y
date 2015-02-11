#Import collections package
import collections

#store the romeo and juliet file name.
file_name = "romeoandjuliet.txt"

#create empty variables that will be used to count the number of lines and words in the file
line_counter = 0
word_counter = 0

#create empty variable that will be used to count the number of characters, excluding spaces between words, in the file. 
character_with_no_spaces_counter = 0

#create empty variable that will be used to count the number of characters, including spaces between words, in the file. 
character_with_spaces_counter = 0

#create an empty list that will be used to store every word in the file
list_of_all_words_in_file = [] 

#open the file.
my_file = open( "romeoandjuliet.txt", "r" )


#loop over lines in file
for current_line in my_file:


    #print the current line - this will show which lines have been processed in the document
    '''print( "current_line:" + current_line )'''

    #count the number of lines in the file - increment line_counter for each line read 
    line_counter = line_counter + 1

    #Remove the extra blank space from the line 
    stripped_string = current_line.strip()

    #split the line into individual words that are stored in a list 
    word_stripped_list = stripped_string.split()

    #increment list_of_all_words_in_file with current list of words
    list_of_all_words_in_file = list_of_all_words_in_file + word_stripped_list  

    #count the number of characters in the line, with spaces included, then use this value to increment character_with_spaces_counter
    character_with_spaces_counter = character_with_spaces_counter + len( stripped_string )

    #count the number of words in the list then use this value to increment word_counter
    word_counter = word_counter + len( word_stripped_list )
    

    #new loop over words in line 
    for current_word in word_stripped_list: 


        #count the number of characters in the word then use this value to increment character_with_no_spaces_counter - this excludes spaces between words
        character_with_no_spaces_counter = character_with_no_spaces_counter + len( current_word )

 	
#end loop over words and lines of file
my_file.close()


#print the final values for number of lines, words, and characters
print( "final line counter:" + str( line_counter) )
print( "final word counter:" + str( word_counter) )
print( "final character counter not including spaces:" + str( character_with_no_spaces_counter) )
print( "final character counter including spaces:" + str( character_with_spaces_counter) )

#print the final catalog - create a dictionary that takes each unique word in the list and counts the number of occurances 
print ( "catalog:" )
print collections.Counter( list_of_all_words_in_file )

