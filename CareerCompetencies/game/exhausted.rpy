label exhausted:
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False

    scene pecanCourtBackground
    "Throughout the past week, you have slowly been getting more exhausted, and a little burnt out."
    "You walk to class and sit down."
    scene classroom
    "{i}Oh great today is another lecture.{/i}"
    pr"Alright, today we are going to talk about the test that's this Friday."
    p"{i}Okay I should definitely try and pay attention to this.{/i}"
    pr"Remember, this test is worth 10 percent of your grade!"
    "On the screen you notice that there are a lot of words... words that feel kinda hard to read."
    pr"{i}Voice fades away...{/i}"
    "..."
    "..."
    "You jolt awake as someone shakes you."
    p"Wha.. did I sleep through class?"
    show whitney
    menu:
        w"Yeah it was quite the drag huh?"
        "Ask what happened in class":
            p"What did I sleep through?"
            w"A lot of info on the test..."
            menu:
                w"Are you doing alright? You usually don't sleep though class."
                "Truth":
                    p"I'm just doing a lot right now."
                "Lie":
                    p"I'm fine."
            menu:
                "Ask for notes":
                    p"Any chance I can see your notes?"
                    w"I didn't take any for this.. Sorry."
                    p"Thanks anyways.. I gotta go, bye."
                    w"Oh alright, see you later!"
                "Leave":
                    "You get up and leave without saying a word."
                    w"Oh okay, see ya later!"
        "Ask for notes":
            p"Can I see your notes"
            w"Oh um... About that..."
            w"I didn't take any for this.. Sorry."
            p"Thanks anyways.. cya."
            w"See ya later, sorry again!"
        "Leave":
            "You get up and leave without saying a word."
            w"Oh okay, see ya!"
    "The next week:"
    "{i}Ugh I absolutely bombed that test, we didn't learn any of that in class!{/i}"
    p"Huh, what's this?"
    "Your advisor sent you an email to have a meeting..."
    p"Hm I wonder what this was about, do I need to do something?"
    p"Well I guess I need to go to this"

    "At the meeting:"
    show advisor
    d"Hey, so how's it been going"

    d"What's been going on in your classes?"
    p"I mean, the usual."
    d"You're failing a class"
    p"Right, well I'm sure I'll get that back up soon."
    d"What all are you doing each day?"
    "You procede to explain everything you do..."
    p"..and I think thats all."
    d"..."
    d"That's a bit much, don't you think?"
    p"Well yeah, it is."
    d"Maybe you should focus more on school and getting sleep..."
    d"You can't be spreading yourself so thin."
    p"You're right. I'll..."
    menu:
        "{i}What do I do?"
        "..drop a club or two":
        "..stop partying as much":
        "..start asking for more help":
        "..stop going to as many Hendrix events":
    d"That's probably for the best."
    
    return