# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
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

for i in range(6):
    jump()
    










################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
