#Two Number Sum
#Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
#If any two numbers in the input array sum up to the largest target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array. 
#You can assume that there will be at most one pair of numbers sum up to the target sum. 
#Sample input:
#array=[3, 5, -4, 8, 11, 1, -1, 6]
#targetSum=10

##Solution 1 | O(n^2) time | O(1)space
def twoNumberSum(array, targetSum):
	for i in range(len(array) - 1):
		firstNumber = array[i]
		for j in range(i + 1, len(array)):
			secondNumber = array[j]
			if firstNumber + secondNumber == targetSum:
				return [firstNumber, secondNumber]
	return []

#Solution 2 | O(n) | O(n) space
def twoNumberSum(array, targetSum):
	numberHashTable = {}
	for number in array: 
		potentialMatch = targetSum - number
		if potentialMatch in numberHashTable:
			return [potentialMatch, number]
		else:
			numberHashTable[number] = True
	return []

#Solution 3 | O(nlog(n)) | O(1) space
def twoNumberSum(array, targetSum):
	array.sort()
	left = 0
	right = len(array)-1
	while left < right: 
		currentSum = array[left] + array[right]
		if currentSum == targetSum:
			return [array[left], array[right]]
		elif currentSum < targetSum:
			left +=1
		elif currentSum > targetSum:
			right -=1
	return []
