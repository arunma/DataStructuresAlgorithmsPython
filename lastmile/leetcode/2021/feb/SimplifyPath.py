class SimplifyPath:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for ch in path.split('/'):
            if stack and ch == '..':
                stack.pop()
            elif ch not in ["", ".", ".."]:
                stack.append(ch)

        return '/'+'/'.join(stack)

if __name__ == '__main__':
    init = SimplifyPath()
    print(init.simplifyPath("/home/")) #/home
    print(init.simplifyPath("/../")) #/
    print(init.simplifyPath("/home//foo/")) #/home/foo
    print(init.simplifyPath("/a/./b/../../c/")) #/c
    print(init.simplifyPath("/../")) #/
