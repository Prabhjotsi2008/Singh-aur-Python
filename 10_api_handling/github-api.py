import requests

base_url = "https://api.github.com/users/"

def fetch_data(username):
    url = f"{base_url}{username}"
    print(url)
    
    response = requests.get(url)
    data = response.json()
    if "name" in data:
        return data
    else:
        raise Exception("Failed to fetch data...")

def print_data(data):
    print(f"{'='*20} GITHUB-PROFILE {'='*20}")
    print(f"Name: {data["name"]} ({data["type"]})")
    print(f"Bio: {data["bio"]}")
    print(f"From: {data["location"]}")
    print(f"Followers: {data["followers"]}")
    print(f"=" * 56)


def main():
    username = input("Enter a valid Github Username: ")
    data = fetch_data(username)
    print_data(data)

if __name__ == "__main__":
    main()