# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define john = Character("john")
define guy = Character("Guy", color="#990000")
image eileen = "Characters/Eileen.png"
image john = "Characters/John.png"
image libraryBackground = "Backgrounds/library.jpg"
image pecanCourtBackground = "Backgrounds/p.jpg"
image welcomeCenterBackground = "Backgrounds/welcomeCenter.jpg"
image sltcBackground = "Backgrounds/sltc.jpg"


#

# The game starts here.

label start:
    $ name = renpy.input(_("What's your name?"))

    $ name = name.strip() or __("No Name")

    $ dev = False
    $ communication = False
    $ thinking = False
    $ equity = False
    $ leadership = False
    $ proffesional = False
    $ teamwork = False
    $ tech = False
    jump begin

label begin:
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    show screen mapUI
    show screen resumeToggle
    scene p


    show eileen

    # These display lines of dialogue.
    e "Press once to get options."

    menu:
        "Show Career and Self-Development on resume?"
        "Sure":
            $ dev = True
            jump begin
        "Nah":
            $ dev = False
            jump begin
        "Quit":
            menu:
                "Do you want to go to quit?"
                "Yes":
                    jump quit
                "No":
                    jump begin

    return

label library:
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide eileen with dissolve

    scene libraryBackground

    show john at right with dissolve
    john "Thanks for visiting, You got teamwork!"
    $ teamwork = True


    jump begin

label sltc:
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    scene sltcBackground
    show eileen
    e "This is where you can find tons of helpful student recources, some great food, and a nice place to hang out!"

    e "Activating Technology!"
    $ tech = True
    jump begin

label welcomecenter:
    hide screen MapUI
    hide screen ResumeUI
    hide screen ResumeText
    hide eileen
    hide pecanCourtBackground
    scene welcomeCenterBackground
    "I should see whats around here, being new and all..."

    "{i}Obtained Leadership{/i}"
    $ leadership = True
    jump begin




label quit:
    return
