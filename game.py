# Date created: 9/04/18
# Author:Matthew King
# Version: 0.2
# What it does: A game that makes dots move towards a goal.
# the dot who reaches the goal first wins
# == == == == == == == == == == == == == == == == == == == == == == == #

# imports
import random
import turtle as tp

screen = tp.Screen()

# create turtles
obstacle = tp.Turtle()  # turtle that will draw obsatcles
obstacle.hideturtle()
# obstacle._tracer(0)

goal = tp.Turtle()  # Turtle that will draw the goal
goal.hideturtle()
# goal._tracer(0)

dot = tp.Turtle()  # turtle that be the dot (player)
dot.pendown()

# variables
fitness = 0  # how well a turtle did
dotNum = 1
scores = []
dead = False
dead_or_alive_tally = []
fitnesses = []  # list of the fitnesses of each dot
instructions1 = []
instructions2 = []
saved = []

# setup
goal_positions = [[0, 400], [0 - 20, 400],
                  [0 - 20, 390], [20, 390], [20, 400], [0, 400]]
goal.penup()
goal.goto(0, 400)
goal.pendown()
goal.begin_fill()
for i in range(5):
    goal.goto(goal_positions[i][0], goal_positions[i][1])


goal.end_fill()

# Obstacle setup
# obstacle_positions = [[50, 200], [50, 150], [0 - 50, 150], [0 - 50, 200]]
i = 0
obstacle.penup()
obstacle.goto(-50, 200)
obstacle.pendown()
obstacle.begin_fill()
obstacle.goto(50, 200)
obstacle.goto(50, 150)
obstacle.goto(0 - 50, 150)
obstacle.goto(0 - 50, 200)
obstacle.end_fill()

# -------------------------------Player random movement ------------------- #
instructions = []

goal_hit = False


def checkifdead(Dead):
    # if it's outside the screen height
    if dot.ycor() > 400 or dot.ycor() < 0 - 400:
        Dead = True
    # if it's is outside the screen width
    elif dot.xcor() > 400 or dot.xcor() < 0 - 400:
        Dead = True
    # if it's inside the obstacle (easiest way to do collision detection)
    elif dot.xcor() > 0 - 50 and dot.xcor() < 50:
        if dot.ycor() > 150 and dot.ycor() < 200:
            Dead = True
        else:
            Dead = False
    return Dead


def checkifhitgoal(goal):
    if dot.xcor() > -20 and dot.xcor() < 20:
        if dot.ycor() > 390 and dot.xcor() < 400:
            goal = True
            scores.append([goal, step_num])


def createInstructions(size, x=180, y=40):
    for i in range(size):
        angle = random.randint(0, x)
        # print(angle)
        randomY = random.randint(0, y)
        # print(randomY)
        instructions.append([angle, randomY])


def dis_from_goal():
    xdis = 390 - dot.xcor()
    print("xdis {}".format(xdis))
    if dot.ycor() > 0:
        ydis = 20 - dot.ycor()
        print("ydis {}".format(ydis))
    else:
        ydis = -20 - dot.ycor()
        print("ydis {}".format(ydis))
    return xdis, ydis


def calc_fitness():
    distance_from_goal = (xdis ** 2) + (ydis ** 2)
    distance_from_goal = distance_from_goal ** 0.5
    fitness = distance_from_goal / step_num
    return fitness


deleted = 1
# --------------------------------- Random movement-------------------------
while True:
    for a in range(2):
        print("a {}".format(a))
        dot.penup()
        createInstructions(100)
        dotNum += 1
        if deleted == 1:
            instructions1.append(instructions)
        if deleted == 2:
            instructions2.append(instructions2)
        # print(instructions)
        for i in range(100):
            dead = checkifdead(dead)
            if dead is False:
                # dot.setheading(90)
                # dot.forward(20)
                dead = checkifdead(dead)
                # print(dead)
#                 if a == 0:
#                     print("1", instructions1[0][i][0])
#                 else:
#                     print("2", instructions2[0][i][1])
                if a == 0:
                    dot.setheading(instructions1[0][i][0])
                    dot.forward(instructions1[0][i][1])
                else:
                    dot.setheading(instructions2[0][i][0])
                    dot.forward(instructions2[0][i][1])
                step_num = i
            elif dead is True:
                print(dead)
                step_num = i
                # print(scores)
                # calculate how far it was from the goal on each axis
                xdis, ydis = dis_from_goal()
                # use the above to calculate the actual distance from the goal
                fitness = calc_fitness()
                dot.goto(0, 0)
                dot.clear()
                break
        dead_or_alive_tally.append([i, dead])
        fitnesses.append([i, fitness])

    print("scores{}".format(scores))
    print("dead or alive {}".format(dead_or_alive_tally))
    print("fitnesses {}".format(fitnesses))

    # attempt 2
    # make the code loop twice, save the instructions of each time

    # choose the best of the 2 run throughs
    if fitnesses[0] > fitnesses[1]:
        instructions1 = []
        deleted = 1
    else:
        instructions2 = []
        deleted = 2
    # mutate the best 1
    if deleted == 1:
        for i in range(100):
            chance = random.randint(0, 10)
            if chance > 3:
                instructions2[0][i][0] = random.randint(0, 40)
                print("mutated {}".format(instructions2[0][i][0]))
            elif chance > 4:
                instructions2[0][i][1] = random.randint(0, 180)
                print("mutated {}".format(instructions2[0][i][1]))
    else:
        for i in range(100):
            chance = random.randint(0, 10)
            if chance > 3:
                instructions1[0][i][0] = random.randint(0, 40)
                print("mutated {}".format(instructions1[0][i][0]))
            elif chance > 4:
                instructions1[0][i][1] = random.randint(0, 180)
                print("mutated {}".format(instructions1[0][i][1]))
    fitnesses = []

    # run the new instuctions
    # randomly generate a new 1
    # repeat

    # -------------------------------player setup--------------------------- #

    # what to do when keys are pressed
    # Commented out because it's not nessescary
    # speed = 1

    # def travel():
    #   dot.forward(speed)
    #   screen.ontimer(travel, 2)

    # screen.listen()
    # screen.onkey(lambda: dot.setheading(90), 'Up')
    # screen.onkey(lambda: dot.setheading(180), 'Left')
    # screen.onkey(lambda: dot.setheading(0), 'Right')
    # screen.onkey(lambda: dot.setheading(270), 'Down')

    # travel()

    # screen.mainloop()
