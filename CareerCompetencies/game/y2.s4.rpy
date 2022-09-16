label summer:
    $ curchpt = 6
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False
    $ didwhatnext = False

    scene study

    "About a month into your spring semester, you and your friends are doing work in the library when the topic of summer comes up."
    show bob at left with dissolve
    show elle at right with dissolve
    p "So what are y'all doing over the summer?"
    el "Well I actually talked to Dr. Maslow and am going to be working with them on their research regarding the role of music in early forming civilizations."
    p "Oh wow! That seems like a great opportunity!"
    el "Yeah I'm excited to learn more about it, and our Odyssey proposal was funded so I get to actually travel and gain in-person experience!"
    b "That's awesome! I applied to a few Chemistry REU's and should be hearing back about those pretty soon!"
    p "I'm sure you got in."
    el "Easily too. What about you [name]?"
    p "I don't actually know. I haven't really put any thought into it. I guess I figured I had more time."
    el "Well that's okay, I'm sure you still do. Is there anything in particular you would want to do?"
    p "I don't really know..."
    p "It seems like research would be a lot of fun after hearing about yours, but I'm not sure if that's for me."
    b "Well there are always internships that you could do!"
    p "Yeah that's a good point. There was that one I saw at Career Fair last year that I liked, but I don't know if they are even hiring."
    el "You should talk to Career Services, they can help you figure out what you may enjoy more and help you apply or get in touch with the right people!"
    hide bob with dissolve
    hide elle with dissolve
    hide study with dissolve
    scene sltc
    show eileenTalk
    e "Hey [name], what can I help you with?"
    hide eileenTalk
    show eileen
    p "Hi Eileen, I was wondering if you could talk with me about summer plans? I'm not really sure what to do and I was told I should come here."
    hide eileen
    show eileenTalk
    e "Of course, that's what we're here for! What are you not sure about?"
    hide eileenTalk
    show eileen
    p "Well I sort of put off thinking about what I wanted to do and now I'm worried that I waited too long and it's too late to find anything."
    p "I would like to get a cool summer experience while my friends are too so I'm not bored all summer."
    hide eileen
    show eileenTalk
    e "Well I won't lie to you, it is a tad late to be working on this sort of thing compared to others, but that doesn't mean there arent options around!"
    e "Do you have any idea on what you would like to go for? At this point you may want to consider to chase after something you have good experience in since summer is months away."
    $ centers = True
    show eileenTalk:
        blur 5
    menu:
        e "You can pick whatever you would like, but I want to make sure you have the best chance possible."
        "Social Sciences Research":
            jump socialsciencesresearch
        "STEM Research":
            jump stemresearch
        "Company X Position":
            jump compx

    jump gameOver




label socialsciencesresearch:
    hide eileenTalk
    show eileen
    p "I think I'm interested in the sleep study, but I think it may be way too late for that. What should I do?"
    hide eileen
    show eileenTalk
    e "Dr. Maslows research is very interesitng! I've read a few of her publications and I think you would have a great time joining Elle with that."
    e "I heard they were funded through Odyssey, you should email them soon stating who you are and why you are interested and try to set up a meeting, make sure to send your resume and possibly CV."
    e "I wish you the best of luck, and I hope they have room to fit you in!"
    hide eileenTalk
    show eileen
    p "Okay, thank you so much for your help and I'll let you know how it goes!"
    hide eileen
    show eileenSmile
    e "Of course, thanks for stopping by!"

    "That's all folks"
    jump gameOver


label stemresearch:
    hide eileenTalk
    show eileen
    p "I think I'm interested in STEM, but I don't have a specific interest. What should I do?"
    hide eileen
    show eileenTalk
    e "Research in STEM, huh? I was helping Bob a few months ago craft his personal statement for his REU applications."
    e "I won't lie to you, you may be too late to apply to most outside opportunities, but what you may be able to od is talk to some of the professors here."
    e "Talking to them directly is always a great idea and they can help guide you to anyone who has openings!"
    hide eileenTalk
    show eileen
    p "Okay, thank you so much for your help and I'll let you know how it goes!"
    hide eileen
    show eileenSmile
    e "Of course, thanks for stopping by!"
    "That's all folks"
    jump gameOver


label compx:
    hide eileenTalk
    show eileen
    p "I think I'm interested in working for Company X, but I don't know how to get into contact with them. What should I do?"
    hide eileen
    show eileenTalk
    e "Oh I love working with Company X! They come to Career Fair every year and they always love to hire Hendrix students."
    e "I can give them a call and see if they ahve any openeings and if so, I'll send you their contact info."
    e "form their You can send in your resume, and CV if you ahve one, and have a nice conversation that hopefully leads to employment!"
    hide eileenTalk
    show eileen
    p "Okay, thank you so much for your help and I'll let you know how it goes!"
    hide eileen
    show eileenSmile
    e "Of course, thanks for stopping by!"
    "That's all folks"
    jump gameOver
