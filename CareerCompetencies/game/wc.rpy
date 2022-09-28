

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
    $ leadership += 5
    $ professional += 5
    return

label Y1_C2_WC:
    "You noticed this morning on the Hendrix Today that the Welcome Center needed tour guides."
    menu:
        "Do you want to be a tour guide?"
        "I would love to!":
            jump Y1_C2_WC1
        "I'm not sure thats for me.":
            "You think through your schedule and realize that you probably wouldn't have the time to do this."
    return

label Y1_C2_WC1:
    show eileenTalk at left
    e "Hey there [name]!"
    e "I hear that you are interested in becoming a Hendrix Tour Guide?"
    p "Yeah! I really want to learn more about the campus and work with incoming students."
    e "That's great, we will get you all registered and let you know when you'll start!"
    p "Great, thanks!"
    $ leadership += 5
    $ professional += 5
    

label Y1_C3_WC:
    "Need osmething here"
    $ leadership += 5
    $ professional += 5
    return

label Y2_C1_WC:
    "{i}Doesn't look like much is going on here...{/i}"
    $ leadership += 5
    $ professional += 5
    return


label Y2_C2_WC:
    "{i}Doesn't look like much is going on here...{/i}"
    $ leadership += 5
    $ professional += 5
    return

label Y2_C3_WC:
    "Need something here"
    $ leadership += 5
    $ professional += 5
    return