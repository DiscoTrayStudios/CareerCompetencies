



label Y1_C1_M:
    "{i}Doesn't look like much is going on here...{/i}"
    return


label Y1_C2_M:
    menu:
        "Which field are you interested in learning about?"
        "Humanities":
            jump Y1_C2_M1

        "Social Sciences":
            jump Y1_C2_M2
    jump Y1_C2_M



label Y1_C2_M1:
    m "Hello there, I am Dr. Maslow, are you interested in the field of humanites?"
    p "Yes! I'm not completely sure but I would love to hear some more of what it's like at Hendrix."
    m "Of course! A few of our majors include art, multiple languag majors, philosophy, and theatre."
    m "We have a great community at Hendrix! We often have showcases, plays, and ensembles for our performative majors."
    m "There are also great multiple weekly discussions about current events, moral ambiguities, and different stances on popular suggestions!"
    m "Our language departments are very immersive in community, and have weekly meals along with even learning houses that help bring students even closer with their interests!"
    m "There is certainly something for everyone here, and I am sure you would enjoy learning more."
    m "Be on the lookout for professors who would like extra help, are giving talks, or doing research!"
    p "Okay, thank you so much!"
    return


label Y1_C2_M2:
    o "Hey there, I'm Dr. Orozco. Are you hear to learn more about the social sciences field at Hendrix?"
    p "Yeah! I'm very interested in it, but unsure of what all it entails."
    o "Well here at Hendrix, we have lots of different ways to explore the human condition."
    o "A few of our majors include, but are not limited to, sociology, anthropology, psychology, economics, and politics."
    o "With a liberal arts education, we are able to expand the bounds of typical classes and look into some specifics with greater detail through multiple courses."
    o "We have had great success with graduating students both finding work in their desired fields, or moving on to higher education such as obtaining a law degree."
    o "If you are interested in going down this path, you should make sure to keep an ear to the ground about any professors wanting extra help or wanting researchers."
    o "There are always opportunities coming and going, so make sure to pay attention!"
    p "You got it, thank you!"
    return
