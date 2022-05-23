#RANDOM PASSWORD GENERATOR IN PYTHON BY HARAJIT ( AT3NA)
import random
lower ="abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol ="~`|•√π÷×¶∆€¥$¢^°{}\%©®™✓[]"
all=lower + upper + number +symbol
length = 10
password = "".join(random.sample(all,length))
print("THE RANDOM PASSWORD IS :",password)