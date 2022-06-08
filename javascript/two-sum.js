/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let mappy = {};
    for (let i = 0; i < nums.length; i++) {
        if (target - nums[i] in mappy) {
            return [mappy[target-nums[i]], i];
        } else {
            mappy[nums[i]] = i;
        }
    }
};
