#ifndef LSWRC_H
#define LSWRC_H

TEST(Solution, lengthOfLongestSubstring){
    
    int test1 = 0;
    test1 = Solution::lengthOfLongestSubstring("abccabcbb");

    ASSERT_EQ(3, test1);
}
#endif