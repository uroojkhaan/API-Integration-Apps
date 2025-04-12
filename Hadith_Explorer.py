import requests
import json

base_url = "https://hadithapi.com/api"

api_key = "$2y$10$BylaBcXs5Lw7ZOtYmQ3PXO1x15zpp26oc1FeGktdmF6YeYoRd88e"

def list_hadiths_books():
    url = f"{base_url}/books?apiKey={api_key}"
    response = requests.get(url)


    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200 :
        books = response.json()['books']
        for book in books :
            print(f"{book['bookSlug']}-{book['bookName']} | Chapters: {book['chapters_count']} | Hadiths :{book['hadiths_count']}")
    else:
            print(" Error fetching books. Check your API key or internet connection.")

def get_chapters(bookslug) :
    url = f"{base_url}/{bookslug}/chapters?apiKey={api_key}"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200:
        chapters = response.json().get('chapters'),[]
        for chapter in chapters :
            print(f"Chapter {chapter['chapterNumber']}: {chapter['chapterEnglish']} (Urdu: {chapter['chapterUrdu']})")

    else:
        print(" Error fetching chapters. Check the bookSlug or internet.")


def get_hadiths(bookslug, chapter):
    url = f"{base_url}/hadiths?apiKey={api_key}&book={bookslug}&chapter={chapter}"
    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200:
        hadiths = response.json()['hadiths']
        for hadith in hadiths:
            print(f"Hadith #{hadith['hadithNumber']}: {hadith['hadithEnglish']}")
    else:
        print(" Error fetching hadiths. Check the chapter number or bookSlug.")

def main():
    while True:
        print("\n*Hadith Explorer App*")
        print("1. List all Hadith Books")
        print("2. Get Chapters of a Book")
        print("3. Get Hadiths from a Chapter")
        print("4. Exit")

        choice = input("Please choose an option: ")

        if choice == "1":
            list_hadiths_books()  # Show all books
        elif choice == "2":
            bookslug = input("Enter the book slug (e.g., bukhari, muslim): ")
            get_chapters(bookslug)  # Show chapters for the selected book
        elif choice == "3":
            bookslug = input("Enter the book slug (e.g., bukhari, muslim): ")
            chapter = input("Enter chapter number: ")
            get_hadiths(bookslug, chapter)  # Fetch hadiths for the selected book and chapter
        elif choice == "4":
            print("\nMay Allah (SWT) grant you success in your pursuit of knowledge.")
            print("JazakAllah Khair for using the Hadith Explorer App. May it benefit you and your loved ones.")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()

