

#You have been deployed as a data vault manager. As part of your assignment, you are required to create Pandas data list. Using your pandas create a list of Dataframes using Python for the following products:
#
#Chips: Simba, Lays
#Cooldrinks: Coke, Fanta
#Chocolates: Cadbury, Tex
#Pies: Pepper Steak, Chicken
#Fruit: Pear, Apple, Orange
#Cupcakes: vanilla, chocolate
#Veggies: spinach, cabbage

import pandas as pd

data = pd.DataFrame({"Chips":["Simba", "Lays",""], 
                   "Cooldrinks":["Coke","Fanta",""], 
                   "Chocolates":["Cadbury", "Tex",""],
                   "Pies":["Pepper Steak", "Chicken",""],
                   "Fruit":["Pear", "Apple", "Orange"],
                   "Cupcakes":["Vanilla", "Chocolate",""],
                   "Veggies":["Spinach", "Cabbage",""]})


def UI(data, column):
 
    ints = [val for val in range(len(data[column].unique()))]
    choices = list(zip(ints, data[column].unique()))
    print("Which row to print?" % column)
    for v in choices:
        print("%s.  %s" % (v))
    user_input = input("Answer: ")
    user_answer = [val[1] for val in choices if val[0]==int(user_input)][0]
    print("'%s' = %s\n" % (column, user_answer)) 
    return user_answer

def main():

    chips_input = UI(data=data, column="Chips")
    cooldrink_input = UI(data=data, column="Cooldrinks")
    data_new = data.loc[(data["Chips"]==chips_input)&(data["Cooldrinks"]==cooldrink_input)]
    print(data_new)

if __name__ == "__main__":
    main()