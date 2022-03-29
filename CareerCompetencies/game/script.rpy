# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen", color="#F5822A", what_color="#F8B55D")
define b = Character("Bob", color="#93143BFF", what_color="#C6476E")
define guy = Character("Guy", color="#990000", what_color="#CC6666")
define r = Character("Roomie", color="#3F888F", what_color="#6FBBBF")
define p = Character("You")
define x = Character("Company X recruiter", color="#990000", what_color="#CC3333")
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


define bbrain = "CompIcons/Black/Black Brain.png"
define gbrain = "CompIcons/Grey/Grey Brain.png"
define obrain = "CompIcons/Orange/Orange Brain.png"






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
    $ name = renpy.input(_("What's your name?"))

    $ name = name.strip() or __("No Name")
    $ p = Character(name, color="#B8B799", what_color="#EBEACC")


    # Competency booleans
    $ dev = True
    $ communication = True
    $ thinking = True
    $ equity = True
    $ leadership = True
    $ proffesional = True
    $ teamwork = True
    $ tech = True

    $ lefts = False
    $ ups = False
    # begin is main 'Go To' scene
    jump begin



label begin:
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide screen resumeToggle
    scene p


    show eileen at right
    $ lefts = True

    # These display lines of dialogue.


    menu:
        "Hi [name]! Where would you like to go?"
        "Chapter 1":
            play sound "audio/click.mp3"
            $ lefts = False
            jump welcome
        "Chapter 2":
            play sound "audio/click.mp3"
            $ lefts = False
            jump Y1_S2_C1
        "Quit":
            play sound "audio/click.mp3"
            menu:
                "Do you want to quit?"
                "Yes":
                    play sound "audio/click.mp3"
                    jump quit
                "No":
                    play sound "audio/click.mp3"
                    jump begin


    return

label library:
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide eileen with dissolve
    scene libraryBackground
    jump libraryHelper

label libraryHelper:
    show confettiLeft
    show confettiRight
    show confettiLeftB
    show confettiRightB
    "Thanks for visiting, You got teamwork as a test!"

    $ teamwork = True
    return


label sltc:
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    scene sltcBackground
    show eileenTalk
    e "This is where you can find tons of helpful student recources, some great food, and a nice place to hang out!"
    jump sltcHelper

label mills:
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    scene p
    show eileen at left
    e "We are at Mills!"
    hide eileen
    return


label sltcHelper:
    hide eileenTalk
    show eileen at left
    menu:
        "Where would you like to visit?"
        "Common area":
            e "Come back soon, this is currently being worked on!"
            jump sltcHelper
        "Odyssey Office":

            e "Sorry, this is in development too!"
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
    $ visited = visited + 1
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide eileen
    hide pecanCourtBackground
    scene welcomeCenterBackground
    jump welcomecenterHelper

label welcomecenterHelper:
    "I should see whats around here, being new and all..."

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

    # [name] = *Enter your name*
    p "[p]"

    r "Alright [p], nice to meet ya."

    "Wait what did they just say their name was.... did it say it on the door? I don't remember.. I'll just call them [r]."

    menu:
        "Look at the door for their name.":
            jump Y1_S1_C1
        "Figure it out later, they might notice.":
            jump Y1_S1_C2


label map:
    if visited < allowed:
        hide screen resumeToggle
        hide screen resumeUI
        hide screen ResumeText
        hide screen mapUI
        hide screen hdxtodayb
        show screen MapUI
        show eileenTalk at right with dissolve

        if not seen_map:
            e "This is an interactive map of Hendrix!"
            e "Clicking on a building will allow you to visit that location, provided you are allowed to."
            e "You may only select buildings that are in full color."
            $ map_interact = True
            $ seen_map = True
        else:
            e "Please click the next location you would like to visit."

        call map

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
    if visited<allowed:
        show screen hdxtodayb
        # call hdxtodaytexthelper

        $ temp = lefts
        $ lefts = False
        $ ups = True
        menu:
            "Continue?":
                hide screen hdxtodayb
                $ lefts = temp
                $ ups = False

label quit:
    return
