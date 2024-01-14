def read_birth_month(birth_months, b):
    birth_months.append(input(f"Enter birth month {b}: "))

def find_same_birth_month(group1, group2, birth_months):
    if any(month in group1 for month in birth_months):
        return "You have the same birth month with at least one of your classmates."
    else:
        return "You don't have the same birth month with one of your classmates."

def main():
    group1 = []
    group2 = []
    birth_months = []

    for i in range(1, 7):
        if i > 0 and i <= 3:
            read_birth_month(group1, i)
        elif i > 3 and i <= 6:
            read_birth_month(group2, i)

    group1_set = set(group1)
    group2_set = set(group2)

    union = group1_set.union(group2_set)
    intersection = group1_set.intersection(group2_set)
    difference = group1_set.difference(group2_set)

    print("Group 1: ", group1_set)
    print("Group 2: ", group2_set)

    birth_month = input("Enter your birth month: ")
    birth_months.append(birth_month)

    print("Union: ", union)
    print("Intersection: ", intersection)
    print("Difference: ", difference)

    print(find_same_birth_month(group1_set, group2_set, birth_months))

if __name__ == "__main__":
    main()