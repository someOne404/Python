#Partner: jl4nq + js8ra

print("hei")
profession1 = input("A profession: ")
task1 = input("Something people do: ")
profession2 = input("Another profession: ")
profession3 = input("A third profession: ")
where = input("A place: ")
event1 = input("A kind of event: ")

print("hei")
#print("When I was younger I wanted to be a", profession1+".", "I pictured myself at a", event1+".", "One person says", '"'+"I'm a", profession2+'."', "Another says", '"'+"I'm a", profession3+",", "just back from", where+'."', "I say", '"'+"I'm a", profession1+'!"', "With a gasp, everyone turns to me.", '"'+"You're a", profession1+'? Tell us more!"')
#print("Then I met you. Now I know that all", profession1+"s", "do is", task1, "and no one cares. Thank you for showing me the true way.")
#paragraph = "When I was younger I wanted to be a", profession1 + ".", "I pictured myself at a", event1 + ".", "One person says", '"' + "I'm a", profession2 + '."', "Another says", '"' + "I'm a", profession3 + ",", "just back from", where + '."', "I say", '"' + "I'm a", profession1 + '!"', "With a gasp, everyone turns to me.", '"' + "You're a", profession1 + '? Tell us more!"'
print("When I was younger I wanted to be a", profession1 + ".", "I pictured myself at a", event1 + ".", "One person says", '"' + "I'm a", profession2 + '."', "Another says", '"' + "I'm a", profession3 + ",", "just back from", where + '."', "I say", '"' + "I'm a", profession1 + '!"', "With a gasp, everyone turns to me.", '"' + "You're a", profession1 + '? Tell us more!"'
)

def madlib():
    paragraph = "When I was younger I wanted to be a", profession1+".", "I pictured myself at a", event1+".", "One person says", '"'+"I'm a", profession2+'."', "Another says", '"'+"I'm a", profession3+",", "just back from", where+'."', "I say", '"'+"I'm a", profession1+'!"', "With a gasp, everyone turns to me.", '"'+"You're a", profession1+'? Tell us more!"'
    print(paragraph)


#def replace_with(prompt, text_so_far, placeholder):
    """returns new text replacing all placeholders with user response to prompt"""

madlib()
