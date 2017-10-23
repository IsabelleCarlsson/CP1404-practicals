import wikipedia

user_search = input("Wikipedia search: ")
while len(user_search) > 0:
    try:
        print("\n" + wikipedia.page(user_search).title)
        print(wikipedia.summary(user_search))
        print(wikipedia.page(user_search).url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.PageError:
        print("Page search '" + user_search + "' does not match any pages. Try another search!")
    user_search = input("\nWikipedia search: ")