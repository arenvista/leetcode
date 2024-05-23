# @leet start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        print(f"path: {path}")
        for element in path: #elements can either be actions or names
            print(element)
            if element == '..':
                if stack:
                    stack.pop()
                    continue
            elif element == '.' or element == '':
                continue
            else:
                stack.append(element)
        return '/' + '/'.join(stack)





# @leet end
