label Y1_S1_C1:
    $ r = Character("Charlie", color="#3F888F", what_color="#6FBBBF")
    hide charlie
    "You decide to look at the door."
    "Their name is [r]! Good to know."
    "They kind of give you a weird look as you just open the door, look at it, then close it again..."

    "Then you notice that [r] started setting up on the side of the dorm you wanted. You had plans!"
    "You were gonna have more outlets, control of the window and AC, and the closet in the arguably better space."
    show charlie at left
    menu:
        "Ask for the space and explain your plans with it.":
            jump Y1_S1_C3_1
        "Just live with it, you snooze you lose.":
            jump Y1_S1_C4
        "Let's get to know them first.":
            jump Y1_S1_C5

label Y1_S1_C2:
    ## You decide to figure it out later
    hide charlie
    "For now you can just not say any name or call them [r]."
    "Very casual. A perfect solution. Nothing could go wrong."

    "Then you notice that the roomie started setting up on the side of the dorm you wanted. You had plans!"
    "You were gonna have more outlets, control of the window and AC, and the closet in the arguably better space."
    show charlie at left
    menu:
        "Ask for the space and explain your plans with it.":
            jump Y1_S1_C3_2
        "Just live with it, you snooze you lose.":
            jump Y1_S1_C4

label Y1_S1_C3_1:
    ## You ask for the space.
    "You need it for your plans! it will be best for the both of you."

    p "Hey [r], can we switch spots.. I really want to be able to set up that space with my TV and other things cause it has more outlets and I see you don't have as many electronics.."

    show charlie
    r "I don't know, I like this spot.. What will I get out of trading spots with you?"

    p "You will get to play with me on my console."

    r "So if I don't I won't be able to??"

    p "If you don't I might not have enough outlets to even hook it up."

    r "Ugh fine."

    hide charlie
    "[r] reluctantly gives you the spot you want, however, you don't think they are happy about this and it may affect your future"
    $ allowed = 1
    $ teamwork -= 5
    $ communication -= 3
    call resume from _call_resume
    call hdxtoday from _call_hdxtoday
    call map from _call_map
    jump Y1_S2_C1

label Y1_S1_C3_2:
    ## You ask for the space.
    "You need it for your plans! it will be best for the both of you."

    p "Hey [r], can we switch spots.. I really want to be able to set up that space with my TV and other things cause it has more outlets and I see you don't have as many electronics.."

    show charlie
    "They give you a weird look. Was it because you called them [r] instead of their name?"

    r "Um no I like this spot, and I chose it first."

    p "Come onnnn."

    r "No."

    hide charlie
    "{i}You are kind of disappointed and you may have made a bad first impression with your roomie...{/i}"

    $ allowed = 1
    $ communication -= 5
    $ teamwork -= 3
    call resume from _call_resume_1
    call hdxtoday from _call_hdxtoday_1
    call map from _call_map_1
    jump Y1_S2_C1

label Y1_S1_C4:
    ## You snooze you lose
    "You decide to let it go, but also don't talk to them for the rest of the day."

    "{i}You both set up your stuff in silence and keep to yourselves{/i}"

    $ allowed = 2
    $ communication -= 3
    hide charlie
    call resume from _call_resume_2
    call hdxtoday from _call_hdxtoday_2
    call map from _call_map_2
    jump Y1_S2_C1

label Y1_S1_C5:
    ## Let's get to know each other!
    p "So [r], what do you like to do for fun?"

    show charlie at left
    $ lefts = False
    r "I like to watch movies and play games."

    p "No way me too! That's why I brought all of this stuff. Maybe we can do stuff together sometime!"

    r "That would be awesome!"

    menu:
        "Ask for the space now.":
            jump Y1_S1_C6
        "We don't need to trade.":
            jump Y1_S1_C7

label Y1_S1_C6:
    ## Ask to Trade
    p "Speaking of games and movies, I was thinking of having my setup over there because there are more outlets, and we could have a better view of the screen. Would that be okay [r]?"

    show charlie
    r "That would be great actually, yeah I guess I can move to the other spot."

    p "Sweet, we are gonna have so much fun."

    "You and Charlie talk for a while longer and you think about how they might be a good first friend"
    $ allowed = 3
    $ communication += 5
    $ teamwork += 3
    hide charlie
    call resume from _call_resume_3
    call hdxtoday from _call_hdxtoday_3
    call map from _call_map_3
    jump Y1_S2_C1

label Y1_S1_C7:
    ## You are content
    show charlie
    p "I can't wait to get everything set up. Where are you from......."

    "You and Charlie talk for while and become what might just be good friends for the next month"

    $ allowed = 3
    $ communication += 5
    $ teamwork += 3
    $ dev += 3
    hide charlie
    call resume from _call_resume_4
    call hdxtoday from _call_hdxtoday_4
    call map from _call_map_4
    jump Y1_S2_C1
