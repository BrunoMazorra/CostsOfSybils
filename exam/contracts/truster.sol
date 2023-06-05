pragma solidity ^0.8.0;

import "../interfaces/IERC20.sol";

contract TrusterLenderPool  {

    IERC20 public GoodToken;

    constructor (address tokenAddress) public {
        GoodToken = IERC20(tokenAddress);
    }

    function flashLoan(
        uint256 borrowAmount,
        address target,
        bytes calldata data
    )
        external
    {
        uint256 balanceBefore = GoodToken.balanceOf(address(this));

        require(balanceBefore >= borrowAmount, "Not enough tokens in pool");
        require(borrowAmount>0, "Borrow more than 0");
        
        GoodToken.transfer(target, borrowAmount);
        (bool success, ) = target.call(data);
        require(success, "External call failed");

        uint256 balanceAfter = GoodToken.balanceOf(address(this));
        require(balanceAfter >= balanceBefore, "Flash loan hasn't been paid back");
    }

}