/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    v1 = version1.split(".")
    v2 = version2.split(".")
    l = Math.max(v1.length, v2.length)
    for (let i =0; i < l; i++) {

        s1 = i < v1.length ? parseInt(v1[i])  : 0
        s2 =  i < v2.length ? parseInt(v2[i]) : 0 
    
        if (s1 > s2) {
            return 1
        } 
        if (s1 < s2) {
            return -1
        }
    }
    
    return 0
};