/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
function checkInclusion(s1, s2) {
    
    if (s1.length > s2.length) {
        return false;
    }
    
    const s1_chars = Object.create(null);
    
    for (const ch of s1) {
        if (!(ch in s1_chars)) {
            s1_chars[ch] = 0;
        }
        ++s1_chars[ch];
    }
    
    const last = s2.length - s1.length;
    let i = 0;
    
    while (i <= last) {
        
        while (i <= last && !(s2[i] in s1_chars)) {
            ++i;
        }
        
        if (i > last) {
            return false;
        }
        
        const sub_chars = Object.create(null);
        let j = i;
        
        while (j < s2.length && s2[j] in s1_chars) {
            
            const ch = s2[j];
            
            if (!(ch in sub_chars)) {
                sub_chars[ch] = 0;
            }
            ++sub_chars[ch];
            
            if (sub_chars[ch] > s1_chars[ch]) {
                break;
            }
            
            ++j;
        }
        
        if (s1.length === j - i) {
            return true;
        }
        
        if (j < s2.length && s2[j] in s1_chars) {
            while (s2[i] !== s2[j]) {
                ++i;
            }
            ++i;
        } else {
            i = j;
        }
    }
    
    return false;
}
