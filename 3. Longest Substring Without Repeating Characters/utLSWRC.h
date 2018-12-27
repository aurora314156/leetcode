#ifndef LSWRC_H
#define LSWRC_H

#include "LSWRC.h"

TEST1 (Solution, lengthOfLongestSubstring){
    
    int test1 = Solution::test1("abccabcbb");

    ASSERT_EQ(3, test1);
}
#endif