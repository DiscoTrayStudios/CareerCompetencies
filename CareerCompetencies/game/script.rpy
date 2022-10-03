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
define mi = Character("Micky", color = "#3F888F", what_color = "#6FBBBF")
define o =  Character("Dr. Orozco", color="#B4C22C", what_color="#E7F00F")
define bl = Character("Blakely", color = "#3F888F", what_color = "#6FBBBF")
define j = Character("Joey", color = "#3F888F", what_color = "#6FBBBF")
define n = Character("Niraj", color = "#3F888F", what_color = "#6FBBBF")
define z = Character("Zach", color = "#3F888F", what_color = "#6FBBBF")
define pr = Character("Dr. Willis", color = "00539CFF", what_color = "EEA47FFF")
image map = "Map/Hdxblank.png"
# Dr. Melicia Reynolds

image eileen = "Characters/Eileen.png"
image eileenTalk = "Characters/EileenTalk.png"
image eileenSmile = "Characters/EileenEyesClosedSmile.png"
image bob = "Characters/bob.png"
image bobTalk = "Characters/bobTalk.png"
image charlie = "Characters/Charlie.png"
image charlieTalk = "Characters/CharlieTalk.png"
image advisor = "Characters/Advisor.png"
image advisorTalk = "Characters/AdvisorTalk.png"
image advisorSmile = "Characters/AdvisorSmile.png"
image librarian = "Characters/Librarian.png"
image librarianTalk = "Characters/LibrarianTalk.png"
image librarianSmile = "Characters/LibrarianSmile.png"
image compx = "Characters/CompanyX.png"
image compxTalk = "Characters/CompanyXRecruiter.png"
image whitney = "Characters/Whitney.png"
image whitneyTalk = "Characters/WhitneyTalk.png"
image taylor = "Characters/Other.png"
image taylorTalk = "Characters/otherTalk.png"
image taylor2 = "Characters/Taylor.png"
image taylor2Talk = "Characters/TaylorSmile.png"
image taylor2Talk = "Characters/TaylotTalk.png"
image smithTalk = "Characters/Smithnew.png"
image smith = "Characters/SmithClosed.png"
image smith2 = "Characters/Smith.png"
image smith2Talk = "Characters/SmithTalk.png"
image orozco = "Characters/Orozco.png"
image orozcoTalk = "Characters/OrozcoTalk.png"
image maslow = "Characters/Maslow.png"
image maslowTalk = "Characters/MaslowTalk.png"
image micky = "Characters/Micky.png"
image mickyTalk = "Characters/MickyTalk.png"
image mickySmile = "Characters/MickySmile.png"
image alex = "Characters/Alex.png"
image alexTalk = "Characters/alexTalk.png"
image elle = "Characters/Elle.png"
image elleTalk = "Characters/elleTalk.png"
image blakely = "Characters/Blakely.png"
image blakelyTalk = "Characters/BlakelyTalk.png"
image blakelySmile = "Characters/BlakelySmile.png"
image niraj = "Characters/Niraj.png"
image nirajTalk = "Characters/NirajTalk.png"
image nirajSmile = "Characters/NirajSmile.png"
image joey = "Characters/Joey.png"
image joeyTalk = "Characters/JoeyTalk.png"
image zach = "Characters/Zach.png"
image zachSmile = "Characters/ZachSmile.png"
image zachTalk = "Characters/ZachTalk.png"
image professor = "Characters/professor.png"
image professorNormal = "Characters/professorNormal.png"


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
image compxoffice = "Backgrounds/compxoffice.jpg"
image millsLibrary = "Backgrounds/mills_library.jpg"
image cabe = "Backgrounds/cabe.jpg"
image burrow = "Backgrounds/Burrow.jpg"

define competencies = "CompIcons/comps.png"

define brain = "CompIcons/Orange/Orange Brain.png"
define briefcase = "CompIcons/Orange/Orange Briefcase.png"
define inclusion = "CompIcons/Orange/Orange EquityInclusion.png"
define career = "CompIcons/Orange/Orange GradHat.png"
define handshake = "CompIcons/Orange/Orange Handshake.png"
define laptop = "CompIcons/Orange/Orange Laptop.png"
define lead = "CompIcons/Orange/Orange MountainTop.png"
define comm = "CompIcons/Orange/Orange TextBubble.png"




# The game starts here.

label start:

    # Checkpoint Booleans
    $ Jobs = 0
    $ CV = False
    $ InternHospital = False
    $ BaileyWorker = False
    $ TaxVol = False
    $ Theatre = False
    $ CellBio = False
    $ Phonathon = False
    $ socialjobs = 0
    $ stemjobs = 0
    $ internjobs = 0
    $ qual = 0
    $ tour = False
    $ burrowvisited = False


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
    $ exhaustion = 0
    $ exhausted = False

    # Competency values
    $ dev = 15
    $ communication = 15
    $ thinking = 15
    $ equity = 15
    $ leadership = 15
    $ professional = 15
    $ teamwork = 15
    $ tech = 15

    $ prevdev = dev
    $ prevcommunication = communication
    $ prevthinking = thinking
    $ prevequity = equity
    $ prevleadership = leadership
    $ prevprofessional = professional
    $ prevteamwork = teamwork
    $ prevtech = tech

    $ lefts = False
    $ ups = False
    $ centers = False

    $ hdxtodayseen = False

    # Location Booleans
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ beenToLibrary = False
    $ beenToMills = False
    $ beenToSLTC = False
    $ beenToWC = False




    if persistent.analytics is None:

        menu:
            "Welcome! This game supports analytics. Enabling it will help us make better games, and will send data to Google Analytics and the developers. Do you want to enable analytics?"

            "Yes.":
                $ persistent.analytics = True
                "Thank you."

            "No.":
                $ persistent.analytics = False
                "No problem!"

    init python:
        def label_callback(label, abnormal):

            # Filter out labels that are part of Ren'Py and not the game.
            filename = renpy.get_filename_line()[0]
            if filename.startswith("renpy/common/"):
                return

            analytics.event("Label", label)

        config.label_callback = label_callback

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
    $ beenToLibrary = True
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
        jump Y1_C3_L
    if curchpt == 4:
        jump Y2_C1_L
    if curchpt == 5:
        jump Y2_C2_L
    if curchpt == 6:
        jump Y2_C3_L
    # "Thanks for visiting, You got teamwork as a test!"

    # $ teamwork = True
    return


label sltc:
    $ changed_location = True
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = True
    $ beenToSLTC = True
    $ atWC = False
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    scene sltcBackground
    show eileenTalk
    e "This is where you can find tons of helpful student resources, some great food, and a nice place to hang out!"
    jump sltcHelper

label mills:
    $ changed_location = True
    $ atLibrary = False
    $ atMills = True
    $ beenToMills = True
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
        jump Y1_C3_M
    if curchpt == 4:
        jump Y2_C1_M
    if curchpt == 5:
        jump Y2_C2_M
    if curchpt == 6:
        jump Y2_C3_M
    return


label sltcHelper:
    scene sltc
    hide eileenTalk
    show eileen at left
    menu:
        "Where would you like to visit?"

        "Burrow":
            if not burrowvisited:
                $ burrowvisited = True
                hide eileen
                if curchpt == 1:
                    call Y1_C1_SLTC
                if curchpt == 2:
                    call Y1_C2_SLTC
                if curchpt == 3:
                    call Y1_C3_SLTC
                if curchpt == 4:
                    call Y2_C1_SLTC
                if curchpt == 5:
                    call Y2_C2_SLTC
                if curchpt == 6:
                    call Y2_C3_SLTC
                jump sltcHelper
            else:
                "{i}I've already been there today..."
                jump sltcHelper
        "Odyssey Office":
            call odysseyscript

            jump sltcHelper
        "Career Services":
            if not been_to_career_services:
                call careerIntro
            else:
                call career
            jump sltcHelper
        "Nevermind":
            show eileenTalk
            hide eileen
            e "That's okay!"
    $ burrowvisited = False
    return





label welcomecenter:
    $ changed_location = True
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = True
    $ beenToWC = True
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
        $ seen_wc = True
    if curchpt == 1:
        jump Y1_C1_WC
    if curchpt == 2:
        jump Y1_C2_WC
    if curchpt == 3:
        jump Y1_C3_WC
    if curchpt == 4:
        jump Y2_C1_WC
    if curchpt == 5:
        jump Y2_C2_WC
    if curchpt == 6:
        jump Y2_C3_WC
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
    e "If you're ever unsure of where to go in life, or want more {color=#FFFF33}{u}Experience{/u}{/color}, make sure to visit us in Career Services in the SLTC and ask what your next steps should be."
    e "We have new stuff all the time, so make sure to visit often if you want new {color=#FFFF33}{u}Experiences{/u}{/color}."
    e "Now, it's your first day on campus so you should go move in!"
    hide eileen with dissolve
    scene couchBackground
    "{i}Ah so this is Couch Hall. This is really close to the caf!"
    "{i} Well, I better start moving in."
    scene couchRoom
    "You just got to your dorm room in Couch Hall."
    "{i}There is already someone in there..."
    # I said Couch since it is not gender-exclusive. However, we can let the players choose later on if we want.

    # We can add randomization here to where some people will get there first and some will get there last.

    # Once you encounter the roommate
    show charlie at left with dissolve
    $ lefts = False
    show charlieTalk at left
    r "Hey! I'm your roommate _**#(@)$)@#()**_ what's your name?"
    hide charlieTalk
    call charmaker from _call_charmaker
    hide charlie
    show charlieTalk at left
    r "Alright [p], nice to meet ya."
    hide charlieTalk
    show charlie at left
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
            call repeat from _call_repeat
        else:
            call map from _call_map_8
    else:
        $ atLibrary = False
        $ atMills = False
        $ atSLTC = False
        $ atWC = False
        $ beenToLibrary = False
        $ beenToMills = False
        $ beenToSLTC = False
        $ beenToWC = False

label resume:
    if visited < allowed:
        show screen ResumeUI
        show screen ResumeText
        hide screen resumeToggle
        $ centers = False
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
        $ prevdev = dev
        $ prevcommunication = communication
        $ prevthinking = thinking
        $ prevequity = equity
        $ prevleadership = leadership
        $ prevprofessional = professional
        $ prevteamwork = teamwork
        $ prevtech = tech
        menu:
            "Continue?":
                hide screen hdxtodayb
                $ lefts = temp
                $ ups = False
                $ hdxtodayseen = True


label quit:
    return


label gameOver:
    "That is the end of the demo so far. We hope you enjoyed and if you could, please fill out this form with questions or comments you have."
    "{a=https://forms.office.com/Pages/ResponsePage.aspx?id=jMH2DNLQP0qD0GY9Ygpj07DpPZamV_BBg8M3_X3radFUQjFLWVdZM0xWMFNRVUhUVzROQ1c4M08zNC4u}{/a}"
    "Thank you for playing :)"

    jump quit
