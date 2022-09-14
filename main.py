phrase = "What a wonderful day to program hello kandhu"
total = 0
for x in phrase:
    if x != " ":
        total += 1
print(total)

s = "what if we went to the zoo"
total = 0
for x in s:
    if x in ['a','e','i','o','u']:
        total +=1
print(total)

word = "onomatopoeia"
# count the num of o

count = 0
for x in word:
    if x == 'o':
        count = count + 1
print("The num of time o appears in the word " + word + " " + "is: " + str(count))

nums = [9, 3, 8, 11, 5, 29, 2]
#getting the max value from the list

max_value = nums[0]
for x in nums:
    if x > max_value:
        max_value = 9
print(max_value)


nums = [9, 3, 8, 11, 5, 29, 2]
#getting the smallest number
min_value = nums[0]

for x in nums:
    if x < min_value:
        min_value = x
print(min_value)

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for x in words:
    if len(x) > 3:
        num_words +=1
print(num_words)

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words:
    if word[-1] == 'e':
        word = word + 'd'
        past_tense = past_tense + [word]
    else:
        word = word + 'ed'
        past_tense = past_tense + [word]
print(past_tense)





