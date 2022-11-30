label summer:
    $ curchpt = 7
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
    show elleTalk at right
    el "Well I actually talked to Dr. Maslow and am going to be working with them on their research regarding the role of music in early forming civilizations."
    hide elleTalk
    p "Oh wow! That seems like a great opportunity!"
    show elleTalk at right
    el "Yeah I'm excited to learn more about it, and our Odyssey proposal was funded so I get to actually travel and gain in-person experience!"
    hide elleTalk
    show bobTalk at left
    b "That's awesome! I applied to a few Chemistry REUs and should be hearing back about those pretty soon!"
    hide bobTalk
    p "I'm sure you got in."
    show elleTalk at right
    el "Easily too. What about you [name]?"
    hide elleTalk
    p "I don't actually know. I haven't really put any thought into it. I guess I figured I had more time."
    show elleTalk at right
    el "Well that's okay, I'm sure you still do. Is there anything, in particular, you would want to do?"
    hide elleTalk
    p "I don't really know..."
    p "It seems like research would be a lot of fun after hearing about yours, but I'm not sure if that's for me."
    show bobTalk at left
    b "Well there are always internships that you could do!"
    hide bobTalk
    p "Yeah that's a good point. There was that one I saw at Career Fair last year that I liked, but I don't know if they are even hiring."
    show elleTalk at right
    el "You should talk to Career Services, they can help you figure out what you may enjoy more and help you apply or get in touch with the right people!"
    hide elleTalk
    hide bob with dissolve
    hide elle with dissolve
    hide study with dissolve
    scene sltc
    show eileenTalk
    e "Hey [name], what can I help you with?"
    hide eileenTalk
    show eileen
    p "Hi Eileen, I was wondering if you could talk with me about summer plans? I'm not sure what to do and I was told I should come here."
    hide eileen
    show eileenTalk
    e "Of course, that's what we're here for! What are you not sure about?"
    hide eileenTalk
    show eileen
    p "Well I sort of put off thinking about what I wanted to do and now I'm worried that I waited too long and it's too late to find anything."
    p "I would like to get a cool summer experience while my friends are too so I'm not bored all summer."
    hide eileen
    show eileenTalk
    e "Well I won't lie to you, it is a tad late to be working on this sort of thing compared to others, but that doesn't mean there aren't options around!"
    e "Do you have any idea what you would like to go for? At this point, you may want to consider chasing after something you have good experience in since summer is months away."
    $ centers = True
    if CV:
        $ qual +=1
    show eileenTalk:
        blur 5
    $ avgcomp = (dev + communication + thinking + equity + leadership + professional + teamwork + tech) / 8

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
    e "Dr. Maslow's research is very interesting! I've read a few of her publications and I think you would have a great time joining Elle with that."
    e "I heard they were funded through Odyssey, you should email them soon stating who you are and why you are interested and try to set up a meeting, make sure to send your resume and possibly CV."
    e "I wish you the best of luck, and I hope they have room to fit you in!"
    hide eileenTalk
    show eileen
    p "Okay, thank you so much for your help and I'll let you know how it goes!"
    hide eileen
    show eileenSmile
    e "Of course, thanks for stopping by!"
    hide eileenSmile
    "After sending an email to Dr. Maslow, they invite you to their office so that they can discuss the possibility of you joining."
    scene office
    show maslow
    m "Hi [name], I'm so glad you're interested in my research! Elle has spoken highly of you so I'm excited to interview you."
    m "I hope you can understand that with an already decided Odyssey budget, adding on a new team member means we have to cut expenses elsewhere."
    p "Of course, I'm happy that you were even open to the idea!"
    m "I won't waste your time, can I see your resume please?"
    "You hand it to them, and after looking it over, she hands it back..."

    if Theatre:
        $ qual +=1
    if BaileyWorker:
        $ qual +=1
    if stemjobs + internjobs >=1:
        $ qual +=1
    if qual >=2 and (Theatre or BaileyWorker) and avgcomp>=35:
        m "You seem to have a great amount of experience, and a great understanding of the Career Competencies we strive for here at Hendrix!"
        p "Thank you, it's been an incredible learning experience and I've had a blast these past two years."
        m "All of this being said, I think you would make a great addition to the team and I can't wait to work with you!"
        m "Come by tomorrow and we can go over what you'll be doing exactly. Welcome aboard!"
        p "Thank you, I won't let you down!"
<<<<<<< Updated upstream
        jump gotsocial
    elif qual >=2 and (Theatre or BaileyWorker) and avgcomp<50:
=======
        jump gotSocial
    elif qual >=2 and (Theatre or BaileyWorker) and avgcomp<35:
>>>>>>> Stashed changes
        m "This is a good-looking resume, and you certainly have great experience, but I'd also like to interview a bit before I make a decision."
        p "Of course, I totally understand."
        "You and Dr. Maslow talk for about half an hour, and you think it's going well!"
        m "[name], I'm sorry but I don't think it would be in the best interest of my group to add you on."
        m "To be honest, it was a slim chance already due to funding, and I think what solidified is that despite your good experience..."
        m "I don't think you have totally got the idea of Career Competencies here at Hendrix and how to fully utilize them."
        m "I am sorry I couldn't fit you in this summer, but I do believe you are on the right path!"
    else:
        m "I'm sorry, [name], but I'm looking for someone who has a bit more experience, especially in the right area."
        m "You should try going to Career Services more and asking what you should do, they always give great answers."
        m "Thank you for coming in, and keep working towards getting that experience and Competencies!"
    hide maslow with dissolve
    jump notin


label stemresearch:
    hide eileenTalk
    show eileen
    p "I think I'm interested in STEM, but I don't have a specific interest. What should I do?"
    hide eileen
    show eileenTalk
    e "Research in STEM, huh? I was helping Bob a few months ago craft his personal statement for his REU applications."
    e "I won't lie to you, you may be too late to apply to most outside opportunities, but what you may be able to do is talk to some of the professors here."
    e "Talking to them directly is always a great idea and they can help guide you to anyone who has openings!"
    hide eileenTalk
    show eileen
    p "Okay, thank you so much for your help and I'll let you know how it goes!"
    hide eileen
    show eileenSmile
    e "Of course, thanks for stopping by!"

    hide eileenSmile
    scene p
    "The next day as you are walking out of class thinking of the future, you run into your Cell Biology professor from last year... literally..."

    show smithTalk with vpunch
    s "OW! That hurt!"
    hide smithTalk
    show smith
    p "I am so sorry Dr. Smith, are you alright?"
    hide smith
    show smithTalk
    s "Yes I'm fine, just be more careful next time."
    hide smithTalk
    show smith
    p "Absolutely, I will. I know this isn't the best greeting, but I was hoping we could talk sometime about summer research opportunities on campus?"
    hide smith
    show smithTalk
    s "Uh yeah sure. I'm busy now but if you want to come by during my office hours later today we can discuss the topic."
    hide smithTalk
    show smith
    p "Great, thank you and I'm sorry again!"
    hide smith with dissolve
    scene office
    "A few hours later, you make your way to Dr. Smith's office. You remember him liking you as a student last year, but not sure how much that changed after earlier."
    show smith with dissolve
    p "Hi Dr. Smith, are you available now?"
    hide smith
    show smithTalk
    s "Yes yes, come on in. What was it you wanted to talk about again?"
    hide smithTalk
    show smith
    p "Summer research here at Hendrix. Specifically in the Biology department. And for this summer."
    hide smith
    show smithTalk
    s "It's a little late to be thinking of that, but you may be in luck. I've actually been looking for a student to help me with research over the summer."
    hide smithTalk
    show smith
    p "Oh wow! What are you researching?"
    hide smith
    show smithTalk
    s "Gene expression in Drosophilia, specifically in regards to temperature changes. Interested?"
    hide smithTalk
    show smith
    p "Yeah, absolutely!"
    hide smith
    show smithTalk
    s "Well like I said, don't get your hopes up. I remember you being good at cell bio, but I want to make sure you have enough experience too. Could you send me your resume?"
    hide smithTalk
    show smith
    p "I actually have one with me!"
    hide smith
    show smithTalk
    s "How dandy, let me look over this and we can talk."
    if InternHospital:
        $ qual +=1
    if CellBio:
        $ qual +=1
    if socialjobs + internjobs >=1:
        $ qual +=1
    if qual >=2 and (InternHospital or CellBio) and avgcomp>=35:
        "After a few minutes of awkward silence, he looks up from the piece of paper with an impossible-to-read expression."
        s "You got some great stuff here, and it seems like you really get our Career Competencies. That's a big help in succeeding in life."
        s "Could you come by tomorrow so we can talk about what your duties and goals for the summer will be?"
        hide smithTalk
        show smith
        p "Yeah, for sure, thank you and I can't wait to get started!"
        jump gotstem
    elif qual >=2 and (InternHospital or CellBio) and avgcomp<35:
        "After a few minutes of awkward silence, he looks up from the piece of paper with an impossible-to-read expression."
        s "You have a good amount of work experience, but I'd like to talk to you for a bit and make sure you would be a good fit for my lab first."
        hide smithTalk
        show smith
        p "Yeah of course."
        hide smith
        show smithTalk
        "After a while of talking he gives you the same expressionless look and says..."
        s "I'm sorry [name], but I think that maybe this lab isn't the right thing for you."
        s "It seems like you are still in the process of getting a good understanding of our Career Competencies..."
        s "but my lab is geared towards those who already have a great understanding. Why don't you come back after summer and we'll talk then."
        s "Thank you for coming in, and I hope you have a great summer."
    else:
        s "I'm sorry, [name], but I'm looking for someone who has a bit more experience, especially in the right area."
        s "You should try going to Career Services more and asking what you should do, they always give great answers."
        s "Thank you for coming in, and keep working towards getting that experience and Competencies!"
    hide smith
    jump notin


label compx:
    hide eileenTalk
    show eileen
    p "I think I'm interested in working for Company X, but I don't know how to get into contact with them. What should I do?"
    hide eileen
    show eileenTalk
    e "Oh I love working with Company X! They come to Career Fair every year and they always love to hire Hendrix students."
    e "I can give them a call and see if they have any openings and if so, I'll send you their contact info."
    e "From there you can send in your resume, and cover letter if you have one, and have a nice conversation that hopefully leads to employment!"
    hide eileenTalk
    show eileen
    p "Okay, thank you so much for your help and I'll let you know how it goes!"
    hide eileen
    show eileenSmile
    e "Of course, thanks for stopping by!"


    hide eileenSmile
    "A few days later, Eileen sends you an email saying that there is, in fact, an internship position available! She gives you the contact info of the hiring manager and days later you have an interview."
    scene compxoffice
    "You walk into the giant building and wait around for a while. You wanted to show up early to be professional, but got there a bit too early."
    "After waiting and practicing your introduction over and over, someone walks towards you."
    show compxTalk with dissolve
    x "Hello, I'm Martha, can I help you?"
    hide compxTalk
    show compx
    define x = Character("Company X recruiter", color="#1AA009", what_color="#5EE44D")
    p "Meet, I am Hello, it is [name] to nice you."
    "{i}Wait, what did I just say?{/i}"
    p "Sorry, just nervous. I'm [name], it's nice to meet you, Martha."

    show compxTalk
    x "Haha, no worries, and no reason to be worried! I just wanted to meet with you because Eileen said she had a prospective student interested in this field of work."
    x "We can get started right away, can I please see your resume?"
    hide compxTalk
    p "Of course, here you go!"
    "She looks over it for a couple of minutes and looks back up"
    if Phonathon:
        $ qual +=1
    if TaxVol:
        $ qual +=1
    if stemjobs + socialjobs >=1:
        $ qual +=1
    if qual >=2 and (Phonathon or TaxVol) and avgcomp>=35:
        show compxTalk
        x "This is an impressive resume, you did great getting all of this experience!"
        x "Not only that, but you seem to have a good understanding of the Career Competencies your school uses and how useful they can be."
        hide compxTalk
        p "Wait, you know about those too?"
        show compxTalk
        x "Oh yeah, that's part of the reason I love to hire from Hendrix! The goals and outlines of students there are incredible."
        x "I think you would make a great addition to our team hear, and I can't wait for you to start!"
        hide compxTalk
        p "Thank you so much, I am incredibly excited as well!"
        jump gotintern
    elif qual >=2 and (Phonathon or TaxVol) and avgcomp<35:
        show compxTalk
        x "I see you have a lot of experience here, and all in the right places for a position like this, but I am also interested in Career Competencies."
        x "I talked to Eileen about them a couple of years ago at one of the Career Fairs and I loved them so much I've started to employ them here as well."
        x "If you don't mind, I'd like to talk to continue the conversation to see if you have been able to fully appreciate them."
        hide compxTalk
        p "Yeah, of course."
        "After a while of talking, she says to you..."
        show compxTalk
        x "I think your progress and experience is impressive, but I think I would like to see a bit more of the competencies before I hire you on."
        x "You have done great and I don't think you have long to go before you have the skills in all the right places."
        x "If you would like, please reach out at the end of summer, and perhaps we can revisit the topic and discuss a part-time position during the school year."
        hide compxTalk
    else:
        show compxTalk
        x "I'm sorry, [name], we would appreciate a bit more experience, especially in our field of work, such as finance and people skills."
        x "You should try going to Career Services more and asking what you should do, they always give great answers."
        x "Please feel free to reschedule an interview if you think you've gained more experience and want to come back!"
        hide compxTalk
    hide compx
    jump notin


label gotsocial:
    "You go to Dr. Maslow's office the next day and talk to her about what it is you'll be doing."
    "As it turns out, Elle just gave a brief description and this entails a lot more than you expected."
    "That being said, you are more excited than ever and cannot wait to be able to get the summer started."
    "Once it does, you have an incredible time and end up traveling to three different early civilization locations!"
    "Music History hadn't been a passion of yours before this but now it is one of your favorite things."
    "After you return and work on writing up your research and reports, school starts, and you and Elle are able to talk about everything you did."
    "It was an incredible experience and although it was tough, all the hard work you had done had paid off you can't wait to see what this year has in store."

    jump gameOver

label gotstem:
    "You go by Dr. Smith's office the next day and it immediately begins to feel like a 5th course."
    "He fills you in on the necessary mechanisms, context, and years of research that led him to what the two of you will be working on."
    "It seems extremely daunting at first, and you get worried you somehow faked your way into this position but once the research started..."
    "you had a natural knack for it and loved it! You and Dr. Smith made some pretty interesting results and he even said that it had potential to be..."
    "publishable data within the next year. You think about working with him over the school year, as long as it's not too much."
    "Once the school year starts, you and your friends get together and talk about what all you did."
    "It was an incredible experience and although it was tough, all the hard work you had done had paid off you can't wait to see what this year has in store."


    jump gameOver

label gotintern:
    "Luckily, this didn't turn out to be like your typical internship with coffee and cold calls."
    "Your first day, you started to shadow someone else and immediately began learning about the work the company does and how to do it."
    "You were such a fast learner, you ended up being a month ahead of their planned schedule for you and were working solo within a couple of weeks."
    "Martha was so impressed with your work, she offered you a part-time position over the school year and a position already for next summer."
    "You made some great friends and contacts that summer and told your friends all about it once you got back."
    "It was an incredible experience and although it was tough, all the hard work you had done had paid off you can't wait to see what this year has in store."

    jump gameOver

label notin:
    scene couchRoom
    "You're disappointed, of course, that you didn't get into the position you wanted. It sucks. It hurts. But you're not going to let this stop you."
    "You start looking around for potential positions in your hometown that are hiring. You find two that seem to be a good choice."
    "You first apply to a local startup company that focuses on generating financial software for other businesses. Your next choice is a job at the local CVS."
    if avgcomp >= 35:
        "..."
        "You get an email a couple of weeks later from the startup. They said they were interested and wanted to schedule a phone interview!"
        "You end up having it that day and it goes great. The conversation is easy, you ask meaningful questions, and even manage to sneak a couple of jokes in!"
        "They ended up loving you so much that they hire you on for a temporary position for the summer."
        "Once you get back home from school, you start working there and love it. It started out as a typical intern position. Fetch coffee, do paperwork."
        "As the weeks pass you ask more and more about how things work and they're happy to teach you. You end up learning about software design and go out to meet potential clients."
        "At the end of the summer, you reflect and realize that you're happy you didn't get into the position you wanted because this was an incredible experience."
        "Even though things didn't go the way you expected, they can still turn out to be better."

    elif (avgcomp < 35 and avgcomp >=20):
        "..."
        "You got an email a couple of weeks later from the startup. Sadly, they ended up denying your request."
        "Luckily a few days later, the CVS ended up getting into contact with you and asked if you were still interested!"
        "You ended up spending your summer there. It was an okay time, friendly coworkers and you were getting paid but it didn't feel very fulfilling."
        "There is always an opportunity to improve, however, you have your whole life ahead of you."
    else:
        "..."
        "Somehow, things got even worse. Both jobs denied you. You kept searching around for something to do over the summer but at this point, there wasn't much."
        "You were able to spend your summer relaxing and doing nothing, which was nice after the stress of school, but mostly you were bored."
        "When you went back to school afterward, it felt like a blink and like summer had never happened. It sucked hearing about everyone's awesome jobs and opportunities."
        "It is important to remember though that, as a new Junior in college, you are still young and have plenty of time so don't stress about it too much."
    jump gameOver
