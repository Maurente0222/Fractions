# Fractions
This project was for the Fall 2017 Advanced Python course at University of South Florida, with Dr. Tindell.

The goal of this project is a program to be used to practice fraction arithmetic, with a graphical interface created using the easygui module. 

Clicking on the Solver button should bring up the Solver window where the user may enter an arbitrary fraction expression.  If the entered string is a valid fraction expression, the value of the expression will be displayed with buttons to solve another or return to the main window; otherwise a window appears with an error message and buttons to try again or return to the main window.

Clicking on the Quizzer button of the main window will bring up the Quizzer window, where the user select one of the operators ('+','-','*'). 

The quiz question window will display a random fraction expression followed by '='and space for the user to enter the answer.  The fractional expression consists of two randomly chosen fractions joined by the operator symbol.  For a random fraction, a random integer between -15 and 15 for the numerator and a random integer in the range from 1 to 15 for the denominator will be chosen. There are three possible outcomes: correct, correct value but not reduced and incorrect.  After the user enters their answer, a message window appears with the results.  There are three possible outcomes: completely correct, correct but not reduced and incorrect.  If the user's answer is completely correct, a congratulations message will appear; if the answer is not completely correct the message will indicate the outcome and show the correct answer in the form of the expression, '=' and the correct answer.
