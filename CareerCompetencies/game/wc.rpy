
$ tour = False


label Y1_C1_WC:
    show eileenTalk at right with dissolve
    e "Welcome new students!"
    e "I'll be giving a quick overview about life at Hendrix and resources to take advantage of while you're here."
    e "Hendrix has a strong sense of community, with tons of ways to be involved. We love our events, traditions, trips, and yes, parties."
    e "There are lots of opportunities to try new things, meet new people, and have a great time so make sure to keep an eye out!"
    e "Our goal at Hendrix is to create a place where everyone belongs and can thrive while gaining a great education."
    e "To help you thrive, we have multiple departments focused entirely on helping you."
    e "Our Odyssey department is a great resource to help you do something that means a lot to you. You can visit them at the SLTC."
    e "For help on goals, planning, and connecting, Career Services is there for you! They are willing to go above and beyond to help you out and love to talk to new students."
    e "Financial Aid is willing to help discuss and talk through anything financial you may have questions about!"
    hide eileenTalk with dissolve
    $ leadership += 5
    $ professional += 5
    return

label Y1_C2_WC:
    "You noticed this morning on the Hendrix Today that the Welcome Center needed tour guides."
    menu:
        "Do you want to be a tour guide?"
        "I would love to!":
            jump Y1_C2_WC1
        "I'm not sure that's for me.":
            "You think through your schedule and realize that you probably wouldn't have the time to do this."
    return

label Y1_C2_WC1:
    show eileenTalk at left with dissolve
    e "Hey there [name]!"
    e "I hear that you are interested in becoming a Hendrix Tour Guide?"
    hide eileenTalk
    show eileen at left
    p "Yeah! I really want to learn more about the campus and work with incoming students."
    show eileenTalk at left
    e "That's great, we will get you all registered and let you know when you'll start!"
    hide eileenTalk
    p "Great, thanks!"

    hide eileen with dissolve
    $ tour = True
    $ leadership += 5
    $ professional += 5
    return
    

label Y1_C3_WC:
    scene couchRoom
    "You lay in your room waiting for your phone to hit 6 PM."
    "As soon as the clock strikes 6, the email for where the Miss Hendrix tickets are hits your inbox."
    "THE WELCOME CENTER"
    scene welcomeCenterBackground

    "You start dashing to the Welcome Center to get your coveted Miss Hendrix tickets."

    "Once you arrive, you wait through the line to get a great seat."
    "As you walk back to your room, you think about just how awesome this weekend is going to be!"
    return

label Y2_C1_WC:
    if tour:

        "You arrive at the Welcome Center to a mob of visiting students."

        "{i}Jeez, I had no idea what I was getting into with this touring job.{/i}"
        "You spend a few hours corraling and leading lots of students around campus"
        "You feel exhausted but you keep pushing through!"
        "By the end of the day you are super drained but you feel accomplished and satisfied with the job you did!"
        $ leadership += 5
        $ professional += 5
    else:

        "You see a mob of students at the Welcome Center while walking to lunch."

        "{i} I'm sure glad that I decided not to sign up and do that! {/i}"
    return


label Y2_C2_WC:
    # finacial aid

    show eileenTalk with dissolve
    e "Hey [name]!"
    e "I'm really glad you came to the financial aid seminar!"
    e "We are going to help you understand the financial side of what we do here at the Welcome Center!"
    hide eileenTalk
    show eileenSmile
    "You listen through the presentation that the financial aid team gives."
    "You feel slightly overwhelmed by how much goes into the process but you walk away feeling like you learned a lot!"
    hide eileenSmile with dissolve

    $ leadership += 5
    $ professional += 5
    return

label Y2_C3_WC:
    "You walk out of the SLTC to go find your car that you parked at the Welcome Center." 
    "As you get closer you notice something on your windshield."
    "{i}Oh no... this isn't what I think it is, is it? {/i}"
    "You wrap around to the front of your car to notice that it is, in fact, a parking ticket"
    "With a sigh, you grab it from the windshield and grumpily drive back to your dorm."
    return