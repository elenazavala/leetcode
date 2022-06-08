
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let mappy = {};
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in mappy) {
            return true;
        } else {
            mappy[nums[i]] = i;
        }
    }
    return false;
};
