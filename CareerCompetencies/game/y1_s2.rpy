label Y1_S2_C1:
    $ curchpt = 2
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False
    $ homework = False
    $ wokeup = False

    scene couchRoom

    "You just get back into your room from being with some friends."
    "You had a great time but you remember that you have some reading and notes to take for your 9AM tomorrow and it's already midnight."
    menu:
        "What do you do?"
        "Stay up and do the work":
            $ homework = True
            jump Y1_S2_C2
        "Go to bed and just wing it in class":
            jump Y1_S2_C3
        "Decide you won't go to that class tomorrow":
            jump Y1_S2_C4


label Y1_S2_C2:
    scene couchRoom
    "You wake up exhausted from spending two hours on that work last night"
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
        p "So does anyone have any strong opinions about the first question"
        "You get some muttered answers and overall not much of a response"
        menu:
            "What do you want to do about it?"
            "Take charge and facilitate the discussion since you did the work":
                jump Y1_S2_C5
            "Try and let someone else start the discussion":
                jump Y1_S2_C6    
    else:
        ## maybe show a student idk?
        ## do part about asking if anyone did work
        hide professor
        "{i} Oh no... I really hope someone in my group did this or its gonna be a struggle. {/i}"
        "Dr. Willis places everyone into groups and everyone starts introducing themselves."
        "You sit in silence for a few moments hoping someone starts the conversation."
        "A couple people say some different things about each question but no real conversation starts"
        "You all begin awkwardly starting at each other and then looking at the paper"
        menu:
            "The professor starts to walk by"
            "You ask your group your group how there weekend was":
                jump Y1_S2_C7
            "You don't say anything":
                jump Y1_S2_C8



label Y1_S2_C4:
    scene couchRoom
    if wokeup:
        "{i} My pillow looks so nice, I accept this.{/i}"
        "You doze back off and happily sleep through your class."
    else:
        "You sleep straight through class without even as much as a thought about what you are missing."
    jump Y1_S3_C1


label Y1_S2_C5:
    scene classroom
    "You begin to step through each question with everyone in your group."
    "{i}Everyone seems to be responding really well to me taking the lead here, I'm really glad that I did this work. {/i}"
    show professor at left
    pr "Alright class! We have about 10 minutes left in class so I want to hear a little from each group"
    pr "[name]'s group, tell me a little bit about your discussion"
    "You start talking about the productive group discussion you had and you can tell your group was happy that you saved them."
    pr "Very nice! That was really insightful and can tell you guys really enjoyed the discussion."
    "The rest of the groups give their insights and you feel confident that your group did the best."
    "{i}You leave class feeling happy that it went that well and look forward to a nice nap!{/i}" 
    jump Y1_S3_C1

label Y1_S2_C6:
    scene classroom
    "You wait to see if anyone is going to say anything"
    "{i} I don't think anyone is gonna talk... {/i}"
    p "Well did anyone do the homework?"
    "Everyone shakes their head and you hear some mumbled no's as well"
    "{i}Well this is just wonderful...{/i}"
    "You make your way through some of the questions with the group but not all of them"
    show professor at left
    pr "Alright class! We have about 10 minutes left in class so I want to hear a little from each group"
    pr "[name]'s group, tell me a little bit about your discussion"
    "You start talking about the group discussion you had and you can tell your group was glad that you had done some work."
    pr "You all made some good points, I enjoyed listenting to that."
    "The rest of the groups give their insights and you feel confident that your group did well but could've been better."
    "{i}You leave class feeling happy that it's over and look forward to a nice nap!{/i}" 
    jump Y1_S3_C1

label Y1_S2_C7:
    scene classroom
    p "So how was everybody's weekend?"
    "Everyone talks a bit about their weekend and it looks to the professor that you guys are having a productive discussion."
    "After talking, your group seems more relaxed and you are able to look at the reading material and you talk to your group about it."
    show professor at left
    pr "Alright class! We have about 10 minutes left in class so I want to hear a little from each group"
    pr "[name]'s group, tell me a little bit about your discussion"
    "Someone else in your group decides to speak up, and talk about the points you made."
    pr "Nice!  I'm glad you pointed it out and hope the rest of your discussion went well"
    "The rest of the groups give their insights and you feel good about yours but know it wasn't the best."
    "{i}You leave class feeling fine that it went that alright but know you should do better next time.{/i}"
    jump Y1_S3_C1

label Y1_S2_C8:
    scene classroom
    "The professor walks by and everyone makes an attempt to seem like there is conversation"
    "Once he is out of earshot, the fake discussion dies off and you are back to awkward silence"
    "{i} This is terrible... why will no one hold a conversation {/i}"
    show professor at left
    pr "Alright class! We have about 10 minutes left in class so I want to hear a little from each group"
    pr "[name]'s group, tell me a little bit about your discussion"
    "You start talking about the little bit of conversation you had but it becomes obvious the longer you talk that you knew very little about the subject matter."
    pr "Alright... well thank you for that [name]'s group"
    "You and group can tell the professor is unhappy with the lackluster answer given."
    "The rest of the class gives their insights and you can tell your group was by far the worst"
    pr "Well I hope everyone has a goof rest of their day! Overall, the discussions were good but some people need to make sure they do the work or else they will start to suffer"
    "{i}You leave class feeling quite disappointed to have been called out like that. You will put more effort into getting your work next time.{/i}"
    jump Y1_S3_C1
    


