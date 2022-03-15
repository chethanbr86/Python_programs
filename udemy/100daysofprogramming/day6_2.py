# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
def mov():
    turn_left()
    turn_left()
    turn_left()

def jump():    
    move()
    turn_left()
    move()
    mov()
    move()
    mov()
    move()
    turn_left()

while not at_goal():
    jump()
    
#if at_goal() is not defined
# x=0
# while x>0:
#     jump()
#     x = x - 1









################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
