from scripts.helpful_scripts import get_account, OPENSEA_URL
from brownie import config, network, SimpleCollectible

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    account = get_account()
    if len(SimpleCollectible) <= 0:
        simple_collectible = SimpleCollectible.deploy(
            {"from": account},
            publish_source=config["networks"][network.show_active()].get(
                "verify", False
            ),
        )
    else:
        simple_collectible = SimpleCollectible[-1]

    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awesome, you can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button.")
    return simple_collectible


def main():
    deploy_and_create()
