from analyzer import Analyzer
from esame import Esame
def main():
    analyzer=Analyzer()
    print("Grade analyzer menu: ")


    while True:
        select=int(input("Select: 1) Calculate arithmetic average - 2) Calculate weighted average - 3) Estimate the grade needed for a target average - 4) Exit: "))
        if(select==1):
            media=analyzer.calculate_average()
            print(f"Your current arithmetic average is: {media:.2f}")
        elif(select==2):
            weighted_average=analyzer.calculate_weighted_average()
            print(f"Your current weighted average is: {weighted_average:.2f}")
        elif(select==3):
            cfu=int(input("How many CFU is the exam worth: "))
            if cfu < 1:
                print("Invalid CFU value!")
            else:
                average=float(input("Target average: "))
            if average > 30 or average <= 0:
                print("Invalid average value!")
            else:
                print(analyzer.estimate_vote_for_average(average, cfu))
        elif(select==4):
            break
        else:
            pass

if __name__ == "__main__":
    main()