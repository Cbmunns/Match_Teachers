from collections import OrderedDict

#dictionaries/hash for quick access simple info               
courses  = {303:'DataStructures', 490:'Web Development', 505:'Algorithms'}            
teachers = {1   : 'John',   2 : 'Alexa',   3 : 'Ralph'}
topics =   {1   : 'Arrays', 2 : 'Vectors', 3 : 'Queues', 4 : 'Javascript', 5 : 'HTML', 6 : 'PHP', 7 :'Dynamic', 8 : 'Greedy', 9 :'DFS'}

#multidimensional arrays/lists to hold and traverse multiple values
            #j     0    1    2    3     4    5    6    7    8    i
courseTopics = [[303, 303, 303, 490,  490, 490, 505, 505, 505], #0 CourseID 
                [  1,   2,   3,   4,    5,   6,   7,   8,   9], #1 TopicID
                [ .2,  .5,  .3,  .15, .75,  .1,  .4,  .4,  .2]] #2 PercentageWeight


            #j   0  1  2  3  4  5  6  7  8    i
expertise    = [[1, 2, 3, 4, 5, 6, 7, 8, 9], #0 TopicID 
                [1, 2, 1, 2, 1, 3, 2, 3, 3], #1 ProfessorID
                [2, 5, 5, 4, 5, 3, 1, 3, 3]] #2 LvlExpertise

#create a value for total num of matches
numOfMatches = len(courses)

#multidimensional array/list to hold all the professors compentency in each course
results = [[0 for x in range(numOfMatches)] for x in range(numOfMatches)]
matched = [[0 for x in range(numOfMatches)] for x in range(numOfMatches)]

    
def findProficiency(): #O(n*m) n is the number of topics and m is the total number of topics professors know
    #iterate through all values in each coloumn  
    for j in range(0, len(courseTopics[0])):
        #then set them to workable values
        thisCourse = courseTopics[0][j]
        thisTopic  = courseTopics[1][j]
        thisWeight = courseTopics[2][j]    
        #iterate professors
        for k in range(0,len(expertise[0])):
            #if the teacher knows the topic
            if (expertise[0][k] == thisTopic):
                #calculate their knowledge*weight of topic 
                #and add to their overall proficiency in the course                
                results[list(courses.keys()).index(thisCourse)][(expertise[1][k])-1] += ((expertise[2][k])/5)*thisWeight
                
def findMatch(): #O(m^2) where m is the number of courses/professors
    #for each course/professor
    for i in range(0,numOfMatches):
        #find the current overall highest proficiency first        
        highestValue = max(map(max, results))
        #then find it's course
        for y in range(0, numOfMatches):            
            if(max(results[y]) == highestValue):
                idexHighestCourse = y
                       
        #find the index/professor with highest proficiency
        idex = results[idexHighestCourse].index(highestValue)

        #convert index to ProfessorID
        ProfessorID = idex + 1 

        #set professors proficiency 
        value = results[idexHighestCourse][idex]

        #print course name, professor name, rounded percentage            
        print(list(courses.values())[idexHighestCourse],teachers[ProfessorID], str(round(value,2) *100) + '%')
        #set course id, professor id, rounded percentage
        matched[i] = list(courses.keys())[idexHighestCourse], ProfessorID, str(round(value,2) *100) + '%'
        #clear values for selected professors to remove them from future choices
        for x in range(0,numOfMatches):

            results[x][idex] = 0  
            

#find professor and course combo    
def courseToTeach():
    findProficiency()
    print(results)
    findMatch()
    
#run code
courseToTeach()
print (matched)


            
expertise    = [[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 9, 9], #0 TopicID 
                [1, 3, 1, 2, 3, 1, 2, 1, 3, 1, 2, 3, 1, 3, 1, 3], #1 ProfessorID
                [2, 4, 3, 5, 4, 5, 4, 5, 3, 5, 1, 4, 3, 5, 1, 1]] #2 LvlExpertise

           
courseTopics = [[303, 303, 303, 490,  490, 490, 505, 505, 505], #0 CourseID 
                [  1,   2,   3,   4,    5,   6,   7,   8,   9], #1 TopicID
                [ .2,  .5,  .3,  .15, .75,  .1,  .4,  .4,  .2]] #2 PercentageWeight

results = [[0 for x in range(numOfMatches)] for x in range(numOfMatches)]
matched = [[0 for x in range(numOfMatches)] for x in range(numOfMatches)]

numOfMatches = len(courses)

#find professor and course combo    
def courseToTeach():
    findProficiency()
    print(results)
    findMatch()
    
#run code
courseToTeach()
print (matched)
