



label Y1_C1_SLTC:
    "{i}Doesn't look like much is going on here...{/i}"
    return


label Y1_C2_SLTC:
    show smith
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
    hide smith
    $ academic += 5
    $ social += 3
    $ dev += 5
    $ proffesional += 3
    return

label Y2_C1_SLTC:
    "Here there will be an ice cream social where you can meet more people!"
    "Thanks for visiting!"
    return


label Y2_C2_SLTC:
    "Need more here"
    "Thanks for visiting!"
    return
