label summer:
    $ curchpt = 6
    $ atLibrary = False
    $ atMills = False
    $ atSLTC = False
    $ atWC = False
    $ hdxtodayseen = False

    scene pecanCourtBackground
    show eileenTalk
    e "Is this thing working?"
    hide eileenTalk
    show eileen
    "I guess it is!"
    hide eileen
    show eileenTalk
    e "Good to hear!"
    
    jump gameOver
