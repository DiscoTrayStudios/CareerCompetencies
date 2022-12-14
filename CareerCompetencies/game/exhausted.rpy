label exhausted:
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False

    if exhaustion < 4 or exhausted == True:
        return

    $ exhausted = True
    scene pecanCourtBackground
    "Throughout the past week, you have slowly been getting more exhausted, and a little burnt out."
    "You walk to class and sit down."
    scene classroom
    show professor at left with dissolve
    "{i}Oh great today is another lecture.{/i}"
    pr"Alright, today we are going to talk about the test that's this Friday."
    p"{i}Okay I should definitely try and pay attention to this.{/i}"
    pr"Remember, this test is worth 10 percent of your grade!"
    "On the screen you notice that there are a lot of words... words that feel kinda hard to read."
    pr"{i}Voice fades away...{/i}"
    hide professor with dissolve
    "..."
    "..."
    "You jolt awake as someone shakes you."
    p"Wha.. did I sleep through class?"
    show whitney at left
    menu:
        w"Yeah it was quite the drag huh?"
        "Ask what happened in class":
            p"What did I sleep through?"
            w"A lot of info on the test..."
            menu:
                w"Are you doing alright? You usually don't sleep through class."
                "Truth":
                    p "I'm just doing a lot right now."
                "Lie":
                    p "I'm fine."
            menu:
                "Ask for notes":
                    p"Any chance I can see your notes?"
                    w"I didn't take any for this... Sorry."
                    p"Thanks anyways... I gotta go, bye."
                    w"Oh alright, see you later!"
                "Leave":
                    "You get up and leave without saying a word."
                    w"Oh okay, see ya later!"
        "Ask for notes":
            p"Can I see your notes"
            w"Oh um... About that..."
            w"I didn't take any for this... Sorry."
            p"Thanks anyways.. cya."
            w"See ya later, sorry again!"
        "Leave":
            "You get up and leave without saying a word."
            w"Oh okay, see ya!"
    hide whitney
    scene pecanCourtBackground
    "The next week:"
    "{i}Ugh I absolutely bombed that test, we didn't learn any of that in class!{/i}"
    p"Huh, what's this?"
    "Your advisor sent you an email to have a meeting..."
    p"Hm I wonder what this was about, do I need to do something?"
    p"Well I guess I need to go to this"
    scene office
    "At the meeting:"
    show advisorTalk with dissolve
    d"Hey, so how's it been going?"

    d"What's been going on in your classes?"
    hide advisorTalk
    show advisor
    p"I mean, the usual."
    hide advisor
    show advisorTalk
    d"You're failing a class."
    hide advisorTalk
    show advisor
    p"Right, well I'm sure I'll get that back up soon."
    hide advisor
    show advisorTalk
    d"What all are you doing each day?"
    hide advisorTalk
    show advisor
    "You proceed to explain everything you do..."
    p"..and I think that's all."
    d"..."
    hide advisor
    show advisorTalk
    d"That's a bit much, don't you think?"
    hide advisorTalk
    show advisor
    p"Well yeah, it is."
    hide advisor
    show advisorTalk
    d"Maybe you should focus more on school and getting sleep..."
    d"You can't be spreading yourself so thin."
    hide advisorTalk
    show advisor
    p"You're right. I'll..."
    show advisor at left
    menu:
        "{i}What do I do?"
        "..drop a club or two":
            d"That's probably for the best."
        "..stop partying as much":
            d"That's probably for the best."
        "..start asking for more help":
            d"That's probably for the best."
        "..stop going to as many Hendrix events":
            d"That's probably for the best."

    return
