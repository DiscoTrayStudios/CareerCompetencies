


label Y1_C1_L:
    $ make_request("Y1_C1_L")
    show librarianTalk
    l "Welcome to Bailey Library!"
    l "As new members of our community, it's important to learn about one another and meet new people!"
    l "We're going to randomly pair you up with another student, and you'll have a bit to talk to them before we move on."
    l "Let's go!"
    hide librarianTalk

    "After a bit of chaotic searching, you finally manage to find your partner"
    show whitney with dissolve
    show whitneyTalk
    w "Hi, are you [name]? I'm Whitney."
    hide whitneyTalk
    p "Yeah I am, it's nice to meet you!"
    show whitneyTalk
    w "You as well! I'm not going to lie I'm pretty bad at the whole small talk thing."
    w "I find these kinda awkward but I figured it would be the fastest way to meet some people on campus."
    hide whitneyTalk
    p "Same here."
    "{i}She was right, it is kind of awkward. I guess I should try to learn more about her?{/i}"
    p "So what are you thinking of majoring in?"
    show whitneyTalk
    w "Right now, I'm going the BCMB to Med school path. What about you?"
    hide whitneyTalk
    p "[maj] right now, but who knows what will happen."
    show whitneyTalk
    w "Sounds like a good plan, that's what a liberal college is for!"
    w "It might be a good idea to reach out to some professors in the fields you become interested in."
    w "Always be sure to talk to your advisor about how you feel about your courses to make sure your major is right for you."
    w "I also saw a flier for Career Services, I'm sure they would be able to help you out if you ever have second thoughts!"
    hide whitneyTalk
    p "Oh wow, thanks for all the advice!"
    show whitney at right with dissolve
    show librarianTalk at left with dissolve
    l "Alright everyone, wrap it up, and let's move on to the next event!"
    hide librarianTalk
    show librarian at left
    show whitneyTalk at right
    w "It was nice meeting you, I'll see you around!"
    hide whitneyTalk
    p "Same here, see ya!"

    hide whitney with dissolve
    "Whitney walks away as the librarian starts explaining the next activity. Feeling less awkward, you stay for the rest of the event"
    hide librarian with dissolve
    "It wraps up shortly, and you're glad you were able to do something new with new people."
    $ communication += 5
    $ teamwork += 5
    return



label Y1_C2_L:
    $ make_request("Y1_C2_L")
    show librarianTalk
    l "Welcome to Peer Learning!"
    l "Finals are coming up, and it's always easier to study with someone."
    l "Our Peer Learning volunteers are extremely useful and can help you bump up your grades!"
    hide librarianTalk
    show librarian
    p "Thanks! I'm studying for an Econ test right now, do you know who I should talk to?"
    hide librarian
    show librarianTalk
    l "You should talk to Alex, they're an accounting major who graduates this semester. Last door on the right"
    hide librarianTalk
    show librarian
    p "Alright, thanks!"
    hide librarian
    "You walk down the hall until you reach the room and knock as you go in."

    scene studyCorral
    p "Hey, are you Alex?"
    show alexTalk
    a "Yeah! Are you here for peer learning?"
    hide alexTalk
    show alex
    p "Yeah I am, I have an Econ final soon and want to make sure I'm prepared."
    "After a while of studying together, and Alex quizzing you, you start to make good progress on the parts you were struggling with."
    show alexTalk
    a "You're getting the hang of this pretty fast! Are you thinking about majoring in this?"
    hide alexTalk
    p "I'm not really sure, I'm thinking about majoring in [maj], but I am just feeling things out for now."
    show alexTalk
    a "I understand. I changed my planned major probably three times my freshman year."
    hide alexTalk
    p "How did you settle on accounting?"
    show alexTalk
    a "Well I went to Career Fair to check out opportunities with what I was going to do, but while there an accounting firm caught my eye."
    a "I decided to talk to them and after hearing more about what it involved, I thought I would like it a lot."
    a "I talked to Career Services afterward and they got me in touch with a more entry-level internship at a local place and I had a blast."
    hide alexTalk
    p "Oh that's awesome!"
    show alexTalk
    a "Yeah they were very nice and helpful. I highly recommend visiting their office if you haven't already."
    hide alexTalk
    p "Thank you, I'll keep that in mind!"
    show alexTalk
    a "Alrighty, let's make sure you ace this test now."
    hide alexTalk
    p "Sounds good to me."
    hide alex
    "You two study for a while longer and you will definitely ace this Econ test tomorrow."
    "{i}I got this...{/i}"
    $ communication += 5
    $ teamwork += 5
    return

label Y1_C3_L:
    $ make_request("Y1_C3_L")
    scene studyCorral
    "You walked through the library to see if anything was going on. You couldn't even find anyone you knew."
    "{i}Well, I walked all this way. May as well not waste it."
    "You end up staying for a couple of hours and manage to put a good dent into all the work you had to do!"
    $ communication += 5
    $ teamwork += 5
    return

label Y2_C1_L:
    $ make_request("Y2_C1_L")
    show librarianTalk
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
    $ communication += 5
    $ teamwork += 5
    hide librarianTalk
    return



label Y2_C2_L:
    $ make_request("Y2_C2_L")
    show librarianTalk
    l "Welcome to Peer Learning!"
    l "Finals are coming up, and it's always easier to study with someone."
    l "Our Peer Learning volunteers are extremely useful and can help you bump up your grades!"
    hide librarianTalk
    show librarian
    p "Thanks! I'm studying for a Biology test right now, do you know who I should talk to?"
    hide librarian
    show librarianTalk
    l "You should talk to Elle, they're a Biology major. Third door on the left"
    hide librarianTalk
    show librarian
    p "Alright, thanks!"
    hide librarian
    "You walk down the hall until you reach the room and knock as you go in."
    scene studyCorral
    p "Hey, are you Elle?"
    show elleTalk
    el "Yeah! Are you here for peer learning?"
    hide elleTalk
    show elle
    p "Yeah I am, I have a Biology final soon and want to make sure I'm prepared."
    "After a while of studying together, and Elle quizzing you, you start to make good progress on the parts you were struggling with."
    show elleTalk
    el "You're getting the hang of it! I think you are gonna ace this."
    hide elleTalk
    p "I'm not really sure about that..."
    show elleTalk
    el "Come on don't doubt yourself! You got this. Just remember to get plenty of sleep tonight and maybe refresh on this in the morning."
    hide elleTalk
    hide elle
    "The two of you continue to study for another hour and then you decide it's time to head back to your dorm."
    show elle
    p "Alright I'm gonna head out now, thanks for the help!"
    show elleTalk
    el "Of course! That's what I'm here for!"
    hide elleTalk
    hide elle
    $ communication += 5
    $ teamwork += 5
    return

label Y2_C3_L:
    $ make_request("Y2_C3_L")
    scene studyCorral
    "You head to the library to work on a group project. A pre-planned time and a pre-planned location. What could go wrong?"
    "In the five minutes that you find the room and get settled, your 'team' has sent several messages stating they can't meet, and those that didn't message just never showed up."
    "You decide to work on your part at least, and have time to do some more work for other classes since you're in the headspace."
    $ communication += 5
    $ teamwork += 5
    return
