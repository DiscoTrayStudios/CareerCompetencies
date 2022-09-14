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
    jump career

label career:
    hide eileen
    hide eileenSmile
    show eileenTalk at left

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
            e "If you are struggling with what major in or what job you want in the future. You can find more info {a=https://www.hendrix.edu/career/focus2/}here!{/a}"
            e "If you are looking for potential jobs, we have lots of resources on creating resumes and where to look for jobs, such as {a=https://hendrix-csm.symplicity.com/}Hire Hendrix!{/a}"
            e "Be sure to schedule an appointment with us {a=https://www.hendrix.edu/career/career.aspx?id=96915}here!{/a}"
            if not didwhatnext:
                call whatnext
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
                e "Communication allows Hendrix Students understand and leverage technologies ethically to enhance efficiencies, complete tasks, and accomplish goals."
            "Equity and Inclusion":
                e "With Equity and Inclusion in mind, we demonstrate the awareness, attitude, knowledge, and skills required to equitably engage and include people from different backgrounds and cultures."
                e "We also engage in practices that actively challenge the systems, structures, and policies of inequity."
            "Leadership":
                e "Leadership is the leverage the strengths of others to achieve common goals and use interpersonal skills to develop others."
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
        e "With college just starting out this can be a scary time to add even more to your busy schedule, but if you are interested it is always a good idea to join different groups to meet new people, and it can even help advance your skills!"
        show eileenTalk at left
        menu:
            e "If you would like, we have several job and volunteer opportunities that are available!"
            "Sure, why not!":
                call whatnext1
            "Not right now, but thank you.":
                show eileenTalk
                hide elieen
                e "Sounds good."

    if curchpt==2:
        show eileenTalk
        e "Bippity Boppity"
    return



label whatnext1:
    hide eileen
    show eileenTalk
    e "Okay, let's talk about our options and find if any of them will be a good fit for you!"
    hide eileenTalk
    show eileen
    "After some discussion, you are able to narrow it down to two options. A part-time student worker postion at the Bailey Library, or volunteer work at the local Conway Regional Health Clinic."
    p "I'm not really sure which to decide between these two. What do you think?"
    hide eileen
    show eileenTalk
    e "Well, as far as hours go they're pretty much identical. The Bailey Library position is paid and is a work-study position. Volunteering at the hospital is great for pre-med though, and you can get Service to the World Odyssey credit."
    e "It really depends on what you value more, although there really are no options and any experience is good experience."
    show eileenTalk at left
    menu:
        e "Which do you choose?"
        "Word-Study at Bailey Library":
            $ BaileyWorker = True
        "Volunteer at the Hospital":
            $ VolunteerHospital = True
    e "That's a good choice, and you can even put this on your resume!"
    hide eileenTalk
    show eileen
    p "Thank you so much for your help, I'll keep you updated on how it goes!"
    show eileenTalk
    hide eileen
    e "Of course, that's why we're here. Any more questions about anything?"
    return
