init python in mystore:


    #string stuff
    txtdict = {}
    chapters = []
    chapters.append(1)
    chapters.append(2)

    txtdict[1] = [["Welcome Center", "Come by the Welcome Center to get an overview of the Hendrix experience!"], ["Library", "Meet and Greet for new students! Come meet some new friends!"], ["SLTC", "Ice cream social! Come meet some people!"], ["Resume Tip #1","Get new experiences!", "Always be on the lookout for new opportunities you would enjoy!"], ["Good Vibe of the Day", "'Thinking: the talking of the soul with itself.'", "           -Plato"]]
    txtdict[2] = [["Welcome Center", "Tour Guides needed! No experience needed!"], ["Library", "Come study for finals with others with Peer Learning!"], ["Mills", "Interested in the Humanities? Come by for an overview of our program!"], ["Resume Tip #2", "Use Reverse Chronological Order!", "List most recent experiences and work backward"], ["Good Vibe of the Day", "'Love and desire are the spirit's wings to great deeds.'", "              -Johann Wolfgang von Goethe"]]
    txtdict[3] = [["Library", "Learn about studying abroad!"], ["SLTC", "Dr. Smith will be discussing research opportunities in the Natural Sciences!"], ["Mills", "Showing of Hendrix Cats!"], ["Resume Tip #3", "Let the job post be your guide! Job descriptions can help you", "decide which skills/experiences to highlight on your resume"], ["Good Vibe of the Day", "'If life were predictable it would cease to be life,", "and be without flavor'", "          -Eleanor Roosevelt"]]
    txtdict[4] = [["Welcome Center", "Tour Guides, come to the Welcome Center."], ["Library", "Student Study Session! Come learn with peers!"], ["Mills", "Wanting summer research in the social sciences? If so, come by Mills!"], ["Resume Tip #4", "Perfect your descriptions!","Read a lot of good resumes and work with a Career Services professional"], ["Good Vibe of the Day", "Today is a good day to try", "         -Quasimodo"]]
    txtdict[5] = [["Library", "Come to the Library for some Peer Learning!"], ["Welcome Center", "Financial aid seminar!"], ["Resume Tip #5", "Keep a master list of all experiences separate from your resume.", "This allows you to edit your resume quicker and easier."], ["Good Vibe of the Day", "What we achieve inwardly will change outwardly reality.", "         -Plutarch"]]
    txtdict[6] = [["Welcome Center", "Remember, don't park your vehicles here!"], ["SLTC", "Come volunteer to help with parents weekend!!!!"], ["Mills", "Did you know you can study in the Mills Library too?!"], ["Resume Tip #6", "Don't use an online template!!", "Make your resume yours."], ["Good Vibe of the Day", "Failure is only the opportunity to begin again.", "         -Uncle Iroh"]]


    def gettxt(chapter, i):
        return txtdict[chapter][i]

    def gettxtblock(chapter):
        return txtdict[chapter]
