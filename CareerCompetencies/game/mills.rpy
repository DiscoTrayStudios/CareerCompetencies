
label Y1_C1_M:
    scene millsBackground
    "You walk into Mills and you see that not a lot is going on."
    "As you wander around you make your way into the Mills library."
    scene millsLibrary
    "You really enjoy how it looks in here and decide to sit down."
    "You wind up studying and getting lots of work done over the next couple hours!"
    "{i}I'm really glad I came here. This might be my new homework spot! {/i}"
    $ dev += 5
    $ thinking += 5
    return


label Y1_C2_M:
    scene millsBackground
    $ centers = True
    menu:
        "Which field are you interested in learning about?"
        "Humanities":
            jump Y1_C2_M1

        "Social Sciences":
            jump Y1_C2_M2
    jump Y1_C2_M



label Y1_C2_M1:
    scene millsBackground
    show maslow
    m "Hello there, I am Dr. Maslow, are you interested in the field of humanities?"
    p "Yes! I'm not completely sure but I would love to hear some more of what it's like at Hendrix."
    m "Of course! A few of our majors include art, multiple language majors, philosophy, and theatre."
    m "We have a great community at Hendrix! We often have showcases, plays, and ensembles for our performative majors."
    m "There are also great multiple weekly discussions about current events, moral ambiguities, and different stances on popular suggestions!"
    m "Our language departments are very immersive in community, and have weekly meals along with even learning houses that help bring students even closer with their interests!"
    m "There is certainly something for everyone here, and I am sure you would enjoy learning more."
    m "Be on the lookout for professors who would like extra help, are giving talks, or doing research!"
    p "Okay, thank you so much!"
    hide maslow
    $ dev += 5
    $ thinking += 5
    return


label Y1_C2_M2:
    scene millsBackground
    show orozco
    o "Hey there, I'm Dr. Orozco. Are you here to learn more about the social sciences field at Hendrix?"
    p "Yeah! I'm very interested in it, but unsure of what all it entails."
    o "Well here at Hendrix, we have lots of different ways to explore the human condition."
    o "A few of our majors include, but are not limited to, sociology, anthropology, psychology, economics, and politics."
    o "With a liberal arts education, we can expand the bounds of typical classes and look into some specifics with greater detail through multiple courses."
    o "We have had great success with graduating students both finding work in their desired fields, or moving on to higher education such as obtaining a law degree."
    o "If you are interested in going down this path, you should make sure to keep an ear to the ground about any professors wanting extra help or wanting researchers."
    o "There are always opportunities coming and going, so make sure to pay attention!"
    p "You got it, thank you!"
    hide orozco
    $ dev += 5
    $ thinking += 5
    return


label Y1_C3_M:
    scene millsBackground
    "You goto Mills and see that Cats is playing in Cabe Theater."
    "{i}Huh.. the Cats musical at Hendrix? I'm interested.. {/i}"
    scene cabe
    "You sit down and the musical begins."
    "!!"
    "{i}What the.....{/i}"
    "As the musical starts, you see that this is not CATS at Hendrix,,, this is the Hendrix Cats."
    "People are dressed up as the Hendrix Cats."
    "The show goes on with everything being mostly the same besides the characters."
    "{i}Honestly? That wasn't too bad{/i}"
    return

label Y2_C1_M:
    scene millsBackground
    ## "This is where a club interaction will take place once we get it implemented!"
    "As you approach Mills you see a big group of people. It looks like some event is happening."
    "{i}I wonder what's happening here.{/i}"
    "You notice a sign that says 'D&D Club Dice Tray Making Event'"
    "{i}Oh I see.. I'll check it out but I won't stay for long.{/i}"
    "Participation is key! You may not be in this club, but they were happy to let you be there and you ended up doing some arts and crafts."
    "Thanks for visiting Mills!"
    $ dev += 5
    $ thinking += 5
    return

label Y2_C2_M:
    scene millsBackground
    "While approach Mills you see that there are quite a few people in the Mills Library."
    scene millsLibrary
    "You enter into the Mills Library to see people working on homework."
    "There's an empty table that will give you plenty of space to work on your homework."
    "{i}I think this will work perfectly.{/i}"
    "You spend a lot of time working on your homework and occasionally talk to the people around you."
    $ dev += 5
    $ thinking += 5
    return

label Y2_C3_M:
    scene millsBackground
    "While trying to enter Mills you discover the doors are locked."
    menu:
        "Do you..."
        "Knock":
            "{i}Knock Knock.{/i}"
            "You see someone run to the door and hold it open for you"
            show blakely
            bl"You're lucky I was still in here."
            p"Yeah haha.. I guess I got here a little late."
            bl"Next time if you want in get here {b}before{/b} it gets dark, or just go to Snoddy."
            p"Thanks for the advice.."
            hide blakely
            scene millsLibrary
            "You enter the Mills Library and work on your homeowork as Blakely leaves."
            "After a while of doing your work you decide it's time to go back home."
        "Leave":
            "Oh well, I guess no Mills today..."
    $ dev += 5
    $ thinking += 5
    return