### Example 1: 

men = [
    Man(id=0, preference_list=[0,1,2]),
    Man(id=1, preference_list=[2,0,1]),
    Man(id=2, preference_list=[1,0,2]),
]

women = [
    Woman(id=0, preference_list=[0,1,2]),
    Woman(id=1, preference_list=[2,0,1]),
    Woman(id=2, preference_list=[1,0,2]),
]

stable_marriage(men, women)

# Output: {0: 0, 2: 1, 1: 2}


### Example 2:

men = [
    Man(id=0, preference_list=[0,4,1,5,2,3]),
    Man(id=1, preference_list=[4,2,5,3,0,1]),
    Man(id=2, preference_list=[4,1,0,3,2,5]),
    Man(id=3, preference_list=[4,3,2,1,0,5]),
    Man(id=4, preference_list=[4,2,3,1,0,5]),
    Man(id=5, preference_list=[0,1,4,2,3,5]),
]

women = [
    Woman(id=0, preference_list=[0,1,4,2,3,5]),
    Woman(id=1, preference_list=[4,2,3,0,1,5]),
    Woman(id=2, preference_list=[5,1,0,3,4,2]),
    Woman(id=3, preference_list=[5,4,3,2,1,0]),
    Woman(id=4, preference_list=[5,3,4,2,1,0]),
    Woman(id=5, preference_list=[0,1,4,2,3,5]),
]

stable_marriage(men, women)

# Output: {0: 0, 2: 1, 1: 2, 4: 3, 5: 4, 3: 5}

### Example 3:

men = [
    Man(id=0, preference_list=[0,4,1,2,3]),
    Man(id=1, preference_list=[4,2,3,0,1]),
    Man(id=2, preference_list=[4,1,0,3,2]),
    Man(id=3, preference_list=[4,3,2,1,0]),
    Man(id=4, preference_list=[4,2,3,1,0]),
]

women = [
    Woman(id=0, preference_list=[0,1,4,2,3]),
    Woman(id=1, preference_list=[4,2,3,0,1]),
    Woman(id=2, preference_list=[1,0,3,4,2]),
    Woman(id=3, preference_list=[4,3,2,1,0]),
    Woman(id=4, preference_list=[3,4,2,1,0]),
]

stable_marriage(men, women)

# Output: {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}