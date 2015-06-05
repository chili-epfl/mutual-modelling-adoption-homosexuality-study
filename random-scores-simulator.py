
import random

LENGTH_VECTOR=18
NB_TRIADS = 3000

def randomdistribution():

    random.seed()
    
    if random.random() < 0.5:
        return 1
    else:
        return random.randint(2,7)


def modelaccuracy(ma,mb):
    return sum([abs(a-b) for a,b in zip(ma, mb)]) * 1./len(ma)

delta1Sum = 0
delta2Sum = 0
delta3Sum = 0

with open("random-data.csv", "w") as dataset:

    for i in range(NB_TRIADS):

        AGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]
        BAGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]
        CAGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]

        #dataset.write("0," + ",".join(map(str,AGrading + BAGrading + CAGrading)) + "\n")

        BGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]
        ABGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]
        CBGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]

        #dataset.write("0," + ",".join(map(str,BGrading + ABGrading + CBGrading)) + "\n")

        CGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]
        ACGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]
        BCGrading = [randomdistribution() for i in range(LENGTH_VECTOR)]

        #dataset.write("0," + ",".join(map(str,CGrading + ACGrading + BCGrading)) + "\n")

        ABScore = modelaccuracy(BGrading, ABGrading)
        BAScore = modelaccuracy(AGrading, BAGrading)
        ACScore = modelaccuracy(CGrading, ACGrading)
        CAScore = modelaccuracy(AGrading, CAGrading)
        CBScore = modelaccuracy(BGrading, CBGrading)
        BCScore = modelaccuracy(CGrading, BCGrading)

        # delta1
        delta1Sum += abs(ABScore - BAScore)
        delta1Sum += abs(BCScore - CBScore)
        delta1Sum += abs(CAScore - ACScore)


        # delta2
        delta2Sum += abs(ABScore - CBScore)
        delta2Sum += abs(BCScore - ACScore)
        delta2Sum += abs(CAScore - BAScore)


        # delta3
        delta3Sum += abs(ABScore - ACScore)
        delta3Sum += abs(BAScore - BCScore)
        delta3Sum += abs(CAScore - CBScore)


print(delta1Sum/(NB_TRIADS * 3))
print(delta2Sum/(NB_TRIADS * 3))
print(delta3Sum/(NB_TRIADS * 3))
