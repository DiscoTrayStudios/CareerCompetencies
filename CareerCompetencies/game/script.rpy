# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define john = Character("john")
define guy = Character("Guy", color="#990000")
define Roomie = Character("Roomie")
define Charlie = Character("Charlie")
define Player = Character("You")
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
        "Test"
            jump welcome
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




label welcome:
    # Welcome to Hendrix!
    "Welcome to Hendrix!"
    "You just got moved into your dorm room in Couch Hall." 
    # I said Couch since it is not gender-exclusive. However, we can let the players choose later on if we want.
    "Your roommate isn't here yet, but hey that just means that you get the first pick on everything!"
    # We can add randomization here to where some people will get there first and some will get there last. 

    # Once you encounter the roommate
    Roomie "Hey! I'm your roommate _**#(@)$)@#()**_ what's your name?"
    
    # [name] = *Enter your name*
    Player "name"
    
    Roomie "Alright name, nice to meet ya."

    "Wait what did they just say their name was.... did it say it on the door? I don't remember.. I'll just call them Roomie."

    menu: 
        "Look at the door for their name.":
            jump Y1_S1_C1
        "Figure it out later, they might notice.":
            jump Y1_S1_C2

label Y1_S1_C1:
    "You decide to look at the door."
    "Their name is Charlie! Good to know."
    "They kind of give you a weird look as you just open the door, look at it, then close it again..."

    "Then you notice that Charlie started setting up on the side of the dorm you wanted. You had plans!" 
    "You were gonna have more outlets, control of the window and AC, and the closet in the arguably better space." 

    menu:
        "Ask for the space and explain your plans with it.":
            jump Y1_S1_C3_1
        "Just live with it, you snooze you lose.":
            jump Y1_S1_C4
        "Let's get to know them first.":
            jump Y1_S1_C5

label Y1_S1_C2:
    ## You decide to figure it out later
    "For now you can just not say any name or call them roomie."
    "Very casual. A perfect solution. Nothing could go wrong."

    "Then you notice that the roomie started setting up on the side of the dorm you wanted. You had plans!"
    "You were gonna have more outlets, control of the window and AC, and the closet in the arguably better space." 

    menu:
        "Ask for the space and explain your plans with it.":
            jump Y1_S1_C3_2
        "Just live with it, you snooze you lose.":
            jump Y1_S1_C4

label Y1_S1_C3_1:
    ## You ask for the space.
    "You need it for your plans! it will be best for the both of you."

    Player "Hey Charlie, can we switch spots.. I really want to be able to set up that space with my TV and other things cause it has more outlets and I see you don't have as many electronics.."

    Charlie "I don't know, I like this spot.. What will I get out of trading spots with you?"

    Player "You will get to play with me on my console."

    Charlie "So if I don't I won't be able to??"

    Player "If you don't I might not have enough outlets to even hook it up."

    Charlie "Ugh fine." 

    "_Charlie reluctantly gives you the spot you want, however, you don't think they are happy about this and it may affect your future_"

    jump start

label Y1_S1_C3_2:
    ## You ask for the space.
    "You need it for your plans! it will be best for the both of you."
    Player "Hey Roomie, can we switch spots.. I really want to be able to set up that space with my TV and other things cause it has more outlets and I see you don't have as many electronics.."

    "They give you a weird look. Was it because you called them Roomie instead of their name?
    Roomie Um no I like this spot, and I chose it first."

    Player "Come onnnn."

    Roomie "No."

    "_You are kind of disappointed and you may have made a bad first impression with your roomie..._"
    
    jump start

label Y1_S1_C4:
    ## You snooze you lose
    "You decide to let it go, but also don't talk to them for the rest of the day."

    "_You both set up your stuff in silence and keep to yourselves_"
    
    jump start

label Y1_S1_C5:
    ## Let's get to know each other!
    Player "So [Charlie], what do you like to do for fun?"
    
    Charlie "I like to watch movies and play games."
    
    Player "No way me too! That's why I brought all of this stuff. Maybe we can do stuff together sometime!"
    
    Charlie "That would be awesome!"

    menu:
        "Ask for the space now.":
            jump Y1_S1_C6
        "We don't need to trade.":
            jump Y1_S1_C7

label Y1_S1_C6:
    ## Ask to Trade
    Player "Speaking of games and movies, I was thinking of having my setup over there because there are more outlets, and we could have a better view of the screen. Would that be okay [Charlie]?" 

    Charlie "That would be great actually, yeah I guess I can move to the other spot."

    Player "Sweet, we are gonna have so much fun." 

    "_You and Charlie talk for a while longer and you think about how they might be a good first friend_"
    
    jump start

label Y1_S1_C7:
    ## You are content

    Player "I can't wait to get everything set up. Where are you from......."

    "_You and Charlie talk for while and become what might just be good friends for the next month_"

label quit:
    return
