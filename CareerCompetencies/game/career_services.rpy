label careerIntro:

    $ didwhatnext = False

    hide eileen
    show eileenTalk
    e "Welcome to Career Services! How may we help you today?"
    hide eileenTalk
    show eileen
    p "I'm not sure, what do you do here?"
    hide eileen
    show eileenTalk
    e "We're all about providing inclusive and insightful Career Services to prepare, inspire, and empower all Hendrix students for future success."
    $ been_to_career_services = True


label career:
    hide eileen
    hide eileenSmile
    show eileenTalk at left
    $ make_request(f"visited_CS_chpt{curchpt}")
    menu:

        e "Here are some of the services we provide. Which would you like to learn about?"
        "Career and Internship Fair":
            show eileenTalk
            hide eileen
            e "The Career and Internship Fair is an exciting event that takes place each spring semester."
            e "Career Services help introduce a wide range of organizations on campus to help students connect to potential internship and employment opportunities."
            e "We highly recommend everyone, no matter their class, experience, or future goals, to attend!"
            jump career
        "Four Year Plan":
            show eileenTalk
            hide eileen
            e "We help provide a guideline for students to help them achieve their fullest potential while at Hendrix."
            e "We have planned out things that will help you succeed, no matter where you are on your Hendrix journey."
            e "If you would like, you can find more information {a=https://www.hendrix.edu/career/career.aspx?id=97251}at this site!{/a}"
            jump career
        "Career Competencies":
            show eileenTalk
            hide eileen
            e "One of the many great things about Hendrix College is that every student is given a breadth of knowledge that equips them to handle any obstacle"
            e "This knowledge is broken down into 8 categories that we call our 'Career Competencies'."
            jump ccompetencies
        "I'm not sure what to do next, what do you suggest?":
            show eileenTalk
            hide eileen
            e "Being unsure is part of the college experience, that's why we're here to help!"
            e "If you are struggling with what major or what job you want in the future. You can find more info {a=https://www.hendrix.edu/career/focus2/}here!{/a}"
            e "If you are looking for potential jobs, we have lots of resources on creating resumes and where to look for jobs, such as {a=https://hendrix-csm.symplicity.com/}Hire Hendrix!{/a}"
            e "Be sure to schedule an appointment with us {a=https://www.hendrix.edu/career/career.aspx?id=96915}here!{/a}"
            if not didwhatnext:
                call whatnext from _call_whatnext
                $ didwhatnext = True
            jump career
        "Leave":
            hide eileen
            hide eileenTalk
            show eileenSmile

            e "Thanks for visiting! If you have any more questions or want more information, please visit {a=https://www.hendrix.edu/career/}this site!{/a}"
    hide eileen
    hide eileenTalk
    hide eileenSmile
    return

    label ccompetencies:
        $ make_request("ccompetencies")
        hide eileenTalk
        show eileen at left
        menu:
            e "Here is a list of the Career Competencies, want to learn about any of them? For more info, click {a=https://www.hendrix.edu/career/career.aspx?id=95102}here{/a}."
            "Critical Thinking":
                e "Critical thinking is the sound reasoning to analyze issues, make decisions, and overcome problems."
            "Career and Self-Development":
                e "With Career and Self-Development Hendrix students proactively identify and articulate their skills, strengths, knowledge, and experiences relevant to their career goals."
                e "They also identify areas necessary for personal and professional growth, navigate career opportunities, and network to build relationships."
            "Communication":
                e "Communication assists Hendrix Students to articulate thoughts and ideas clearly and communicate their findings effectively and persuasively."
                e "They can do this through written, oral, experiential, visual, or other appropriate methods."
            "Equity and Inclusion":
                e "With Equity and Inclusion in mind, we demonstrate the awareness, attitude, knowledge, and skills required to equitably engage and include people from different backgrounds and cultures."
                e "We also engage in practices that actively challenge the systems, structures, and policies of inequity."
            "Leadership":
                e "Leadership is the leverage of the strengths of others to achieve common goals and use interpersonal skills to develop others."
                e "One uses empathetic skills to motivate and guide others. They organize, prioritize, and delegate work."
            "Professionalism":
                e "Hendrix students demonstrate personal accountability and effective work habits. This is professionalism."
                e "They demonstrate integrity and ethical behavior, act responsibly with the interests of the larger community in mind, and can learn from their mistakes."
            "Teamwork":
                e "At Hendrix, we build and maintain collaborative relationships to work effectively toward common goals. They appreciate diverse viewpoints & understand the importance of shared responsibilities."
            "Technology":
                e "In the modern world we must understand and leverage technologies ethically to enhance efficiencies, complete tasks, and accomplish goals."
            "I've learned enough":
                hide eileen
                show eileenSmile
                e "I hope you found these helpful!"
                hide eileenSmile
                jump career
        jump ccompetencies
                # e "{b}{size=+6}Critical Thinking{/size}{/b}\nHendrix students exercise sound reasoning to analyze issues, make decisions, and overcome problems."
                # e "{b}{size=+6}Career and Self-Development{/size}{/b}\nHendrix students proactively identify and articulate their skills, strengths, knowledge, and experiences relevant to their career goals."
                # e "{b}{size=+6}Career and Self-Development (cont.){/size}{/b}\nThey identify areas necessary for personal and professional growth, navigate career opportunities, and network to build relationships."
                # e "{b}{size=+6}Communication{/size}{/b}\nHendrix Students understand and leverage technologies ethically to enhance efficiencies, complete tasks, and accomplish goals."
                # e "{b}{size=+6}Equity and Inclusion{/size}{/b}\nHendrix students demonstrate the awareness, attitude, knowledge, and skills required to equitably engage and include people from different backgrounds and cultures."
                # e "{b}{size=+6}Equity and Inclusion (cont.){/size}{/b}\nThey engage in practices that actively challenge the systems, structures, and policies of inequity."
                # e "{b}{size=+6}Leadership{/size}{/b}\nHendrix students leverage the strengths of others to achieve common goals and use interpersonal skills to develop others."
                # e "{b}{size=+6}Leadership (cont.){/size}{/b}\nThey use empathetic skills to motivate and guide others. They organize, prioritize, and delegate work."
                # e "{b}{size=+6}Professionalism{/size}{/b}\nHendrix students demonstrate personal accountability and effective work habits. They demonstrate integrity and ethical behavior,"
                # e "{b}{size=+6}Professionalism (cont.){/size}{/b}\nact responsibly with the interests of the larger community in mind, and can learn from their mistakes."
                # e "{b}{size=+6}Teamwork{/size}{/b}\nHendrix students build and maintain collaborative relationships to work effectively toward common goals. They appreciate diverse viewpoints & understand the importance of shared responsibilities."
                # e "{b}{size=+6}Technology{/size}{/b}\nHendrix students understand and leverage technologies ethically to enhance efficiencies, complete tasks, and accomplish goals."

label whatnext:
    if curchpt==1:
        show eileenTalk
        e "A good place to start with anything career-related, is working on first impressions and this means creating a Resume and a Cover Letter."
        e "Have you by chance already made these before?"
        hide eileenTalk
        show eileen
        p "I have made a resume, although admittedly it is pretty empty. I'm not really sure what a cover letter is though."
        hide eileen
        show eileenTalk at left
        menu:
            e "That's okay! If you would like, we can go over cover letters and create one together? You can always find more information {a=https://www.hendrix.edu/career/printresourcesandmore/}here!{/a}"
            "Yeah, that sounds great!":
                call whatnext1 from _call_whatnext1
            "I think I'm okay, but thank you!":
                e "Of course, feel free to come back anytime. New opportunities pop up all the time and this is the place to find them!"

    if curchpt==2:
        show eileenTalk
        e "With college just starting out this can be a scary time to add even more to your busy schedule, but if you are interested, it is always a good idea to join different groups to meet new people, and it can even help advance your skills!"
        show eileenTalk at left
        menu:
            e "If you would like, we have several jobs and volunteer opportunities that are available!"
            "Sure, why not!":
                call whatnext2 from _call_whatnext2
            "I'm good, but thank you.":
                show eileenTalk
                hide elieen
                e "Please come back again, we always have new stuff going on so it's a different experience every time!"

    if curchpt==3:
        show eileenTalk
        e "Volunteering is always a great way to both build experience in new fields, while also showing you like to serve your community!"
        e "Every year when tax season is upon us, we have students volunteer with AR Asset Builders to help others file their taxes."
        e "In doing so, you'll also get certification and tax experience!"
        menu:
            e "Sound like something you may be interested in?"
            "Let's crunch some numbers!":
                call whatnext3 from _call_whatnext3
            "Doesn't sound like my thing, thank you though!":
                e "Please come back again, we always have new stuff going on so it's a different experience every time!"

    if curchpt==4:
        show eileenTalk
        e "Is there anything, in particular, I can help you out with?"
        hide eileenTalk
        show eileen
        p "I was thinking of getting a part-time job on campus. I kind of want to try something new but I'm not sure where to start."
        hide eileen
        show eileenTalk
        e "HireHendrix is your best friend then, you can always look on there to see if anyone is hiring for student worker positions!"
        e "Let's see if there is anything available now."
        e "So it seems like, with your schedule, your best bets are going to be an assistant for the Theatre and Dance department or a TA position for Cell Biology."
        e "Based on your grades from last year, and your courses, you should be qualified enough to get either one of those."
        show eileenTalk at left
        menu:
            e "Are you interested in them?"
            "Yeah, let's hear more about them.":
                call whatnext4 from _call_whatnext4
            "I think I'm good, thank you though.":
                e "Please come back again, we always have new stuff going on so it's a different experience every time!"

    if curchpt==5:
        show eileenTalk
        e "Do you have any more questions?"
        hide eileenTalk
        show eileen
        p "Yeah I'm trying to make some quick money with not a large time commitment. What do you suggest?"
        hide eileen
        show eileenTalk
        e "Our Fall Phonathon is starting soon! It only takes up about 6 hours a week but you can work more if you'd like, and it's only a 5-week position."
        e "It's also a great way to build people skills and talk to old alumni!"
        show eileenTalk at left
        menu:
            e "Would you like to sign up for the Phonathon?"
            "Sure!":
                call whatnext5 from _call_whatnext5
            "No thank you.":
                e "Please come back again, we always have new stuff going on so it's a different experience every time!"
    if curchpt==6:
        $ make_request("what_next_6")
        e "That's about all I have for you. I'm sorry but there are no opportunities at the moment."
        e "Go ahead and take this time to reflect on the choices you've made and plan for the future!"
        e "See ya later!"
    return


label whatnext1:
    $ make_request("what_next_1")
    show eileenTalk
    e "Great! Although they are not always required, cover letters are a great way to present yourself and motivate employers to invite you in for an interview."
    e "It is important to note that when made effectively, cover letters and resumes work together to enhance them both!"
    e "Whereas resumes are typically bullet points and straight to the point, a cover letter is a more in-depth introduction into who you are and why you should be considered."
    e "These usually consist of multiple paragraphs, and you can think of splitting it into four main sections:"
    e "Catching the reader's attention. Communicating skills and experiences. Supporting with specifics. Compelling reader to act."
    e "While cover letters are usually tailored to the specific position you are applying for, it never hurts to build a template for yourself. Let's work on making one now!"
    e "Please come back again, we always have new stuff going on so it's a different experience every time!"
    $ CV = True
    return
label whatnext2:
    $ make_request("what_next_2")
    hide eileen
    show eileenTalk
    e "Okay, let's talk about our options and find if any of them will be a good fit for you!"
    hide eileenTalk
    show eileen
    "After some discussion, you narrow it down to two options. A part-time student worker position at the Bailey Library, or intern work at the local Conway Regional Health Clinic."
    p "I'm not really sure which to decide between these two. What do you think?"
    hide eileen
    show eileenTalk
    e "Well, as far as hours go they're pretty much identical. The Bailey Library position is paid and is a work-study position. Interning at the hospital is great for pre-med though and is really good on resumes."
    e "It really depends on what you value more, although there really are no bad options and any experience is a good experience."
    show eileenTalk at left
    menu:
        e "Which do you choose?"
        "Work-Study at Bailey Library":
            $ BaileyWorker = True
            $ Jobs +=1
            $ socialjobs +=1
        "Intern at the Hospital":
            $ InternHospital = True
            $ Jobs +=1
            $ stemjobs +=1
    show eileenTalk
    e "That's a good choice, and you can even put this on your resume!"
    hide eileenTalk
    show eileen
    p "Thank you so much for your help, I'll keep you updated on how it goes!"
    show eileenTalk
    hide eileen
    e "Please come back again, we always have new stuff going on so it's a different experience every time!"
    return


label whatnext3:
    $ make_request("what_next_3")
    show eileenTalk
    hide eileen
    e "Luckily this is a fairly straightforward and fast process. You will just have to study for a short exam and upon completion, you'll be certified to help others."
    hide eileenTalk
    show eileen
    p "Sounds great. What exactly is this good for besides volunteer hours?"
    show eileenTalk
    hide eileen
    e "This certification is proof that you were verified to responsibly handle others' finances and help others as well. This can be looked highly favorable on a resume."
    e "Especially with corporate or office jobs, they love to see this sort of thing."
    e "Besides, volunteer work like this can go towards getting a Service to the World Odyssey credit!"
    hide eileenTalk
    show eileen
    p "Sweet, thank you!"
    e "Of course, please come back again, we always have new stuff going on so it's a different experience every time!"
    $ TaxVol = True
    $ internjobs +=1
    $ Jobs +=1
    return


label whatnext4:
    $ make_request("what_next_4")
    hide eileenTalk
    show eileen
    p "What are those jobs like?"
    show eileenTalk
    hide eileen
    e "The theatre assistant consists of setting up productions and projects and helping bring them down as well. They seem to have a lot of variety in work and multiple options."
    e "The Cell Bio lab TA will help set up labs, help students during lab, and be available for questions."
    show eileenTalk at left
    menu:
        e "Which would you like to apply for?"
        "Theatre Assistant":
            $ Theatre = True
            $ Jobs +=1
            $ socialjobs +=1
        "Cell Bio TA":
            $ CellBio = True
            $ Jobs +=1
            $ stemjobs +=1
    show eileenTalk
    e "Good choice, good luck and I'm sure you'll get it!"
    e "Please come back again, we always have new stuff going on so it's a different experience every time!"
    return


label whatnext5:
    $ make_request("what_next_5")
    show eileenTalk
    hide eileen
    e "Okay awesome! I hope you have a great time and learn a lot!"
    e "Please come back again, we always have new stuff going on so it's a different experience every time!"
    $ Phonathon = True
    $ Jobs +=1
    $ internjobs +=1
    return
