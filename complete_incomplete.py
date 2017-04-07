def complete(learning_outcomes):
    complete = {}

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
    # return "\n".join(complete.keys())
