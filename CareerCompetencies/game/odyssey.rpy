label odysseyscript:
    e "The Odyssey Program is one of the many things that make Hendrix unique!"
    e "The purpose of this program is to provide students the recources necessary in order to learn in a project promoting self-growth."
    e "Odyssey projects can fall under one of 6 categories, which I can talk more about later on."
    e "Throughout your Hendrix career, you will complete at least 3 projects, with each one being in different categories."
    e "It may sound like a lot, but opportunities to earn these credits pop up everywhere! Many courses at Hendrix include Odyssey credit as well!"
    e "I won't talk your ear off explaining all of the ins and outs of the program, but please feel free to visit {a=https://hendrix.sharepoint.com/sites/OdysseyProgram}this website{/a} to learn more!"
    jump ocategories
label ocategories:
    show eileen at left
    hide eileenTalk
    menu:
        "Here are the categories of Odyssey projects. You can find more information {a=https://hendrix.sharepoint.com/sites/OdysseyProgram/SitePages/Odyssey-Categories.aspx}here{/a} as well! Which would you like to learn about?"
        "Artistic Creativity":
            show eileenTalk
            hide eileen
            e "Artistic Creativity description goes here!"
            jump ocategories
        "Global Awareness":
            show eileenTalk
            hide eileen
            e "Global Awarness description goes here!"
            jump ocategories
        "Professional and Leadership Development":
            show eileenTalk
            hide eileen
            e "Professional and Leadership Development description goes here!"
            jump ocategories
        "Service to the World":
            show eileenTalk
            hide eileen
            e "Service to the World description goes here!"
            jump ocategories
        "Undergraduate Research":
            show eileenTalk
            hide eileen
            e "Undergraduate Research description goes here!"
            jump ocategories
        "Special Projects":
            show eileenTalk
            hide eileen
            e "Special Projects description goes here!"
            jump ocategories
        "Leave":
            hide eileen
            hide eileenTalk
            show eileenSmile
            e "Thanks for visiting! If you have any more questions or want more information, please visit {a=https://hendrix.sharepoint.com/sites/OdysseyProgram/SitePages/Odyssey-Categories.aspx}this site!{/a}"
    hide eileen
    hide eileenTalk
    hide eileenSmile
    return
