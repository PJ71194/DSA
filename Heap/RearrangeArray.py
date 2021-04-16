import heapq

def rearrangeArray(arr):
	n = len(arr)
	
	charFreqHeap = []
	freq = {}
	for char in arr:
		if char in freq:
			freq[char] += 1
		else:
			freq[char] = 1

	for key in freq:
		heapq.heappush(charFreqHeap, (0 - freq[key], key))
	
	prevChar = ''
	prevCharFreq = 0
	resultantStr = ""
	while charFreqHeap:
		freq, char = heapq.heappop(charFreqHeap)
		resultantStr += char
		if prevChar != '' and prevCharFreq > 0:
			heapq.heappush(charFreqHeap, (0 - prevCharFreq, prevChar))

		prevChar = char
		prevCharFreq = 0 - freq - 1
	
	if prevCharFreq > 0:
		resultantStr = "Not possible"

	return resultantStr

for _ in range(int(input())):
	str = input()
	print(rearrangeArray(str))
		