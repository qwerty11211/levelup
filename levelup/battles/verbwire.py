import requests

token=""
contractAddress=""
testnet='bsc-testnet'



def create_token(tokenInitialSupply=2):
    url = "https://api.verbwire.com/v1/nft/mint/createToken1155"
    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"allowPlatformToOperateToken\"\r\n\r\ntrue\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"chain\"\r\n\r\n{testnet}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tokenInitialSupply\"\r\n\r\n10\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"contractAddress\"\r\n\r\{contractAddress}\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "accept": "application/json",
        "content-type": "multipart/form-data; boundary=---011000010111000001101001",
        "X-API-Key": token
    }

    response = requests.post(url, data=payload, headers=headers)
    return response

def view_minted_nft():
    url = "https://api.verbwire.com/v1/nft/userOps/nftsMinted"
    headers = {
        "accept": "application/json",
        "X-API-Key": token
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    return response.text

def mint_nft_from_image(name,description,filename):
    url = "https://api.verbwire.com/v1/nft/mint/mintFromFile"

    files = {"filePath": (filename, open(name, "rb"), "image/png")}
    payload = {
        "allowPlatformToOperateToken": "true",
        "quantity": "1",
        "chain": "{testnet}",
        "name": name,
        "contractAddress": contractAddress,
        "description": description
    }
    headers = {
        "accept": "application/json",
        "X-API-Key":token
    }

    response = requests.post(url, data=payload, files=files, headers=headers)
    print(response.text)
    return response


def withdraw_fund(address):
    url = "https://api.verbwire.com/v1/nft/update/withdrawFundsToWallet"
    payload = f"chain={testnet}&contractAddress={contractAddress}&withdrawAddress={address}"
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "X-API-Key": token
    }

    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    return response

def transfer_token(fromAddress, toAddress):
    url = "https://api.verbwire.com/v1/nft/update/transferToken"

    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"chain\"\r\n\r\n{testnet}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"contractAddress\"\r\n\r\n{contractAddress}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"fromAddress\"\r\n\r\n{fromAddress}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"toAddress\"\r\n\r\n{toAddress}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tokenId\"\r\n\r\n12121\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "accept": "application/json",
        "content-type": "multipart/form-data; boundary=---011000010111000001101001",
        "X-API-Key": token
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.text)
    return response