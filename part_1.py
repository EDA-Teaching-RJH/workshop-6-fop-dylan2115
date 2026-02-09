#task1 part1 
#make the list 

sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

print(f"first_sample {sample_bay[0]}")
print(f"last_sample {sample_bay[-1]}")
print(f"sample_total: {len(sample_bay)}")

#task1 part2
#write code to transmitt data from rover to hq

for i in range(4):
    print(f"Transmitting data for: [{sample_bay[i]}]")

