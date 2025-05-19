#US Medical Insurance Costs Project

# the scope or goal of this project is:
#   - to organize the data into 2 dictionarys: one based on columns and the other based on rows 
#   - determine the total average insurance cost for all individuals
#   - compare it to the individual average costs of females and males
#   - determine the total average insurance cost for smoking individuals 
#   - compare it to the indivdual average costs of smoking females and smoking males

import csv

#lists for each variable in US insurance data
ages = []
sexes = []
bmis = []
kids = []
smokers = []
regions = []
costs = []

#appending data to the lists
with open('insurance.csv') as insurance_file:
    insurance_dict = csv.DictReader(insurance_file)
    for row in insurance_dict:
        ages.append(row['age'])
        sexes.append(row['sex'])
        bmis.append(row['bmi'])
        kids.append(row['children'])
        smokers.append(row['smoker'])
        regions.append(row['region'])
        costs.append(row['charges'])

#defining fnc to create the insurance_data dictionary from the lists (based on columns)
def create_dict(ages, sexes, bmis, kids, smokers, regions, costs):
    insurance_data = {}
    for i in range(0,len(ages)):
        insurance_data['age'] = ages
        insurance_data['sex'] = sexes
        insurance_data['bmi'] = bmis
        insurance_data['children'] = kids
        insurance_data['smoker'] = smokers
        insurance_data['region'] = regions
        insurance_data['charges'] = costs
    return insurance_data

insurance_data = create_dict(ages, sexes, bmis, kids, smokers, regions, costs)
#print(insurance_data)

#creating dictionaries from each row and appending to a bigger insurance_records dictionary (based on rows)

with open("insurance.csv") as insurance_file:
    file_reader = csv.reader(insurance_file)
    column_name = next(file_reader)

    insurance_records = {}
    row_number = 1
    
    for row in file_reader:
        row_dict = {name: value for name, value in zip(column_name, row)}
        insurance_records[row_number] = row_dict
        row_number += 1
#print(insurance_records)

#for the analyses below, the insurance_records dictionary is used more often as the functions are tailored for a row-based dictionary
print("The total number of female and male patients in the survey is " + str(len(sexes)))

females = 0 
males = 0

def count_sexes(females, males):
    for sex in sexes:
        if sex == 'female':
            females += 1
        elif sex == 'male':
            males += 1
    print("The total number of females in the survey is: " + str(females))
    print("The total number of males in the survey is: " + str(males))

count_sexes(females, males)

 
def average_cost(costs):
    total_cost = 0
    for cost in costs:
        total_cost += float(cost)
    avg_cost = total_cost/(len(costs))
    return avg_cost

print("The average cost of insurance is: " + str(average_cost(costs)))

female_costs = []
male_costs = []

for i in insurance_records.values():
    sex = i["sex"]
    charges = i["charges"]
    
    if sex == "female":
        female_costs.append(charges)
    else:
        male_costs.append(charges)

#print(female_costs) #to check if the for statement allocated the costs properly

female_total = 0
male_total = 0

for x in female_costs:
    if x:
        female_total += float(x)

for y in male_costs:
    if y:
        male_total += float(y)

print("The total insurance charges for all surveyed females is " + str(female_total))
print("The total insurance charges for all surveyed males is " + str(male_total))

#using these totals, averages for both now can be calculated using the count of males and females from before
def average_cost_fnc(total, count):
    return round((total/count), 2)

female_avg = average_cost_fnc(female_total, 662)
male_avg = average_cost_fnc(male_total, 676)

print("The average insurance cost for females in the survey is " + str(female_avg))
print("The average insurance cost for males in the survey is " + str(male_avg))


#conclusion: males in the survey have a higher average of insurance charges than females as well as the total average
#in contrast: the females have a lower average insurance cost than the total average. 
#attributes other than sex are most likely at play to explain the higher averages for males

#the analysis is extended to the smoking attribute and applied it to both females and males:

#average charges for smokers in the survey:
smoker_costs = []
smoker_total = 0

for i in insurance_records.values():
    smoker = i["smoker"]
    charges = i['charges']
    
    if smoker == "yes":
        smoker_costs.append(charges)

for x in smoker_costs:
    if x:
        smoker_total += float(x)

smoker_avg = average_cost_fnc(smoker_total, len(smoker_costs))
print("Average insurance costs for smokers in the survey: " + str(smoker_avg))

#the average for smokers is already much greater than the regular average for all patients
#next, calculations are done for the averages for smoking females and smoking males separately:

smoking_females = 0 
smoking_males = 0

smoking_females_charges = []
smoking_males_charges = []

for i in insurance_records.values():
    sex = i["sex"]
    smoker = i["smoker"]
    charges = i['charges']
    
    if sex == "female" and smoker == 'yes':
        smoking_females += 1
        smoking_females_charges.append(charges)
    elif sex == 'male' and smoker == 'yes':
        smoking_males += 1
        smoking_males_charges.append(charges)

print("The total number of smoking females in the survey is: " + str(smoking_females))    
print("The total number of smoking males in the survey is: " + str(smoking_males))

sm_female_total = 0
sm_male_total = 0

for x in smoking_females_charges:
    if x:
        sm_female_total += float(x)

for y in smoking_males_charges:
    if y:
        sm_male_total += float(y)

print("Total charges for smoking females: " + str(sm_female_total))
print("Total charges for smoking males: " + str(sm_male_total))

#averages calculated for smoking females and males using the avg fnc from before:

smoking_female_avg = average_cost_fnc(sm_female_total, 115)
smoking_male_avg = average_cost_fnc(sm_male_total, 159)

print("Average insurance costs for the smoking female: " + str(smoking_female_avg))
print("Average insurance costs for the smoking male: " + str(smoking_male_avg))

#the average for smoking females is slightly lower than the smoker's average, while the average for smoking males is higher than the females as well as the total smoker's average. 
#this is affirming that due to the higher count of smoking males, the higher averages for male overall insurance costs correlates with more smoking male individuals collected in the survey than females.









    