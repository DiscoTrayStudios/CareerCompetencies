


label Y1_C1_L:
    show librarian
    l "Welcome to Bailey Library!"
    l "As new members of our community, it's important to learn about one another and meet new people!"
    l "We're going to randomly pair you up with another student, and you'll have a bit to talk to them before we move on."
    l "Let's go!"
    hide librarian

    "After a bit of chaotic searching, you finally manage to find your partner"
    show whitney with dissolve

    w "Hi, are you [name]? I'm Whitney."
    p "Yeah I am, it's nice to meet you!"
    w "You as well! I'm not going to lie I'm pretty bad at the whole small talk thing."
    w "I find these kinda awkward but I figured it would be the fastest way to meet some people on campus."
    p "Same here."
    "{i}She was right, it is kind of awkward. I guess I should try to learn more about her?{/i}"
    p "So what are you thinking of majoring in?"
    w "Right now, I'm going the BCMB to Med school path. What about you?"
    #FIX FIX FIX YOU KNOW WHAT THE MAJOR IS NOW FIX THIS NOW
    p "Oh nice! I have no idea myself, but I figure I'll find out what I like along the way."
    w "Sounds like a good plan, that's what college is for!"
    w "It might be a good idea to reach out to some professors in the fields you become interested in."
    w "I also saw a flier for career services, I'm sure they would be able to help you out!"
    p "That's a good idea, thanks!"
    show whitney at right with dissolve
    show librarian at left with dissolve
    l "Alright everyone, wrap it up and let's move on to the next event!"
    w "It was nice meeting you, I'll see you around!"
    p "Same here, see ya!"

    hide whitney with dissolve
    "Whitney walks away as the librarian starts explaining the next activity. Feeling less awkward, you stay for the rest of the event"
    hide librarian with dissolve
    "It wraps up shortly, and you're glad you were able to do something new with new people."
    $ social += 10
    $ communication += 5
    $ teamwork += 3
    return



label Y1_C2_L:
    show librarian
    l "Welcome to Peer Learning!"
    l "Finals are coming up, and it's always easier to study with someone."
    l "Our Peer Learning volunteers are extremely useful and can help you bump up your grades!"
    p "Thanks! I'm studying for an Econ test right now, do you know who I should talk to?"
    l "You should talk to Alex, they're an accounting major who graduates this semester. Last door on the right"
    p "Alright, thanks!"
    hide librarian
    "You walk down the hall until you reach the room and knock as you go in."
    p "Hey, are you Alex?"
    a "Yeah! Are you here for peer learning?"
    p "Yeah I am, I have an Econ final soon and want to make sure I'm prepared."
    "After a while of studying together, and Alex quizzing you, you start to make good progress on the parts you were struggling with."
    a "You're getting the hang of this pretty fast! Are you thinking about majoring in this?"
    p "I'm not really sure, I don't have a set plan and am just feeling things out for now."
    a "I understand. I changed my planned major probably three times my freshman year."
    p "How did you settle on accounting?"
    a "Well I went to Career Fair to check out opportunities with what I was going to do, but while there an accounting firm caught my eye."
    a "I decided to talk to them and after hearing more about what it involved, I thought I would like it a lot."
    a "I talked to career services afterward and they got me in touch with a more entry-level internship at a local place and I had a blast."
    p "Oh that's awesome!"
    a "Yeah they were really nice and helpful. I highly recommend visiting their office if you haven't already."
    p "Thank you, I'll keep that in mind!"
    a "Alrighty, let's make sure you ace this test now."
    p "Sounds good to me."
    $ social += 5
    $ academic += 15
    $ thinking += 7
    $ dev += 4
    $ tech += 3
    return


label Y2_C1_L:
    show librarian
    l "Welcome to the Library! Let's learn about studying abroad."
    l "Our program allows the opportunity to study in over 300 universities across six continents."
    l "With so many options it may seem a bit daunting, but this just means there's one perfect for you!"
    l "Studying abroad has many benefits such as gaining a new perspective of the world, being able to immerse in a different culture,"
    l "and meet incredible people all while gaining college and odyssey credit!"
    l "Our Study Abroad office at Hendrix is more than happy to help you learn more about the program and help you apply!"
    l "If you would like to learn more, you can go to {a=https://www.hendrix.edu/InternationalPrograms/StudyAway.aspx?id=34572}this site{/a}!"
    l "Also, one thing that most people forget when they study abroad is that it looks incredible on a resume!"
    l "It shows a lot of personal development, willingness to learn, and that you can offer different perspectives."
    l "Thanks for visiting!"
    $ dev += 5
    $ tech += 5
    hide librarian
    return



label Y2_C2_L:
    "Student Study Session coming soon!"
    "Thanks for visiting!"
    return
