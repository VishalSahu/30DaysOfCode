
        self.maxDifference = 0

	# Add your code here
    def computeDifference(self):
        min_element = min(self.__elements)
        max_element = max(self.__elements)
        self.maximumDifference = max_element -min_element 
