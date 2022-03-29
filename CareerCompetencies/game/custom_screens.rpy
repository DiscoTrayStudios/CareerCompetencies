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
    text "{size=-5}{color=#000000}Competencies:{/color}{/size}"  xoffset 1100 yoffset 190
    text "{size=-5}{color=#000000}Experience:{/color}{/size}"  xoffset 600 yoffset 300
    if dev:
        text "{size=-5}{color=#000000}Career  and  Self-Development{/color}{/size}" xoffset 1000 yoffset 270
        add bbrain xoffset 880 yoffset 220
    if communication:
        text "{size=-5}{color=#000000}Communication{/color}{/size}"  xoffset 1000 yoffset 350
        add gbrain xoffset 880 yoffset 305
    if thinking:
        text "{size=-5}{color=#000000}Critical Thinking{/color}{/size}" xoffset 1000 yoffset 430
        add obrain xoffset 880 yoffset 390
    if equity:
        text "{size=-5}{color=#000000}Equity and Inclusion{/color}{/size}"  xoffset 1000 yoffset 510
    if leadership:
        text "{size=-5}{color=#000000}Leadership{/color}{/size}"  xoffset 1000 yoffset 590
    if proffesional:
        text "{size=-5}{color=#000000}Professionalism{/color}{/size}"  xoffset 1000 yoffset 670
    if teamwork:
        text "{size=-5}{color=#000000}Teamwork{/color}{/size}"  xoffset 1000 yoffset 750
    if tech:
        text "{size=-5}{color=#000000}Technology{/color}{/size}"  xoffset 1000 yoffset 830


screen hdxtodayb:
    add "UI/hdxtodayb.jpg" xalign 0.5 yalign 0.5
    add "UI/hdxtoday.png" xalign 0.5 yalign 0.2
    $ things = mystore.gettxtblock(curchpt)
    vbox:
        for item in things:
            vbox:
                text "{size=-5}{color=#000000}[item]{/color}{/size}" xoffset 680 yoffset 400
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
        idle "Map/LibraryIdle.png"
        hover "Map/LibraryHover.png"
        if map_interact:
            if visited < allowed:
                action Call("library")

    imagebutton:
        xpos 653
        ypos 251
        idle "Map/SLTCIdle.png"
        hover "Map/SLTCHover.png"
        if map_interact:
            if visited < allowed:
                action Call("sltc")

    imagebutton:
        xpos 665
        ypos 9
        idle "Map/WelcomeCenterIdle.png"
        hover "Map/WelcomeCenterHover.png"
        if map_interact:
            if visited < allowed:
                action Call("welcomecenter")

    text "{i}{b}{size=-5}{color=#00FFFF}SLTC{/color}{/size}{b}{i}" xoffset 685 yoffset 260
    text "{i}{b}{size=-5}{color=#00FFFF}WC{/color}{/size}{b}{i}" xoffset 675 yoffset 50
    text "{i}{b}{size=-5}{color=#00FFFF}Library{/color}{/size}{b}{i}" xoffset 125 yoffset 70
