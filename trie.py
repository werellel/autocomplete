from collections import deque
''' https://en.wikipedia.org/wiki/Trie '''

class Node:
   def __init__(self) -> None:
       # Note that using a dictionary for children (as in this implementation)
       # would not by default lexicographically sort the children, which is
       # required by the lexicographic sorting mentioned in the next section
       # (Sorting).
       self.children = {}  # mapping from character to Node
       self.value = None

class Trie:
    def __init__(self) -> None:
        self.node = Node()

    def find(self, key: str):
        """Find value by key in node."""
        node = self.node
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.value

    def insert(self, key: str, value=None) -> None:
        """Insert key/value pair into node."""
        if value == None:
            value = key 
        node = self.node
        for char in key:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.value = value

    def find_prefix(self, key: str):
        curr_node = self.node 
        result = [] 
        subtrie = None 
        for char in key: 
            if char in curr_node.children: 
                curr_node = curr_node.children[char] 
                subtrie = curr_node 
            else: 
                return None 

        dq = deque(subtrie.children.values()) 
        while dq: 
            curr = dq.popleft() 
            if curr.value != None: 
                result.append(curr.value) 

            dq += list(curr.children.values()) 

        return result

if __name__ == '__main__':
    trie = Trie()
    trie.insert('g')
    trie.insert('ga')
    trie.insert('go')
    trie.insert('goo')
    trie.insert('god') 
    trie.insert('good')
    print(trie.find_prefix('g'))