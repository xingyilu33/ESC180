# do a docstring double check with the rubric

def get_cur_hedons(): # returns the number of hedons that the user has accumulated so far
    global hedons
    return hedons

def get_cur_health(): # returns the number of HP that the user has accumulated so far 
    global health_points
    return health_points

def offer_star(activity): # if 3 stars are offered within the span of 2 hours, the user loses interest, and will not get additional hedons due to stars for the rest of the simulation
    # offers start for particular activity -- > this function offers the user a star for engaging in the exercise (activity)
    global star_activation
    global star_timer2 # second star timer
    global star_timer # first star timer
    global time
    global star1
    global star2
    global star_time
    global bored

    if bored == True:
        return

    if star_timer >= 120:
        star_timer = 0
        star1 = False
    if star_timer2 >= 120:
        star_timer = 0
        star2 = False

    if star_timer <= 0 and star_timer2 <= 0:
        star_activation = activity
        star1 = True
 
    elif star_timer > 0 and star_timer2 <= 0:
        star_activation = activity
        star2 = True

    elif star_timer > 0 and star_timer2 > 0:
        bored = True


def perform_activity(activity, duration): # duration is an integer # activity has to be running, textbooks, or resting
    global hedons
    global health_points
    global star_activation
    global time
    global star_timer
    global star_timer2
    global star1
    global star2
    global tired
    global run_counter

    if activity == "running" or activity == "textbooks":
        if time < 120:
            tired = True
        if time >= 120: 
            tired = False

    if tired == True:# running and carrying textbooks both give -2 hedons per minute if the user is tired and isn't using a star 
        if activity == "running" and run_counter + duration > 180:
            health_points = health_points + (180-run_counter)*3 + (duration-(180 - run_counter)) #how much can be applied left to the 3* multiplier and then that remainder applied to the 1* multiplier
            run_counter = run_counter + duration                                              
            if star_activation == "running": # since duration > 180 > 10
                hedons = hedons + (30 - 2*(duration))
            elif star_activation != "running":
                hedons = hedons + duration*-2
        time = 0
        if activity == "running" and run_counter <= 180:
            health_points = health_points + duration*3
            run_counter = run_counter + duration
            if star_activation == "running" and duration > 10:
                hedons = hedons + (30 - 2*(duration))
            if star_activation == "running" and duration <= 10:
                hedons = hedons + duration
            elif star_activation != "running":
                hedons = hedons + duration*-2 # Since running while being tired with no star activation will result in a loss of -2 hedons per minute.
            time = 0

        if activity == "textbooks":
            health_points = health_points + duration*2
            if star_activation == "textbooks" and duration > 10:
                hedons = hedons + (30 - 2*(duration))
            if star_activation == "textbooks" and duration <= 10:
                hedons = hedons + duration
            if star_activation != "textbooks":
                hedons = hedons + duration*-2
            time = 0
            run_counter = 0

        if activity == "resting": # we assume stars cannot be given for resting
            run_counter = 0


    if tired == False:
        if activity == "running" and run_counter + duration > 180:
            health_points = health_points + (180-run_counter)*3 + (duration-(180 - run_counter)) # because health points duration is greater than 180 minutes, the first 180 minutes gives 3 hp/minute (540) and each subsequent gives 1 hp/min
            run_counter = run_counter + duration
            if star_activation == "running":
                hedons = hedons + (50 - 2*(duration-10)) # since duration is already > 180 > 10, hedon addition is (3 star boost+2)*10 minutes of running and then subtracting 2*duration for each subsequent minute. 
            if star_activation != "running":
                hedons = hedons + 20 - 2*(duration-10) # since duration is already > 180 > 10, hedon addition is 2*10 minutes of running and then -2*duration for each subsequent minute
            time = 0
        if activity == "running" and run_counter <= 180:
            health_points = health_points + duration*3 # health points for running is 3 health points/minute up to 180 minutes and since duration <= 180, the penalty will not be applied.
            run_counter = run_counter + duration
            if star_activation == "running" and duration > 10: # since the duration is bigger than 10, the star bonus will maximize at 30 hedons 
                hedons = hedons + (50 - 2*(duration-10)) # if the duration is greater than 10, then running will give a -2 hedon penalty
            elif star_activation == "running" and duration <= 10:
                hedons = hedons + duration*5 # since the duration is smaller than 10, the star bonus and activity will sum to a +5 hedon addition for each minute
            elif star_activation != "running" and duration > 10: # since the duration is larger than 10 and there's no star bonus, the hedon addition will maximize at 2*10 minutes of running then -2*duration for each subsequent minute
                hedons = hedons + 20 - 2*(duration-10)
            elif star_activation != "running" and duration <= 10:
                hedons = hedons + duration*2 #since the duration is smaller than 10 and there is no star bonus, there will be no -2 penalty and the hedon addition will just 2*duration
            time = 0

        if activity == "textbooks":
            health_points = health_points + duration*2 # carrying textbooks gives 2 health points per minute
            if star_activation == "textbooks" and duration > 20:
                hedons = hedons + (50 - (duration-20)) # since the duration is larger than 20 and there's a star bonus, the hedon addition will maximize at 3 star bonus*10 minutes + 1 hedon*20 minutes = 50 then subtract the penalty for each subsequent minute
            elif star_activation == "textbooks" and 10 < duration <= 20:
                hedons = hedons + (duration + 30) # since the 30 hedons has been applied from the star bonus already, the remaining hedons gained is just the 1 hedon per minute
            elif star_activation == "textbooks" and duration <= 10:
                hedons = hedons + duration*4 # since the star bonus adds 3 hedons per minute and carrying textbooks adds 1 hedon per minute, the total is 4 hedons per minute
            elif star_activation != "textbooks" and duration > 20:
                hedons = hedons + (20 - (duration-20))
            elif star_activation != "textbooks" and duration < 20:
                hedons = hedons + duration
            time = 0
            run_counter = 0
            
        if activity == "resting": # we assume stars cannot be given for resting
            run_counter = 0
    
    if star1 == True:
        star_timer = star_timer + duration

    if star2 == True:
        star_timer2 = star_timer2 + duration

    
    time = time + duration
    star_activation = None


def star_can_be_taken(activity): # returns true if and only if a star can be used to get more hedons for activity (activity) --> # stars do not affect HP
    if activity == "running" and star_activation == "running":
            return True
    elif activity == "textbooks" and star_activation == "textbooks":
            return True
    else:
        return False
    
def most_fun_activity_minute(): # returns the activity that would give the most hedons if the person performed it for one minute at the curret time. We assume two stars can't be given at the same time.
    global tired
    global time
    global star_activation

    if time < 120:
        if star_activation == "running":
            return "running"
        elif star_activation == "textbooks":
            return "textbooks"
        else:
             return "resting"
    
    if time >= 120:
        if star_activation == "running":
            return "running"
        elif star_activation == "textbooks":
            return "textbooks"
        else:
             return "running"

def initialize():
    global health_points 
    global hedons
    global star_activation
    global tired
    global time
    global star_time
    global star_timer
    global star_timer2
    global run_counter
    global bored
    global star1
    global star2
    health_points = 0 # the user starts out with 0 health points
    hedons = 0 # the user starts out with 0 hedons
    tired = False
    star_activation = False
    time = 120 # starting a backwards counter at 2 hours as the time for the activity cooldown
    star_timer = 0 # starting an upwards counter for 2 hours as the time for the star cooldown
    star_timer2 = 0
    run_counter = 0
    bored = False
    star_time = 0
    star1 = False
    star2 = False

if __name__ == "__main__":
    initialize()
    perform_activity("running", 30) 
    print(get_cur_hedons()) #-20 = 10 * 2 + 20 * (-2)
    print(get_cur_health()) # 90 = 30 * 3 
    print(most_fun_activity_minute()) #resting 
    perform_activity("resting", 30) 
    offer_star("running") 
    print(most_fun_activity_minute()) # running 
    perform_activity("textbooks", 30) 
    print(get_cur_health()) # 150 = 90 + 30*2
    print(get_cur_hedons()) #-80 =-20 + 30 * (-2)
    offer_star("running") 
    perform_activity("running", 20) 
    print(get_cur_health())  # 210 = 150 + 20 * 3
    print(get_cur_hedons()) #-90 =-80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170) 
    print(get_cur_health())  # 700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons()) #-430 =-90 + 170 * (-2)
