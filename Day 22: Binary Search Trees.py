

    def getHeight(self,root):
        if not root:
            return -1
        if not root.left and not root.right:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height,right_height)+1
        #Write your code here

