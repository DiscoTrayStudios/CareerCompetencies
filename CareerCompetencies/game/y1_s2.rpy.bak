label Y1_S2_C1:
    $ curchpt = 2
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False

    scene sltcLobby
    show bob at left with dissolve
    $ lefts = False
    b "Welcome to the Career and Internship Fair!"
    b "Feel free to walk around and look at the organizations here. We are also going to have a presentation on professionalism if you are interested!"
    menu:
        "What would you like to do?"
        "Look around":
            jump Y1_S2_C2
        "Go to presentation":
            jump Y1_S2_C3


label Y1_S2_C2:
    p "I think I am going to see what's around first."

    b "Sounds good, I'm going to go to the presentation."

    hide bob with dissolve

    "You walk around and see what the fair has to offer. It seems to have some pretty cool companies but you are only interested in looking."

    "That was the case, until you saw Company X. It had everything you hoped for out of a job and you couldn't believe they were looking for someone here. Someone like you!"

    "You walk up to their booth."

    p "Uh, hi there, are you still looking to hire someone?"

    x "Yes! We are looking to hire graduates for full time positions and undergraduates for internship programs. Are you interested?"

    p "Very! What do I need to do to apply?"

    x "Well I see you have a resume in hand, do you mind if I look over it real fast?"

    p "Have at it!"

    "You hand her the resume. She spends a minute reading over it before handing it back"

    x "You've done some great work so far, but I'm afraid our company is looking for applicants with a little more experience."

    p "I understand, is there anything I can specifically do to help me out?"

    "She points to a big sign in the room that says 'Culteral Competencies'"

    x "Those eight concepts are very important to our business. Once you get a good understanding of them, and gain a bit more experience, we would love to have you on the team."

    x "I would reccomend talking to Career Services. They put this fair together and can help tremendously. I believe you can find them in the SLTC."

    p "Okay, thank you for your time!"

    $ communication = True
    show confettiLeft
    show confettiRight
    "{i}Communication achieved!"

    "A little dissapointed but filled with motivation, you decide to work hard to reach your goal of working with that team."
    $ allowed = allowed + 2
    hide bob with dissolve
    call resume
    call hdxtoday
    call map

    jump begin


label Y1_S2_C3:
    p "I think I'll go to the presentation."

    b "Mind if I join? I planned on doing the same thing."

    "Bob walks with you to the talk, also interested in what there is to learn"

    b "So, is this your first time at the Career and Internship Fair, [name]?"

    p "Yeah it is, I'm just a freshman so this is my first one."

    b "Hey way to get started early! I wish I had started coming to these my freshman year. I had no idea you could learn so much from them."

    p "I'm excited. This should be fun!"

    "You both enter the room and take a seat. Somone walks on stage and begins to talk about personal accountability."

    "The talk develops and you become encapsulated by what the speaker is saying. You learn a lot throughout this talk and walk out feeling a higher sense of responsibility."

    $ proffesional = True
    show confettiLeft
    show confettiRight
    "{i}Professionalism achieved!"

    b "That was great! I really didn't expect to get that much out of it."

    p "No me neither, I'm glad we did this!"

    "You walk around the career fair a bit more, but things are winding down and you decide to call it a night."
    $ allowed = allowed + 2
    hide bob with dissolve
    call resume
    call hdxtoday
    call map
    jump begin

label Y1_S2_C4:
    b "I agree!"
    call resume
    call map
    jump begin
