from web3 import Web3


# 开发者    https://twitter.com/blate666

def start(mintNum: int):
    num = 0
    for i in range(0, mintNum):
        print()
        nonce = web3.eth.get_transaction_count(address_self)
        print(f'nonce-> {nonce}')
        gasPriceWei = web3.eth.gas_price  # 传统gas费 wei
        # gasPrice = web3.eth.max_priority_fee  # 高优gas费 wei
        gasPriceGWei = web3.from_wei(gasPriceWei, 'gwei')
        print(f'预估gasPrice-> {gasPriceGWei} gwei')
        tx = {
            'nonce': nonce,
            'chainId': chain_id,
            'to': address_to,
            'from': address_self,
            'data': inputHex,
            'gasPrice': gasPriceWei,
            'value': value
        }

        try:
            gas = web3.eth.estimate_gas(tx)
            print(f'预估gas-> {gas}')
            tx['gas'] = gas
            print(f'交易预览-> {tx}')
            signed_tx = web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = web3.to_hex(web3.eth.send_raw_transaction(signed_tx.rawTransaction))
            print(f"交易Hash: {tx_hash}")
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            # print(f"交易回执-> {receipt}")
            if receipt.status == 1:
                num += 1
                print("%s Mint Success!" % num)
                continue
            else:
                continue
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # 开发者    https://twitter.com/blate666
    # 开发者    https://twitter.com/blate666
    # 开发者    https://twitter.com/blate666
    # 开发者    https://twitter.com/blate666


    # 只需要改这里两处即可，自己地址和私钥，然后直接启动！
    address = '' # 自己地址
    private_key = ''  # 自己地址私钥


    # 开发者    https://twitter.com/blate666
    # 开发者    https://twitter.com/blate666
    # 开发者    https://twitter.com/blate666
    # 开发者    https://twitter.com/blate666
    # 开发者    https://twitter.com/blate666









    # 开发者    https://twitter.com/blate666
    chain_id = 56  # 改链id
    rpc_url = "https://bsc.blockpi.network/v1/rpc/public"  # rpc
    # 开发者    https://twitter.com/blate666
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    address_self = web3.to_checksum_address(address)
    address_to = web3.to_checksum_address('0xB2192D26FCaee34eCD82537505f7dE83cbD9d379')  # 狗日项目方地址
    value_eth = 0.001  # bnc20要求0.001到项目方，不然不索引(余额)
    value = web3.to_wei(value_eth, 'ether')
    inputHex = '0x646174613a2c7b2270223a22626e632d3230222c226f70223a226d696e74222c227469636b223a22626d6578222c22616d74223a22313030227d'  # 改16进制
    start(999999)  # 交易多少次，自己改，99999999也可以
