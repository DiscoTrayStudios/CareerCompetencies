## Screen with Stats Button
## Found from https://zeillearnings.itch.io/map-navigation
default resumeShown = False
default regularFont = "cello-sans/hinted-CelloSans-Regular.ttf"
screen mapUI:
    imagebutton:
        xalign 0.0
        yalign 0.0
        xoffset 30
        yoffset 420
        auto "UI/map_%s.png"
        action ToggleScreen("MapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

screen resumeToggle:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 680
        auto "UI/resume_%s.png"
        action [ToggleScreen("ResumeUI"), ToggleScreen("ResumeText")]


label call_resumeUI:
    if resumeShown:
        hide screen ResumeUI
        $resumeShown = False
    else:
        call screen ResumeUI
        $resumeShown = True



screen ResumeUI:
    add "UI/hdxtodayb.jpg" xalign 0.5 yalign 0.5


screen CharMaker:
    add "UI/hdxtodayb.jpg" xalign 0.5 yalign 0.19

screen CharMakerText:
    text "{size=+10}{color=#000000}Character Creator{/color}{/size}" xoffset 800 yoffset 80
    text "{size=+6}{color=#000000}Name: {/color}{/size}" xoffset 540 yoffset 190
    text "{size=+10}{color=#000000}Pronouns: {/color}{/size}" xoffset 540 yoffset 290
    text "{size=+10}{color=#000000}Planned Major:{/color}{/size}" xoffset 540 yoffset 390
    text "{size=+10}{color=#000000}Interested in athletics?{/color}{/size}" xoffset 540 yoffset 490




screen ResumeText:
    text "{size=+10}{color=#000000}[name]{/color}{/size}" xoffset 580 yoffset 190
    text "{size=+1}{color=#000000}Competencies:{/color}{/size}"  xoffset 1000 yoffset 190
    text "{size=+1}{color=#000000}Experience:{/color}{/size}"  xoffset 600 yoffset 300

    text "{size=-6}{color=#000000}Career & Self-Development{/color}{/size}" xoffset 1000 yoffset 235
    add career xoffset 870 yoffset 210
    frame:
        xoffset 1000 yoffset 265
        xsize 300
        bar:
            value StaticValue(dev, 100)

    text "{size=-6}{color=#000000}Communication{/color}{/size}"  xoffset 1000 yoffset 305
    add comm xoffset 880 yoffset 295
    frame:
        xoffset 1000 yoffset 335
        xsize 300
        bar:
            value StaticValue(communication, 100)

    text "{size=-6}{color=#000000}Critical Thinking{/color}{/size}" xoffset 1000 yoffset 395
    add brain xoffset 880 yoffset 379
    frame:
        xoffset 1000 yoffset 425
        xsize 300
        bar:
            value StaticValue(thinking, 100)

    text "{size=-6}{color=#000000}Equity and Inclusion{/color}{/size}"  xoffset 1000 yoffset 487
    add inclusion xoffset 875 yoffset 475
    frame:
        xoffset 1000 yoffset 517
        xsize 300
        bar:
            value StaticValue(equity, 100)

    text "{size=-6}{color=#000000}Leadership{/color}{/size}"  xoffset 1000 yoffset 575
    add lead xoffset 870 yoffset 550
    frame:
        xoffset 1000 yoffset 605
        xsize 300
        bar:
            value StaticValue(leadership, 100)

    text "{size=-6}{color=#000000}Professionalism{/color}{/size}"  xoffset 1000 yoffset 660
    add briefcase xoffset 880 yoffset 645
    frame:
        xoffset 1000 yoffset 690
        xsize 300
        bar:
            value StaticValue(proffesional, 100)

    text "{size=-6}{color=#000000}Teamwork{/color}{/size}"  xoffset 1000 yoffset 740
    add handshake xoffset 880 yoffset 730
    frame:
        xoffset 1000 yoffset 770
        xsize 300
        bar:
            value StaticValue(teamwork, 100)

    text "{size=-6}{color=#000000}Technology{/color}{/size}"  xoffset 1000 yoffset 825
    add laptop xoffset 880 yoffset 815
    frame:
        xoffset 1000 yoffset 855
        xsize 300
        bar:
            value StaticValue(tech, 100)



    ###EXPERIENCE###
    if VolunteerHospital:
        text "{size=-5}{color=#000000}* Volunteered at Hospital{/color}{/size}" xoffset 520 yoffset 375
    if BaileyWorker:
        text "{size=-5}{color=#000000}* Worked at Bailey Library{/color}{/size}" xoffset 520 yoffset 375




screen hdxtodayb:
    add "UI/hdxtodayb.jpg" xalign 0.5 yalign 0.5
    add "UI/hdxtodayl.png" xalign 0.5 yalign 0.2
    $ things = mystore.gettxtblock(curchpt)
    vbox:
        for item in things:
            vbox:
                for t in range(len(item)):
                    vbox:
                        $ a = item[t]
                        if t == 0:
                            text "{size=-6}{color=#000000}{b}[a]{/b}{/color}{/size}" xoffset 580 yoffset 350
                        else:
                            text "{size=-11}{color=#000000}[a]{/color}{/size}" xoffset 610 yoffset 350
                text " "





# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
    call screen MapUI

screen MapUI:
    $ seen_map = True

    add "Map/Hdxblank.png"

    # Could add boolean checkers to see if can press button
    imagebutton:
        xpos 69
        ypos 22
        if atLibrary:
            idle "Map/LibraryAt.png"
        else:
            idle "Map/LibraryIdle.png"
        hover "Map/LibraryHover.png"
        if map_interact:
            if visited < allowed:
                if not atLibrary:

                    action Call("library")

                else:
                    action Call("alreadythere")

    imagebutton:
        xpos 653
        ypos 251
        if atSLTC:
            idle "Map/SLTCAt.png"
        else:
            idle "Map/SLTCIdle.png"
        hover "Map/SLTCHover.png"
        if map_interact:
            if visited < allowed:
                if not atSLTC:

                    action Call("sltc")
                else:
                    action Call("alreadythere")

    imagebutton:
        xpos 665
        ypos 9
        if atWC:
            idle "Map/WelcomeCenterAt.png"
        else:
            idle "Map/WelcomeCenterIdle.png"
        hover "Map/WelcomeCenterHover.png"
        if map_interact:
            if visited < allowed:
                if not atWC:

                    action Call("welcomecenter")
                else:
                    action Call("alreadythere")

    imagebutton:
        xpos 23
        ypos 252
        if atMills:
            idle "Map/MillsAt.png"
        else:
            idle "Map/MillsIdle.png"
        hover "Map/MillsHover.png"
        if map_interact:
            if visited < allowed:
                if not atMills:

                    action Call("mills")
                else:
                    action Call("alreadythere")

    text "{i}{b}{size=-6}{color=#00FFFF}SLTC{/color}{/size}{b}{i}" xoffset 685 yoffset 260
    text "{i}{b}{size=-6}{color=#00FFFF}WC{/color}{/size}{b}{i}" xoffset 675 yoffset 50
    text "{i}{b}{size=-6}{color=#00FFFF}Library{/color}{/size}{b}{i}" xoffset 120 yoffset 70
    text "{i}{b}{size=-6}{color=#00FFFF}Mills{/color}{/size}{b}{i}" xoffset 40 yoffset 450

screen ss:
    add "Tutorial/SaveScreen.png" xalign 0.02 yalign 0.2
label alreadythere:
    "I'm already here..."


screen CharAnswerText:
    if spot > 0:
        text "{size=+7}{color=#000000}[name]{/color}{/size}" xoffset 680 yoffset 190
    if spot > 1:
        text "{size=+7}{color=#000000}[pro]{/color}{/size}" xoffset 760 yoffset 293
    if spot > 2:
        text "{size=+7}{color=#000000}[maj]{/color}{/size}" xoffset 870 yoffset 393
    if spot > 3:
        text "{size=+7}{color=#000000}[ath]{/color}{/size}" xoffset 1000 yoffset 490

screen CharAnswerButtons:
    hbox xalign 0.39 yalign 0.55:
        spacing 60
        frame:
            xpadding 20
            ypadding 10
            textbutton _("Yes"):
                action Call("yesathlete")
        frame:
            xpadding 20
            ypadding 10
            textbutton _("No"):
                action Call("noathlete")






label yesathlete:
    $ ath = "Yes"
    $ decisionMade = True
    return
label noathlete:
    $ decisionMade = True
    $ ath = "No"
    return
