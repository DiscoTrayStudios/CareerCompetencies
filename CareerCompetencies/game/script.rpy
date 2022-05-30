# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen", color="#F5822A", what_color="#F8B55D")
define b = Character("Bob", color="#3F888F", what_color="#6FBBBF")
define guy = Character("Guy", color="#990000", what_color="#CC6666")
define r = Character("Roomie", color="#3F888F", what_color="#6FBBBF")
define a = Character("Alex", color = "#3F888F", what_color = "#6FBBBF")
define el = Character("Elle", color = "#3F888F", what_color = "#6FBBBF")
define t = Character("Taylor", color = "#3F888F", what_color = "#6FBBBF")
define w = Character("Whitney", color = "#3F888F", what_color = "#6FBBBF")
define p = Character("You")
define x = Character("Company X recruiter", color="#1AA009", what_color="#5EE44D")
define l = Character("Librarian", color="#B4C22C", what_color="#E7F00F")
define d = Character("Dr. Reynolds", color="#F5822A", what_color="#F8B55D")
define s = Character("Dr. Smith", color="#B4C22C", what_color="#E7F00F")
define m = Character("Dr. Maslow", color="#B4C22C", what_color="#E7F00F")
define o =  Character("Dr. Orozco", color="#B4C22C", what_color="#E7F00F")
define bl = Character("Blakely", color = "#3F888F", what_color = "#6FBBBF")
define j = Character("Joey", color = "#3F888F", what_color = "#6FBBBF")
define n = Character("Niraj", color = "#3F888F", what_color = "#6FBBBF")
define z = Character("Zach", color = "#3F888F", what_color = "#6FBBBF")
image map = "Map/Hdxblank.png"
# Dr. Melicia Reynolds
image eileen = "Characters/Eileen.png"
image eileenTalk = "Characters/EileenTalk.png"
image eileenSmile = "Characters/EileenEyesClosedSmile.png"
image bob = "Characters/bob.png"
image charlie = "Characters/Charlie.png"
image advisor = "Characters/Advisor.png"
image librarian = "Characters/Librarian.png"
image compx = "Characters/CompanyXRecruiter.png"
image whitney = "Characters/Whitney.png"
image taylor = "Characters/Other.png"
image smith = "Characters/Smithnew.png"
image orozco = "Characters/Orozco.png"
image maslow = "Characters/Maslow.png"
image alex = "Characters/Alex.png"
image elle = "Characters/Elle.png"
image blakely = "Characters/Blakely.png"
image niraj = "Characters/Niraj.png"
image joey = "Characters/Joey.png"
image zach = "Characters/Zach.png"


image libraryBackground = "Backgrounds/library.jpg"
image pecanCourtBackground = "Backgrounds/p.jpg"
image welcomeCenterBackground = "Backgrounds/welcomeCenter.jpg"
image sltcBackground = "Backgrounds/sltc.jpg"
image sltcLobby = "Backgrounds/sltclobby.jpg"
image couchBackground = "Backgrounds/couch.jpg"
image couchRoom = "Backgrounds/couchRoom.jpg"
image millsBackground = "Backgrounds/mills.jpg"
image snoddyCenter = "Backgrounds/snoddy.jpg"
image studyCorral = "Backgrounds/study.jpg"
image office = "Backgrounds/office.jpg"
image careerfairtalk = "Backgrounds/CareerFairTalk.jpg"
image careerterm = "Backgrounds/CareerTerm.jpg"
image careerfair = "Backgrounds/career fair.jpg"

define competencies = "CompIcons/comps.png"

define brain = "CompIcons/Orange/Orange Brain.png"
define briefcase = "CompIcons/Orange/Orange Briefcase.png"
define inclusion = "CompIcons/Orange/Orange EquityInclusion.png"
define career = "CompIcons/Orange/Orange GradHat.png"
define handshake = "CompIcons/Orange/Orange Handshake.png"
define laptop = "CompIcons/Orange/Orange Laptop.png"
define lead = "CompIcons/Orange/Orange MountainTop.png"
define comm = "CompIcons/Orange/Orange TextBubble.png"








#

# The game starts here.

label start:
    # General Data
    $ seen_map = False
    $ been_to_career_services = False
    $ map_interact = False
    $ visited = 0
    $ allowed = 0
    $ compsgot = 0
    $ curchpt = 0
    $ changed_location = False
    $ seen_wc = False
    # Name stuff


    #Social and Academic Values
    $ social = 20
    $ academic = 20
    $ sleep = 20

    # Competency values
    $ dev = 15
    $ communication = 15
    $ thinking = 15
    $ equity = 15
    $ leadership = 15
    $ proffesional = 15
    $ teamwork = 15
    $ tech = 15

    $ lefts = False
    $ ups = False
    $ centers = False

    $ hdxtodayseen = False

    # Location Booleans
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False

    # begin is main 'Go To' scene
    jump begin



label begin:
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide screen resumeToggle
    scene p

    jump welcome

    return

label library:
    $ changed_location = True
    $ atLibrary = True
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide eileen with dissolve
    scene libraryBackground
    jump libraryHelper

label libraryHelper:
    if curchpt == 1:
        jump Y1_C1_L
    if curchpt == 2:
        jump Y1_C2_L
    if curchpt == 3:
        jump Y2_C1_L
    if curchpt == 4:
        jump Y2_C2_L
    show confettiLeft
    show confettiRight
    show confettiLeftB
    show confettiRightB
    # "Thanks for visiting, You got teamwork as a test!"

    # $ teamwork = True
    return


label sltc:
    $ changed_location = True
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = True
    $ atWC = False
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    scene sltcBackground
    show eileenTalk
    e "This is where you can find tons of helpful student recources, some great food, and a nice place to hang out!"
    jump sltcHelper

label mills:
    $ changed_location = True
    $ atLibrary = False
    $ atMills = True
    $ atSLTC = False
    $ atWC = False
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    scene p
    if curchpt == 1:
        jump Y1_C1_M
    if curchpt == 2:
        jump Y1_C2_M
    if curchpt == 3:
        jump Y2_C1_M
    if curchpt == 4:
        jump Y2_C2_M
    return


label sltcHelper:
    hide eileenTalk
    show eileen at left
    menu:
        "Where would you like to visit?"
        "Burrow":
            hide eileen
            if curchpt == 1:
                jump Y1_C1_SLTC
            if curchpt == 2:
                jump Y1_C2_SLTC
            if curchpt == 3:
                jump Y2_C1_SLTC
            if curchpt == 4:
                jump Y2_C2_SLTC
            "We are not on Ch1 or 2"
            jump sltcHelper
        "Odyssey Office":
            e "Sorry, this is in development!"
            jump sltcHelper
        "Career Services":
            if not been_to_career_services:
                jump careerIntro
            else:
                jump career
        "Nevermind":
            show eileenTalk
            hide eileen
            e "That's okay!"
    return





label welcomecenter:
    $ changed_location = True
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = True
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide eileen
    hide pecanCourtBackground
    scene welcomeCenterBackground

    jump welcomecenterHelper

label welcomecenterHelper:
    if not seen_wc:
        "{i}I should see what's around here, being new and all...{/i}"
        $ seen_wc = True
    if curchpt == 1:
        jump Y1_C1_WC
    if curchpt == 2:
        jump Y1_C2_WC
    if curchpt == 3:
        jump Y2_C1_WC
    if curchpt == 4:
        jump Y2_C2_WC
    "{i}Obtained Leadership{/i}"
    show confettiLeft
    show confettiRight
    # $ leadership = True
    return




label welcome:
    hide eileen
    hide screen ResumeUI
    hide screen ResumeText
    hide screen resumeToggle
    $ curchpt = 1
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False

    $ hdxtodayseen = False
    # Welcome to Hendrix!
    show eileen with dissolve
    e "Welcome to Hendrix!"

    e "I am Eileen, and I'll be around to help you get adjusted to the Hendrix life and explain some things about Hendrix!"
    e "You'll be seeing me a lot, so it's nice to meet you!"
    e "Now, it's your first day on campus so you should go move in!"
    hide eileen with dissolve
    scene couchBackground
    "{i}Ah so this is Couch Hall. This is really close to the caf!"
    "{i} Well, I better start moving in."
    scene couchRoom
    "You just got to your dorm room in Couch Hall."
    "{i}There is already someone in there..."
    # I said Couch since it is not gender-exclusive. However, we can let the players choose later on if we want.
    # "Your roommate isn't here yet, but hey that just means that you get the first pick on everything!"

    # We can add randomization here to where some people will get there first and some will get there last.

    # Once you encounter the roommate
    show charlie at left with dissolve
    $ lefts = False
    r "Hey! I'm your roommate _**#(@)$)@#()**_ what's your name?"

    call charmaker from _call_charmaker

    r "Alright [p], nice to meet ya."

    "{i}Wait what did they just say their name was.... did it say it on the door? I don't remember.. I'll just call them [r].{/i}"

    menu:
        "Look at the door for their name":
            jump Y1_S1_C1
        "Figure it out later, they might notice":
            jump Y1_S1_C2

label charmaker:
    hide charlie
    show charlie:
        blur 8
    show screen CharMaker
    show screen CharMakerText
    $ spot = 1
    $ ath = ""
    $ pro = ""
    $ maj = ""
    $ name = renpy.input(_("What's your name?"))
    $ name = name.strip() or __("No Name")
    $ p = Character(name, color="#B8B799", what_color="#EBEACC")
    show screen CharAnswerText
    $ spot = 2
    $ pro = renpy.input(_("What are your pronouns?"))
    $ pro = pro.strip() or __("None")
    $ spot = 3
    $ maj = renpy.input(_("What is your planned major, if any?"))
    $ maj = maj.strip() or __("None")
    $ spot = 4
    $ decisionMade = False
    show screen CharAnswerButtons
    while not decisionMade:
        "Please make a decision."

    hide screen CharAnswerButtons
    "Thank you for completing Character Creation."
    hide screen CharMaker
    hide screen CharMakerText
    hide screen CharAnswerText
    show charlie:
        blur 0
    return





label map:
    scene p
    if visited < allowed:
        $ changed_location = False
        hide screen resumeToggle
        hide screen resumeUI
        hide screen ResumeText
        hide screen mapUI
        hide screen hdxtodayb
        show screen MapUI with dissolve
        show eileenTalk at right with dissolve


        if not seen_map:
            e "This is an interactive map of Hendrix!"
            e "Clicking on a building will allow you to visit that location, provided you are allowed to."
            e "You may only select buildings that are in full color."
            $ map_interact = True
            $ seen_map = True

        else:
            label repeat:
                e "Please click the next location you would like to visit."

        if seen_map and renpy.get_screen("MapUI"):
            call repeat
        else:
            call map
    else:
        $ atLibrary = False
        $ atMills = False
        $ atSLTC = False
        $ atWC = False

label resume:
    if visited<allowed:
        show screen ResumeUI
        show screen ResumeText
        hide screen resumeToggle

        $ temp = lefts
        $lefts = False
        $ ups = True
        menu:
            "Continue?":
                $ ups = False
                $lefts = temp
                hide screen ResumeUI
                hide screen ResumeText
                hide screen resumeToggle
                return

label hdxtoday:
    scene p
    if visited < allowed and not hdxtodayseen:
        show screen hdxtodayb with dissolve

        $ temp = lefts
        $ lefts = False
        $ ups = True
        menu:
            "Continue?":
                hide screen hdxtodayb
                $ lefts = temp
                $ ups = False
                $ hdxtodayseen = True


label quit:
    return


label gameOver:
    "That is the end of the demo so far, thank you for playing!"
    jump quit
