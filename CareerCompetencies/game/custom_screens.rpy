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





screen ResumeText:
    text "{size=+10}{color=#000000}[name]{/color}{/size}" xoffset 580 yoffset 190
    text "{size=+1}{color=#000000}Competencies:{/color}{/size}"  xoffset 1000 yoffset 190
    text "{size=+1}{color=#000000}Experience:{/color}{/size}"  xoffset 600 yoffset 300
    if dev:
        text "{size=-6}{color=#000000}Career & Self-Development{/color}{/size}" xoffset 1000 yoffset 255
        add career xoffset 870 yoffset 210
    if communication:
        text "{size=-6}{color=#000000}Communication{/color}{/size}"  xoffset 1000 yoffset 325
        add comm xoffset 880 yoffset 295
    if thinking:
        text "{size=-6}{color=#000000}Critical Thinking{/color}{/size}" xoffset 1000 yoffset 415
        add brain xoffset 880 yoffset 379
    if equity:
        text "{size=-6}{color=#000000}Equity and Inclusion{/color}{/size}"  xoffset 1000 yoffset 507
        add inclusion xoffset 875 yoffset 475
    if leadership:
        text "{size=-6}{color=#000000}Leadership{/color}{/size}"  xoffset 1000 yoffset 595
        add lead xoffset 870 yoffset 550
    if proffesional:
        text "{size=-6}{color=#000000}Professionalism{/color}{/size}"  xoffset 1000 yoffset 680
        add briefcase xoffset 880 yoffset 645
    if teamwork:
        text "{size=-6}{color=#000000}Teamwork{/color}{/size}"  xoffset 1000 yoffset 760
        add handshake xoffset 880 yoffset 730
    if tech:
        text "{size=-6}{color=#000000}Technology{/color}{/size}"  xoffset 1000 yoffset 845
        add laptop xoffset 880 yoffset 815


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


label alreadythere:
    "I'm already here..."
