import requests
import json
# API Key
API_KEY = "977cb40d05c6fe82d7e0c42c75bf2da0"
BASE_URL = "https://gnews.io/api/v4/top-headlines?token=977cb40d05c6fe82d7e0c42c75bf2da0&lang=en&max=5"


def get_news():
    params = {
        "token": API_KEY,  
        "lang": "eng",      
        "country": "us",   
        "max": 5           
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        news_data = response.json()
        for i, article in enumerate(news_data["articles"]):
            print(f"{i+1}. {article['title']}")
            print(f"   {article['description']}")
            print(f"   Kaynak: {article['source']['name']}")
            print(f"   URL: {article['url']}\n")
    else:
        print("Hata:", response.status_code)

get_news()

def save_news_to_file(news_list, filename="news.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(news_list, file, indent=4, ensure_ascii=False)
    print(f"✅ Haberler {filename} dosyasına kaydedildi!")

news_data = [
    {"title": "Python API Kullanımı", "description": "Haber açıklaması", "source": "TechNews", "url": "https://example.com"},
    {"title": "Yapay Zeka Güncellemeleri", "description": "Yeni AI modelleri tanıtıldı.", "source": "AI Times", "url": "https://example.com"}
]

save_news_to_file(news_data)

def read_news_from_file(filename="news.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            news_list = json.load(file)
            if not isinstance(news_list, list):  
                return []
            return news_list
    except FileNotFoundError:
        print("⚠ Dosya bulunamadı. Yeni bir dosya oluşturuluyor...")
        return []  
    except json.JSONDecodeError:
        print("⚠ JSON dosyasında hata var! Boş listeye geri dönülüyor...")
        return [] 



def add_news(title, description, source, url, filename="news.json"):
    news_list = read_news_from_file(filename)
    new_news = {
        "title": title,
        "description": description,
        "source": source,
        "url": url
    }
    news_list.append(new_news)
    save_news_to_file(news_list, filename)
    print("✅ Yeni haber eklendi!")


def update_news(index, updated_data, filename="news.json"):
    news_list = read_news_from_file(filename)
    if 0 <= index < len(news_list):
        news_list[index].update(updated_data)
        save_news_to_file(news_list, filename)
        print(f"✅ {index+1}. haber güncellendi.")
    else:
        print("❌ Geçersiz haber numarası!")


def delete_news(index, filename="news.json"):
    news_list = read_news_from_file(filename)
    if 0 <= index < len(news_list):
        deleted_item = news_list.pop(index)
        save_news_to_file(news_list, filename)
        print(f"🗑 Silinen haber: {deleted_item['title']}")
    else:
        print("❌ Geçersiz haber numarası!")

if __name__ == "__main__":
    print("📂 Haberleri Listele")
    read_news_from_file()

    print("\n➕ Yeni Haber Ekle")
    add_news("Python API Kullanımı", "Haber açıklaması", "TechNews", "https://example.com")

    print("\n📝 Haberi Güncelle")
    update_news(0, {"title": "Güncellenmiş Haber Başlığı"})

    print("\n🗑 Haberi Sil")
    delete_news(1)
