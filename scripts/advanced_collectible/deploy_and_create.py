from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import config, network, AdvancedCollectible


def deploy_and_create():
    account = get_account()
    if len(AdvancedCollectible) <= 0:
        advanced_collectible = AdvancedCollectible.deploy(
            get_contract("vrf_coordinator"),
            get_contract("link_token"),
            config["networks"][network.show_active()]["keyhash"],
            config["networks"][network.show_active()]["fee"],
            {"from": account},
            publish_source=config["networks"][network.show_active()].get(
                "verify", False
            ),
        )
    else:
        advanced_collectible = AdvancedCollectible[-1]

    token_count = advanced_collectible.tokenCounter()
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)

    print("New token has been created!")
    return advanced_collectible, creating_tx, token_count

    # tx = advanced_collectible.createCollectible(sample_token_uri, {"from": account})
    # tx.wait(1)
    # print(
    #     f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    # )
    # print("Please wait up to 20 minutes, and hit the refresh metadata button.")
    # return simple_collectible


def main():
    deploy_and_create()
