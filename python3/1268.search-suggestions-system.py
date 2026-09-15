#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    # def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    #     products.sort()
    #     n = len(searchWord)
    #     filtered = [i for i in range(len(products))]
    #     ans = []
    #     for i in range(n):
    #         temp = []
    #         for j in filtered:
    #             if i < len(products[j]) and searchWord[i] == products[j][i]:
    #                 temp.append(j)
    #         filtered = temp   

    #         result = []
    #         c = 0
    #         while c < 3 and c < len(filtered):
    #             result.append(products[filtered[c]])
    #             c += 1
    #         ans.append(result)
    #     return ans
    # 
    # classic trie solution  
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        trie = {}
        for product in products:
            curr = trie
            for c in product:
                if c not in curr:
                    curr[c] = {"suggestions": []}
                curr = curr[c]
                if len(curr["suggestions"]) < 3:
                    curr["suggestions"].append(product)

        ans = []
        curr = trie
        for c in searchWord:
            if curr and c in curr:
                curr = curr[c]
                ans.append(curr['suggestions'])
            else:
                curr = None
                ans.append([])
        return ans
# @lc code=end

