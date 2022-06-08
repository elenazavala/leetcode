
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
const groupAnagrams = (strs) => {
  const res = [];
  const mappy = new Map();
  for (let i = 0; i < strs.length; i++) {
    const sorted = strs[i].split("").sort().join("");
    
    console.log(sorted);
    if (mappy.has(sorted)) {
      mappy.get(sorted).push(strs[i]); 
    } else {
      mappy.set(sorted, [strs[i]]); 
    }
  }

  for (let [key, value] of mappy) {
    res.push(value);
  }
  return res;
};
