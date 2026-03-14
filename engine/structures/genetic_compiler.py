from engine.structures import Gen


def compilation(mgs, act, inf):
    M = []
    A = []
    I = []
    for i in range(len(mgs)):
        morphogen = Gen.Morphogenes(mgs[i][0], mgs[i][1], mgs[i][2], mgs[i][3])
        M.append(morphogen)

    for i in range(len(act)):
        action = Gen.Actions(act[i][0], act[i][1], act[i][2])
        A.append(action)

    for i in range(len(inf)):
        information = Gen.Informations(inf[i][0])
        I.append(information)

    return Gen.DNA(M,A,I)