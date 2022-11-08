import findBlockByTS

#validates that input is number or letter and number
def inputNumber(message):
  while True:
    userInput = input(message)
    if (userInput.isdigit()):
        return int(userInput)
    if (userInput[1:].isdigit()):
        return int(userInput[1:])
    else:
        print("Not an integer! Try again.")
        continue
     
inputTS = inputNumber("Please enter TS: ")
blockHeight = findBlockByTS.FindLastBlockBeforeTS(inputTS)
print('the N block is: ' + str(blockHeight))