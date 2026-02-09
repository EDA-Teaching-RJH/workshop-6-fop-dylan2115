#task1 part1 
#make the list 
print("current invintory")
print("-----------------")

sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

print(f"first_sample {sample_bay[0]}")
print(f"last_sample {sample_bay[-1]}")
print(f"sample_total: {len(sample_bay)}")

print("-----------------")

#task1 part2
#write code to transmitt data from rover to hq

print("transmiting data please stand by")
print("--------------------------------")

for i in range(4):
    print(f"Transmitting data for: [{sample_bay[i]}]")

print("data sucsefully transferd")
print("-------------------------")

#task1 part 3 
#make a empty list and fill it with user input 

print("new sample inventory")
print("--------------------")

new_sample_finding = [] 

print("please input the new saples")
print("---------------------------")

for i in range(3):
    
    new_sample = (input("new sample found: "))
    new_sample_finding.append(new_sample)

print(f"new sample: " + str(new_sample_finding))

print("new sample inventory displayed")
print("------------------------------")