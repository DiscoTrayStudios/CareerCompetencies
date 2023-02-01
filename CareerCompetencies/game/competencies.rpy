

label comps:
    scene p
    show eileen at left with dissolve
    show screen compshelper
    $ make_request("show_career_comps")
    "Here are the Career Competencies that we focus on in the game. Working on developing these helpful skills can be extremely beneficial in all aspects of life!"
    "Press any button to go back to the main menu."


screen compshelper:
    add competencies xoffset 950 yoffset 7
