/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
  let i = 0;
  let j = 0;
  while (i < t.length && j < s.length) {
    if (s[j] == t[i]) {
      j++;
    }
    i++;
  }
  if (j == s.length) {
    return true;
  }
  return false;
};
