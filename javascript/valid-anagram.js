/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let mappy = {};
    
    if (s.length !== t.length) {
        return false;
    }
    
    for (let i = 0; i < s.length; i++) {
        if (mappy[s[i]]) {
            mappy[s[i]]++;
        } else {
            mappy[s[i]] = 1;
        }
    }
    
    for (let i = 0;  i < t.length; i++) {
        if (mappy[t[i]]) {
            mappy[t[i]]--;
        } else {
            return false;
        }
    }
    return true; 
};
