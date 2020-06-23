import requests

url = "https://discord.com/api/v6/users/@me"

input_path = input("Enter the file path of the tokens you wish to check: ")
output_path = input("Enter the file path to output the working tokens to: ")    

print(f"Working tokens: \n")

with open(input_path, 'r') as f:
    file = f.read().splitlines()
    for token in file:
        r = requests.get(url, headers={"authorization":token})
        if r.status_code == 200:
            print(token)
            o = open(output_path, 'a')
            o.write(f"{token} \n")
            o.close()
