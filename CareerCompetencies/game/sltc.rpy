


label Y1_C1_SLTC:
    "Free ice cream? Obviously."
    "You make your way inside the burrow and see people having a great time chatting and enjoying their free treat."
    "You grab yourself a bowl and make your way towards the center. You don't really know that many people here but they probably don't either."
    "Two people take notice of you and start to make conversation. They seem like they're a bit older than first-years, but what the heck."
    show niraj at left with dissolve
    show alex at right with dissolve
    n "Hey there, I'm Niraj!"
    a "And I'm Alex, nice to meet you!"
    p "Yeah same here, I'm [name]!"
    n "Did you just move in? I know it can be pretty intimidating being new here. Hopefully you're starting to meet some people you enjoy?"
    p "Yes I did, and you're right it is scary but stuff like this makes it easier. I mean it's hard to have a hard time with ice cream."
    a "I'm glad you think so, Niraj and I actually organized this for new students to help them out. Keep your eye out for more, they're bound to happen."
    a "We won't hold you too long though, go socialize with some more people in your class and make some new friends!"
    p "Yeah for sure, thank you for this and it was nice meeting you!"
    hide niraj with dissolve
    hide alex with dissolve
    "You hang around for a half hour and talk to some more people, half of which you already forgot their names but you know you'll see them again."
    $ tech += 5
    $ equity += 10
    return


label Y1_C2_SLTC:
    "You head to the burrow to do a bit of work. You don't really want to do it but you have nothing better to do."
    "While you're there, you run into some friends you recently made at last weeks party."
    "You end talking more than working, but you had a good time and made more plans for this weekend!"
    $ tech += 5
    $ equity += 5
    return

label Y1_C3_SLTC:
    show smithTalk
    s "Hey, I'm Dr. Smith! Are you interested in majoring in a field in the natural sciences?"
    p "Yes I am! I'm not totally sure but I wanted to know a bit more about the programs involved."
    s "Well here at Hendrix, we have a lot of options to choose from!"
    s "A few examples of our Natural Sciences majors are Biochemistry/Microbiology, Physics, Computer Science, Mathematics, Chemistry, and Biology."
    s "The most popular route students take in the natural sciences is to go to medical school with a Biology or BCMB major, but those aren't required majors for that."
    s "If that doesn't interest you, we still have incredible opportunities, recourses, and experiences that are going to be made available to you."
    s "Our programs are highly renowned, and we have graduates all over the world doing incredible things."
    s "One great advantage of a career in the natural sciences with a liberal arts background is a great range in the learning process that allows students to view issues from all sorts of angles."
    s "Also, an Interdisciplinary Study is always an option, so that you can pursue exactly what you want to!"
    s "If you want to become even more involved, keep an eye out for any professors wanting help or potential research opportunities."
    p "Wow! Thank you so much!"
    hide smithTalk
    $ tech += 10
    $ equity += 10
    return

label Y2_C1_SLTC:
    "It's been a long day, and nothing sounds better than a coffee from the burrow. You head that way and plan to do a bit of your Spanish homework while you're there."
    "You realize though your laptop is dead and you don't have your charger. All your notes are online but you decide to try anyway."
    "it's obvious you don't know what you're doing after a bit. Someone notices and walks up to you."
    show blakely with dissolve
    bl "Hey I'm sorry to be a bother, but if you're struggling with that spanish work, I could help you out, I help with the peer learning."
    p "Uh yeah, sure that would be great thank you."
    "Blakely helps you out for a while and you actually understand the topic a lot better!"
    "She then shows you a cool website that has a ton of topics and helpful ways to learn"
    "Once y'all are done, you buy her a coffee as well as a thank you and say goodbye."
    $ tech += 10
    $ equity += 5
    return


label Y2_C2_SLTC:
    "You head to the burrow to do a bit of work. You don't really want to do it but you have nothing better to do."
    "While you're there, you run into some friends you recently made at last weeks party."
    "You end talking more than working, but you had a good time and made more plans for this weekend!"
    $ tech += 5
    $ equity += 5
    return


label Y2_C3_SLTC:
    "You walk in the burrow and remember it's parents weekend! The place is super crowded and bustling."
    "Someone walks up to you, clipboard in hand and stress on their face."
    show whitney with dissolve
    w "Hey are you looking for parents or are you scheduled to help volunteer."
    p "Uh neither. Do you need help though it looks a little chaotic in here."
    w "I would love help. Half the people didn't show up so thank you."
    w "If you can just sign families in and give them information on the events for this weekend that would be great."
    hide whitney with dissolve
    "Whitney walks away and leaves you to sign in people"
    "You're not really sure why you agreed to this but it feels nice to help and you were bored anyway."
    "After a couple of hours the majority of parents signed in and Whitney tells you you can head out if you'd like."
    "You are pretty tired so you take her up on the offer and head back to the dorm. As a thank you she buys you a mug from the student store."
    $ tech += 5
    $ equity += 10
    return
