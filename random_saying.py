import requests
import json

def fetch_advice():
    url = "https://korean-advice-open-api.vercel.app/api/advice"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def update_readme(advice_data):
    if not advice_data:
        return
    
    readme_content = f"""# 내가 보려 만든 명언 리스트

##  {advice_data['author']}({advice_data['authorProfile']})
> {advice_data['message']}

출처 : https://github.com/gwongibeom/korean-advice-open-api/blob/main/README.md
재밌게 보려고 만들었습니다.
"""
    
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

def main():
    advice = fetch_advice()
    update_readme(advice)

if __name__ == "__main__":
    main()
