## Screen with Stats Button
## Found from https://zeillearnings.itch.io/map-navigation
screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png"
        action Jump ("call_mapUI")
        # You may also use the code below depending on your needs.
        # action ShowMenu("mapUI")
        # This was the same code used in the vlog.

# If you just want to show a map that does nothing more than just an indicator, it's good to use ShowMenu.
# If you want to navigate using the map, it's prefered to use "call".
# When in skip mode (tab key on keyboard), this prevents the game to be skipped.
label call_mapUI:
    call screen MapUI

screen MapUI:
    add "Map/Hdxblank.png"


    # Could add boolean checkers to see if can press button
    imagebutton:
        xpos 37
        ypos 12
        idle "Map/LibraryIdle.png"
        hover "Map/LibraryHover.png"
        action Jump("library")

    imagebutton:
        xpos 348
        ypos 135
        idle "Map/SLTCIdle.png"
        hover "Map/SLTCHover.png"
        action Jump("sltc")

    imagebutton:
        xpos 354
        ypos 5
        idle "Map/WelcomeCenterIdle.png"
        hover "Map/WelcomeCenterHover.png"
        action Jump("welcomecenter")
