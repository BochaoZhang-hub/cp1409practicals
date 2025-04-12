import wikipedia
from wikipedia.exceptions import DisambiguationError

def main():
        title = input("Enter page title: ").strip()

        while title != "":
            try:
                page = wikipedia.page(title, auto_suggest=False)
                print(page.title)
                print(page.summary)
                print(page.url)
            except DisambiguationError as e:
                print(e.options)

        print("Thankyou")


if __name__ == '__main__':
    main()