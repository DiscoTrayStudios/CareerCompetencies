label Y1_S2_C1:
    scene sltcLobby
    show bob with dissolve
    b "Welcome to the Career and Internship Fair!"
    $ dev = True
    menu:
        "What fields are interested in checking out?"
        "Medical":
            jump Y1_S2_C2
        "Humanities":
            jump Y1_S2_C3
        "Leave":
            jump begin
        # NEED MORE


#Medical
label Y1_S2_C2:
    b "This is for medical."
    jump begin


#Humanities
label Y1_S2_C3:
    b "This is for Humanities"
    jump begin
