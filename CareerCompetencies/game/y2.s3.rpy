label Y2_S3_C0_CareerTermYorNo:
    $ curchpt = 6
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False
    $ didwhatnext = False

    scene sltcBackground
    # Lose dev and Comm
    "You get an email about 'Career Term' coming up."
    # Might Include more Dialogue at a later date, perhaps dialogue with friends about if you should do Career Term or not?
    "It seems like a good opportunity, but it means you have less free time for a little bit..."

    "It seems like a good opportunity, but it means you have less of a Winter Break..."
    $ centers = True
    menu:
        "Would you like to sign up for it?"
        "Yes":
            $ centers = False
            jump Y2_S3_C1_CTYes

        "No":
            $ centers = False
            jump Y2_S3_C1_CTNo

label Y2_S3_C1_CTNo:

    "Ehh, it probably isn't worth losing some of your Winter Break."

    "..."

    "After Career Term ends your friends are talking about how good it was and make you feel a little bad for not going."

    $ allowed = allowed + 1
    call resume from _call_resume_17
    call hdxtoday from _call_hdxtoday_21
    call map from _call_map_23
    jump summer

label Y2_S3_C1_CTYes:

    $ dev += 30
    $ equity += 10
    $ leadership += 30
    $ professional += 30
    $ tech += 10
    $ exhaustion += 1

    "Some time passes and Career Term occurs."
    scene careerterm
    "Workshops cover topics such as résumé writing and job interview skills, graduate school planning and preparations,"
    "how to find an internship, professional dress and etiquette, networking and personal branding, and professional communication."
    "Hendrix alumni share their professional experiences, and answer students' career questions,"
    "and offer students important insight on networking and making connections in the professional world."
    "It was a really good experience! You learned a lot!"

    "During one of your small group workshops, you get into a conversation with one of the speakers."
    "They interest you and might be able to help you as a connection on your new LinkedIn account!"
    $ centers = True
    menu:
        "Do you connect with them on LinkedIn?"
        "Yes":
            $ centers = False
            jump Y2_S3_C2_CTConnect
        "No":
            $ centers = False
            jump Y2_S3_C2_CTDontConnect

label Y2_S3_C2_CTConnect:

    $ communication += 30

    "There is no harm in connecting with people! Only good things could come from it."

    "Career Term continues without a hitch and you get a lot of new skills to carry on to your career."

    $ allowed = allowed + 3
    call exhausted from _call_exhausted_11
    call resume from _call_resume_18
    call hdxtoday from _call_hdxtoday_22
    call map from _call_map_24
    jump summer

label Y2_S3_C2_CTDontConnect:

    "You don't know this person, so why should you connect with them on LinkedIn?"

    "Anyways, Career Term continues and you make the most out of it."

    "You get a lot of new skills to carry on to your career."

    $ allowed = allowed + 2
    call exhausted from _call_exhausted_12
    call resume from _call_resume_19
    call hdxtoday from _call_hdxtoday_23
    call map from _call_map_25
    jump summer
