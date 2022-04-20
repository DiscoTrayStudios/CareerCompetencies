# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen", color="#F5822A", what_color="#F8B55D")
define b = Character("Bob", color="#3F888F", what_color="#6FBBBF")
define guy = Character("Guy", color="#990000", what_color="#CC6666")
define r = Character("Roomie", color="#3F888F", what_color="#6FBBBF")
define a = Character("Alex", color = "#3F888F", what_color = "#6FBBBF")
define t = Character("Taylor", color = "#3F888F", what_color = "#6FBBBF")
define w = Character("Whitney", color = "#3F888F", what_color = "#6FBBBF")
define p = Character("You")
define x = Character("Company X recruiter", color="#1AA009", what_color="#5EE44D")
define l = Character("Librarian", color="#B4C22C", what_color="#E7F00F")
define s = Character("Dr. Smith", color="#B4C22C", what_color="#E7F00F")
define m = Character("Dr. Maslow", color="#B4C22C", what_color="#E7F00F")
define o =  Character("Dr. Orozco", color="#B4C22C", what_color="#E7F00F")
image map = "Map/Hdxblank.png"
image eileen = "Characters/Eileen.png"
image eileenTalk = "Characters/EileenTalk.png"
image eileenSmile = "Characters/EileenEyesClosedSmile.png"
image bob = "Characters/bob.png"
image charlie = "Characters/Charlie.png"
image libraryBackground = "Backgrounds/library.jpg"
image pecanCourtBackground = "Backgrounds/p.jpg"
image welcomeCenterBackground = "Backgrounds/welcomeCenter.jpg"
image sltcBackground = "Backgrounds/sltc.jpg"
image sltcLobby = "Backgrounds/sltclobby.jpg"


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

    $ hdxtodayseen = False

    # Location Booleans
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False

    # begin is main 'Go To' scene
    jump begin


label Tutorial:
    scene p
    show eileenTalk
    e "This is the Tutorial!"
    e "Here we'll go over what the game is about, and how to properly use the game system to your advantage!"
    e "The purpose of this game is to give you, the player, and insight into what a generalized life at Hendrix can be like, with an emphasis on career development."
    e "Through focusing on career development earlier rather than later, it should become apparent that college becomes easier and presents more opportunities."
    e "Our hope is that through playing you can become a bit more informed how to take advantage of the recources offered at Hendrix and help get you thinking about what is next!"
    e "Now on how to use the game system!"
    show screen ss
    hide eileenTalk
    show eileenTalk at right
    e "At any point, you can access the game menu by right-clicking or hitting the escape button"
    e "Some of these game menu options are always available in the menu at the bottom of the screen"
    e "The game menu includes all saves of the game. Clicking on one of these slots will create a save at whatever point you are at in the game."
    e "There is no limit on the number of saves you can make, which is helpful in case you ever want to go back and pick a different decision!"
    e "If you would ever like to delete a save, hover over the save slot and hit the 'delete' key on your keyboard."
    e "Using the Load menu is much the same, but allows you to go back to any point you have previously saved."
    e "There is also a Preferences screen that holds valuable controls over the game such as text speed and volume controls."
    e "There are also helpful keyboard and mouse shortcuts, so make sure to explore the game menu!"
    hide screen ss
    e "Thanks for sticking around for my long speech, now let's go on to the game!"

    jump start
label begin:
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide screen resumeToggle
    scene p

    jump welcome

    return

label library:
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
    show confettiLeft
    show confettiRight
    show confettiLeftB
    show confettiRightB
    "Thanks for visiting, You got teamwork as a test!"

    $ teamwork = True
    return


label sltc:
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
    return


label sltcHelper:
    hide eileenTalk
    show eileen at left
    menu:
        "Where would you like to visit?"
        "Common area":
            hide eileen
            if curchpt == 1:
                jump Y1_C1_SLTC
            if curchpt == 2:
                jump Y1_C2_SLTC
            if curchpt == 3:
                jump Y2_C1_SLTC
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


label careerIntro:
    hide eileen
    show eileenTalk
    e "Welcome to career services! How may we help you today?"
    hide eileenTalk
    show eileen
    p "I'm not sure, what do you do here?"
    hide eileen
    show eileenTalk
    e "We're all about providing inclusive and insightful career services to prepare, inspire, and empower all Hendrix students for future success."
    $ been_to_career_services = True
    jump career

label career:
    show eileen at left
    hide eileenTalk
    menu:
        "Here are some of the services we provide. Which would you like to learn about?"
        "Career and Internship Fair":
            show eileenTalk
            hide eileen
            e "The Career and Internship Fair is an exciting event that takes place each spring semester."
            e "Career Services help introduce a wide range of organizations on campus to help students connect to potential internship and employment opportunities."
            e "We highly reccomend everyone, no matter their class, experience, or future goals, to attend!"
            jump career
        "Four Year Plan":
            show eileenTalk
            hide eileen
            e "We help provide a guideline for students to help them achieve their fullest potential while at Hendrix."
            e "We have planned out things that will help you succeed, no matter where you are on your Hendrix journey."
            jump career
        "Culteral Competencies":
            show eileenTalk
            hide eileen
            e "One of the many great things about Hendrix College is that every student is given a breadth of knowledge that equips them to handle any obstacle"
            e "This knowledge is broken down into 8 categories that we call our 'Culteral Competencies'."
            e "Here are a list of the eight of them, along with a description."
            e "{b}{size=+6}Critical Thinking{/size}{/b}\nHendrix students exercise sound reasoning to analyze issues, make decisions, and overcome problems."
            e "{b}{size=+6}Career and Self-Development{/size}{/b}\nHendrix students proactively identify and articulate their skills, strengths, knowledge, and experiences relevant to their career goals."
            e "{b}{size=+6}Career and Self-Development{/size}{/b}\nThey identify areas necessary for personal and professional growth, navigate career opportunities, and network to build relationships."
            e "{b}{size=+6}Communication{/size}{/b}\nHendrix Students understand and leverage technologies ethically to enhance efficiencies, complete tasks, and accomplish goals."
            e "{b}{size=+6}Equity and Inclusion{/size}{/b}\nHendrix students demonstrate the awareness, attitude, knowledge, and skills required to equitably engage and include people from different backgrounds and cultures."
            e "{b}{size=+6}Equity and Inclusion{/size}{/b}\nThey engage in practices that actively challenge the systems, structures, and policies of inequity."
            e "{b}{size=+6}Leadership{/size}{/b}\nHendrix students leverage the strengths of others to achieve common goals and use interpersonal skills to develop others."
            e "{b}{size=+6}Leadership{/size}{/b}\nThey use empathetic skills to motivate and guide others. They organize, prioritize, and delegate work."
            e "{b}{size=+6}Professionalism{/size}{/b}\nHendrix students demonstrate personal accountability and effective work habits. They demonstrate integrity and ethical behavior,"
            e "{b}{size=+6}Professionalism{/size}{/b}\nact responsibly with the interests of the larger community in mind, and are able to learn from their mistakes."
            e "{b}{size=+6}Teamwork{/size}{/b}\nHendrix students build and maintain collaborative relationships to work effectively toward common goals. They appreciate diverse viewpoints & understand the importance of shared responsibilities."
            e "{b}{size=+6}Technology{/size}{/b}\nHendrix students understand and leverage technologies ethically to enhance efficiencies, complete tasks, and accomplish goals."
            hide eileenTalk
            show eileenSmile
            e "I hope you found these helpful!"
            hide eileenSmile
            jump career
        "I'm not sure what to do next, what do you suggest?":
            show eileenTalk
            hide eileen
            e "Being unsure is part of the college experience, that's why we're here to help!"
            e "If you are struggling with what major in or what job you want in the future. You can find more info {a=https://www.hendrix.edu/career/focus2/}here!{/a}"
            e "If you are looking for potential jobs, we have lots of recources on creating resumes and where to look for jobs, such as Hire Hendrix!"
            jump career
        "Leave":
            hide eileen
            hide eileenTalk
            show eileenSmile
            e "Thanks for visiting! If you have anymore questions or want more information, please visit {a=https://www.hendrix.edu/career/}this site!{/a}"
    hide eileen
    hide eileenTalk
    hide eileenSmile
    return


label welcomecenter:
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
    if curchpt == 1:
        jump Y1_C1_WC

    jump welcomecenterHelper

label welcomecenterHelper:
    "I should see whats around here, being new and all..."
    if curchpt == 1:
        jump Y1_C1_WC
    if curchpt == 2:
        jump Y1_C2_WC
    if curchpt == 3:
        jump Y2_C1_WC
    "{i}Obtained Leadership{/i}"
    show confettiLeft
    show confettiRight
    $ leadership = True
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
    "Welcome to Hendrix!"
    "You just got moved into your dorm room in Couch Hall."
    # I said Couch since it is not gender-exclusive. However, we can let the players choose later on if we want.
    "Your roommate isn't here yet, but hey that just means that you get the first pick on everything!"

    # We can add randomization here to where some people will get there first and some will get there last.

    # Once you encounter the roommat
    show charlie at left
    $ lefts = False
    r "Hey! I'm your roommate _**#(@)$)@#()**_ what's your name?"

    call charmaker

    r "Alright [p], nice to meet ya."

    "Wait what did they just say their name was.... did it say it on the door? I don't remember.. I'll just call them [r]."

    menu:
        "Look at the door for their name.":
            jump Y1_S1_C1
        "Figure it out later, they might notice.":
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
    $ pro = renpy.input(_("What are your preffered pronouns?"))
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
    if visited < allowed:
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
            e "Please click the next location you would like to visit."

        call map from _call_map_8
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

        "{i}Updated resume now available{/i}"
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

label hdxtoday:
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
