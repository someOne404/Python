def agreement(i1, i2):
    ans = []
    for element in i1:
        if element in i2:
            ans.append(element)
    return ans


def disagreement(i1, i2):
    ans = []
    for element in i1:
        if element not in i2:
            ans.append(element)
    for element in i2:
        if element not in i1:
            ans.append(element)
    return ans


def compatibility(i1, i2):
    number_shared = len(agreement(i1, i2))
    number_not_shared = len(disagreement(i1, i2))
    score = number_shared / (number_shared + number_not_shared)
    return  score


def bestmatch(me, others):
    """Returns a most-compatible person.

    Parameters:
        me:     a list of things I like

        others: a list of pairs, where each pair is a name
                and a list of things that person likes; for example,
                [ ["Scrooge", ["money", "food"]],
                  ["Cratchit", ["family", "heat", "food"]]
                ]
    """
    whom = 'no one'
    comp = -1
    for person in others:
        name, likes = person
        match = compatibility(me, likes)
        if match > comp:
            comp = match
            whom = name
    return whom

#jl4nq