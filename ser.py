with open('data.txt') as f:
    lines = f.readlines()

tm_dict = {}  #to make a list of time zones
code_dict = {} #to make the list of telephone codes
for line in lines:
    parsed = line.split("\t")
    parsed_tm = parsed[2].split("\n")
    code_dict[parsed[0]] = parsed[1]
    tm_dict[parsed[0]] = parsed_tm[0]

# [print(item) for item in tm_dict.keys()]
# print("\n\n")
# [print(item) for item in code_dict.keys()]

def find_ans(n, dict):
    try:
        if dict == "code":
            a = code_dict[n]
            print(a)
            return a
        elif dict == "time":
            a = tm_dict[n]
            return a
    except:
        return "Invalid Country Name"
