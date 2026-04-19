def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():    
    turn_left()
    move()
    
def right():
    turn_right()
    move()
    turn_right()
    move()


while not at_goal():
    if right_is_clear():
        right()    
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()    
    else:
        turn_left()
        move()
   
    
    

        
        
     
    
        
    


