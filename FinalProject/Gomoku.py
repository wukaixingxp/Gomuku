import graphics


#Introduction Class Runs Introduction Program to GoMoku.

class IntroScreen:
    
    def __init__(self):
        
        self.win = graphics.GraphWin("Gomoku Start",300,300)
        self.win.setCoords(0,0,300,300)
    
    def intro(self):
        
        '''
        Main intro page function. Runs generateIntro. "Searches" for a click on either the "play" or "instructions" button
        using a while loop set to true. When one button is clicked the intro page is undrawn and the appropriate function
        is run. When the self.chooseOpponent function and all of its subsidiaries are run, the values chosen in them are returned
        via this function to the main function.
        '''
        
        self.generateIntro()
        while True:
            click = self.win.getMouse()
            X = click.getX()
            Y = click.getY()
            if 70 < Y < 120:
                if 20 < X < 140:
                    self.unDrawObjects()
                    return self.chooseOpponent()
                    
                if 160 < X < 280:
                    self.unDrawObjects()
                    self.instruct()
                    self.generateIntro()
                      
    def instruct(self):
        
        '''
        Instructions page function. Displays instructions. Returns to intro page when "back" button is clicked (uses
        a while loop set to true).
        '''
        
        Title = graphics.Text(graphics.Point(150, 275), "Instructions")
        Title.setSize(24)
        Title.draw(self.win)
        instructions = graphics.Text(graphics.Point(150,185), "GoMoku or GoBang is an oriental\n board-game, similar to the game" +
        " Go. Players \n alternate placing black and white stones \n on the vertices of the board. The game is \n won when a player manages" +
        " to place five \n stones of the same color in a row (horizontally, \n diagonally, or vertically). Try it out for yourself!")
        instructions.setSize(14)
        instructions.draw(self.win)
        
        backButton = graphics.Rectangle(graphics.Point(110,100),graphics.Point(190,40))
        backButton.setFill("red")
        backButtonText = graphics.Text(graphics.Point(150,70), "Back")
        backButtonText.setSize(16)
        backButtonText.setStyle("bold")
        backButtonText.setTextColor("white")
        backButton.draw(self.win)
        backButtonText.draw(self.win)
        
        while True:
            click = self.win.getMouse()
            X = click.getX()
            Y = click.getY()
            if 110 < X < 190:
                if 40 < Y < 100:
                    instructions.undraw()
                    backButton.undraw()
                    backButtonText.undraw()
                    Title.undraw()
                    return
    
    def chooseOpponent(self):
        
        '''
        Another game-set-up page. User is presented with two options (computer or human opponent) and chooseColor
        function runs when one is clicked (methodology is the same as intro page). Additionally the difficulty
        funciton runs if computer is selected.
        '''
        
        typeText = graphics.Text(graphics.Point(150,250),"Choose an opponent!")
        typeText.setSize(24)
        typeText.draw(self.win)
        
        self.playButton.setFill("Blue")
        self.playButton.draw(self.win)
        self.humanButtonText = graphics.Text(graphics.Point(80,95), "Human")
        self.humanButtonText.setSize(20)
        self.humanButtonText.setTextColor("white")
        self.humanButtonText.draw(self.win)

        self.instructButton.setFill("Orange")
        self.instructButton.draw(self.win)
        self.computerButtonText = graphics.Text(graphics.Point(220,95), "Computer")
        self.computerButtonText.setSize(20)
        self.computerButtonText.draw(self.win)
        
        while True:
            click = self.win.getMouse()
            X = click.getX()
            Y = click.getY()
            if 70 < Y < 120:
                if 20 < X < 140:
                    typeText.undraw()
                    self.playButton.undraw()
                    self.humanButtonText.undraw()
                    self.instructButton.undraw()
                    self.computerButtonText.undraw()
                    return self.chooseColor("Human", 0)
                    
                if 160 < X < 280:
                    typeText.undraw()
                    self.playButton.undraw()
                    self.humanButtonText.undraw()
                    self.instructButton.undraw()
                    self.computerButtonText.undraw()
                    difficulty = self.difficulty()
                    return self.chooseColor("Computer", difficulty)
                    
    def difficulty(self):
        
        '''
        Another game-set-up page. User is presented with two difficulty options (easy or hard) and chooseColor
        function runs when one is clicked (methodology is the same as intro page).
        '''
        
        difficultyText = graphics.Text(graphics.Point(150,250),"Choose a difficulty!")
        difficultyText.setSize(24)
        difficultyText.draw(self.win)
        
        self.playButton.setFill("Purple")
        self.playButton.draw(self.win)
        self.easyButtonText = graphics.Text(graphics.Point(80,95), "Easy")
        self.easyButtonText.setSize(20)
        self.easyButtonText.setTextColor("white")
        self.easyButtonText.draw(self.win)

        self.instructButton.setFill("Yellow")
        self.instructButton.draw(self.win)
        self.hardButtonText = graphics.Text(graphics.Point(220,95), "Hard")
        self.hardButtonText.setSize(20)
        self.hardButtonText.draw(self.win)
        
        while True:
            click = self.win.getMouse()
            X = click.getX()
            Y = click.getY()
            if 70 < Y < 120:
                if 20 < X < 140:
                    difficultyText.undraw()
                    self.playButton.undraw()
                    self.humanButtonText.undraw()
                    self.instructButton.undraw()
                    self.computerButtonText.undraw()
                    return "Easy"
                    
                if 160 < X < 280:
                    difficultyText.undraw()
                    self.playButton.undraw()
                    self.easyButtonText.undraw()
                    self.instructButton.undraw()
                    self.hardButtonText.undraw()
                    return "Hard"
                    
    def chooseColor(self,opponent, difficulty):
        
        '''
        Another game-set-up page. User is presented with two options (black or white, black plays first) and both the opponent
        and the color are returned when one is clicked (methods used are same as the intro page function).
        '''
        
        typeText = graphics.Text(graphics.Point(150,250),"Choose a team color! \n Black moves first.")
        typeText.setSize(24)
        typeText.draw(self.win)
        
        self.playButton.setFill("Black")
        self.playButton.draw(self.win)

        self.instructButton.setFill("white")
        self.instructButton.draw(self.win)
        
        while True:
            click = self.win.getMouse()
            X = click.getX()
            Y = click.getY()
            if 70 < Y < 120:
                if 20 < X < 140:
                    return [opponent, difficulty, "Black"]
                    
                if 160 < X < 280:
                    return [opponent, difficulty, "White"]
    
    def generateIntro(self):
        
        #Generates a number of graphics objects for intro page 
        
        self.introText =  graphics.Text(graphics.Point(150,250), "Welcome to Gomoku!")
        self.introText.setSize(30)
        self.introText.draw(self.win)
        
        self.playButton = graphics.Rectangle(graphics.Point(20,120),graphics.Point(140,70))
        self.playButton.setFill("Green")
        self.playButton.draw(self.win)
        self.playButtonText = graphics.Text(graphics.Point(80,95), "Play Game!")
        self.playButtonText.setSize(20)
        self.playButtonText.draw(self.win)
        
        self.instructButton = graphics.Rectangle(graphics.Point(160,120),graphics.Point(280,70))
        self.instructButton.setFill("Purple")
        self.instructButton.draw(self.win)
        self.instructButtonText = graphics.Text(graphics.Point(220,95), "Instructions")
        self.instructButtonText.setSize(20)
        self.instructButtonText.setTextColor("white")
        self.instructButtonText.draw(self.win) 
    
    def unDrawObjects(self):
        
        #Undraws objects for the intro screen.
        
        self.introText.undraw()
        self.playButtonText.undraw()
        self.instructButtonText.undraw()
        self.playButton.undraw()
        self.instructButton.undraw()


#____________________________________________________________________________

'''
This is the board class. Its purpose is to generate a graphical interface players can use to interact
with the program. Size is a parameter because some variations of GoMoku call for a larger board (and different
winning conditions, but we use the standard 15X15 here for AI consistency.
'''


class Board:
    
    def __init__(self, size):
       
    #Board generation instance variables
    
        self.win = graphics.GraphWin("Gomoku",600,600)
        self.win.setCoords(-50, -50, 550, 550)
        
        self.size = size
        
    #Generates stones objects. Detailed below and in readme.
        self.generateStones()
        self.stonesGraphic = []
        self.stonesOrder = []
        self.undoList = []
        
    #Generates graphical board objects
    
        self.background()
        self.lines()
        self.generateButtons()
        
#Board generation methods
    
    '''
    Stone generation function. Using lists we generate 15 lists, each with 15 stone objects inside of them. The lists
    themselves represent the positions of the stones; i.e. if  a stone is in the first list its x positions is the first
    vertical line on our grid. The stone's placement in the list represents its y position, so the fourth stone in 
    every list is on the fourth horizontal line from the bottom of the grid. The stones have a default team of "0", to
    indicate that nobody has played a stone on that vertex yet.
    '''
       
    def generateStones(self):
        
        self.stones = []
        for i in range(16):
            list = []
            for j in range(16):
                stone = Stone(0)
                list.append(stone)
            self.stones.append(list)
    
    #Generates 16 vertical and horizontal lines and appends them to a list of lines. Lines are spaced 
    #30 pixels apart using "for" loops. Lines are then drawn on board.
    
    def lines(self):

        lines = []
        for i in range(self.size):
            vertLine = graphics.Line(graphics.Point(30*i, 0),graphics.Point(30*i, 420))
            lines.append(vertLine)
        for i in range(self.size):
            horizLine = graphics.Line(graphics.Point(0, 30*i),graphics.Point(420, 30*i))
            lines.append(horizLine)
        for item in lines:
            item.draw(self.win)
    
    def background(self):       
        
        self.board = graphics.Image(graphics.Point(100,200), "wood.ppm")
        self.board.draw(self.win)
    
    #Generates the game title and "undo, newgame, and resign" buttons respectively.
    
    def generateButtons(self):
        
        self.gomokuText = graphics.Text(graphics.Point(230,495), "G o m o k u")
        self.gomokuText.setStyle("bold")
        self.gomokuText.setSize(36)
        self.gomokuText.setFace("helvetica")
        self.gomokuText.draw(self.win)
        
        self.undoButton = graphics.Rectangle(graphics.Point(465,300), graphics.Point(545,350))
        self.undoButton.setFill("red")
        self.undoButton.draw(self.win)
        self.undoText = graphics.Text(graphics.Point(505,325), "Undo")
        self.undoText.setSize(14)
        self.undoText.setStyle("bold")
        self.undoText.setTextColor("white")
        self.undoText.draw(self.win)
        
        self.newGame = graphics.Rectangle(graphics.Point(465,200), graphics.Point(545,250))
        self.newGameText = graphics.Text(graphics.Point(505,225), "New Game")
        self.newGame.setFill("blue")
        self.newGameText.setSize(14)
        self.newGameText.setTextColor("white")
        self.newGame.draw(self.win)
        self.newGameText.draw(self.win)
        
        self.resign = graphics.Rectangle(graphics.Point(465,100), graphics.Point(545,150))
        self.resign.setFill("black")
        self.resign.draw(self.win)
        self.resignText = graphics.Text(graphics.Point(505,125), "Resign")
        self.resignText.setSize(14)
        self.resignText.setTextColor("white")
        self.resignText.draw(self.win)
        
        self.quit = graphics.Rectangle(graphics.Point(465,0), graphics.Point(545,50))
        self.quit.setFill(graphics.color_rgb(100,200,100))
        self.quit.draw(self.win)
        self.quitText = graphics.Text(graphics.Point(505,25), "Quit")
        self.quitText.setSize(14)
        self.quitText.setTextColor("white")
        self.quitText.draw(self.win)
        
        
    
    '''
    This function allows us to analyze user clicks on the board. It takes the x and y pixel of the click as inputs
    and outputs that click to the nearest "30" (the board's vertices are located at intervals of 30 pixels on the 
    screen. This way, if a player clicks near a vertex, but not directly on it, the program still recognizes the 
    click as a valid move. The modified point is returned.
    '''
    
    def findPoint(self,X,Y):
        
        divideX = X // 30
        remainderX = X % 30
        divideY =  Y // 30
        remainderY = Y % 30
       
        if remainderX > 14:
            divideX = divideX + 1
        if remainderY > 14: 
            divideY = divideY + 1
        point = (divideX*30, divideY*30)
        
        return point
 
        
#Board modification methods    
    
    '''
    This method is extremely long (and repetitive, but for good reason), so we have taken all the comments we would
    have put in it and put them out in this paragraph. In order to add a stone, we first generate a completely new stone
    (so replacing the previous unactualized one) that has the associated team. We append this stone to the stonesOrder 
    list and replace the old unactualzied stone in "stones". Then we begin modifying priorities. We use an if statement
    to seperate the cases where the stone is white and where the stone is black. We do so because, despite the inefficiency,
    we need to determine whether the stone affects the white priorities or the black ones. Next we run eight for loops,
    representing the eight cardinal directions. The for loops assess the interaction between the new stone and each
    stone within four vertices of it (in every direction). Depending on the team of the stone, we enter into a 
    different if statement. If the stones are the same team they have the same amount of priority added to the
    opposite directions (for example xP and xM, since they "face" one another in different directions). The amount
    of priority is dependent on the distance between them, i. If the "stone" is unactualized i.e. has no team, the 
    unactualized stone's priority is changed, but the new one's is not. If the stone's are opposite teams, they cause
    their corresponding priority values to be zero. However, this value is saved in the second entry of their priority
    list (each priority value takes the form [x,y]) so that it can be switched back in removeStone in case the newly
    placed stone is removed. This proces continues for all 16 priority values. 
    '''
    
    #One might complain that the code here is excessively long. Because we have 16 uniquely named priorities, it 
    #became necessary to make them that long--we would have needed to initialized them as a list otherwise. While this
    #is possible, we feel that the code is more malleable and thus useful when each different priority value can be 
    #individually modified.
    
    #undoList has been added to fix AI errors with the undo button.
    
    def addStone(self, xPos, yPos,color):
        
        stone = Stone(color)
        self.stonesOrder.append([xPos,yPos,stone])
        self.undoList.append(self.stones[xPos][yPos])
        self.stones[xPos][yPos] = stone
        
        if color == "White":
            for i in range(1,5):
                if self.stones[min(xPos+i, 15)][yPos].team == color:
                    if xPos+i < 16:
                        self.stones[min(xPos+i, 15)][yPos].wxM[0] += 5 - i
                        self.stones[xPos][yPos].wxP[0] += 5 - i
                elif self.stones[min(xPos+i, 15)][yPos].team == 0:
                     self.stones[min(xPos+i, 15)][yPos].wxM[0] += 5 - i
                else:
                    self.stones[min(xPos+i, 15)][yPos].wxM[1] = self.stones[min(xPos+i, 15)][yPos].wxM[0]
                    self.stones[xPos][yPos].wxP[1] = self.stones[xPos][yPos].wxP[0]
                    self.stones[min(xPos+i, 15)][yPos].wxM[0] = 0
                    self.stones[xPos][yPos].wxP[0] = 0
            for i in range(1,5):
                if xPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][yPos].team == color:
                    if xPos-i > -1:
                        self.stones[max(xPos-i, 0)][yPos].wxP[0] += 5 - i
                        self.stones[xPos][yPos].wxM[0] += 5 - i
                elif self.stones[max(xPos-i, 0)][yPos].team == 0:
                    if xPos-i != 0:
                       self.stones[max(xPos-i, 0)][yPos].wxP[0] += 5 - i
                else:
                    self.stones[max(xPos-i, 0)][yPos].wxP[1] = self.stones[max(xPos-i, 0)][yPos].wxP[0]
                    self.stones[xPos][yPos].wxM[1] = self.stones[xPos][yPos].wxM[0]
                    self.stones[max(xPos-i, 0)][yPos].wxP[0] = 0
                    self.stones[xPos][yPos].wxM[0] = 0
            for i in range(1,5):
                if self.stones[xPos][min(yPos+i, 15)].team == color:
                    if yPos+i<16:
                        self.stones[xPos][min(yPos+i, 15)].wyM[0] += 5 - i
                        self.stones[xPos][yPos].wyP[0] += 5 - i
                elif self.stones[xPos][min(yPos+i, 15)].team == 0:
                    self.stones[xPos][min(yPos+i, 15)].wyM[0] += 5 - i
                else:
                    self.stones[xPos][min(yPos+i, 15)].wyM[1] = self.stones[xPos][min(yPos+i, 15)].wyM[0]
                    self.stones[xPos][yPos].wyP[1] = self.stones[xPos][yPos].wyP[0]
                    self.stones[xPos][min(yPos+i, 15)].wyM[0] = 0
                    self.stones[xPos][yPos].wyP[0] = 0
            for i in range(1,5):
                if yPos == 0:
                    donothing = 0
                elif self.stones[xPos][max(yPos-i, 0)].team == color:
                    if yPos-i > -1:
                        self.stones[xPos][max(yPos-i, 0)].wyP[0] += 5 - i
                        self.stones[xPos][yPos].wyM[0] += 5 - i
                elif self.stones[xPos][max(yPos-i, 0)].team == 0:
                     self.stones[xPos][max(yPos-i, 0)].wyP[0] += 5 - i
                else:
                    self.stones[xPos][max(yPos-i, 0)].wyP[1] = self.stones[xPos][max(yPos-i, 0)].wyP[0]
                    self.stones[xPos][yPos].wyM[1] = self.stones[xPos][yPos].wyM[0]
                    self.stones[xPos][max(yPos-i, 0)].wyP[0] = 0
                    self.stones[xPos][yPos].wyM[0] = 0
            for i in range(1,5):
                if self.stones[min(xPos+i, 15)][min(yPos+i, 15)].team == color:
                    if xPos+i <16 or yPos+i <16:
                        self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[0] += 5 - i
                        self.stones[xPos][yPos].wxPyP[0] += 5 - i
                elif self.stones[min(xPos+i, 15)][min(yPos+i, 15)].team == 0:
                     self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[0] += 5 - i
                else:
                    self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[1] = self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[0]
                    self.stones[xPos][yPos].wxPyP[1] = self.stones[xPos][yPos].wxPyP[0]
                    self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[0] = 0
                    self.stones[xPos][yPos].wxPyP[0] = 0
            for i in range(1,5):
                if xPos == 0 or yPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][max(yPos-i, 0)].team == color:
                    if xPos-i > -1 or yPos-i > -1:
                        self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[0] += 5 - i
                        self.stones[xPos][yPos].wxMyM[0] += 5 - i
                elif self.stones[max(xPos-i, 0)][max(yPos-i, 0)].team == 0:
                     self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[0] += 5 - i
                else:
                    self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[1] = self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[0]
                    self.stones[xPos][yPos].wxMyM[1] = self.stones[xPos][yPos].wxMyM[0]
                    self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[0] = 0
                    self.stones[xPos][yPos].wxMyM[0] = 0
            for i in range(1,5):
                if xPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][min(yPos+i, 15)].team == color:
                    if xPos-i> -1 or yPos+i <16:
                        self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[0] += 5 - i
                        self.stones[xPos][yPos].wxMyP[0] += 5 - i
                elif self.stones[max(xPos-i, 0)][min(yPos+i, 15)].team == 0:
                     self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[0] += 5 - i
                else:
                    self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[1] = self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[0]
                    self.stones[xPos][yPos].wxPyM[1] = self.stones[xPos][yPos].wxMyP[0]
                    self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[0] = 0
                    self.stones[xPos][yPos].wxMyP[0] = 0
            for i in range(1,5):
                if yPos == 0:
                    donothing = 0
                if self.stones[min(xPos+i, 15)][max(yPos-i, 0)].team == color:
                    if xPos+i<15 or yPos-i > -1:
                        self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[0] += 5 - i
                        self.stones[xPos][yPos].wxPyM[0] += 5 - i
                elif self.stones[min(xPos+i, 15)][max(yPos-i, 0)].team == 0:
                     self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[0] += 5 - i
                else:
                    self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[1] = self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[0]
                    self.stones[xPos][yPos].wxPyM[1] = self.stones[xPos][yPos].wxPyM[0]
                    self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[0] = 0
                    self.stones[xPos][yPos].wxPyM[0] = 0
        elif color == "Black":
            for i in range(1,5):
                if self.stones[min(xPos+i, 15)][yPos].team == color:
                    if xPos+i < 16:
                        self.stones[min(xPos+i, 15)][yPos].bxM[0] += 5 - i
                        self.stones[xPos][yPos].bxP[0] += 5 - i
                elif self.stones[min(xPos+i, 15)][yPos].team == 0:
                     self.stones[min(xPos+i, 15)][yPos].bxM[0] += 5 - i
                else:
                    self.stones[min(xPos+i, 15)][yPos].bxM[1] = self.stones[min(xPos+i, 15)][yPos].bxM[0]
                    self.stones[xPos][yPos].bxP[1] = self.stones[xPos][yPos].bxP[0]
                    self.stones[min(xPos+i, 15)][yPos].bxM[0] = 0
                    self.stones[xPos][yPos].bxP[0] = 0
            for i in range(1,5):
                if xPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][yPos].team == color:
                    if xPos-i > -1:
                        self.stones[max(xPos-i, 0)][yPos].bxP[0] += 5 - i
                        self.stones[xPos][yPos].bxM[0] += 5 - i
                elif self.stones[max(xPos-i, 0)][yPos].team == 0:
                    if xPos-i != 0:
                       self.stones[max(xPos-i, 0)][yPos].bxP[0] += 5 - i
                else:
                    self.stones[max(xPos-i, 0)][yPos].bxP[1] = self.stones[max(xPos-i, 0)][yPos].bxP[0]
                    self.stones[xPos][yPos].bxM[1] = self.stones[xPos][yPos].bxM[0]
                    self.stones[max(xPos-i, 0)][yPos].bxP[0] = 0
                    self.stones[xPos][yPos].bxM[0] = 0
            for i in range(1,5):
                if self.stones[xPos][min(yPos+i, 15)].team == color:
                    if yPos+i<16:
                        self.stones[xPos][min(yPos+i, 15)].byM[0] += 5 - i
                        self.stones[xPos][yPos].byP[0] += 5 - i
                elif self.stones[xPos][min(yPos+i, 15)].team == 0:
                    self.stones[xPos][min(yPos+i, 15)].byM[0] += 5 - i
                else:
                    self.stones[xPos][min(yPos+i, 15)].byM[1] = self.stones[xPos][min(yPos+i, 15)].byM[0]
                    self.stones[xPos][yPos].byP[1] = self.stones[xPos][yPos].byP[0]
                    self.stones[xPos][min(yPos+i, 15)].byM[0] = 0
                    self.stones[xPos][yPos].byP[0] = 0
            for i in range(1,5):
                if yPos == 0:
                    donothing = 0
                elif self.stones[xPos][max(yPos-i, 0)].team == color:
                    if yPos-i > -1:
                        self.stones[xPos][max(yPos-i, 0)].byP[0] += 5 - i
                        self.stones[xPos][yPos].byM[0] += 5 - i
                elif self.stones[xPos][max(yPos-i, 0)].team == 0:
                     self.stones[xPos][max(yPos-i, 0)].byP[0] += 5 - i
                else:
                    self.stones[xPos][max(yPos-i, 0)].byP[1] = self.stones[xPos][max(yPos-i, 0)].byP[0]
                    self.stones[xPos][yPos].byM[1] = self.stones[xPos][yPos].byM[0]
                    self.stones[xPos][max(yPos-i, 0)].byP[0] = 0
                    self.stones[xPos][yPos].byM[0] = 0
            for i in range(1,5):
                if self.stones[min(xPos+i, 15)][min(yPos+i, 15)].team == color:
                    if xPos+i <16 or yPos+i <16:
                        self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[0] += 5 - i
                        self.stones[xPos][yPos].bxPyP[0] += 5 - i
                elif self.stones[min(xPos+i, 15)][min(yPos+i, 15)].team == 0:
                     self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[0] += 5 - i
                else:
                    self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[1] = self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[0]
                    self.stones[xPos][yPos].bxPyP[1] = self.stones[xPos][yPos].bxPyP[0]
                    self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[0] = 0
                    self.stones[xPos][yPos].bxPyP[0] = 0
            for i in range(1,5):
                if xPos == 0 or yPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][max(yPos-i, 0)].team == color:
                    if xPos-i > -1 or yPos-i > -1:
                        self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[0] += 5 - i
                        self.stones[xPos][yPos].bxMyM[0] += 5 - i
                elif self.stones[max(xPos-i, 0)][max(yPos-i, 0)].team == 0:
                     self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[0] += 5 - i
                else:
                    self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[1] = self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[0]
                    self.stones[xPos][yPos].bxMyM[1] = self.stones[xPos][yPos].bxMyM[0]
                    self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[0] = 0
                    self.stones[xPos][yPos].bxMyM[0] = 0
            for i in range(1,5):
                if xPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][min(yPos+i, 15)].team == color:
                    if xPos-i> -1 or yPos+i <16:
                        self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[0] += 5 - i
                        self.stones[xPos][yPos].bxMyP[0] += 5 - i
                elif self.stones[max(xPos-i, 0)][min(yPos+i, 15)].team == 0:
                     self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[0] += 5 - i
                else:
                    self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[1] = self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[0]
                    self.stones[xPos][yPos].bxPyM[1] = self.stones[xPos][yPos].bxMyP[0]
                    self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[0] = 0
                    self.stones[xPos][yPos].bxMyP[0] = 0
            for i in range(1,5):
                if yPos == 0:
                    donothing = 0
                if self.stones[min(xPos+i, 15)][max(yPos-i, 0)].team == color:
                    if xPos+i<15 or yPos-i > -1:
                        self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[0] += 5 - i
                        self.stones[xPos][yPos].bxPyM[0] += 5 - i
                elif self.stones[min(xPos+i, 15)][max(yPos-i, 0)].team == 0:
                     self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[0] += 5 - i
                else:
                    self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[1] = self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[0]
                    self.stones[xPos][yPos].bxPyM[1] = self.stones[xPos][yPos].bxPyM[0]
                    self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[0] = 0
                    self.stones[xPos][yPos].bxPyM[0] = 0
        
                
    '''
    This function does the exact opposite of what the addStone function does. First it "undoes" all the priority
    modification done in the addStone function. It does so by identifying every stone (in the same manner as addStone)
    that would have been modified when the stone was added and doing the opposite operation to that stone. For example,
    if we added four priority to the xP value of a stone when the stone was added, we would now subtract four priority 
    from the xP value of the modified stone. Similarly, if a stone was placed that "zeroed" the priority of another stone,
    we "restore" the priority of that stone by switching the first and second items of the priority value so that the 
    stores value is now the first value.
    '''
    
    def removeStone(self, xPos, yPos):
        
        color = self.stones[xPos][yPos].team
        
        if color == "White":
            for i in range(1,5):
                if self.stones[min(xPos+i, 15)][yPos].team == color:
                    if xPos+i < 16:
                        self.stones[min(xPos+i, 15)][yPos].wxM[0] += i - 5
                        self.stones[xPos][yPos].wxP[0] += i - 5
                elif self.stones[min(xPos+i, 15)][yPos].team == 0:
                     self.stones[min(xPos+i, 15)][yPos].wxM[0] += i - 5
                else:
                    self.stones[min(xPos+i, 15)][yPos].wxM[0] = self.stones[min(xPos+i, 15)][yPos].wxM[1]
                    self.stones[xPos][yPos].wxP[0] = self.stones[xPos][yPos].wxP[1]
                    self.stones[min(xPos+i, 15)][yPos].wxM[1] = 0
                    self.stones[xPos][yPos].wxP[1] = 0
            for i in range(1,5):
                if xPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][yPos].team == color:
                    if xPos-i > -1:
                        self.stones[max(xPos-i, 0)][yPos].wxP[0] += i - 5
                        self.stones[xPos][yPos].wxM[0] += i - 5
                elif self.stones[max(xPos-i, 0)][yPos].team == 0:
                    if xPos-i != 0:
                       self.stones[max(xPos-i, 0)][yPos].wxP[0] += i - 5
                else:
                    self.stones[max(xPos-i, 0)][yPos].wxP[0] = self.stones[max(xPos-i, 0)][yPos].wxP[1]
                    self.stones[xPos][yPos].wxM[0] = self.stones[xPos][yPos].wxM[1]
                    self.stones[max(xPos-i, 0)][yPos].wxP[1] = 0
                    self.stones[xPos][yPos].wxM[1] = 0
            for i in range(1,5):
                if self.stones[xPos][min(yPos+i, 15)].team == color:
                    if yPos+i<16:
                        self.stones[xPos][min(yPos+i, 15)].wyM[0] += i - 5
                        self.stones[xPos][yPos].wyP[0] += i - 5
                elif self.stones[xPos][min(yPos+i, 15)].team == 0:
                    self.stones[xPos][min(yPos+i, 15)].wyM[0] += i - 5
                else:
                    self.stones[xPos][min(yPos+i, 15)].wyM[0] = self.stones[xPos][min(yPos+i, 15)].wyM[1]
                    self.stones[xPos][yPos].wyP[0] = self.stones[xPos][yPos].wyP[1]
                    self.stones[xPos][min(yPos+i, 15)].wyM[1] = 0
                    self.stones[xPos][yPos].wyP[1] = 0
            for i in range(1,5):
                if yPos == 0:
                    donothing = 0
                elif self.stones[xPos][max(yPos-i, 0)].team == color:
                    if yPos-i > -1:
                        self.stones[xPos][max(yPos-i, 0)].wyP[0] += i - 5
                        self.stones[xPos][yPos].wyM[0] += i - 5
                elif self.stones[xPos][max(yPos-i, 0)].team == 0:
                     self.stones[xPos][max(yPos-i, 0)].wyP[0] += i - 5
                else:
                    self.stones[xPos][max(yPos-i, 0)].wyP[0] = self.stones[xPos][max(yPos-i, 0)].wyP[1]
                    self.stones[xPos][yPos].wyM[0] = self.stones[xPos][yPos].wyM[1]
                    self.stones[xPos][max(yPos-i, 0)].wyP[1] = 0
                    self.stones[xPos][yPos].wyM[1] = 0
            for i in range(1,5):
                if self.stones[min(xPos+i, 15)][min(yPos+i, 15)].team == color:
                    if xPos+i <16 or yPos+i <16:
                        self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[0] += i - 5
                        self.stones[xPos][yPos].wxPyP[0] += i - 5
                elif self.stones[min(xPos+i, 15)][min(yPos+i, 15)].team == 0:
                     self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[0] += i - 5
                else:
                    self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[0] = self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[1]
                    self.stones[xPos][yPos].wxPyP[0] = self.stones[xPos][yPos].wxPyP[1]
                    self.stones[min(xPos+i, 15)][min(yPos+i, 15)].wxMyM[1] = 0
                    self.stones[xPos][yPos].wxPyP[1] = 0
            for i in range(1,5):
                if xPos == 0 or yPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][max(yPos-i, 0)].team == color:
                    if xPos-i > -1 or yPos-i > -1:
                        self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[0] += i - 5
                        self.stones[xPos][yPos].wxMyM[0] += i - 5
                elif self.stones[max(xPos-i, 0)][max(yPos-i, 0)].team == 0:
                     self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[0] += i - 5
                else:
                    self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[0] = self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[1]
                    self.stones[xPos][yPos].wxMyM[0] = self.stones[xPos][yPos].wxMyM[1]
                    self.stones[max(xPos-i, 0)][max(yPos-i, 0)].wxPyP[1] = 0
                    self.stones[xPos][yPos].wxMyM[1] = 0
            for i in range(1,5):
                if xPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][min(yPos+i, 15)].team == color:
                    if xPos-i> -1 or yPos+i <16:
                        self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[0] += i - 5
                        self.stones[xPos][yPos].wxMyP[0] += i - 5
                elif self.stones[max(xPos-i, 0)][min(yPos+i, 15)].team == 0:
                     self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[0] += i - 5
                else:
                    self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[0] = self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[1]
                    self.stones[xPos][yPos].wxPyM[0] = self.stones[xPos][yPos].wxMyP[1]
                    self.stones[max(xPos-i, 0)][min(yPos+i, 15)].wxPyM[1] = 0
                    self.stones[xPos][yPos].wxMyP[1] = 0
            for i in range(1,5):
                if yPos == 0:
                    donothing = 0
                if self.stones[min(xPos+i, 15)][max(yPos-i, 0)].team == color:
                    if xPos+i<15 or yPos-i > -1:
                        self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[0] += i - 5
                        self.stones[xPos][yPos].wxPyM[0] += i - 5
                elif self.stones[min(xPos+i, 15)][max(yPos-i, 0)].team == 0:
                     self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[0] += i - 5
                else:
                    self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[0] = self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[1]
                    self.stones[xPos][yPos].wxPyM[0] = self.stones[xPos][yPos].wxPyM[1]
                    self.stones[min(xPos+i, 15)][max(yPos-i, 0)].wxMyP[1] = 0
                    self.stones[xPos][yPos].wxPyM[1] = 0
        elif color == "Black":
            for i in range(1,5):
                if self.stones[min(xPos+i, 15)][yPos].team == color:
                    if xPos+i < 16:
                        self.stones[min(xPos+i, 15)][yPos].bxM[0] += i - 5
                        self.stones[xPos][yPos].bxP[0] += i - 5
                elif self.stones[min(xPos+i, 15)][yPos].team == 0:
                     self.stones[min(xPos+i, 15)][yPos].bxM[0] += i - 5
                else:
                    self.stones[min(xPos+i, 15)][yPos].bxM[0] = self.stones[min(xPos+i, 15)][yPos].bxM[1]
                    self.stones[xPos][yPos].bxP[0] = self.stones[xPos][yPos].bxP[1]
                    self.stones[min(xPos+i, 15)][yPos].bxM[1] = 0
                    self.stones[xPos][yPos].bxP[1] = 0
            for i in range(1,5):
                if xPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][yPos].team == color:
                    if xPos-i > -1:
                        self.stones[max(xPos-i, 0)][yPos].bxP[0] += i - 5
                        self.stones[xPos][yPos].bxM[0] += i - 5
                elif self.stones[max(xPos-i, 0)][yPos].team == 0:
                    if xPos-i != 0:
                       self.stones[max(xPos-i, 0)][yPos].bxP[0] += i - 5
                else:
                    self.stones[max(xPos-i, 0)][yPos].bxP[0] = self.stones[max(xPos-i, 0)][yPos].bxP[1]
                    self.stones[xPos][yPos].bxM[0] = self.stones[xPos][yPos].bxM[1]
                    self.stones[max(xPos-i, 0)][yPos].bxP[1] = 0
                    self.stones[xPos][yPos].bxM[1] = 0
            for i in range(1,5):
                if self.stones[xPos][min(yPos+i, 15)].team == color:
                    if yPos+i<16:
                        self.stones[xPos][min(yPos+i, 15)].byM[0] += i - 5
                        self.stones[xPos][yPos].byP[0] += i - 5
                elif self.stones[xPos][min(yPos+i, 15)].team == 0:
                    self.stones[xPos][min(yPos+i, 15)].byM[0] += i - 5
                else:
                    self.stones[xPos][min(yPos+i, 15)].byM[0] = self.stones[xPos][min(yPos+i, 15)].byM[1]
                    self.stones[xPos][yPos].byP[0] = self.stones[xPos][yPos].byP[1]
                    self.stones[xPos][min(yPos+i, 15)].byM[1] = 0
                    self.stones[xPos][yPos].byP[1] = 0
            for i in range(1,5):
                if yPos == 0:
                    donothing = 0
                elif self.stones[xPos][max(yPos-i, 0)].team == color:
                    if yPos-i > -1:
                        self.stones[xPos][max(yPos-i, 0)].byP[0] += i - 5
                        self.stones[xPos][yPos].byM[0] += i - 5
                elif self.stones[xPos][max(yPos-i, 0)].team == 0:
                     self.stones[xPos][max(yPos-i, 0)].byP[0] += i - 5
                else:
                    self.stones[xPos][max(yPos-i, 0)].byP[0] = self.stones[xPos][max(yPos-i, 0)].byP[1]
                    self.stones[xPos][yPos].byM[0] = self.stones[xPos][yPos].byM[1]
                    self.stones[xPos][max(yPos-i, 0)].byP[1] = 0
                    self.stones[xPos][yPos].byM[1] = 0
            for i in range(1,5):
                if self.stones[min(xPos+i, 15)][min(yPos+i, 15)].team == color:
                    if xPos+i <16 or yPos+i <16:
                        self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[0] += i - 5
                        self.stones[xPos][yPos].bxPyP[0] += i - 5
                elif self.stones[min(xPos+i, 15)][min(yPos+i, 15)].team == 0:
                     self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[0] += i - 5
                else:
                    self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[0] = self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[1]
                    self.stones[xPos][yPos].bxPyP[0] = self.stones[xPos][yPos].bxPyP[1]
                    self.stones[min(xPos+i, 15)][min(yPos+i, 15)].bxMyM[1] = 0
                    self.stones[xPos][yPos].bxPyP[1] = 0
            for i in range(1,5):
                if xPos == 0 or yPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][max(yPos-i, 0)].team == color:
                    if xPos-i > -1 or yPos-i > -1:
                        self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[0] += i - 5
                        self.stones[xPos][yPos].bxMyM[0] += i - 5
                elif self.stones[max(xPos-i, 0)][max(yPos-i, 0)].team == 0:
                     self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[0] += i - 5
                else:
                    self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[0] = self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[1]
                    self.stones[xPos][yPos].bxMyM[0] = self.stones[xPos][yPos].bxMyM[1]
                    self.stones[max(xPos-i, 0)][max(yPos-i, 0)].bxPyP[1] = 0
                    self.stones[xPos][yPos].bxMyM[1] = 0
            for i in range(1,5):
                if xPos == 0:
                    donothing = 0
                elif self.stones[max(xPos-i, 0)][min(yPos+i, 15)].team == color:
                    if xPos-i> -1 or yPos+i <16:
                        self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[0] += i - 5
                        self.stones[xPos][yPos].bxMyP[0] += i - 5
                elif self.stones[max(xPos-i, 0)][min(yPos+i, 15)].team == 0:
                     self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[0] += i - 5
                else:
                    self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[0] = self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[1]
                    self.stones[xPos][yPos].bxPyM[0] = self.stones[xPos][yPos].bxMyP[1]
                    self.stones[max(xPos-i, 0)][min(yPos+i, 15)].bxPyM[1] = 0
                    self.stones[xPos][yPos].bxMyP[1] = 0
            for i in range(1,5):
                if yPos == 0:
                    donothing = 0
                if self.stones[min(xPos+i, 15)][max(yPos-i, 0)].team == color:
                    if xPos+i<15 or yPos-i > -1:
                        self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[0] += i - 5
                        self.stones[xPos][yPos].bxPyM[0] += i - 5
                elif self.stones[min(xPos+i, 15)][max(yPos-i, 0)].team == 0:
                     self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[0] += i - 5
                else:
                    self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[0] = self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[1]
                    self.stones[xPos][yPos].bxPyM[0] = self.stones[xPos][yPos].bxPyM[1]
                    self.stones[min(xPos+i, 15)][max(yPos-i, 0)].bxMyP[1] = 0
                    self.stones[xPos][yPos].bxPyM[1] = 0
        
        
        #Lastly we set the stone's team to zero again (denoting that it is now an open vertex) and take it out of the
        #stonesOrder list.
        
        self.stones[xPos][yPos]=self.undoList[-1]
        self.stonesOrder.pop()
        self.undoList.pop()
    
    '''    
    This function graphicallly places a stone on the board. It takes its xPos and yPos input and converts them into the 
    corresponding pixel form. It then draws the stone. It also appends this graphics object to a list, in case we need
    to remove it.
    '''
    
    def placeStone(self,xPos,yPos,color):
        
        Stone = graphics.Circle(graphics.Point(30*xPos,30*yPos), 10)
        Stone.setFill(color)
        self.stonesGraphic.append([xPos, yPos, Stone])
        Stone.draw(self.win)


'''
This is the stone class. Stones have no position because the stones list in the board class keeps track of their 
position for them (every vertex on the board is considered a stone). Thus, for any given vertex we only need to know
the team it is on (White, Black, or 0 for neutral) and its position in relation to other stones. The instance variables
that follow self.team are the relational variables. There are sixteen: 8 for each color (so "w" represents relation towards
white stones and "b" for black), and two for each direction (xP is the x positive direction, xM the x minus direction. The 
same follows for yM and YP. Acroynyms like "xPyP" represent the positive x/y direction, so the northeast direction, and so
on). We also have a method that groups these values (known as priorities) into lists by color.
'''

#How priorities are calculated is explained in the add stone function.



class Stone:
        
    def __init__(self, team):
        
        self.team = team
        
        '''
        Also note that "priority" values are actually two values in a list. When a stone has stones of a similar team near
        it in the same direction, its priority value for that direction and team increase. However, when there also 
        exists an opposing team's stone nearby in that direction, the priority becomes zero (because we cannot line up 
        five stones in a row of the same color if a stone of the opposite color is in the way). But we might at some point 
        want to recover that first priority value (that was turned to zero by an opposing stone) if the opposing stone is
        eventually removed. Thus, we store the first value in the second spot on the list when the first spot is turned to
        zero, in case we need that value again.
        '''
        
        self.wxP = [0,0]
        self.wxM = [0,0]
        self.wyP = [0,0]
        self.wyM = [0,0]
        self.wxPyP = [0,0]
        self.wxPyM = [0,0]
        self.wxMyP = [0,0]
        self.wxMyM = [0,0]
        
        self.bxP = [0,0]
        self.bxM = [0,0]
        self.byP = [0,0]
        self.byM = [0,0]
        self.bxPyP = [0,0]
        self.bxPyM = [0,0]
        self.bxMyP = [0,0]
        self.bxMyM = [0,0]
        
        self.priority = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        
    #This method exist primarily to test if a player has won. It groups all the priority values that are of the same
    #team as the stone itself in a list, and then returns the list.
  
    def priorityList(self):
        if self.team == "White":
            self.priority = [self.wxP, self.wxM, self.wyP, self.wyM, self.wxPyP, self.wxPyM, self.wxMyP, self.wxMyM]
        elif self.team == "Black":
            self.priority = [self.bxP, self.bxM, self.byP, self.byM, self.bxPyP, self.bxPyM, self.bxMyP, self.bxMyM]
        return self.priority
    
    
'''
This is the human player class. It is relatively simple, containing only one main method and some other "sub"methods.
It takes its team-color as an input, as well as the board it is playing on, and intiializes them as instance variables.
'''    
    
    
class HumanPlayer:
    
    def __init__(self,teamColor,board):
        
        self.color = teamColor
        self.board = board
    
    '''
    The turn method allows the player to go about their turn. We first print some text on the board that denotes whose turn
    it is. Next, using a while loop set to true, we let the user click on the board to determine their move. Once a click
    is clicked (we get the click by running the getClick method), we look at its value. If it is a string with a command,
    we do that command (using if statements). If it is a point, we turn the point from "pixel" form to "vertex" form (so 
    we divide it by thirty) and search the stone list to determine if the vertex is open. If it is, we run the addStone and
    placeStone functions, placing that stone on the board, and end the turn. If it is not, the while loop repeats.
    '''
        
    def turn(self):
        
        #Text changes for new turn
        self.turnText = graphics.Text(graphics.Point(230,-27), self.color + "'s Turn!")
        if self.color == "White":
            self.turnText.setTextColor("white")
        self.turnText.setSize(20)
        self.turnText.draw(self.board.win)
        
        #Getting a click and determining what to do
        while True:
            point = self.getClick()
            if point == "done":
                return "done"
            
            elif type(point) != type("string"):
                i = int(point[0] / 30)
                j = int(point[1] / 30)
                stone = self.board.stones[i][j] 
                
                if stone.team == 0:
                    self.board.addStone(i,j,self.color)
                    self.board.placeStone(i,j,self.color)
                    self.turnText.undraw()
                    return 0
    
    '''
    This is the getClick method. Using a while loop we "force" the user to click the board. We first run otherClick to check
    if the click was for any of the buttons on the board. If it was, we return the value of the otherClick method.
    If not, we modify the click using the findPoint method, check to see whether the point is within the board, and then 
    return the point.
    '''
    
    def getClick(self):
        
        while True:
            
            click = self.board.win.getMouse()
            X = click.getX()
            Y = click.getY()
            
            value = self.otherClick(X,Y)
            if value != 0:
                return value
            
            point = self.board.findPoint(X,Y)	
            if  (-10 < point[0] < 430) and (-10 < point[1] < 430):
                return point
    
    #Using code similar to the intro page, we check to see if the click was within the buttons on the board. If so, we run
    #those functions. If not, we return 0.
    
    def otherClick(self,X,Y):
        
        if  465 < X < 545:
        	if 300 < Y < 350:
        		return self.undo()
        	elif 200 < Y < 250:
        		return self.makeNewGame()
        	elif 100 < Y <  150:
        		return self.resigning()
        	elif 0 < Y < 50:
        	    return self.quit()
    
        return 0
    
    '''
    This function "undos" the last two turns on the board. First it uses the remove stone function to remove the stone from
    the directory of stones and to undo any priority modifications that occurred when the stone was placed. Then we identify
    the stones in the stoneGraphic list, undraw it, and remove them from the list as well.
    '''
             
    def undo(self):
        
        for i in range(2):
            self.board.removeStone(self.board.stonesOrder[-1][0],self.board.stonesOrder[-1][1])
            stone = self.board.stonesGraphic[-1][2]
            stone.undraw()
            self.board.stonesGraphic.pop()
        return "not done"
   
   #This function makes a new game when the New Game button is clicked. It also returns done, which prompts the program
   #to end in a series of return sequences.
   
    def makeNewGame(self):
        self.board.win.close()
        main()
        return "done"
      
    #This functions prints resign text when the resign button is clicked. It also returns done, which prompts the program to
    #end in a series of return sequences.
    
    def resigning(self):
    	self.turnText.undraw()
    	
    	resignText = graphics.Text(graphics.Point(230,-10), self.color + " Resigned :( \n" + "Better Luck Next Time!" )
    	resignText.setSize(36)
    	resignText.setTextColor(self.color)
    	resignText.setFace("helvetica")
    	resignText.draw(self.board.win)
    	click = self.board.win.getMouse()
    	self.board.win.close()
    	main()
    	return "done"
    
    #Returns "done", which prompts a series of return sequences that end the program.
    
    def quit(self):
        return "done"


'''
This is the computer class. It has a number of instance variables and methods. Self.P3 represents the pseudo computer, which
is used to recursively calculate future moves. We also have the turn and calculate values methods. Turn, as expected, 
is the main function that determines what the computer does each turn. Calculate values returns the best moves the 
computer has, based on values calculated in the function. Lastly, self.level represents the number of recursive
loops we will calculate.
'''

    	
class Computer:
    
    def __init__(self, teamColor, difficulty, level, P3, board):
        self.color = teamColor
        self.board = board
        self.P3 = P3
        self.level = level
        
        #If the computer is going first, we have mandated it's first move so that it doesn't get confused (there are
        #no other stones to based it's move off of on the first move).
        
        if self.color == "Black":
            self.start = 1
        else:
            self.start = 0
        
        self.difficulty = difficulty    
    
    '''
    This function determines where the computer goes for it's turn. When it is not the first turn the computer defaults
    to the else statement below. It runs calculate values to return a list of moves paired with their associated values.
    It then uses, if the difficulty is hard, a for loop and the Pseudo Computer class to recursively generate the
    values of our moves based on the "future" move potential they have (i.e. Pseudo Computer assigns an average value
    to the sequences of moves that can result from playing a given move and returns this value. We then add the immediate
    value of our moves to their future values, choose the move with the largest total value, and run addStone and placeStone
    with that move.
    '''
    
    #!!! At the present time the hard difficulty is actually easier. This is due to a tendency towards aggressiveness
    #in the PseudoComputer AI that has not been fixed. See readme for more details.
    
    def turn(self):
        
        if  self.start == 1:
            self.start = 0
            self.board.addStone(7,7,self.color)
            self.board.placeStone(7,7,self.color)
            return 0
            
        else:
            movesList = self.calculateValues()
            futureList = []
            valuator = []
            
            for i in range(3):
                #By multiplying our move values with self.level ** 1.5 we weight these moves more heavily than the 
                #future moves--our thought process is that if there is an immediate way to win or lose we 
                #ought to play towards that. 
                valuator.append(self.level**(1.4) * movesList[i][0])
            
            if self.difficulty == "Hard":
                for i in range(3):
                    self.board.addStone(movesList[i][1][0],movesList[i][1][1],self.color)
                    output = self.P3.virtualCalculations(movesList[i][1],self.level)
                    self.board.removeStone(movesList[i][1][0],movesList[i][1][1])
                    valuator[i] = valuator[i] + output
            
            ind = valuator.index(max(valuator))
            move = movesList[ind][1]
        
            self.board.addStone(move[0],move[1],self.color)
            self.board.placeStone(move[0],move[1],self.color)
            return 0
    
    '''
    This function looks at every empty vertex on the board and generates a "value" for that vertex. This value is simply the 
    sum of all of a stone's priority values to the sixth power. Thus, when a stone has higher priorities values, these values
    disproportionately contribute to a high value. Once our for loops have run we sort the list of moves by their values, and
    put the three highest moves into movesList. We then return this list of three moves (and their associated values.
    '''
                
    def calculateValues(self):
        tempMovesList = []
        
        for i in range(0,15):
            for j in range(1,15):
                if self.board.stones[i][j].team == 0:
                    value = self.board.stones[i][j].wxP[0]**6 + self.board.stones[i][j].wxM[0]**6 + self.board.stones[i][j].wyP[0]**6 + \
                    self.board.stones[i][j].wyM[0]**6 + self.board.stones[i][j].wxPyP[0]**6 + self.board.stones[i][j].wxPyM[0]**6 + \
                    self.board.stones[i][j].wxMyP[0]**6 + self.board.stones[i][j].wxMyM[0]**6 + self.board.stones[i][j].bxP[0]**6 + \
                    self.board.stones[i][j].bxM[0]**6 + self.board.stones[i][j].byP[0]**6 + self.board.stones[i][j].byM[0]**6 + \
                    self.board.stones[i][j].bxPyP[0]**6 + self.board.stones[i][j].bxPyM[0]**6 + self.board.stones[i][j].bxMyP[0]**6 + \
                    self.board.stones[i][j].bxMyM[0]**6
                    
                    tempMovesList.append([value,[i,j]])

        tempMovesList.sort()
        length = len(tempMovesList)
        movesList = tempMovesList[length - 3:length]
        return movesList


'''
This is the Pseudo Computer class. It mostly functions as a way for us to logically seperate the actual move step of the 
computer with the calculations for its moves. Having this class is actually less efficient and takes up more space in our code,
but we find it valuable because it easily allows us to modify "how" the computer looks at future moves, i.e. what specifically
does it choose to value in future moves.
'''


class PseudoComputer:
    
    def __init__(self, teamColor, opColor, board):
        
        #Instance variables for PseudoComputer. It's team is the opposite of the computer's.
        
        self.color = teamColor
        self.opColor = opColor
        self.board = board
        self.tempMoveList = []
        self.movelist = []
    
    '''
    The calculating method of the class. It first assesses the level value. Level = 1 is the base case, and in that case
    it simply returns the value of the move that was in its input. Otherwise, the function continues on. If the level is odd,
    we say we are moving for the computer, and when the level is even we are moving for the human player. For this reason
    the inital value of level must always be even; we are always first calculating what we think an opponent will do in 
    reaction to the computer's moves. We then continue on, and, using the same calculations as we did in calculatevalues,
    we calculate the best three moves for the given player. Then we branch into three new recursive loops, each representing
    one of the three new moves. This continues until we reach the base case. The output of ever recrusive loop is the sum of the
    negation of the beginning move's value plus the average of the branches' values, i.e. a tree with three branches and one
    starting point would have a value of -starting point value + (branch1 value + branche2 value + branch3 value)/3 = Total.
    This summation process occurs for every loop, including the beginning loops. The value at the end of the first function
    is the average of the three values generated by the begining loops. This value is returned as the "future" move valuation.
    
    The above is actually slightly incorrect. The "signage" of a value depends on its color, or the player who would be
    playing the move associated with the value. So it would only be true that the first recursive move is negative
    and the branches are positive if the first recursive move was a move that the human would play.
    
    We negate the opponent's moves like this because, from the computer's perspective, it is usually bad for them to be able
    to play moves with higher valuation.
    '''
    
    def virtualCalculations(self,move,level):
        
        if level == 1:
            value = move[0]
            return value
        
        if level % 2 == 0:
            color = self.color
            sign = -1
        else:
            color = self.opColor
            sign = 1
        
        tempList = []
        moveList = []
        
        for i in range(0,15):
            for j in range(0,15):
                if self.board.stones[i][j].team == 0:
                    
                    value = self.board.stones[i][j].wxP[0]**6 + self.board.stones[i][j].wxM[0]**6 + self.board.stones[i][j].wyP[0]**6 + \
                    self.board.stones[i][j].wyM[0]**6 + self.board.stones[i][j].wxPyP[0]**6 + self.board.stones[i][j].wxPyM[0]**6 + \
                    self.board.stones[i][j].wxMyP[0]**6 + self.board.stones[i][j].wxMyM[0]**6 + self.board.stones[i][j].bxP[0]**6 + \
                    self.board.stones[i][j].bxM[0]**6 + self.board.stones[i][j].byP[0]**6 + self.board.stones[i][j].byM[0]**6 + \
                    self.board.stones[i][j].bxPyP[0]**6 + self.board.stones[i][j].bxPyM[0]**6 + self.board.stones[i][j].bxMyP[0]**6 + \
                    self.board.stones[i][j].bxMyM[0]**6
                    tempList.append([value,[i,j]])

        tempList.sort()
        length = len(tempList)
        moveList = tempList[length - 3:length]
        
        self.board.addStone(moveList[0][1][0],moveList[0][1][1],color)
        moveA = sign*level*moveList[0][0] + self.virtualCalculations(moveList[0][1][:],level-1)
        self.board.removeStone(moveList[0][1][0],moveList[0][1][1])
        self.board.addStone(moveList[1][1][0],moveList[1][1][1],color)
        moveB = sign*level*moveList[1][0] + self.virtualCalculations(moveList[1][1][:],level-1)
        self.board.removeStone(moveList[1][1][0],moveList[1][1][1])
        self.board.addStone(moveList[2][1][0],moveList[2][1][1],color)
        moveC = sign*level*moveList[2][0] + self.virtualCalculations(moveList[2][1][:],level-1)
        self.board.removeStone(moveList[2][1][0],moveList[2][1][1])
        
        return moveA


'''
The GoMoku class. This class serves as the overarching class of the game. It allows the two players to alternate
taking turns, checking for a winner inbetween the turns. When a winner is found, it prints a message and then
runs the main function of the program again. 
'''


class GoMoku:
    
    #Initializer. We set the player instance variables according to which player is which color.
    
    def __init__(self,player1,player2,board):
        
        if player1.color == "Black":
            self.player1 = player1
            self.player2 = player2
        else:
            self.player2 = player1
            self.player1 = player2
        
        self.p1Color = "Black"
        self.p2Color = "White"
        self.board = board
    
    #This method checks for a winning position after every turn. It looks at every stone that has a team (so is actualized)
    #on the board. It calls the list of priorities for this stone and assesses whether any of them is over 9 (since 10+ is
    #a winning priority). If so it returns the string "win"; if not "no winner".
    
    def checkWinning(self):
        for item in self.board.stones:
            for stone in item:
                if stone.team != 0:
                    stone.priorityList()
                    for i in range(8):
                        if stone.priority[i][0] > 9:
                            win = "Win"
                            return win
                                
        return "no winner"
        
    '''
    This is the runGame function. Using a while loop, it infinitely runs, letting players alternate their turns and 
    checking for a winning board after every turn. When someone has won, it prints winning text on the board, waits for 
    a click, and then runs the game again.
    '''
    
    def runGame(self):
        
        win = "no winner"
        
        while win == "no winner":
            
            #The player turns return a value depending on what they did during their turn. If during their turn they
            #chose to end the game or start a new one, "done" is returned and the program ends. Thus, the variable "a"
            #acts as a dummy variable.
            
            a = self.player1.turn()
            if a == "done":
                return
            
            win = self.checkWinning()
            if win == "Win":
                winText = graphics.Text(graphics.Point(230,-20), self.p1Color + " Wins!" )
                winText.setSize(36)
                winText.setTextColor(self.p1Color)
                winText.setFace("helvetica")
                winText.draw(self.board.win)
                self.board.win.getMouse()
                self.board.win.close()
                main()
                return
            
            a = self.player2.turn()
            if a == "done":
                return
            
            win = self.checkWinning()
            if win == "Win":
                winText = graphics.Text(graphics.Point(230,-20), self.p2Color + " Wins!" )
                winText.setSize(36)
                winText.setTextColor(self.p2Color)
                winText.setFace("helvetica")
                winText.draw(self.board.win)
                self.board.win.getMouse()
                self.board.win.close()
                main()
                return

#_______________________________________________________________________

'''
Method that runs GoMoku game. First we determine the colors of the players depending on the color parameter.
A board class is generated (with the number of squares being fifteen). Then a human player (P1) class and an
opponent class (either a human or computer, depending on user choice in chooseOpponent) is generated. We also generate
a pseudo computer class (in the case that a computer is chosen as the opponent) for AI capabilities. Finally, a game class
is generated and the runGame method is run.
'''


def play(opponent, difficulty, color):
        
        if color == "White":
            opColor = "Black"
        elif color == "Black":
            opColor ="White"
        theBoard = Board(15)
        P1 = HumanPlayer(color,theBoard)
        
        if opponent == "Computer":
            P2 = PseudoComputer(color,opColor,theBoard)
            #Level must be set to an even number; see Pseudo Computer for reasoning.
            P3 = Computer(opColor, difficulty, 6, P2,theBoard)
        else:
            P3 = HumanPlayer(opColor,theBoard)
        game = GoMoku(P1,P3,theBoard)
        game.runGame()
        

'''
The main function of the program. First we run the intro screen to introduce the game and determine what type of game
the player would like to play. This class returns the parameters of the game. The intro screen is then closed and 
the play function is run with the chosen parameters.
'''


def main():
    intro = IntroScreen()
    parameters = intro.intro()
    intro.win.close()
    play(parameters[0], parameters[1], parameters[2])
    
if __name__ == '__main__':
    main()