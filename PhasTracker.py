'''
This code is to allow people who are watching people play Phasmophobia and want to keep track of what ghosts are possible and follow along.
Input: Pressing Buttons For Evidence Or Selecting Ghosts
Output: A GUI That Shows Possible Ghosts Based On Evidence And If User Stated It Is Not Possible
Author: MadiSperry
'''

# Import Necessary Libraries
from tkinter import *
import tkinter
from tkinter.ttk import *
import tkinter.font as tkFont
from PIL import Image, ImageTk

# Config Variables for PNGs
evidencePNGPath = "C:\\personalFiles\\Coding\\Python\\randomProjects\\PhasmophobiaTracker\\evidencePNG\\"
evidencePNG = ["EMF", "SpiritBox", "Fingerprints", "GhostOrb", "WritingBook", "Thermo", "DOTS"]
thumbnailWidth, thumbnailHeight = 154, 101

# Non-Config Variables
evidenceTypes = ["EMF 5", "Spirit Box", "Fingerprints", "Ghost Orbs", "Ghost Writing", "Freezing Temps", "D.O.T.S."]
ghosts = ["Spirit", "Wraith", "Phantom", "Poltergeist", "Banshee", "Jinn", "Mare", "Revenant", "Shade", "Demon", "Yurei", 
          "Oni", "Yokai", "Hantu", "Goryo", "Myling", "Onryo", "Twins", "Raiju", "Obake", "Mimic", "Moroi", "Deogen", "Thaye"]

# 3 States (0,1,2) for (Not Selected, Confirmed, Confirmed Impossible) Respectively
EMFConfirmed = 0
SBConfirmed = 0
FingersConfirmed = 0
OrbsConfirmed = 0
WritingConfirmed = 0
FreezingConfirmed = 0
DOTSConfirmed = 0

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
        evidence = Image.open(evidencePNGPath + name + ".png").resize((thumbnailWidth, thumbnailHeight), Image.ANTIALIAS)
        evidence = ImageTk.PhotoImage(evidence)
        evidencePNG[i] = evidence
        i += 1

##########################################################################################################################################################################

# Function For Every Time An Evidence Button is hit.
def pressButton(evidence):
    global EMFConfirmed, SBConfirmed, FingersConfirmed, OrbsConfirmed, WritingConfirmed, FreezingConfirmed, DOTSConfirmed
    
    if evidence == evidenceTypes[0]:
        # If Not Selected, Set as Confirmed Evidence
        if EMFConfirmed == 0:
            EMFConfirmed = 1
            evidenceCollected.append(evidenceTypes[0])
        # If Confirmed, Set as Confirmed Impossible Evidence
        elif EMFConfirmed == 1:
            EMFConfirmed = 2
            evidenceCollected.remove(evidenceTypes[0])
        # If not Not Selected and not Confirmed, Set as Not Selected
        else:
            EMFConfirmed = 0
    elif evidence == evidenceTypes[1]:
        if SBConfirmed == 0:
            SBConfirmed = 1
            evidenceCollected.append(evidenceTypes[1])
        elif SBConfirmed == 1:
            SBConfirmed = 2
            evidenceCollected.remove(evidenceTypes[1])
        else:
            SBConfirmed = 0
    elif evidence == evidenceTypes[2]:
        if FingersConfirmed == 0:
            FingersConfirmed = 1
            evidenceCollected.append(evidenceTypes[2])
        elif FingersConfirmed == 1:
            FingersConfirmed = 2
            evidenceCollected.remove(evidenceTypes[2])
        else:
            FingersConfirmed = 0
    elif evidence == evidenceTypes[3]:
        if OrbsConfirmed == 0:
            OrbsConfirmed = 1
            evidenceCollected.append(evidenceTypes[3])
        elif OrbsConfirmed == 1:
            OrbsConfirmed = 2
            evidenceCollected.remove(evidenceTypes[3])
        else:
            OrbsConfirmed = 0
    elif evidence == evidenceTypes[4]:
        if WritingConfirmed == 0:
            WritingConfirmed = 1
            evidenceCollected.append(evidenceTypes[4])
        elif WritingConfirmed == 1:
            WritingConfirmed = 2
            evidenceCollected.remove(evidenceTypes[4])
        else:
            WritingConfirmed = 0
    elif evidence == evidenceTypes[5]:
        if FreezingConfirmed == 0:
            FreezingConfirmed = 1
            evidenceCollected.append(evidenceTypes[5])
        elif FreezingConfirmed == 1:
            FreezingConfirmed = 2
            evidenceCollected.remove(evidenceTypes[5])
        else:
            FreezingConfirmed = 0
    elif evidence == evidenceTypes[6]:
        if DOTSConfirmed == 0:
            DOTSConfirmed = 1
            evidenceCollected.append(evidenceTypes[6])
        elif DOTSConfirmed == 1:
            DOTSConfirmed = 2
            evidenceCollected.remove(evidenceTypes[6])
        else:
            DOTSConfirmed = 0
    main_menu()
    
# Function Called Every Time A Change Is Made To main_menu() And Is Called.
def compilePossibleGhosts(evidences):
    global possibleGhosts, ghosts
    evidenceSet = []
    possibleGhosts = []

    # If No Evidence, All Ghosts Are Possible
    if len(evidences) == 0:
        possibleGhosts = ghosts
    else:
        # For Each Evidence Selected, Create A List For All Ghosts For Each Evidence
        for evidence in evidences:
            if evidence == "EMF 5":
                evidenceSet += [EMFGhosts]
            elif evidence == "Spirit Box":
                evidenceSet += [SBGhosts]
            elif evidence == "Fingerprints":
                evidenceSet += [FingersGhosts]
            elif evidence == "Ghost Orbs":
                evidenceSet += [OrbsGhosts]
            elif evidence == "Ghost Writing":
                evidenceSet += [WritingGhosts]
            elif evidence == "Freezing Temps":
                evidenceSet += [FreezingGhosts]
            elif evidence == "D.O.T.S.":
                evidenceSet += [DOTSGhosts]
    
    # If No Evidence, Return To main_menu(), Else If Each Ghost Is In Each List, Add It To possibleGhosts
    if len(evidences) == 0:
        main_menu()
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
    main_menu()

# If User Clicks A Ghost Name, That Ghost Name Is Added Or Removed From userDeniedGhosts
def createUserDeclinedGhosts(ghost):
    global userDeniedGhosts
    if ghost in userDeniedGhosts:
        userDeniedGhosts.remove(ghosts[ghost])
    else:
        userDeniedGhosts += [ghosts[ghost]]
    print(userDeniedGhosts)
    main_menu()

# Decides The Color Of The Button If Evidence Is Not Selected, Confirmed, or Confirmed Impossible
def decideColor(evidence):
    if evidence == "EMF 5":
        if EMFConfirmed == 0:
            return "#f0f0f0"
        elif EMFConfirmed == 1:
            return "#c9ffad"
        elif EMFConfirmed == 2:
            return "#ffadad"
    elif evidence == "Spirit Box":
        if SBConfirmed == 0:
            return "#f0f0f0"
        elif SBConfirmed == 1:
            return "#c9ffad"
        elif SBConfirmed == 2:
            return "#ffadad"
    elif evidence == "Fingerprints":
        if FingersConfirmed == 0:
            return "#f0f0f0"
        elif FingersConfirmed == 1:
            return "#c9ffad"
        elif FingersConfirmed == 2:
            return "#ffadad"
    elif evidence == "Ghost Orbs":
        if OrbsConfirmed == 0:
            return "#f0f0f0"
        elif OrbsConfirmed == 1:
            return "#c9ffad"
        elif OrbsConfirmed == 2:
            return "#ffadad"
    elif evidence == "Ghost Writing":
        if WritingConfirmed == 0:
            return "#f0f0f0"
        elif WritingConfirmed == 1:
            return "#c9ffad"
        elif WritingConfirmed == 2:
            return "#ffadad"
    elif evidence == "Freezing Temps":
        if FreezingConfirmed == 0:
            return "#f0f0f0"
        elif FreezingConfirmed == 1:
            return "#c9ffad"
        elif FreezingConfirmed == 2:
            return "#ffadad"
    elif evidence == "D.O.T.S.":
        if DOTSConfirmed == 0:
            return "#f0f0f0"
        elif DOTSConfirmed == 1:
            return "#c9ffad"
        elif DOTSConfirmed == 2:
            return "#ffadad"

##########################################################################################################################################################################

# Function To Reset All Variables To Defaults
def reset():
    global EMFConfirmed, SBConfirmed, FingersConfirmed, OrbsConfirmed, WritingConfirmed, FreezingConfirmed, DOTSConfirmed, evidenceCollected, userDeniedGhosts
    EMFConfirmed = 0
    SBConfirmed = 0
    FingersConfirmed = 0
    OrbsConfirmed = 0
    WritingConfirmed = 0
    FreezingConfirmed = 0
    DOTSConfirmed = 0
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
    clear_root()
    compilePossibleGhosts(evidenceCollected)

    # Create frames for the main_menu
    frame1 = createFrame(TOP)
    frame2 = createFrame(TOP)
    frame3 = createFrame(TOP)
    frame4 = createFrame(TOP)
       
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
            if ghosts[i] in possibleGhosts and ghosts[i] not in userDeniedGhosts:
                tkinter.Button(frame3, text = ghosts[i], command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = normal_Font, fg = "#000000", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] not in possibleGhosts and ghosts[i] not in userDeniedGhosts:
                tkinter.Button(frame3, text = ghosts[i], command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = normal_Font, fg = "#d1d1d1", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] in possibleGhosts and ghosts[i] in userDeniedGhosts:
                tkinter.Button(frame3, text = ghosts[i], command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = strike_Font, fg = "#000000", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            elif ghosts[i] not in possibleGhosts and ghosts[i] in userDeniedGhosts:
                tkinter.Button(frame3, text = ghosts[i], command = lambda i=i: createUserDeclinedGhosts(i), compound = CENTER, font = strike_Font, fg = "#d1d1d1", borderwidth=0, height = 0).grid(column = x, row = y, pady=0, padx=10)
            i += 1

    # Create reset button to set everything back to defaults
    tkinter.Button(frame4, text = "Reset", compound = CENTER, font = ("papyrus", 15), command = reset).grid(column = 1, row = 1, pady=20, padx=25) 

##########################################################################################################################################################################

# Function To Reset All Variables To Defaults
def reset():
    global EMFConfirmed, SBConfirmed, FingersConfirmed, OrbsConfirmed, WritingConfirmed, FreezingConfirmed, DOTSConfirmed, evidenceCollected, userDeniedGhosts
    EMFConfirmed = 0
    SBConfirmed = 0
    FingersConfirmed = 0
    OrbsConfirmed = 0
    WritingConfirmed = 0
    FreezingConfirmed = 0
    DOTSConfirmed = 0
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

# Create root GUI, give it a name, make it full screened
root = Tk()
root.geometry('1000x300')
root.title("MadiSperry's Phasmophobia Tracker")
root.state('zoomed')

# Set Normal Font And A Font With A Strikethrough
normal_Font = tkFont.Font(family="Papyrus", size=20, overstrike = 0)
strike_Font = tkFont.Font(family="Papyrus", size=20, overstrike = 1)

# Run function to create The Evidence Thumbnails
createEvidenceThumbnails()

# Run the main_menu function to start out with the main scene of the GUI
main_menu()
root.mainloop()