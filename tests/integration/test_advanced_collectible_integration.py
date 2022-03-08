from brownie import network
import time
import pytest
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_contract,
    get_account,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")

    # Act
    advanced_collectible, creation_transaction, token_count_before = deploy_and_create()
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == token_count_before + 1


def temp(advanced_collectible, token_count_before, range=30):
    for i in range(1, range):
        time.sleep(10)
        print(f"{advanced_collectible.tokenCounter()} {token_count_before + 1}")
