import random as r

def garments():
    #choices we have
    categories = ["adult", "kid"]
    outfits = ["trousers", "shirts", "dress pants", "dress shirts"]
    sleeves = ["full", "half"]
    kids_sizes = ["small", "medium", "large"]
    adult_sizes = ["large", "extra large"]
    adults_clr = ["blue", "black"]
    kids_clr = ["blue", "green", "yellow"]
    
    #variable to keep the count of number of items purchased
    count = 0

    print("Category\t  Outfit\t\tColor\tSleeves\tSize" )

    for i in range(20):

        #choosing randomly
        category = r.choice(categories)
        outfit = r.choice(outfits)
        sleeve = r.choice(sleeves)

        if category == "adult":
            size = r.choice(adult_sizes)
            clr = r.choice(adults_clr)

        else:
            size = r.choice(kids_sizes)
            clr = r.choice(kids_clr)    

       
        #our choices
        if category == "adult": 
            if outfit == "dress pants" and size == "large" and clr == "blue":
                print("*", end="")
                count +=1   
                #incrementing count with each matched item
                           
            elif outfit == "shirts" and clr == "black" and sleeve == "half":
                print("*", end="")
                count +=1

        elif category == "kid":
            if outfit == "trousers" and clr == "blue" and size == "medium":
                print("*", end="")
                count +=1

            elif outfit == "dress shirts" and clr == "green" and size == "medium" and sleeve == "half":
                print("*", end="")
                count +=1

            elif outfit == "shirts" and clr == "yellow" and size == "large" and sleeve == "full":
                print("*", end="")
                count +=1


        #printing the item generated

        if outfit == "shirts" or outfit == "dress shirts":
            print(f"{category.title()} \t\t {outfit} \t\t{clr}\t{sleeve}\t{size} ") 

        elif outfit == "pants" or "dress pants":
            print(f"{category.title()} \t\t {outfit} \t\t{clr} \t\t{size}")

    print(f"Total items purchased: {count}")    

garments()
