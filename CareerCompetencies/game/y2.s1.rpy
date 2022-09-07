label Y2_S1_C0:
    $ curchpt = 3
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False
    $ centers = True

    scene p


    "You are now in your Sophomore Year... After a long week, you are stuck with a decision."
    "It's been a busy week! You have so much homework due next week, and a project due as well."
    "{i}Maybe I should take a break... There is that party that's happening tonight, but then again I have a lot of homework...{/i}"
    menu:
        "What would you like to do?"
        "Do some homework":
            jump Y2_S1_C1_H
        "Go to the party":
            jump Y2_S1_C1_P

label Y2_S1_C1_H:
    $ academic += 5
    $ social -= 3
    "{i}The party seems fun, but I know I should do schoolwork first. The only question is where?{/i}"
    menu:
        "Where will you do work?"
        "The library sounds nice":
            jump Y2_S1_C2_1_H
        "Kinda don't feel like going out":
            jump Y2_S1_C2_2_H


label Y2_S1_C2_2_H:
    $ academic += 2
    $ social -= 2
    "You decide to stay in your room. You can always go out next time."
    "The night passes as you do work. It's pretty productive although you do get stuck for a while."
    "{i}I'm satisfied with my work, I'm calling it and going to sleep."
    $ allowed += 2
    $ centers = False
    call resume from _call_resume_10
    call hdxtoday from _call_hdxtoday_9
    call map from _call_map_11
    jump Y2_S2_C0_ClubEnter
    #REVISE WITH ROOMATE DRAMA

label Y2_S1_C1_P:
    $ academic -= 4
    $ social += 6
    "Why not, it's been a long week and homework can be a future you problem!"
    "{i}It's only 4:00, so I have a bit of time to relax before the party, but what should I wear tonight?"
    "{i}There is a theme... but I'm sure that not everyone is going to dress up."
    menu:
        "Do you dress up?"
        "If I don't go in style, I don't go at all":
            jump Y2_S1_C2_1_P
        "It would be fun, but it's too much work":
            jump Y2_S1_C2_2_P


label Y2_S1_C2_2_P:
    $ academic -= 2
    "Not worth the effort, you spend the afternoon relaxing until it is time for the party."
    "You debate with yourself if you want to go with friends, or just by yourself for the night."
    menu:
        "Social or Solo?"
        "Friends are fun!":
            jump Y2_S1_C3_1_P
        "I'll meet them at the party":
            jump Y2_S1_C3_2_P

label Y2_S1_C2_1_P:
    $ academic -= 2
    $ social += 2
    "Okay! The theme is 80's"
    "A quick closet check lets you know you don't have anything on hand, so it's time to go shopping!"
    "Once you get back with your parachute pants and leather jacket, you put it all on and get ready to head out."
    "The only thing left is to go with friends, or make a dramatic entrance yourself."
    menu:
        "Social or Solo?"
        "Friends are fun!":
            jump Y2_S1_C3_1_P
        "I'll meet them at the party":
            jump Y2_S1_C3_2_P




label Y2_S1_C3_1_P:
    $ social += 4
    "You have friends! Go with them! You meet up with your friends and hang with them until the party."
    "You end up having a blast and having one of the most fun weekends of your life"
    $ allowed += 1
    $ sleep -= 4
    $ centers = False
    call resume from _call_resume_11
    call hdxtoday from _call_hdxtoday_10
    call map from _call_map_12
    jump Y2_S2_C0_ClubEnter

label Y2_S1_C3_2_P:
    $ social += 4
    "You will just meet them there! For now, let's just kill some time and relax."
    "Once you get to the party, you actually can't find your friends..."
    "You decide to not waste your time and just start chatting up strangers"
    "Everyone is in a good mood and you end up making some nice party friends!"
    "Maybe you'll see them around campus!"
    #Dialogue here????????
    $ allowed += 1
    $ communication += 10
    $ sleep -= 4
    $ centers = False
    call resume from _call_resume_12
    call hdxtoday from _call_hdxtoday_11
    call map from _call_map_13
    jump Y2_S2_C0_ClubEnter


label Y2_S1_C2_1_H:
    $ academic += 2
    scene libraryBackground
    "You walk to the library, and it's a nice fall night with a cool breeze."
    "Once You arrive at the library and see a group of people that you sort of know in the Snoddy Center with your friend, Taylor."
    "{i}It might be good to work on stuff around people to stay productive and off my phone.{/i}"
    "{i}On the other hand, if they start talking a lot I might not be able to focus well.{/i}"
    menu:
        "Work alone or join the group?"
        "What's the harm in a bit of talking":
            jump Y2_S1_C3_1_H
        "I want to hone in on my work":
            jump Y2_S1_C3_2_H


label Y2_S1_C3_2_H:
    $ academic += 4
    $ sleep -= 8
    scene studyCorral
    "You find an empty study room and you get straight to work. After all, if you get everything done now then you can just relax later."
    "{i}... It's 4:00...{/i}"
    "{i}... It's 6:00...{/i}"
    "You get some done, but are starting to get stuck. You decide to struggle through"
    "{i}... It's 7:0?...{/i}"
    "{i}... It's 8:??...{/i}"
    "{i}... It's ?:??...{/i}"
    "You lose track of time in the process and suddenly {i}It's midnight!?{/i}"
    "You could've sworn you weren't working for 6 hours straight. Oh well... You should probably head back to your room to sleep..."
    "However, you are almost done with all your work, maybe just finish it up real quick?"
    menu:
        "Stay late or call it a night?"
        "I'll push through, I'm already here":
            jump Y2_S1_C5_1_H
        "I should sleep before I try any more":
            jump Y2_S1_C5_2_H

label Y2_S1_C5_1_H:
    $ sleep -= 8
    "You continue to work..."
    "{i}... It's 12:10...{/i}"
    "{i}... {size=-3}It's 12:11{/size}...{/i}"
    "{i}... {size=-6}It's 12:12...{/size}{/i}"
    "Your eyes get heavy..."
    "..."
    "{i}No I can't fall asleep, I'm almost done! Besides it isn't even that late.{/i}"
    "..."
    "{i}Wait a minute...{/i}"
    "You check the time, It's 1:48 A.M. You fell asleep and didn't even realize it."
    "Defeated, and having made little progress on your work in the last 2 hours, you decide to go back to your room."
    "Tonight is not gonna be good sleep."
    $ allowed += 1
    $ centers = False
    call resume from _call_resume_13
    call hdxtoday from _call_hdxtoday_12
    call map from _call_map_14
    jump Y2_S2_C0_ClubEnter

label Y2_S1_C5_2_H:
    $ sleep += 8
    "{i}I should probably just go to sleep.{/i}"
    "Your eyes are already a little heavy anyways and the rest of the work can wait until later."
    scene p
    "You get back to the room and your roommate isn't there... {i}Oh well I'm sure they will show up later{/i}."
    "You get ready for bed and as your head hits your pillow you fall into a whimsical world of dreams."
    "It would be nice if you would've spent some time with people today, but there's always tomorrow."
    $ allowed += 3
    $ centers = False
    call resume from _call_resume_14
    call hdxtoday from _call_hdxtoday_13
    call map from _call_map_15
    jump Y2_S2_C0_ClubEnter


label Y2_S1_C3_1_H:
    $ academic += 4
    $ social += 2
    "You decide it will be good to be around people."
    "At least as long as everybody is working as well it will work out!"
    "Worst things worst, you can still bounce ideas off of people."
    scene snoddyCenter
    "As you head into the Snoddy Center your friends recognize you and wave."
    p "Hey, can I do my work with you guys?"
    show taylor at left with dissolve
    show whitney at right with dissolve
    t "Of course! Everyone, this is [name]. [name], this is Whitney, John, and Suzy."
    p "It's great to meet you all!"
    "Everyone else says their hellos and after some quick small talk, everyone goes back to their work."
    "As time passes you get stuck and ask for help."
    w "Oh for sure, I actually took that class last year, let me help you!"
    "Whitney helps you out, and they were extremely helpful and you got work done quickly."
    "Everyone starts to take breaks, so you talk to them a bit more and get to know a bit more about them."
    "At one point in the conversation, tonight's party comes up and that they will be leaving for it soon."
    t "Are you going to come, [name]?"
    w "You totally should, it'll be a ton of fun!"
    $ teamwork += 10
    $ centers = True
    show taylor at left:
        blur 5
    show whitney at right:
        blur 5
    menu:
        "Do you join?"
        "I got some work done, I deserve a break":
            hide taylor
            show taylor at left
            hide whitney
            show whitney at right
            $ centers = False
            jump Y2_S1_C4_1_H
        "I still have quite a bit to do, maybe later":
            hide taylor
            show taylor at left
            hide whitney
            show whitney at right
            $ centers = False

            jump Y2_S1_C4_2_H


label Y2_S1_C4_1_H:
    $ social += 4
    p "Sure, why not!"
    "You all pack up and head to the party."
    hide taylor with dissolve
    hide whitney with dissolve
    "Whitney was right, everyone has a ton of fun, and you even managed to get a bit of work done!"

    $ allowed += 2

    $ centers = False
    call resume from _call_resume_15
    call hdxtoday from _call_hdxtoday_14
    call map from _call_map_16
    jump Y2_S2_C0_ClubEnter

label Y2_S1_C4_2_H:
    $ academic += 2
    $ social -= 2

    p "Nah, I think I'll stay here and do a bit more work before heading to bed."
    p "Y'all have fun though, stay safe!"
    t "Sounds good, we'll see you later!"
    hide taylor with dissolve
    hide whitney with dissolve
    "They leave, and although part of you does want to go, you know doing work now will be better later."
    $ allowed += 2
    $ centers = False
    call resume from _call_resume_16
    call hdxtoday from _call_hdxtoday_15
    call map from _call_map_17
    jump Y2_S2_C0_ClubEnter
