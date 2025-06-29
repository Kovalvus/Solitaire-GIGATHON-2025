# I.K. Pasjans (Solitaire) Gigathon II etap

import random


class Card:     # Class for creating colored Cards
    RED = '\033[91m'
    BLACK = '\033[30m'
    RESET = '\033[0m'

    def __init__(self, suit, value, hidden=False):
        self.suit = suit
        self.value = value
        self.hidden = hidden

    def is_red(self):
        return self.suit in ['♥', '♦']    # If one of the given symbols is detected inside Card() the card is going to get printed in red

    def __str__(self):
        if self.hidden:     # If a card has its attribute "hidden" set to True, the card will be hidden
            return "███"
        color = self.RED if self.is_red() else self.BLACK
        return f"{color}{self.suit}{self.value}{self.RESET}"


# Assingning variables

Suits = ['♥', '♦', '♠', '♣']
Values = ['A ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', 'J ', 'Q ', 'K ']
Deck = []   # The deck at first used to create and distribute all cards, later used for drawing cards (not implemented)
Counter = 0

while (Counter < 4):    # Creating the deck
    for ValueId in range(len(Values)):
        Deck.append(Card(Suits[Counter], Values[ValueId]))
        ValueId += 1
    Counter += 1

random.shuffle(Deck)
Col1 = []   # First in-game column etc..
Col2 = []
Col3 = []
Col4 = []
Col5 = []
Col6 = []
Col7 = []

Columns = [Col1, Col2, Col3, Col4, Col5, Col6, Col7]

# Finishing stacks:
HeartsStack = []  # ♥ 
DiamondsStack = []  # ♦
SpadesStack = []  # ♠
ClubsStack = []  # ♣

# Creating 7 starting columns
Col1.append(Deck.pop(0))    

Col2.extend(Card(card.suit, card.value, hidden=True) for card in Deck[:2])  # A column is created with all its cards hidden at first
Col2[-1].hidden = False # Displaying the last card
del Deck[:2]    # Deleting the cards moved into Column 2 from the main deck
# Repeat for all columns

Col3.extend(Card(card.suit, card.value, hidden=True) for card in Deck[:3])
Col3[-1].hidden = False
del Deck[:3]

Col4.extend(Card(card.suit, card.value, hidden=True) for card in Deck[:4])
Col4[-1].hidden = False
del Deck[:4]

Col5.extend(Card(card.suit, card.value, hidden=True) for card in Deck[:5])
Col5[-1].hidden = False
del Deck[:5]

Col6.extend(Card(card.suit, card.value, hidden=True) for card in Deck[:6])
Col6[-1].hidden = False
del Deck[:6]

Col7.extend(Card(card.suit, card.value, hidden=True) for card in Deck[:7])
Col7[-1].hidden = False
del Deck[:7]


# Functions

def PrintColumns(): # Print the game visual

    print("\n=== STOSY KOŃCOWE ===")
    for card in HeartsStack:
        print(card)
    for card in DiamondsStack:
        print(card)
    for card in SpadesStack:
        print(card)
    for card in ClubsStack:
        print(card)

    print("\n=== PLANSZA ===")
    for row in range(max(len(col) for col in Columns)):
        for col in Columns:
            if row < len(col):
                print(col[row], end="  ")  # print a card
            else:
                print("     ", end="")     # if column doesn't have anymore cards print a blank space
        print() 

random.shuffle(Deck)    # Shuffling the deck once again


def MoveCards(ChosenCol, CardAmount):   # Function responsible for all things related to moving cards between stacks (not final stacks)
    if(len(Columns[ChosenCol-1]) >= CardAmount and (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount].hidden == False):   # Checking if: the chosen column has the same amount OR more cards than you want to move and if the last (towards the top) card is hidden or not(if it's hidden it's still not discovered = can't move all cards)
                        
        try:
                            
            ToCol = int(input("Na którą kolumnę chcesz je przenieść?: "))
                            
            if(ToCol in range(1,8)):
                CardToMoveValue = (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount].value    # Getting the values of cards, CardToMoveValue = the one you're moving (or the one's that's on the top of the stack you're moving), CardToMoveToValue = the one you're moving TO
                CardToMoveToValue = (Columns[ToCol-1])[len(Columns[ToCol-1])-1].value 
                            
                CardToMoveSuit = (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount].suit  # Getting the suits of cards
                CardToMoveToSuit = (Columns[ToCol-1])[len(Columns[ToCol-1])-1].suit 


            if(Values.index(CardToMoveValue) == Values.index(CardToMoveToValue)-1): # Checking if value of the card you want to move is 1 lower than the value of the card you want to move to (for example: if CardToMoveValue is a Q then CardToMoveToValue would have to be K to be able to move)
                if( ((CardToMoveSuit == "♥" or CardToMoveSuit == "♦") and (CardToMoveToSuit == "♠" or CardToMoveToSuit == "♣")) or ((CardToMoveSuit == "♠" or CardToMoveSuit == "♣") and (CardToMoveToSuit == "♥" or CardToMoveToSuit == "♦")) ):   # Checking if cards are Red/Black or Black/Red
                                        
                    (Columns[ToCol-1]).extend((Columns[ChosenCol-1])[-CardAmount:])    # Adding chosen cards to the chosen column
                    del (Columns[ChosenCol-1])[-CardAmount:]    # Deleting moved cards from their original place
                    
                    if((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1] != []):
                        (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                    PrintColumns()

                                            
                else:
                                
                    print("Liczba nie znajduje się w przedziale 1-7!")
        except:
                            
                print("Wybierz liczbę!")
    else:
                    
            print("Nie można przenieść tylu kart!")


# One time use difficulty choice

DifficultyChosen = 0
while(DifficultyChosen == 0):
    print("Witaj, na jakim poziomie trudności chcesz zagrać?")
    print("Łatwy / Trudny")
    Difficulty = str(input("Wpisz L lub T: ")).lower()

    if(Difficulty == "l"):
        print("\nWybrano poziom łatwy!\n")
        DifficultyChosen = 1
        PrintColumns()

    elif(Difficulty == "t"):
        print("\nWybrano poziom trudny!\n")
        DifficultyChosen = 1
        PrintColumns()

    else:
        print("\nNieodpowiednia odpowiedź!\n")


running = 1 # Variable which allows for the program to be turned off at anytime by simply changing its value
while (running == 1):   # The main game

    print("Wpisz W, żeby zakończyć grę lub R, żeby ponownie wyświetlić planszę gry")
    print("Wybierz, z której kolumny chcesz zabrać kartę")
    try:

        ChosenCol = str(input("1-7: ")).lower() # Choosing from which column you want to take the card or if you want to leave/redraw the game
        
        if(ChosenCol == "w"):
            running = 0
                
        elif(ChosenCol == "r"):
             PrintColumns()

        else:
            ChosenCol = int(ChosenCol)

        if(ChosenCol in range(1,8)):
            
            try:

                CardAmount = int(input("Ile kart chcesz przenieść?: "))

                if(CardAmount == 1):    # If the player picked up 1 card, they get a choice between moving it and placing it on a final stack
                    print("Chcesz przenieść kartę, czy odłożyć ją na stos? (P - przenieść, S - stos)")
                    MoveChoice = str(input("P/S: ")).lower()
                    
                    if(MoveChoice == "s"):  # Placing the card onto a final stack
                        
                        CardToPutAwaySuit = (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount].suit   # The suit of the chosen card as a variable
                        CardToPutAwayValue = (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount].value     # The value of the chosen card as a variable

                        if(CardToPutAwaySuit == "♥"):
                            print(len(HeartsStack))

                            if(HeartsStack[-1:] == Values.index(CardToPutAwayValue)-1):     # If there's already cards on the stack (picked up card isn't an Ace) || doesn't work -> the value of HeartStack[-1] card should be used inside Values.index, but no matter what I do it only broke the rest of the program
                                HeartsStack.append((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount])
                                del (Columns[ChosenCol-1])[-1:]
                                (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                                PrintColumns()

                            elif(HeartsStack[-1:] == []):   # If there aren't any cards on the stack, picked up card has to be an Ace to be able to be placed on it
                                if(CardToPutAwayValue == "A "):
                                    HeartsStack.append((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount])
                                    del (Columns[ChosenCol-1])[-1:]
                                    (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                                    PrintColumns()
                            
                            else:
                                print("Nie możesz odłożyć tej karty na stos!")
                        
                        # The same loops but for the rest of the suits:
                         
                        elif(CardToPutAwaySuit == "♦"):    

                            if(DiamondsStack[-1:] == Values.index(CardToPutAwayValue)-1):
                                DiamondsStack.append((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount])
                                del (Columns[ChosenCol-1])[-1:]
                                (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                                PrintColumns()
                            
                            elif(DiamondsStack[-1:] == []):
                                if(CardToPutAwayValue == "A "):
                                    DiamondsStack.append((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount])
                                    del (Columns[ChosenCol-1])[-1:]
                                    (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                                    PrintColumns()
                           
                            else:
                                print("Nie możesz odłożyć tej karty na stos!")

                        elif(CardToPutAwaySuit == "♠"):

                            if(SpadesStack[-1:] == Values.index(CardToPutAwayValue)-1):
                                SpadesStack.append((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount])
                                del (Columns[ChosenCol-1])[-1:]
                                (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                                PrintColumns()

                            elif(SpadesStack[-1:] == []):
                                if(CardToPutAwayValue == "A "):
                                    SpadesStack.append((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount])
                                    del (Columns[ChosenCol-1])[-1:]
                                    (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                                    PrintColumns()
                            
                            else:
                                print("Nie możesz odłożyć tej karty na stos!")

                        elif(CardToPutAwaySuit == "♣"):

                            if(ClubsStack[-1:] == Values.index(CardToPutAwayValue)-1):
                                ClubsStack.append((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount])
                                del (Columns[ChosenCol-1])[-1:]
                                (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                                PrintColumns()

                            elif(ClubsStack[-1:] == []):
                                if(CardToPutAwayValue == "A "):
                                    ClubsStack.append((Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-CardAmount])
                                    del (Columns[ChosenCol-1])[-1:]
                                    (Columns[ChosenCol-1])[len(Columns[ChosenCol-1])-1].hidden = False
                                    PrintColumns()
                            
                            else:
                                print("Nie możesz odłożyć tej karty na stos!")

                    elif(MoveChoice == "P" or MoveChoice == "p"):   # If the player chose to move the card, MoveCards function is called
                        MoveCards(ChosenCol, CardAmount)

                    else:
                        print("Wybierz P lub S!")
                        
                else:
                    MoveCards(ChosenCol, CardAmount)    # If the player picked up more than 1 card, MoveCards function is called

            except:
                
                print("Wybierz liczbę!")

        else:
            
            print("Liczba nie znajduje się w przedziale 1-7!")
    except:
        
        print("Wybierz liczbę!")

    
    
    
