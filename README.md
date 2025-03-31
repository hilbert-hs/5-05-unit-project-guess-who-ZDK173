[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18940317)
# 5.05-Unit-Project-Guess-Who

In Guess Who, you'll be building a text-based version of the classic board game. Dictionaries will be the key to this project...

##Overview

The game should store information on at least 5 different characters. Each character should have a name and 4 other traits (like gender, age, height, hair color). These traits should overlap: that is, at least 2 characters should share the same age, another 2 the same hair color, etc.

When the game begins, a character should be randomly selected by the program. The player can ask for 2 pieces of information about the random character's traits, then has to make a guess as to who was picked.

### Behavior / Commands

* `list`: list out all the character's names
* `gender/age/height/hair`: asks for a piece of information about a specific trait
* `guess`: guess a character
* `help`: display's all commands
* `quit`: exits the game

### Implementation Details

To store and accesss the information, you'll use a dictionary of dictionaries, which will allow for quick and direct access. Your keys can be the characters' names, and the values will be dictionaries of their traits. 

## Example Output

```
>>>What would you like to do? list
mike: 
['Male', '15', "6'1", 'Blonde']
liv: 
['Female', '25', "5'11", 'Blonde']
lisa: 
['Female', '15', "5'10", 'Red']
linda: 
['Female', '25', "5'7", 'Brown']
bill: 
['Male', '20', "5'5", 'Brown']
>>>What would you like to do? age
25 
>>>What would you like to do? hair 
Brown 
>>>What would you like to do? guess liv 
You lost...
```
```
>>>What would you like to do? gender 
Female 
>>>What would you like to do? height 
5'7
>>>What would you like to do? guess linda 
You won!
```

## Grading Scheme / Rubric

| <strong> Functional Correctness (behavior) </strong>      |           |       |
|-----------------------------------------------------------|-----------|-------|
| List Command                                              | 5 points  |       |
| gender / age / haie / etc. (or other traits)              | 10 points |       |
| guess command                                             | 5 points  |       |
| help command                                              | 3 points  |       |
| quit command                                              | 2 points  |       |
| <strong> Subtotal </strong>                               | 25 points |       |
| <strong> Technical Correctness </strong>                  |           |       |
| Correct use of dictionaries                               | 15 points |       |
| Correct use of variables and game loop                    | 10 points |       |
| Correct use of printing / formatting                      | 10 points |       |
|  <strong> Sub Total </strong>                             | 35 Points |       |
|  <strong> Project Total </strong>                         | 60 points |       |


