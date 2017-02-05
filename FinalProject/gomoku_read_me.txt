Jonathan Gillespie and Kaixing Wu
Computer Science 111
Anna Rafferty

Gomoku Read-Me

This program runs a game of Gomoku with AI and human opponent options. It utilizes the 
graphics.py module to support a graphical interface. The program can be run from the command
line with the commands "python3 gomoku.py" or from the python3 shell by importing the module
and running the function "gomoku.main().

The game is briefly described in our intro page, but here we will describe it as well.
Gomoku is actually a "watered" down version of the popular game "Go". A possibly bad but not
entirely misplaced analogy could be made as follows: Go is to chess as Gomoku is to checkers.  
Players play on a gridded board, taking turns placing "stones", or black and white dots,
on vertices. The board can be various sizes, but the game is commonly played on 15x15, 
17x17, 19x19, and 21x21 boards. The goal of the game is to place five stones of the same
color in a row. Stones cannot be removed. So essentially tic-tac-toe with a lot more room
and five instead of three pieces in a row.

The first window that appears is the intro page. The user can move through these windows 
by clicking buttons that are displayed. When the color is picked, this window closes and
the main game window opens--it displays a board, a title, four "option" buttons, and the 
player whose turn it is. The user can play the game by clicking anywhere on the board. A
click places a stone at the nearest vertex, or, if the click is not near the board, does
nothing. Additionally, if an "option" button is clicked, the function associated with this 
option will be run--undo will undo the last two turns, new game starts a new game, resign 
ends the game, and quit quits the game. The game continues until one of the ending option
buttons is chosen or until five stones are placed in a row on the board. When this occurs
a winning message is displayed, and on the next click the game starts over from the intro
page.

The program utilizes a number of classes. The first class, the Intro class, serves to introduce
the game Gomoku and allows the user to choose what type of game they would like to play
(human or computer opponent, color of pieces, difficulty). 

The board class acts as the data storage and graphics class for the program; it stores game
data in the form of "stones" (the circular dots players place on the board) and generates
a window with the board and the option buttons. The stones themselves are a class. When a 
board class is generated, 225 stones are generated inside it (one for each vertex on the board.
These stones are stored in a stones list; this list is actually a list of fifteen lists, with
fifteen stones each inside. The index of a stones' individual list in the giant list represents
the stones' x value, while the index of a stone in it's specific list represents the stone's 
y value. This eliminates the need to store positional data in the stones themselves, and 
lets us easily locate each stone at all time.

The stones themselves store two types of data: team and priority. Team data is represented
by either a string (black or white) or the number "0". When stones are first generated they
are assigned the neutral "0" team. Whenever a stone's team is 0, it does not appear graphically
on the board. In this way every vertex on the board is continuously modified, despite the
fact that some vertices are empty and some are full.

There are sixteen priority values for each stone. They represent the eight cardinal directions,
with one value for each team color. The value represents the summation of the relational
values between stones in a certain direction. We only count stones for four vertices in any
direction because stones beyond that cannot form five stones in a row with a stone. The closer
two stones are, the larger amount of priority they add to one another. For example, two 
stones directly next to one another add four priority to their corresponding directions, while
stones with two spaces in-between only add two. If stones of opposing teams are in the same
"direction" and within five stones of one another, their priorities of that given direction
go to zero, since they cannot form five stones in a row in that direction.

The board class also has methods that modify stones; namely addStone and removeStone. These
methods change the team of the stones and recalculate the priorities of the stones based
on the new stone when players choose to place a stone, or on the removal of a stone when
a player removes it.

The Gomoku class acts as an overarching game class that allows interaction between the two
players and the board. It alternates the players' turns and checks to see if a player has
won after every turn. It does so by reviewing all the stones that have a team and by checking
to see if any stone has a priority over 9. Any actualized stone with a priority 10 in any 
direction has won, since a stone of the same-team next to that stone is worth 4 priority, 
a stone 2 spots away is worth 3, 3 spots is worth 2 and four spots is worth 1 (4+3+2+1=10).

The human class acts as the class for a human; it's methods allow a human player to interact
with the board. By clicking on the board the human can place a stone on the nearest vertex,
and by clicking on the option buttons the player can choose to enact one of the options.

Finally, the computer class acts as a computer player. The computer utilizes the priorities
of the stones in order to determine its move. It takes all the un-actualized stones (the 
ones who have a team of 0) and sums the sixth power of their priorities. (p_1^6+p_2^6+...).
It then take the moves with the three highest values and sorts them into a list. One by one it
tests the “future” moves prompted by this move, i.e. it checks the three likely best moves by 
its opponent on the next turn, and the three moves it will have available after each of these
three moves, and so on… It does so only for a certain number of designated times (the number
must be low for sake of speed).

We should also note it does so using a recursive function written in another class, the Pseudo
Computer class. While this function could actually have been in the computer class, it was easier
for us to organize them separately. The recursive function calculates a single value based on the
future move sequences that might be played, and this value is added to the corresponding move value.
We then take the highest combination of present and future move values to determine the move of the AI.
The AI then plays this move and graphically draws it.

There are easy and hard difficulties to this game. The easy version utilizes no recursion (so it just
take the move with the initial highest value. We have actually found that the “easy” version isn’t exactly
easier to beat than the hard version… there are a couple specific move sequences that tend to fool both 
programs (but you’ll have to discover them yourself!). The main difference between the two is that the 
recursive method is able to play more sophisticated offensive sequences because it can “see” a couple 
moves ahead—often it knows if one move will lead to a victory three turns later.


We would like to reiterate that despite the fact that there are ways to beat this program, the program
is fully functional, and runs without noticeable errors. The game can only end when one of the “ending”
option buttons is clicked OR five stones in a row are placed, and the “easy” computer AI is fairly
sophisticated and difficult to beat (Sometimes it beats this game http://gomokuonline.com/ and sometimes
it loses, but they usually have a good match. Also, the online game doesn’t have an undo button. So
clearly it is inferior ;).


*An additional note: We have submitted the program with the “level” of the Computer class set to 6. This is high
(although we wish we could go higher! If we had more time we could make it more efficient!) and thus causes
about a one second pause between computer moves. It is a natural, perhaps even preferred pause in gameplay, but
it is a pause. If one wishes to speed up gameplay, setting the level to 4 (see line 1365 in the play function) will
make the game run nine times faster, a pace where the pause is imperceptible!





