label Y2_S3_C0_CareerTermYorNo:
    $ curchpt = 5
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False

    scene sltcBackground

    "You get an email about 'Career Term' coming up."
    # Might Include more Dialogue at a later date, perhaps dialogue with friends about if you should do Career Term or not?
    "It seems like a good opportunity, but it means you have less free time for a little bit..."

    menu:
        "Would you like to sign up for it?"
        "Yes":
            jump Y2_S3_C1_CTYes

        "No":
            jump Y2_S3_C1_CTNo

label Y2_S3_C1_CTNo:

    "Ehh, it probably isn't worth losing some of your Winter Break."

    "..."

    "After Career Term ends your friends are talking about how good it was and make you feel a little bad for not going."

    $ allowed = allowed + 1
    # call resume
    # call hdxtoday
    # call map
    jump gameOver

label Y2_S3_C1_CTYes:

    $ dev += 15
    $ equity += 5
    $ leadership += 15
    $ proffesional += 15
    $ tech += 5

    "Some time passes and Career Term occurs."

    "Workshops cover topics such as résumé writing and job interview skills, graduate school planning and preparations,"
    "how to find an internship, professional dress and etiquette, networking and personal branding, and professional communication."
    "Hendrix alumni share their professional experiences, answer students' career questions,"
    "and offer students important insight on networking and making connections in the professional world."
    "It was a really good experience! You learned a lot!"

    "During one of your small group workshops, you get into a conversation with one of the speakers."
    "They interest you and might be able to help you as a connection on your new LinkedIn account!"

    menu:
        "Do you connect with them on LinkedIn?"
        "Yes":
            jump Y2_S3_C2_CTConnect
        "No":
            jump Y2_S3_C2_CTDontConnect

label Y2_S3_C2_CTConnect:

    $ communication += 15

    "There is no harm in connecting with people! Only good things could come from it."

    "Career Term continues without a hitch and you get a lot of new skills to carry on to your career."

    $ allowed = allowed + 3
    # call resume
    # call hdxtoday
    # call map
    jump gameOver

label Y2_S3_C2_CTDontConnect:

    "You don't know this person, so why should you connect with them on LinkedIn?"

    "Anyways, Career Term continues and you make the most out of it."

    "You get a lot of new skills to carry on to your career."

    $ allowed = allowed + 2
    # call resume
    # call hdxtoday
    # call map
    jump gameOver
