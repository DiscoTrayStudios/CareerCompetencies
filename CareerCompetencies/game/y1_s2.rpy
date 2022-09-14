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
    "You had a great time but you remember that you have some reading and notes to take for your 9AM tomorrow and it's already 12."
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
        "Dr. Willis places everyone into groups and everyone starts introducing each other."
        "{i} You notice no one seems to be wanting to say anything. {/i}"
        menu:
            "Take charge and faciliate the discussion since you did the work":
                jump Y1_S2_C5
            "Try and let someone else start the discussion":
                jump Y1_S2_C6

        p "So does anyone have any strong opinions about the first question"
    #else:
        #talk about not doing wor
    jump Y1_S2_C1_1


label Y1_S2_C4:
    scene couchRoom
    if wokeup:
        "{i} My pillow looks so nice, I accept this.{/i}"
        "You doze back off and happily sleep through your class."
    else:
        "You sleep straight through class without even as much as a thought about what you are missing."
    jump Y1_S3_C1


label Y1_S2_C5:

##Scene is for a good discussion

label Y1_S2_C6:

## You did the work but tried to let someone else lead the discussion

label Y1_S2_C7:

## You didn't do the work