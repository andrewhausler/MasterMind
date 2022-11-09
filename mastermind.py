import pygame
import random
pygame.init()

def masterMind():

    class Colors:
        def __init__(self, width, height, x, y, color):
            shape = pygame.draw.rect(gameDisplay, color, pygame.Rect(x, y, width, height))
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.display = shape
    
    wait = 0
    activateCPU = False

    # Colors
    red = (255, 0, 0)
    darkRed = (210, 20, 20)
    orange = (255, 140, 0)
    darkOrange = (255, 100, 0)
    yellow = (255, 255, 0)
    darkYellow = (204, 204, 0)
    green = (0, 255, 0)
    darkGreen = (0, 204, 0)

    # Fonts/Text
    titleFont = pygame.font.Font("airmill_o.ttf", 60)
    title = titleFont.render("MasterMind", True, False)
    textFont = pygame.font.Font("airmill_o.ttf", 30)
    correct = textFont.render("Total Correct", True, False)
    incorrect = textFont.render("Total Incorrect", True, False)
    colorButtons = textFont.render("Color Buttons", True, False)
    colorPick = textFont.render("Create A Sequence Out Of These Colors", True, False)
    guessOrder = textFont.render("Guess The Sequence", True, False)
    playAgain = textFont.render("Play Again?", True, red)
    playAgainDark = textFont.render("Play Again?", True, green)
    yourGuess = textFont.render("Your Guess is", True, False)
    youWon = textFont.render("Congrats! You Guessed Correctly", True, False)
    playCPU = textFont.render("CPU", True, False)
    playCPUDark = textFont.render("CPU", True, darkGreen)
    playCPU2 = textFont.render("Or", True, False)

    # Mouse Pressing
    pressed = False
    press_count = 0
    allowPressCount = False
    notUsedRed = True
    notUsedOrange = True
    notUsedYellow = True
    notUsedGreen = True

    gameDisplay = pygame.display.set_mode((600, 600))
    gameCaption = pygame.display.set_caption("")
    startPosition = 200

    # Set Player Color Order List
    colorOrder = []
    colorGuess = []
    totalCorrect = 0
    totalIncorrect = 0
    finalScore = False
    myGuessPosition = 50

    colors = []
    colors.append(red)
    colors.append(orange)
    colors.append(yellow)
    colors.append(green)
    colorOrderCPU = []
    for i in range(4):    
        randomNums = random.randrange(len(colors))
        colorOrderCPU.append(colors[randomNums])
        colors.pop(randomNums)

    remove = False

    while True:
        if finalScore == True:
            notUsedRed = True
            notUsedOrange = True
            notUsedYellow = True
            notUsedGreen = True
        
        mouse = pygame.mouse.get_pos()
        gameDisplay.fill((255, 255, 255))
        gameDisplay.blit(title, (120, 20))
        gameDisplay.blit(correct, (400, 100))
        gameDisplay.blit(incorrect, (400, 200))
        if remove == False:    
            gameDisplay.blit(colorButtons, (220, 460))
        if notUsedRed == True and remove == False:   
            square1 = Colors(50, 50, 200, 500, red)
        if notUsedOrange == True and remove == False:   
            square2 = Colors(50, 50, 255, 500, orange)   
        if notUsedYellow == True and remove == False:    
            square3 = Colors(50, 50, 310, 500, yellow)
        if notUsedGreen == True and remove == False:    
            square4 = Colors(50, 50, 365, 500, green)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
                    allowPressCount = True
            if event.type == pygame.MOUSEBUTTONUP:
                    pressed = False
                    press_count = 0
                    allowPressCount = False

        if allowPressCount == True:
            press_count += 1

        if len(colorOrder) < 4:
            gameDisplay.blit(colorPick, (50, 300))
            gameDisplay.blit(playCPU2, (285, 340))
            if mouse[0] >= 265 and mouse[0] <= 265 + 80 and mouse[1] <= 380 + 30 and mouse[1] >= 380:
                gameDisplay.blit(playCPUDark, (265, 380))
                if pressed == True and press_count == 1:
                    activateCPU = True
            else:
                gameDisplay.blit(playCPU, (265, 380))

        if activateCPU == True:
            colorOrder = colorOrderCPU
        
        if len(colorOrder) == 4 and len(colorGuess) == 0:
            notUsedRed = True
            notUsedOrange = True
            notUsedYellow = True
            notUsedGreen = True
            
        if len(colorGuess) < 4 and len(colorOrder) == 4:
            gameDisplay.blit(guessOrder, (190, 300))

        if notUsedRed == True and remove == False:    
            if mouse[0] >= square1.x and mouse[0] <= square1.x + square1.width and mouse[1] <= square1.y + square1.height and mouse[1] >= square1.y:
                if notUsedRed == True:   
                    square1Dark = Colors(50, 50, 200, 500, darkRed) 
                if pressed == True and press_count == 1:
                    if len(colorOrder) < 4:   
                        colorOrder.append(red)
                        notUsedRed = False
                    elif len(colorGuess) < 4:
                        colorGuess.append(red)
                        notUsedRed = False
                    
        if notUsedOrange == True and remove == False:    
            if mouse[0] >= square2.x and mouse[0] <= square2.x + square2.width and mouse[1] <= square2.y + square2.height and mouse[1] >= square2.y:
                if notUsedOrange == True:    
                    square2Dark = Colors(50, 50, 255, 500, darkOrange)
                if pressed == True and press_count == 1:
                    if len(colorOrder) < 4:
                        colorOrder.append(orange)
                        notUsedOrange = False
                    elif len(colorGuess) < 4:
                        colorGuess.append(orange)
                        notUsedOrange = False
                    
        if notUsedYellow == True and remove == False:   
            if mouse[0] >= square3.x and mouse[0] <= square3.x + square3.width and mouse[1] <= square3.y + square3.height and mouse[1] >= square3.y:
                if notUsedYellow == True:    
                    square3Dark = Colors(50, 50, 310, 500, darkYellow)
                if pressed == True and press_count == 1:
                    if len(colorOrder) < 4:   
                        colorOrder.append(yellow)
                        notUsedYellow = False
                    elif len(colorGuess) < 4:
                        colorGuess.append(yellow)
                        notUsedYellow = False
                    
        if notUsedGreen == True and remove == False:   
            if mouse[0] >= square4.x and mouse[0] <= square4.x + square4.width and mouse[1] <= square4.y + square4.height and mouse[1] >= square4.y:
                if notUsedGreen == True:    
                    square4Dark = Colors(50, 50, 365, 500, darkGreen)
                if pressed == True and press_count == 1:
                    if len(colorOrder) < 4:   
                        colorOrder.append(green)
                        notUsedGreen = False
                    elif len(colorGuess) < 4:
                        colorGuess.append(green)
                        notUsedGreen = False

        if pressed == True and press_count == 1 and remove == False:
            if finalScore == True:
                colorGuess = []
                finalScore = False
        
        if len(colorGuess) == 4 and finalScore != True and finalScore != True:
            totalCorrect = 0
            totalIncorrect = 0
            for i in range(len(colorGuess)):
                if colorGuess[i] == colorOrder[i]:
                    totalCorrect += 1
                else:
                    totalIncorrect += 1
                finalScore = True      
            
        gameDisplay.blit(textFont.render(f"{totalCorrect}", True, False), (500, 150))
        gameDisplay.blit(textFont.render(f"{totalIncorrect}", True, False), (500, 250))

        if totalCorrect == 4:
            remove = True
            gameDisplay.blit(youWon, (100, 300))
            if mouse[0] >= 220 and mouse[0] <= 220 + 160 and mouse[1] <= 350 + 30 and mouse[1] >= 350:   
                gameDisplay.blit(playAgainDark, (220, 350))
                if pressed == True and press_count == 1:
                    masterMind()
            else:    
                gameDisplay.blit(playAgain, (220, 350))

        if finalScore == True:
            myGuessPosition = 120
            gameDisplay.blit(yourGuess, (100, 200))
            for i in colorGuess:
                Colors(30, 30, myGuessPosition, 240, i)
                myGuessPosition += 35
   
        pygame.display.update()

masterMind()
