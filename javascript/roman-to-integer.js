/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    let romans = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    };

    let temp = s.split("");

    let sum = 0;

    for (let i = temp.length - 1; i >= 0; i--) {

      if (romans[temp[i]] === romans["V"]) {
            if (romans[temp[i - 1]] === romans["I"]) {
                sum -= 1 * 2;
            }
        }

      if (romans[temp[i]] === romans["X"]) {
            if (romans[temp[i - 1]] === romans["I"]) {
                sum -= 1 * 2;
            }
        }
       
        if (romans[temp[i]] === romans["L"]) {
            if (romans[temp[i - 1]] === romans["X"]) {
                sum -= 10 * 2;
            }
        }

      if (romans[temp[i]] === romans["C"]) {
            if (romans[temp[i - 1]] === romans["X"]) {
                sum -= 10 * 2;
            }
        }

      if (romans[temp[i]] === romans["D"]) {
            if (romans[temp[i - 1]] === romans["C"]) {
                sum -= 100 * 2;
            }
        }

      if (romans[temp[i]] === romans["M"]) {
            if (romans[temp[i - 1]] === romans["C"]) {
                sum -= 100 * 2;
            }
        }

        sum += romans[temp[i]];
    }

    return sum;
};
