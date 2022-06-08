/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let max_profit = 0;
    let min = prices[0];
    
    for(let i = 1; i < prices.length; ++i) { 
        if(min > prices[i]) {
            min = prices[i];
        } else if(prices[i] - min > max_profit) {
            max_profit = prices[i] - min;
        }
    }
    
    return max_profit;
};
