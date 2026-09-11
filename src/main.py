from analyzer import Analyzer
from esame import Esame
def main():
    analyzer=Analyzer()
    print("Grade analyzer menu: ")


    while True:
        select=int(input("Select: 1: Calculate exam average - 2: Calculate exam weighted average - 3: Do an average simulation to know witch vote you need - 4: Exit   "))
        if(select==1):
            media=analyzer.calculate_average()
            print(f"Your actual aritmetic average is: {media:.2f}")
        elif(select==2):
            weighted_average=analyzer.calculate_weighted_average()
            print(f"Your actual weighted average is: {weighted_average:.2f}")
        elif(select==3):
            cfu=int(input("How many cfu is the exam: "))
            if cfu < 1:
                print("Cfu value is not valid!")
            else:
                average=int(input("Goal average: "))
            if average > 30 or average <= 0:
                print("Average value is not valid!")
            else:
                print(analyzer.estimate_vote_for_average(average, cfu))
        elif(select==4):
            break
        else:
            pass

if __name__ == "__main__":
    main()