/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
const characterReplacement = (s, k) => {
  let left = 0;
  let right = 0;
  let max = 0; // max character count
  const seen = {};

  while (right < s.length) 
  {
    const char = s[right];
    seen[char] = seen[char] ? seen[char] + 1 : 1;

    if (seen[char] > max)
    {
      max = seen[char];
    }
    
    if (right - left + 1 - max > k) 
    {
      seen[s[left]]--;
      left++;
    }

    right++;
  }

  return right - left;
};
