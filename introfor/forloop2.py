#!/usr/bin/env python3
def main():
    """RZFeeser | Alta3 Research
        learning about for logic"""

    # create the list called vendors
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

    # create a second list of strings
    approved_vendors = ["cisco", "juniper", "nig_ip"]
    count = 1
    # CHALLENGE 1
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        print(farm.get("name"), end=":\n")
        for industry in farm.get("agriculture"):
            print(" " + str(count) + ") " + industry)
            count += 1
        count = 1
        print()

    # loop across the list vendors
    for x in vendors:
        print("The vendor is:" + x)  # each time through the loop print value of x
        if x not in approved_vendors:
            print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended.")  # when the loop ends print this

if __name__ == "__main__":
    main()
