Class Definition (word_reverser):
        This class defines a word reverser object.

1) Method reverse_word:
        This method takes a single word as input and reverses it character by character.
        It iterates through each character in the word from the last character to the first, appending each character to a new string in reverse order.
        For example, "instructions!" becomes "!snoitcurtsni".

2) Method reverse_line:
        This method takes a line of text as input and reverses each word in the line.
        It splits the line into individual words using the space character as a delimiter.
        It then applies the reverse_word method to each word in the line.
        Finally, it concatenates the reversed words back into a single string with spaces between them.
        For example, "sq: RV128 only" becomes ":qs 821VR ylno".

3) Method process_line:
        This method takes a line of text as input and processes it.
        If the line is empty, it returns the line unchanged.
        Otherwise, it reverses the line using the reverse_line method.

4) Method process_input:
        This method continuously reads lines from standard input until it reaches the end of the input (EOF).
        For each line, it processes the line using the process_line method and prints the result.
        This method effectively applies the word reversal logic to each line of input text.

5) Entry Point (main function):
        The main function creates an instance of the word_reverser class and calls its process_input method to start the input processing loop.


To run ocml program:
Firstly compile the program through this command

```ocamlc -o reverse_file reverse_file.ml```

Then execute the compiled file using the following command

``` ./reverse_file < input.txt```