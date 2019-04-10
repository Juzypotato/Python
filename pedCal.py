
def pedCal(Q1,Q2,P1,P2):
    ans = ((Q2-Q1)/Q1)/((P2-P1)/P1)
    return (ans)


if __name__ == '__main__':
    var = input("Please enter Q1, Q2, P1, P2 separated by '-' : ").split('-')
    ped = pedCal(float(var[0]),float(var[1]),float(var[2]),float(var[3]))
    print("Your PED is : ",abs(ped))
