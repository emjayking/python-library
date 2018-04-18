# Ionic calulator
""" this will hopefully calculate what the outcome of a neutralisation reaction will be when the user selects an acid and base following text prompts."""
print("initalising neutralisation calculator v0.4.1")
print("loading database")
# list of all possible ingrediants in the reaction
acids = ["hydrochloric acid", "sulfuric acid", "nitric acid"]
# because a base is a combination of a metal and an something else I'm going to split the base in too two parts

basestart = ["ammonium", "sodium", "magnesium", "potassium", "silver", "lithium", "calcium", "copper", "lead", "iron(2)", "berrylium", "zinc", "barium", "aluminium", "iron(3)"]
baseend = ["oxide", "hydroxide", "carbonate"]


""" these are the possible salts that can be formed in the neutralisation process"""
salts = ["chloride", "sulfate", "nitrate"]

""" the reaction also forms byproducts such as water and carbon dioxide depending on the non metalic part of the base used"""
byproducts = ["water", "water and carbon dioxide", "water and carbon dioxide"]

# now the code finds out what acid and base the user wants to combine and determines the results
print("database bootup successfull... ")
tutorial = input("would you like a list of all the available acids and bases? if you would then type 'yes' ")
try:
    tutorial.lower()
    tutorial.strip()
except ValueError:
    # I put this 'nothing' variable in here because otherwise my IDLE had major issues running an empty except statement
    nothing = "do nothing"
if tutorial == "yes":
    print("""this is a list of available acids: {}
        Bases are comprised of
        two main parts, the first
        part can be made from any of
        these: {} and the second part
        can be made from any of these {}""".format(acids, basestart, baseend))
print("opening command line...")
while True:
    acidused = input("What acid is being used?"
                     )
    acidused.lower()
    if acidused in acids[0] or acidused in acids[1] or acidused in acids[2]:
        print("acid successfully retrieved")
        # determines what the salt will be formed bsaed on the acid used
        if acidused in acids[0]:  # hydrochloric
            salt = salts[0]  # chloride
        elif acidused in acids[1]:  # sulfuric
            salt = salts[1]  # sulfate
        else:  # it must be nitric acid
            salt = salts[1]  # nitrate

    else:
        print("acid retrieval failed, please try again")
        continue
    baseused = input("what base is being used?"
                     )
    baseused.lower()
    basecomponents = baseused.split(" ")
    # because the first part of an acid is always a metal. and that metal remains unchanged throughout the reaction i'm simply going to take the first part of the base (the metal) and put it in a variable called 'metal'

    metal = basecomponents[0]

    """this while loop finds out what number the base is within our list and then determines what this will cause the reation to do based on a list called 'byproducts'  and stores that information in the variable 'byproduct' """
    i = 0
    while i != 4:
        if i == 4:
            print("Error 605 base retrevial failed at attempt no.{} ... reason: base not in database".format(i))
        if basecomponents[1] in baseend[i]:
            byproduct = byproducts[i]
            i = 4
        else:
            print("Error 404 base not found, attempt {} commencing".format(i + 1))
            i += 1

    print("running tests, collecting results. printing results")

    # joins it all together to show the final reaction
    print("{} + {} -> {} {} + {}".format(acidused, baseused, metal, salt, byproduct))
    # asking the user if they want to try again
    repeat = input("would you like to continue? please type 't' or 'f'")
    if repeat == "t":
        continue
    else:
        print("shutting down")
        break
