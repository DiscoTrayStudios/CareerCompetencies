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

    player "Hey Charlie, can we switch spots.. I really want to be able to set up that space with my TV and other things cause it has more outlets and I see you don't have as many electronics.."

    Charlie "I don't know, I like this spot.. What will I get out of trading spots with you?"

    player "You will get to play with me on my console."

    Charlie "So if I don't I won't be able to??"

    player "If you don't I might not have enough outlets to even hook it up."

    Charlie "Ugh fine."

    "_Charlie reluctantly gives you the spot you want, however, you don't think they are happy about this and it may affect your future_"
    $ allowed = 1
    call map
    jump Y1_S2_C1

label Y1_S1_C3_2:
    ## You ask for the space.
    "You need it for your plans! it will be best for the both of you."
    player "Hey Roomie, can we switch spots.. I really want to be able to set up that space with my TV and other things cause it has more outlets and I see you don't have as many electronics.."

    "They give you a weird look. Was it because you called them Roomie instead of their name?"
    Roomie "Um no I like this spot, and I chose it first."

    player "Come onnnn."

    Roomie "No."

    "{i}You are kind of disappointed and you may have made a bad first impression with your roomie...{/i}"

    $ allowed = 1

    call map
    jump Y1_S2_C1

label Y1_S1_C4:
    ## You snooze you lose
    "You decide to let it go, but also don't talk to them for the rest of the day."

    "{i}You both set up your stuff in silence and keep to yourselves{/i}"

    $ allowed = 2

    call map
    jump Y1_S2_C1

label Y1_S1_C5:
    ## Let's get to know each other!
    player "So [Charlie], what do you like to do for fun?"

    Charlie "I like to watch movies and play games."

    player "No way me too! That's why I brought all of this stuff. Maybe we can do stuff together sometime!"

    Charlie "That would be awesome!"

    menu:
        "Ask for the space now.":
            jump Y1_S1_C6
        "We don't need to trade.":
            jump Y1_S1_C7

label Y1_S1_C6:
    ## Ask to Trade
    player "Speaking of games and movies, I was thinking of having my setup over there because there are more outlets, and we could have a better view of the screen. Would that be okay [Charlie]?"

    Charlie "That would be great actually, yeah I guess I can move to the other spot."

    player "Sweet, we are gonna have so much fun."

    "_You and Charlie talk for a while longer and you think about how they might be a good first friend_"
    $ allowed = 3
    call map
    jump Y1_S2_C1

label Y1_S1_C7:
    ## You are content

    player "I can't wait to get everything set up. Where are you from......."

    "_You and Charlie talk for while and become what might just be good friends for the next month_"

    $ allowed = 3

    call map
    jump Y1_S2_C1
