class Node:
    def __init__(self,data):
        self.val = data
        self.p  = self.left = self.right = None
    def levo(self):
        if self:
            opt = []
            queue = []
            queue.append(self)
            while not queue.empty():
                
                
                
                
def levoconstruct(LOlist):
    c = 1
    if not LOlist.empty():
        root = Node(LOlist[0])
        while(c<len(LOlist)):
            a=b=False
            if 2*c+1<len(LOlist): a=True
            if 2*c+2<len(LOlist): b=True
            if a:
                root.left = Node(LOlist[2*c+1])
            if b:
                root.right = Node(LOlist[2*c+2]) 
            c+=1
    return root
    
                   
#             buildtree(root,LOlist)
# def buildtree(root,LOlist):
#     if root:
        
        

        