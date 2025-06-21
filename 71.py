class Solution:
    def simplifyPath(self, path: str) -> str:
        # time: O(n), space: O(n)
        components = path.split("/")
        st = []
        for comp in components:
            if comp == "" or comp == ".":
                continue
            elif comp == "..":
                if st:
                    st.pop()
            else:
                st.append(comp)
        return "/" + "/".join(st)