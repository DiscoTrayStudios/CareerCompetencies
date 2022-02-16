label start:
    # use the code below to show the "map" button
    show screen gameUI
    "The game UI is apprearing."
    "test2"
    return

label house1_pressed:
    scene bg classroom
    "House 1 was pressed!"
    jump after_house_choice

label house2_pressed:
    "House 2 was pressed!"
    jump after_house_choice


label after_house_choice:
    "Tada!"
    return