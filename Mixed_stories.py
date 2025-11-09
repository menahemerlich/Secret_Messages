
story1 = "story_A.txt"
story2 = "story_B.txt"

count = 1
f = open("mixed_stories.txt", "r")
# for line in f:
#     print(line)

f1 = open(story1, "a")
f2 = open(story2, "a")

for line in f:
    if count %2 != 0:
        f1.write(line)
        count += 1
    else:
        f2.write(line)
        count += 1





