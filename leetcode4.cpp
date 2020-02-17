class Solution {
	vector<int>vc;
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

		int s1_length = nums1.size();

		int s2_length = nums2.size();

		s1_length > s2_length ? Median(nums2, nums1, s2_length, s1_length) : Median(nums1, nums2, s1_length, s2_length);

		double ans_index;

		if (vc.size() & 1)
		{
			int ans_index = vc.size() / 2;
			
			return vc.at(ans_index);
			
		}
		else {

			ans_index = vc.size() / 2;

			double ans = (vc.at(ans_index) + vc.at(ans_index - 1)) / 2.0;

			return ans;

			
		}
	}
	void Median(vector<int>& nums1, vector<int>& nums2, int s1_length, int s2_length)
	{

		int i = 0, j = 0;

		while (i < s1_length && j < s2_length)
		{
			if (nums1.at(i) > nums2.at(j))
			{
				vc.push_back(nums2.at(j));
				++j;
			}
			else if (nums1.at(i) < nums2.at(j))
			{
				vc.push_back(nums1.at(i));
				++i;
			}
			else
			{
				vc.push_back(nums1.at(i));
				vc.push_back(nums2.at(j));
				++i;
				++j;
			}
		}

		if (i >= s1_length)
		{
			for (; j < s2_length; ++j)
				vc.push_back(nums2.at(j));
		}
		if (j >= s2_length)
		{
			for (; i < s1_length; ++i)
				vc.push_back(nums1.at(i));
		}

	}
};