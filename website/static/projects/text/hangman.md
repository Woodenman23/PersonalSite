 A hangman CLI game that chooses a random word from list of words. It then has user guess letters until all letters are guessed or wrong guesses are made.

The interface shows guessed letters alongside dashes (_) to show position of non-guessed letters. It also shows the user what letters they have already guessed. Errors are handled well; with user told to attempt a new input if non-alphabetic input is made. Inputs are not case sensitive; all lowercase inputs are converted to uppercase before checked against word.

The interface will also display graphic of noose and fill in hanged man as incorrect guesses are made. This was acheived using a "draw" helper function (funtion in external python file). 