pragma solidity ^0.8.0;

import "../interfaces/IERC20.sol";

contract Rewarder {


    IERC20 public GoodToken;
    event Deposited(address indexed payee, uint256 weiAmount);
    event Rewarder(address receiver, uint256 amount);

    modifier OnlyHolders {
        require(GoodToken.balanceOf(msg.sender)> 0, "You are not a holder");
        _;
    }
 
    constructor (address tokenAddress) public {
        GoodToken = IERC20(tokenAddress);
    }


    function deposit() public payable {
        emit Deposited(msg.sender, msg.value);
    }
    
    function reward() public OnlyHolders {
        require(address(this).balance >= 1 ether, "not enough ether");
        emit Rewarder(msg.sender, 1 ether);

        payable(msg.sender).transfer(1 ether);

    }

}