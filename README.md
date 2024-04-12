# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

B, A,     D,     C,     B  <br>
5, 5.655, 2.459, 5.089, 20.1299


## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

If I add the liquidity into the specific pool, there may be other providers manipulating the swap action during the process of my swap. Hence, it may change the ideal swap token in my own action. 
You need to set the “amount out min” in order to make the transaction meet your expectation.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

To prevent an attacker from owning the entire liquidity pool and blocking other providers from adding liquidity.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?


liquidity = Math.min(amount0.mul (_totalSupply) / _reserve0, amount1.mul(_totalSupply) / _reserve1); 
The intention behind this specific formula is to maintain a fair and efficient liquidity provision mechanism within the Uniswap protocol. This approach helps prevent any single party from disproportionately influencing the liquidity pool and ensures that liquidity provision remains decentralized and accessible to all participants.



## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

Assume a transaction : trade asset A to another asset Y
The attacker founded the transaction, and Front-Runs the victim by purchasing asset Y before the large trade is approved. The action raise the price of the asset Y, which means the attacker can sell at a higher price.

