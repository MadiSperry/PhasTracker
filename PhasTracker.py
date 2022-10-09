'''
This code is to allow people who are watching people play Phasmophobia and want to keep track of what ghosts are possible and follow along.
Input: Pressing Buttons For Evidence Or Selecting Ghosts
Output: A GUI That Shows Possible Ghosts Based On Evidence And If User Stated It Is Not Possible
Author: MadiSperry
'''

# Import Necessary Libraries
import os
from tkinter import *
import tkinter
from tkinter.ttk import *
import tkinter.font as tkFont
from PIL import Image, ImageTk

# Config Variables for PNGs
evidencePNG = ["EMF", "SpiritBox", "Fingerprints", "GhostOrb", "WritingBook", "Thermo", "DOTS"]
thumbnailWidth, thumbnailHeight = 154, 101

# Non-Config Variables
evidenceTypes = ["EMF 5", "Spirit Box", "Fingerprints", "Ghost Orbs", "Ghost Writing", "Freezing Temps", "D.O.T.S."]
ghosts = ["Spirit", "Wraith", "Phantom", "Poltergeist", "Banshee", "Jinn", "Mare", "Revenant", "Shade", "Demon", "Yurei", 
          "Oni", "Yokai", "Hantu", "Goryo", "Myling", "Onryo", "Twins", "Raiju", "Obake", "Mimic", "Moroi", "Deogen", "Thaye"]

# 3 States (0,1,2) for (Not Selected, Confirmed, Confirmed Impossible) Respectively
evidenceStates = [0,0,0,0,0,0,0]
ghostsStates = [0 for i in range(len(ghosts))]

# Each Type Of Ghost Possible With Each Evidence Type
EMFGhosts = ["Spirit", "Wraith", "Jinn", "Shade", "Oni", "Goryo", "Myling", "Twins", "Raiju", "Obake"]
SBGhosts = ["Spirit", "Wraith", "Phantom", "Poltergeist", "Mare", "Yokai", "Onryo", "Twins", "Mimic", "Moroi", "Deogen"]
FingersGhosts = ["Phantom", "Poltergeist", "Banshee", "Jinn", "Demon", "Hantu", "Goryo", "Myling", "Obake", "Mimic"]
OrbsGhosts = ["Banshee", "Mare", "Revenant", "Yurei", "Yokai", "Hantu", "Onryo", "Raiju", "Obake", "Mimic", "Thaye"]
WritingGhosts = ["Spirit", "Poltergeist", "Mare", "Revenant", "Shade", "Demon", "Myling", "Moroi", "Deogen", "Thaye"]
FreezingGhosts = ["Jinn", "Revenant", "Shade", "Demon", "Yurei", "Oni", "Hantu", "Onryo", "Twins", "Mimic", "Moroi"]
DOTSGhosts = ["Wraith", "Phantom", "Banshee", "Yurei", "Oni", "Yokai", "Goryo", "Raiju", "Deogen", "Thaye"]

evidenceCollected = []
possibleGhosts = ghosts
userDeniedGhosts = []

##########################################################################################################################################################################

# Function To Create The Thumbnails To Go On Each Evidence Button
def createEvidenceThumbnails():
    i = 0
    for name in evidencePNG:
        evidence = Image.open(os.getcwd() + "\\resources\\evidencePNG\\" + name + ".png").resize((thumbnailWidth, thumbnailHeight), Image.ANTIALIAS)
        evidence = ImageTk.PhotoImage(evidence)
        evidencePNG[i] = evidence
        i += 1

##########################################################################################################################################################################

# Function For Every Time An Evidence Button is hit.
def pressButton(evidence):
    index = evidenceTypes.index(evidence)

    # If Not Selected, Set as Confirmed Evidence
    if evidenceStates[index] == 0:
        evidenceStates[index] = 1
        evidenceCollected.append(evidenceTypes[index])
    # If Confirmed, Set as Confirmed Impossible Evidence
    elif evidenceStates[index] == 1:
        evidenceStates[index] = 2
        evidenceCollected.remove(evidenceTypes[index])
    # If not Not Selected and not Confirmed, Set as Not Selected
    else:
        evidenceStates[index] = 0

    main_menu()
    
# Function Called Every Time A Change Is Made To main_menu() And Is Called.
def compilePossibleGhosts(evidences):
    global possibleGhosts, ghosts
    evidenceGhosts = [EMFGhosts, SBGhosts, FingersGhosts, OrbsGhosts, WritingGhosts, FreezingGhosts, DOTSGhosts]
    evidenceSet = []
    possibleGhosts = []

    # If No Evidence, All Ghosts Are Possible
    if len(evidences) == 0:
        possibleGhosts = ghosts
    else:
        # For Each Evidence Selected, Create A List For All Ghosts For Each Evidence
        for evidence in evidences:
            index = evidenceTypes.index(evidence)
            evidenceSet += [evidenceGhosts[index]]

    # If No Evidence, Return To main_menu(), Else If Each Ghost Is In Each List, Add It To possibleGhosts
    if len(evidences) == 0:
        return
    elif len(evidences) == 1:
        possibleGhosts = evidenceSet[0]
    elif len(evidences) == 2:
        for ghost in evidenceSet[0]:
            if ghost in evidenceSet[1]:
                possibleGhosts.append(ghost)    
    elif len(evidences) == 3:
        for ghost in evidenceSet[0]:
            if ghost in evidenceSet[1] and ghost in evidenceSet[2]:
                possibleGhosts.append(ghost)
    elif len(evidences) == 4:
        for ghost in evidenceSet[0]:
            if ghost in evidenceSet[1] and ghost in evidenceSet[2] and ghost in evidenceSet[3]:
                possibleGhosts.append(ghost)
    return

# If User Clicks A Ghost Name, That Ghost Name Is Added Or Removed From userDeniedGhosts
def createUserDeclinedGhosts(ghost):
    global userDeniedGhosts
    
    if ghostsStates[ghost] == 0:
        ghostsStates[ghost] = 1
    elif ghostsStates[ghost] == 1:
        ghostsStates[ghost] = 2
        userDeniedGhosts += [ghosts[ghost]]
    elif ghostsStates[ghost] == 2:
        ghostsStates[ghost] = 0
        userDeniedGhosts.remove(ghosts[ghost])

    for i in range(len(ghostsStates)):
        if i == ghost:
            pass
        elif ghostsStates[i] == 1:
            ghostsStates[i] = 0
    main_menu()

# Decides The Color Of The Button If Evidence Is Not Selected, Confirmed, or Confirmed Impossible
def decideColor(evidence):
    index = evidenceTypes.index(evidence)

    if evidenceStates[index] == 0:
        return "#f0f0f0"
    elif evidenceStates[index] == 1:
        return "#c9ffad"
    elif evidenceStates[index] == 2:
        return "#ffadad"

##########################################################################################################################################################################

# Function To Reset All Variables To Defaults
def reset():
    global evidenceStates, evidenceCollected, userDeniedGhosts, ghostsStates
    ghostsStates = [0 for i in range(len(ghosts))]
    evidenceStates = [0 for i in range(len(evidenceTypes))]
    evidenceCollected = []
    userDeniedGhosts = []
    main_menu()

# Function To Clear The Window
def clear_root():
    for child in root.winfo_children():
        child.destroy()

# Function To Create Frames To Be Used In The Window
def createFrame(magnetizedSide):
    f = Frame(root)
    f.pack(side = magnetizedSide)
    return f

##########################################################################################################################################################################

def main_menu():
    global ghostsStates
    clear_root()
    compilePossibleGhosts(evidenceCollected)

    # Create frames for the main_menu
    frame1, frame2, frame3, frame4 = createFrame(TOP), createFrame(TOP), createFrame(TOP), createFrame(TOP)
       
    # Add title label to root
    Label(frame1, text = 'MadiSperry\'s Phasmophobia Tracker', font ='papyrus 30 bold').grid(row = 0, column = 0, padx = 10, pady = 25)
    
    # Create buttons for each evidence
    i,y = 0,0
    for y in range(0, 7):
        tkinter.Button(frame2, text = evidenceTypes[y], bg = decideColor(evidenceTypes[y]), image = evidencePNG[y], compound = BOTTOM, font = ("papyrus", 15), command = lambda i=i: pressButton(evidenceTypes[i])).grid(column = y, row = 1, pady=10, padx=10)        
        i += 1

    # Create buttons with each ghosts name with the respective colors and strikethroughs based on possibleGhosts and userDeniedGhosts
    i,x,y = 0,0,0
    for y in range(0, 8):
        for x in range(0, 3):
            if ghosts[i] in possibleGhosts and ghosts[i] not in userDeniedGhosts and ghostsStates[i] == 1:
                tkinter.Button(frame3, text = ghosts[i], image = circleImage, command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = normal_Font, fg = "#000000", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] in possibleGhosts and ghosts[i] not in userDeniedGhosts:
                tkinter.Button(frame3, text = ghosts[i], command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = normal_Font, fg = "#000000", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] not in possibleGhosts and ghosts[i] not in userDeniedGhosts and ghostsStates[i] == 1:
                tkinter.Button(frame3, text = ghosts[i], image = grayCircleImage, command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = normal_Font, fg = "#d1d1d1", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] not in possibleGhosts and ghosts[i] not in userDeniedGhosts:
                tkinter.Button(frame3, text = ghosts[i], command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = normal_Font, fg = "#d1d1d1", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] in possibleGhosts and ghosts[i] in userDeniedGhosts and ghostsStates[i] == 1:
                tkinter.Button(frame3, text = ghosts[i], image = circleImage, command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = strike_Font, fg = "#000000", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] in possibleGhosts and ghosts[i] in userDeniedGhosts:
                tkinter.Button(frame3, text = ghosts[i], command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = strike_Font, fg = "#000000", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] not in possibleGhosts and ghosts[i] in userDeniedGhosts and ghostsStates[i] == 1:
                tkinter.Button(frame3, text = ghosts[i], image = grayCircleImage, command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = strike_Font, fg = "#d1d1d1", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] not in possibleGhosts and ghosts[i] in userDeniedGhosts:
                tkinter.Button(frame3, text = ghosts[i], command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = strike_Font, fg = "#d1d1d1", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            i += 1

    # Create reset button to set everything back to defaults
    tkinter.Button(frame4, text = "Reset", compound = CENTER, font = ("papyrus", 15), command = reset).grid(column = 1, row = 1, pady=20, padx=25) 

##########################################################################################################################################################################

# Create root GUI, give it a name, make it full screened
root = Tk()
root.geometry('1000x300')
root.title("MadiSperry's Phasmophobia Tracker")
root.state('zoomed')

circleImage = Image.open(os.getcwd() + "\\resources\\" + "circle" + ".png").resize((thumbnailWidth, int(thumbnailHeight/2)), Image.ANTIALIAS)
grayCircleImage = Image.open(os.getcwd() + "\\resources\\" + "circle1" + ".png").resize((thumbnailWidth, int(thumbnailHeight/2)), Image.ANTIALIAS)
circleImage = ImageTk.PhotoImage(circleImage)
grayCircleImage = ImageTk.PhotoImage(grayCircleImage)
#lightCircleImage = circleImage.color(fg = "#d1d1d1")

# Set Normal Font And A Font With A Strikethrough
normal_Font = tkFont.Font(family="Papyrus", size=20, overstrike = 0)
strike_Font = tkFont.Font(family="Papyrus", size=20, overstrike = 1)

# Run function to create The Evidence Thumbnails
createEvidenceThumbnails()

# Run the main_menu function to start out with the main scene of the GUI
main_menu()
root.mainloop()
