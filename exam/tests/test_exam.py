from brownie import accounts,GoodToken,Rewarder,ExtractReward, TrusterLenderPool
from brownie import network

ex1 = True
ex3 = False
ex4 = False
ex5 = False
ex6 = False
bonus = False
def test():
    deployer = accounts[0]
    you = accounts[1]
    TOTAL_TOKENS = 1000000e18
    assert deployer.balance() == 100e18
    # Deployment of contracts
    token = GoodToken.deploy(TOTAL_TOKENS,{"from": deployer})
    reward_contract = Rewarder.deploy(token.address, {"from": deployer})
    assert deployer.balance() == 100e18
    reward_contract.deposit({"from":deployer,"value": "10 ether"})

    if ex1:
        # 1st exercise. Make a transfer from deployer to you of 100 tokens
        # Assert 1st exercise
        assert token.balanceOf(you.address) == 1e20, "First exercise fail."
    if ex3:
        # 3rd exercise. First deploy then deposit 1 ETH deploy it with name attack_contract
        first_balance = you.balance()

        # 3rd exercise asserts.
        assert attack_contract.balance() == 1e18
        assert you.balance()  == first_balance - 1e18
    if ex4:
        balance_deployer = deployer.balance()
        contract_balance = attack_contract.balance()
        # 4rth exercise Call thankYou() function

        
        # Asserts 4rth exerice
        assert balance_deployer + contract_balance == deployer.balance()
        assert attack_contract.balance() == 0
    if ex5:
        your_balance = you.balance()
        # 5th exercise. Claim etheres from reward.sol
        # Assert 5th
        assert you.balance() == your_balance + 1e18
    if ex6:
        rewarder_balance = reward_contract.balance()
        your_balance = you.balance()
        # 6th exercise. Claim all the rewards in one transaction.

        # Write code here
        # asserts
        assert you.balance() == rewarder_balance + your_balance
    if bonus:
        # Bonus exercise
        you2 = accounts[2]
        flashloan_contract = TrusterLenderPool.deploy(token.address,{"from":deployer})
        reward_contract.deposit({"from":deployer,"value": "10 ether"})
        token.transfer(flashloan_contract.address,10000e18,{"from":deployer})
        assert token.balanceOf(flashloan_contract.address) == 10000e18
        # Write code here
        # Asserts
        assert you2.balane() == 100e18+10e18
