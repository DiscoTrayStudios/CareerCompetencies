label odysseyscript:
    e "The Odyssey Program is one of the many things that make Hendrix unique!"
    e "The purpose of this program is to provide students the resources necessary to learn in a project promoting self-growth."
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
            $ make_request("AC")
            show eileenTalk
            hide eileen
            e "As one of the most venerable instances of giving concrete expression to an idea, art represents an ideal marriage of theory and practice."
            e "Activities that satisfy this category may be creative both conceptually and expressively, as in the production of visual art, poetry, musical compositions, performance art, or the presentation of original creative writing."
            e "They may also be interpretive, as when the artist performs or executes an idea originally developed by someone else, for instance directing a play, performing a dance or musical piece, or interpreting literature orally."
            e "In either case, the activity will demonstrate both understanding of the concept and skill in executing or expressing it to an audience."
            hide eileenTalk
            show eileenSmile
            e "I hope that helps!"
            hide eileenSmile
            jump ocategories

        "Global Awareness":
            $ make_request("GA")
            show eileenTalk
            hide eileen
            e "The aim of the Global Awareness (GA) component of the Odyssey experience is to help students understand and appreciate cultures or environments other than their own."
            e "Toward that end, students are encouraged to engage in learning outside the classroom that broadens their intellectual horizons and deepens their understanding of the political, social, cultural, environmental, spiritual and economic issues affecting the world today."
            e "Global Awareness opportunities are also designed to promote personal growth and self-reliance as well as to provide new perspectives about the student’s own culture or environment."
            e "Any Global Awareness activity for which Odyssey credit is awarded must contain both an immersion component and a reflection component. Exposure to the target culture or environment shall be direct and substantial: one to two weeks of continuous immersion should be viewed as a minimum."
            e "The reflection component may include such things as guided small- and large-group discussions, papers, journals, and oral presentations."
            hide eileenTalk
            show eileenSmile
            e "I hope that helps!"
            hide eileenSmile
            jump ocategories

        "Professional and Leadership Development":
            $ make_request("PL")
            show eileenTalk
            hide eileen
            e "Odyssey experiences that fall in this category may be distinctly professional or leadership-focused; some experiences may well fall into both categories simultaneously."
            e "A Professional Development experience allows the student to develop or refine skills related to a specific professional field or immerses the student in a well-focused exploration of the student’s choice of profession or vocation."
            e "Whether focused on a specific profession or an exploration of career and vocational options, Professional Development experiences include an evaluation of the student’s values, interests, strengths, and abilities as they relate to the field or vocational options being explored."
            e "Leadership Development experiences focus on the development of a student’s unique leadership style as well as enhancing the student’s awareness of group dynamics and the fulfillment of goals through engaging with a group."
            hide eileenTalk
            show eileenSmile
            e "I hope that helps!"
            hide eileenSmile
            jump ocategories

        "Service to the World":
            $ make_request("SW")
            show eileenTalk
            hide eileen
            e "Service to the World experiences engage students in service projects for communities directly involved in providing resources, goods, political access, systemic change, or other services in response to serious human and environmental problems."
            e "Both activities that aim at alleviating present suffering and those that strive for long-term social change are appropriate to this category."
            e "Odyssey credit requires a minimum of 30 on-site service hours, though the 30 hours need not be completed in one semester or consecutive semesters. They may be spread among several projects and over four years."
            hide eileenTalk
            show eileenSmile
            e "I hope that helps!"
            hide eileenSmile
            jump ocategories

        "Undergraduate Research":
            $ make_request("UR")
            show eileenTalk
            hide eileen
            e "Each Odyssey research project, whether curricular or extracurricular, whether on-campus or off-campus, must be conducted under the supervision of a Hendrix faculty member in the field of study related to the research in question."
            e "The faculty supervisor must be consulted in the planning stages of the research and frequently throughout the duration of the project."
            e "Faculty supervisors of undergraduate research projects not only attend to the quality of a student’s research in the discipline but also, as appropriate, help the student use the experience to explore his or her potential as a researcher or other professional in the field of study."
            e "The final product must be shared in a way that is appropriate to the academic discipline and open to an outside audience. This can occur, for example, at a professional meeting, via publication, or at an on-campus venue."
            hide eileenTalk
            show eileenSmile
            e "I hope that helps!"
            hide eileenSmile
            jump ocategories

        "Special Projects":
            $ make_request("SP")
            show eileenTalk
            hide eileen
            e "Special projects allow students to extend, connect, or deepen their liberal arts learning in unique ways. The Special Projects category includes:"
            e "1 - Projects that apply different ways of knowing (e.g., oral, verbal, tactile, imaginative, rational, intuitive, artistic, scientific)."
            e "2 - Projects that bring together the methods, insights, concerns, or subject matters of different disciplines."
            e "3 - Projects that entail non-traditional ways of approaching a topic."
            e "4 - Projects that are in the spirit of engaged learning but do not properly fit in the other Odyssey categories."
            e "Proposals for special projects must include an explanation of how a particular project meets one of the descriptions above."
            e "Although the projects belonging to this category will differ widely, a special project must entail at least 30 hours of work on the part of each student involved."
            e "​​​​​​​The outcome of a special project does not need to be a “product” per se, but proposals must indicate the anticipated outcomes of the project. Projects must incorporate a component that will allow students to reflect on their experience in writing and conversation."
            hide eileenTalk
            show eileenSmile
            e "I hope that helps!"
            hide eileenSmile
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
