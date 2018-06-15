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
all_instuctions = []
new_instructions = []
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


# --------------------------------- Random movement-------------------------
while True:
    a = 0
    size = 100 - len(instructions)
    print(size)
    print("length of instructions{}".format(len(instructions)))
    while a != 2:
        dot.penup()
        createInstructions(size)
        dotNum += 1
        all_instuctions.append([a, instructions])  # a instuctions

        # print(instructions)
        for i in range(100):
            dead = checkifdead(dead)
            if dead is False:
                # dot.setheading(90)
                # dot.forward(20)
                dead = checkifdead(dead)
                # print(dead)
                dot.setheading(instructions[i][0])
                dot.forward(instructions[i][1])
                step_num = i
            elif dead is True:
                print(dead)
                scores.append([dotNum, i])
                # print(scores)
                # calculate how far it was from the goal on each axis
                xdis, ydis = dis_from_goal()
                # use the above to calculate the actual distance from the goal
                fitness = calc_fitness()
                dot.goto(0, 0)
                dot.clear()
                break

        a += 1
        dead_or_alive_tally.append([a, dead])
        fitnesses.append([a, fitness])

    print("scores{}".format(scores))
    print("dead or alive {}".format(dead_or_alive_tally))
    print("fitnesses {}".format(fitnesses))
    print("all instuctions {}".format(all_instuctions))
    # ------------------------------Find fittest run through ---------------- #
    # add all the fitnesses together
    # divide by number of fitnesses
    # if dot is above the average number of fitnesses then save its instuctions
    fitnesses_total = 0
    for i in range(len(fitnesses)):
        fitnesses_total += fitnesses[i][1]
    fitnesses_total /= len(fitnesses)
    for i in range(len(fitnesses)):
        if fitnesses[i][1] > fitnesses_total:
            saved.append([i, True])
        else:
            saved.append([i, False])
    print("fitnesses total {}".format(fitnesses_total))
    print("saved {}".format(saved))

    # if a set of instuctions was saved , add it to a new list
    for i in range(len(all_instuctions)):
        if saved[i][1] is True:
            new_instructions.append(all_instuctions[i][1])
    print("new instructions".format(new_instructions))

    # find the dot with the least steps taken

    bestDot = scores[0][1]
    best_dot_steps = 0
    best_dot_steps_index = 0
    for i in range(2):
        if scores[i][1] < bestDot:
            best_dot_steps_index = scores[i][0]
            best_dot_steps = scores[i][1]
    # print(scores)
    print("The best score was {}, attempt number {}"
          .format(best_dot_steps, best_dot_steps_index))
    # ------------------------------- Generate new Instructions ------------- #
    # mutate new instructions
    mutation_rate = 3
    for i in range(len(new_instructions)):
        print("length of new instructions {}".format(len(new_instructions)))
        mutate = random.randint(0, 10)
        if mutate < 3:
            new_instructions[i][0] = random.randint(0, 180)
        else:
            new_instructions[i][0] = instructions[i][0]
        if mutate < 5:
            new_instructions[i][1] = random.randint(0, 40)
        else:
            new_instructions[i][0] = instructions[i][0]
    print("new instructions {}".format(new_instructions))
    instructions = []
    print("blank instructions {}".format(instructions))
    for i in range(len(new_instructions)):
        instructions.append([new_instructions[i][0], new_instructions[i][1]])
        print("appended instructions {}".format(instructions))
        print("length of appended instructions {}".format(len(instructions)))


# Calculate fitness as distance from goal/steps taken


# -------------------------------player setup------------------------------ #


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
