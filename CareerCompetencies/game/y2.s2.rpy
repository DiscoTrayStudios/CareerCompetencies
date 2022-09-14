label Y2_S2_C0_ClubEnter:
    $ curchpt = 4
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False

    $ kittyvisit = False
    $ socovisit = False
    $ senatevisit = False
    $ khdxvisit = False

    $ seenclubintro = False

    $ joinedany = False
    $ joinedkitty = False
    $ joinedsoco = False
    $ joinedkhdx = False

    scene sltcBackground


    "Some more time passes, and as you are walking to the SLTC to get some lunch when you see a large crowd in front."
    "You're intrigued, so you start heading that way. Once you get closer, you start to remember from your email that today is the Club Fair!"
    $ centers = True
    menu:
        "Would you like to check it out?"
        "Yes":
            $ centers = False
            jump Y2_S2_C1_Stay

        "No":
            $ centers = False
            jump Y2_S2_C1_Leave

label Y2_S2_C1_Leave:
    "While it seems like some fun, you decide that you don't have time for it."
    "Besides, lunch is definitely more important than some club."
    "You head in and leave the fair for another day"

    $ allowed = allowed + 2
    call resume from _call_resume_8
    call hdxtoday from _call_hdxtoday_7
    call map from _call_map_9
    jump Y2_S3_C0_CareerTermYorNo


label Y2_S2_C1_Stay:
    $ social += 2
    if not seenclubintro:
        "Why not, you're an adventurous person."
        "You make your way around the fair and while some of the clubs are seeming like fun, you still are not sure."
        "{i}I don't know if I have time for this kind of thing... maybe if I went with one of the bigger clubs, they wouldn't have to rely on me so much, just in case?"
        "You start to walk around  a bit to gauge what the larger-looking clubs are all about."
    $ seenclubintro = True
    $ centers = True
    menu:
        "Where would you like to go?"
        "Campus Kitty":
            if not kittyvisit:
                $ centers = False
                jump Y2_S2_C2_CampusKitty
            else:
                $renpy.notify("You already visited them...")
                pause 1.3
                $renpy.notify("You can always scroll back to an earlier point!")
                jump Y2_S2_C1_Stay
        "SoCo":
            if not socovisit:
                $ centers = False
                jump Y2_S2_C2_SOCO

            else:
                $renpy.notify("You already visited them...")
                pause 1.3
                $renpy.notify("You can always scroll back to an earlier point!")
                jump Y2_S2_C1_Stay
        "Student Senate":
            if not senatevisit:
                $ centers = False
                jump Y2_S2_C2_StudentSenate
            else:
                $renpy.notify("You already visited them...")
                pause 1.3
                $renpy.notify("You can always scroll back to an earlier point!")
                jump Y2_S2_C1_Stay
        "KHDX":
            if not khdxvisit:
                $ centers = False
                jump Y2_S2_C2_KHDX
            else:
                $renpy.notify("You already visited them...")
                pause 1.3
                $renpy.notify("You can always scroll back to an earlier point!")
                jump Y2_S2_C1_Stay
        "Leave the fair":
            $ centers = False
            jump Y2_S2_C2_LeaveClubFair



label Y2_S2_C2_CampusKitty:
    $ kittyvisit = True
    show joey at left with dissolve
    j "Hi, there! We're Campus Kitty, a non-profit organization that raises money for local charities!"
    j "We plan and implement a week-long series of charity fundraising events geared toward the entire campus every spring."
    j "Campus Kitty Week is one of the most popular times of the year at Hendrix, and culminates in the most anticipated night of the year--the Miss Hendrix Pageant."
    j "Last year, Campus Kitty raised more than $38,000 in money and goods, providing for 10 local charities."
    j "Our goal is to raise as much money and have as much fun as possible while doing so!"

    menu:
        j "Are you interested in joining?"
        "Yes":
            jump Y2_S2_C3_KittyYes

        "No":
            jump Y2_S2_C3_KittyNo

label Y2_S2_C3_KittyYes:
    $ social += 2
    $ equity += 15
    $ exhaustion += 1
    $ joinedany = True
    $ joinedkitty = True
    j "Awesome! We're glad to have you! We usually have our meetings in the SLTC, but make sure to keep an eye out for updates in HendrixToday to see if we have a meeting scheduled!"
    j "They aren't required, but members who actively participate usually find themselves in  {color=#FFFF33}Leadership{/color} roles!"
    p "Sounds good, thank you, and have a good day!"
    hide joey with dissolve
    jump Y2_S2_C1_Stay


label Y2_S2_C3_KittyNo:
    j "Well, that's okay! Make sure to still come to our events and check out the other clubs!"
    hide joey with dissolve
    "You head out to keep roaming the club fair."

    jump Y2_S2_C1_Stay


label Y2_S2_C2_SOCO:
    $ socovisit = True
    show blakely at left with dissolve
    bl "Hey, we're the Social Committee, or SOCO for short."
    bl "We are responsible for hosting creative, social events on campus.  These range from themed parties to recreational events and film screenings."
    bl "We help bind the Hendrix community together and help create some of the biggest events of the year, such as our Formal Dance or SoCo 54."
    menu:
        bl "Are you interested in joining?"
        "Yes":
            jump Y2_S2_C3_SOCOYes

        "No":
            jump Y2_S2_C3_SOCONo


label Y2_S2_C3_SOCONo:
    p "Thank you, but I don't think this club would be for me."
    bl "That's cool! Make sure to come to our events though, they are literally the best things to happen on this campus"
    bl "Although I am a bit biased."
    hide blakely with dissolve
    "You head out to keep roaming the club fair."
    jump Y2_S2_C1_Stay


label Y2_S2_C3_SOCOYes:
    $ social += 2
    $ equity += 15
    $ exhaustion += 1
    $ joinedany = True
    $ joinedsoco = True
    bl "Sweet! I hope you enjoy your time with us!  We usually have our meetings in Mills, but make sure to keep an eye out for updates in HendrixToday to see if we have a meeting scheduled!"
    bl "They aren't required, but members who actively participate usually find themselves in  {color=#FFFF33}Leadership{/color} roles!"
    p "Sounds good, thank you!"
    hide blakely with dissolve
    jump Y2_S2_C1_Stay
label Y2_S2_C2_StudentSenate:
    $ senatevisit = True
    show niraj at left with dissolve
    n "Hey there! We are the Hendrix College Student Senate, your student body government!"
    n "We are a diverse body of students focused on improving the Hendrix community and on representing YOU."
    n "We're here to help you make Hendrix into the best place it can possibly be."
    n "Our mission is to give direction and voice to student concerns, and provide a framework for a number of activities and services for students."
    n "We also help to fund campus events such as SoCo 54, Toga, concerts, and more."

    menu:
        n "Is this something you may be interested in?"
        "Yes":
            jump Y2_S2_C3_SenateYes

        "No":
            jump Y2_S2_C3_SenateNo

label Y2_S2_C3_SenateYes:
    $ social += 2
    $ exhaustion += 1
    n "Okay, so since this is the official student body government, it works a bit differently than the regular clubs. We're here now just to make people aware of it."
    n "Essentially, all positions are specified by a certain group, so for instance to be the Couch Senator, you must live in Couch."
    n "Once it is time to prepare for elections, we will have interest meetings to make you aware of everything it will include."
    n "After that, you can start campaigning and if you are voted in by your peers, you will attend weekly Tuesday meetings and join one of the sub-committees."
    n "We will present and discuss concerns of the student body and then you will inform your constituents of what is going on."
    n "Once this process starts, you will be seeing it in HendrixToday, so make sure to always read it."
    p "Sounds good, thank you, and have a good day!"
    hide niraj with dissolve
    jump Y2_S2_C1_Stay

label Y2_S2_C3_SenateNo:
    n "Sounds good, thank you for stopping by, and don't forget that we are always here to support you!"
    hide niraj with dissolve
    "You head out to keep roaming the club fair."
    jump Y2_S2_C1_Stay



label Y2_S2_C2_KHDX:
    show zach at left with dissolve
    $ khdxvisit = True
    z "What's up! We are KHDX-FM 93.1, the Hendrix College student-run radio station!"
    z "Our mission is to provide unique programming to campus, the city of Conway, and the globe through the FM airwaves, digital streaming, and our website."
    z "We accomplish this goal by allowing students to create and broadcast content with which they are deeply connected."
    z "Our passions manifest in the form of recorded and live music, spoken word, news, sports, and educational programming."
    z "In DJ and executive staff positions, students get a chance to engage in developing content, organizing events, and managing/participating in a volunteer-based organization that impacts the student experience on Hendrix campus."
    z "The result is a station that represents the dynamic diversity of our student body."
    z "We also book musical events and have even had artists at the school such as Lizzo, Black Bear, and Iann Dior!"

    menu:
        z "Would you be interested in joining?"
        "Yes":
            jump Y2_S2_C3_KHDXYes

        "No":
            jump Y2_S2_C3_KHDXNo


label Y2_S2_C3_KHDXYes:
    $ social += 1
    $ equity += 15
    $ exhaustion += 1
    $ joinedany = True
    $ joinedkhdx = True
    z "Sweet, you're going to have a rockin time here! Corny, I know, but I love those jokes. We usually have our meetings in the SLTC, but make sure to keep an eye out for updates in HendrixToday to see if we have a meeting scheduled!"
    z "They aren't required, but members who actively participate usually find themselves in  {color=#FFFF33}Leadership{/color} roles!"
    "Sounds good, thank you, and have a good day!"
    hide zach with dissolve
    jump Y2_S2_C1_Stay


label Y2_S2_C3_KHDXNo:
    p "Thank you, but I don't think this is quite the club for me."
    z "Sounds good! Well, don't forget to tune in or let us know if you have any ideas for what to broadcast!"
    hide zach with dissolve
    "You head out to keep roaming the club fair."

    jump Y2_S2_C1_Stay



label Y2_S2_C2_LeaveClubFair:
    "After looking around at some of the clubs offered you feel pretty satisfied and decide to leave for the day."

    if joinedany:
        "You're excited by what joining a club will entail and are looking forward to your first meeting as you head in for lunch"

    else:
        "Clubs aren't your thing, and that's okay! Time to get some lunch."
    $ allowed += 1
    call resume from _call_resume_9
    call hdxtoday from _call_hdxtoday_8
    call map from _call_map_10
    jump Y2_S3_C0_CareerTermYorNo
