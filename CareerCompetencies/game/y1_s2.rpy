label Y1_S2_C1:
    $ curchpt = 2
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False
    $ homework = False
    $ wokeup = False
    $ didwhatnext = False

    scene couchRoom

    "The last couple of weeks have been pretty good! You made some friends, and have only gotten lost on your way to classes once!"
    "You really enjoyed your Orientation trip as well... besides the fact that it {b}rained{/b}."
    "It supposedly always rains during Orientation... {i}Ugh.{/i}"
    "You just got back into your room from being with some friends."
    "You had a great time but you remember that you have some reading and notes to take for your 9 AM tomorrow and it's already midnight."
    menu:
        "What do you do?"
        "Stay up and do the work":
            $ make_request("Y1_S2_C2")
            $ homework = True
            jump Y1_S2_C2
        "Go to bed and just wing it in class":
            $ make_request("Y1_S2_C2")
            jump Y1_S2_C3
        "Decide you won't go to that class tomorrow":
            $ make_request("Y1_S2_C4")
            jump Y1_S2_C4


label Y1_S2_C2:
    scene couchRoom
    "You wake up exhausted from spending two hours on that work last night."
    $ exhaustion += 1
    $ wokeup = True
    "{i}Your bed seems so tempting to stay in but you don't want your work to go to waste.{/i}"
    menu:
        "Sleep through class":
            jump Y1_S2_C4
        "Get up and go to class":
            jump Y1_S2_C3



label Y1_S2_C3:
    scene classroom
    show professor at left
    pr "Hello class!"
    pr "I hope that everyone did their reading and made notes about the discussion questions because ..."
    pr "Today you will be randomly assigned groups!"
    if homework:
        hide professor
        ## show a student or something
        "{i}Thankfully I did all this last night so this should go well! {/i}"
        "Dr. Willis places everyone into groups and everyone starts introducing themselves."
        "{i} You notice no one seems to be wanting to say anything. {/i}"
        p "So does anyone have any strong opinions about the first question?"
        "You get some muttered answers and overall not much of a response."
        menu:
            "What do you want to do about it?"
            "Take charge and facilitate the discussion since you did the work.":
                jump Y1_S2_C5
            "Try and let someone else start the discussion.":
                jump Y1_S2_C6
    else:
        ## maybe show a student idk?
        ## do part about asking if anyone did work
        hide professor
        "{i} Oh no... I really hope someone in my group did this or it's gonna be a struggle. {/i}"
        "Dr. Willis places everyone into groups and everyone starts introducing themselves."
        "You sit in silence for a few moments hoping someone starts the conversation."
        "A couple of people say some different things about each question but no real conversation starts."
        "You all begin awkwardly staring at each other and then looking at the paper."
        menu:
            "The professor starts to walk by"
            "You ask your group your group how their weekend was":
                jump Y1_S2_C7
            "You don't say anything":
                jump Y1_S2_C8



label Y1_S2_C4:
    scene couchRoom
    $ professional -= 10
    $ communication -= 5
    if wokeup:
        $ exhaustion -= 1
        "{i} My pillow looks so nice, I accept this.{/i}"
        "You doze back off and happily sleep through your class."
    else:
        "You sleep straight through class without even as much as a thought about what you are missing."
    $ allowed = allowed + 1
    call resume from _call_resume_20
    call hdxtoday from _call_hdxtoday_16
    call map from _call_map_18
    jump Y1_S3_C1


label Y1_S2_C5:
    scene classroom
    "You begin to step through each question with everyone in your group."
    "{i}Everyone seems to be responding really well to me taking the lead here, I'm really glad that I did this work. {/i}"
    show professor at left
    pr "Alright class! We have about 10 minutes left in class so I want to hear a little from each group."
    pr "[name]'s group, tell me a little bit about your discussion."
    show professorNormal at left
    "You start talking about the productive group discussion you had and you can tell your group was happy that you saved them."
    hide professorNormal
    pr "Very nice! That was insightful and can tell everyone really enjoyed the discussion."
    show professorNormal at left
    "The rest of the groups give their insights and you feel confident that your group did the best."
    hide professorNormal
    hide professor
    $ leadership += 10
    $ teamwork += 5
    $ allowed = allowed + 3
    call resume from _call_resume_21
    call hdxtoday from _call_hdxtoday_17
    call map from _call_map_19
    jump Y1_S3_C1

label Y1_S2_C6:
    scene classroom
    "You wait to see if anyone is going to say anything."
    "{i} I don't think anyone is gonna talk... {/i}"
    p "Well did anyone do the homework?"
    "Everyone shakes their head and you hear some mumbled no's as well."
    "{i}Well this is just wonderful...{/i}"
    "You make your way through some of the questions with the group but not all of them."
    show professor at left
    pr "Alright class! We have about 10 minutes left in class so I want to hear a little from each group."
    pr "[name]'s group, tell me a little bit about your discussion."
    show professorNormal at left
    "You start talking about the group discussion you had and you can tell your group was glad that you had done some work."
    hide professorNormal
    pr "You all made some good points, I enjoyed listening to that."
    show professorNormal at left
    "The rest of the groups give their insights and you feel confident that your group did well but could've been better."
    hide professorNormal
    hide professor
    "{i}You leave class feeling happy that it's over and look forward to a nice nap!{/i}"
    $ leadership -= 5
    $ allowed = allowed + 3
    call resume from _call_resume_22
    call hdxtoday from _call_hdxtoday_18
    call map from _call_map_20
    jump Y1_S3_C1

label Y1_S2_C7:
    scene classroom
    p "So how was everybody's weekend?"
    "Everyone talks a bit about their weekend and it looks to the professor that you all are having a productive discussion."
    "After talking, your group seems more relaxed and you can look at the reading material and you talk to your group about it."
    show professor at left
    pr "Alright class! We have about 10 minutes left in class so I want to hear a little from each group."
    pr "[name]'s group, tell me a little bit about your discussion."
    show professorNormal at left
    "Someone else in your group decides to speak up, and talk about the points you made."
    hide professorNormal
    pr "Nice!  I'm glad you pointed it out and hope the rest of your discussion went well."
    show professorNormal at left
    "The rest of the groups give their insights and you feel good about yours but know it wasn't the best."
    hide professorNormal
    hide professor
    "{i}You leave class feeling fine but know you should do better next time.{/i}"
    $ communication += 5
    $ allowed = allowed + 2
    call resume from _call_resume_23
    call hdxtoday from _call_hdxtoday_19
    call map from _call_map_21
    jump Y1_S3_C1

label Y1_S2_C8:
    scene classroom
    "The professor walks by and everyone attempts to seem like there is a conversation."
    "Once he is out of earshot, the fake discussion dies off and you are back to awkward silence."
    "{i} This is terrible... why will no one hold a conversation. {/i}"
    show professor at left
    pr "Alright class! We have about 10 minutes left in class so I want to hear a little from each group."
    pr "[name]'s group, tell me a little bit about your discussion."
    show professorNormal at left
    "You start talking about the little bit of conversation you had but it becomes obvious the longer you talk that you knew very little about the subject matter."
    hide professorNormal
    pr "Alright... well thank you for that [name]'s group."
    show professorNormal at left
    "You and the group can tell the professor is unhappy with the lackluster answer given."
    "The rest of the class gives their insights and you can tell your group was by far the worst."
    hide professorNormal
    pr "Well I hope everyone has a good rest of their day! Overall, the discussions were good but some people need to make sure they do the work or else they will start to suffer."
    hide professor
    "{i}You leave class feeling quite disappointed to have been called out like that. You will put more effort into getting your work next time.{/i}"

    $ leadership -= 5
    $ professional -= 5
    $ teamwork -= 5
    $ communication -= 5
    $ allowed = allowed + 2
    call resume from _call_resume_24
    call hdxtoday from _call_hdxtoday_20
    call map from _call_map_22
    jump Y1_S3_C1
