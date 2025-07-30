class Solution:
    def simplifyPath(self, path: str) -> str:
        # time: O(n), space: O(n)
        comps = path.split("/")
        s = []
        for c in comps:
            if c == "" or c == ".":
                continue
            elif c == "..":
                if s:
                    s.pop()
            else:
                s.append(c)
        return "/" + "/".join(s)

        # time: O(n), space: O(n)
        # res = []
        # s = []
        # for c in path:
        #     if not s:
        #         s.append(c)
        #     else:
        #         if s[-1] == "/" and c == "/":
        #             continue
        #         if s[-1] != "/" and c == "/":
        #             if len(s) >= 3:
        #                 if s[-3] == "/" and s[-2] == "." and s[-1] == ".":
        #                     if res:
        #                         res.pop()
        #                     s = [c]
        #                 else:
        #                     if s != ["/"]:
        #                         res.append(s)
        #                     s = [c]
        #             elif len(s) >= 2:
        #                 if s[-2] == "/" and s[-1] == ".":
        #                     s = [c]
        #                 else:
        #                     if s != ["/"]:
        #                         res.append(s)
        #                     s = [c]
        #             else:
        #                 if s != ["/"]:
        #                     res.append(s)
        #                 s = [c]
        #         else:
        #             s.append(c)
        # if len(s) >= 3:
        #     if s[-3] == "/" and s[-2] == "." and s[-1] == ".":
        #         if res:
        #             res.pop()
        #         s = [c]
        #     else:
        #         if s != ["/"]:
        #             res.append(s)
        #         s = [c]
        # elif len(s) >= 2:
        #     if s[-2] == "/" and s[-1] == ".":
        #         s = [c]
        #     else:
        #         if s != ["/"]:
        #             res.append(s)
        #         s = [c]
        # if not res:
        #     return "/"
        # ans = ""
        # for r in res:
        #     ans += "".join(r)
        # return ans