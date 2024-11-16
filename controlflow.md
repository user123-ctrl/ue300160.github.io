# control flow

## if-else statements

x = 10
y = 4

if x > y:
    print("hurray!")
    print("x is indeed greater than y")
    print(x-4)
    for i in range(x):
        print("oh happy day!")
else:
    print("sigh...")

## combining if/else with loops

list_of_words = [
    "sponge", "bob", "square",
    "[pants", "cat", "spider", "squid", "starfosh",
    "snake", "circle", "duck", "chicken", 'fword',
    "laptop", "potato", 'eight', "foods", "coffee",
    "apple", "bread", "mitosis"
]

for word in list_of_words:
    if word == "fword":
        continue
    else:
        print(word)
