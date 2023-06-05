pragma solidity ^0.8.0;

import "../interfaces/IERC20.sol";
import "./reward.sol";
import "./truster.sol";

contract ExtractReward {

    

    fallback() external payable {
        // React to receiving ether to this contract.
    }
    // Receive function
    receive() external payable {
        // React to receiving ether to this contract.
    }
}