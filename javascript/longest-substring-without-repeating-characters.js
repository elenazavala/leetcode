/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (str) {
  const mappy = {};
  let start = 0;
  let max = 0;

  for (let i = 0; i < str.length; i++) {
    let right_char = str[i];

    if (!(right_char in mappy)) mappy[right_char] = 0;
    mappy[right_char] += 1;

    while (mappy[right_char] > 1) 
    {
      let left_char = str[start];
      start += 1;

      if (left_char in mappy) mappy[left_char] -= 1;
      if (mappy[left_char] === 0) delete mappy[left_char];
    }
    max = Math.max(max, i - start + 1);
  }
  return max;
};
