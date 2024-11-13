fibinacci_number=[1,1]
for i in range(8):
  fibinacci_number.append(fibinacci_number[i]+fibinacci_number[i+1])
print(fibinacci_number)