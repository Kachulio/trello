import pprint


def mark_skills():
    global learning_outcomes
    learning_outcomes = {
    '01': {'Version Control': 'N'},
    '02': {'Agile Methodology': 'N'},
    '03': {'Programming Logic': 'N'},
    '04': {'Object-oriented Programming': 'N'},
    '05': {'Test-Driven Development': 'N'},
    '06': {'Databases': 'N'},
    '07': {'HTTP and Web Services': 'N'},
    '08': {'Front-end Development': 'N'},
    '09': {'Growth Mindset': 'N'},
    '10': {'Relationship Building': 'N'},
    '11': {'Ask Questions': 'N'},
    '12': {'Motivation and Commitment': 'N'},
    '13': {'Adaptability': 'N'},
    '14': {'Seeks Feedback': 'N'},
    '15': {'Speaking to be Understood': 'N'},
    '16': {'Writing Professionally': 'Y'},
    '17': {'Git': 'N'},
}

    pprint.pprint(learning_outcomes)
    print("")
    print("")
    print("")
    print ("To mark a skill enter the skill number and followed by OK")
    print("")
    print("")
    boot_camper = input("For example [ 01 OK ]: ")
    print("")
    status = boot_camper.split()
    key = status[0]
    value = status[1]



    if value == "OK":
        print (value)
        for j in learning_outcomes:
            if j == key:
                for k in learning_outcomes[j]:
                # print k

                    for i in learning_outcomes[j][k]:
                    # print i,
                        # print(learning_outcomes[j])
                        learning_outcomes[j][k] = 'Y'

        pprint.pprint (learning_outcomes)
        return learning_outcomes


def complete():
    learning_outcomes
    complete = {}
    incomplete = {}

    for j in learning_outcomes:
        # print j
        for k in learning_outcomes[j]:
            # print k
            for i in learning_outcomes[j][k]:
                # print i,
                if i == 'N':
                    # print i
                    # incomplete = {k:v for x, v in k if k[i] == 'Not done'}
                    incomplete[k] = 'Not done'
                elif i == 'Y':
                    # complete = {k:v for x, v in k if k[i] == 'done'}
                    complete[k] = 'done'

    # return "\n".join(incomplete.keys())
    return "\n".join(complete.keys())

def incomplete(learning_outcomes):
    complete = {}
    incomplete = {}

    for j in learning_outcomes:
        # print j
        for k in learning_outcomes[j]:
            # print k
            for i in learning_outcomes[j][k]:
                # print i,
                if i == 'N':
                    # print i
                    # incomplete = {k:v for x, v in k if k[i] == 'Not done'}
                    incomplete[k] = 'Not done'
                elif i == 'Y':
                    # complete = {k:v for x, v in k if k[i] == 'done'}
                    complete[k] = 'done'

    return "\n".join(incomplete.keys())
    #return "\n".join(complete.keys())


def shell():
    print("")
    print("")
    print("BOOTCAMP PROGRESS TRACKER!")
    print("")
    print("")
    print("WELCOME!")
    print("")
    print("")

    while True:

        print("1. Mark a skill as Done")
        print("2. View list of completed skills")
        print("3. View list of incomplete skills")
        print("4. View progress")

        print("")
        print("")
        user = input("Enter a number[eg. 1] to perform an action: ")
        if user == "1":
            mark_skills()
        elif user == "2":
            complete()
        elif user == "3":
           incomplete()
        #elif user == "4":
         #   progress()
        else:
            print("Invalid input!")
            user = input("Enter a number[eg. 1] to perform an action: ")
        



if __name__=="__main__":
    shell()


__author__ = 'Justin M'
