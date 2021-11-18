import DictionarySearch as h
import timeit as t


def main():
    start_time = t.default_timer()
    differences = h.wordfile_differences_linear_search("british-english", "american-english")
    time_spent = t.default_timer() - start_time
    print(time_spent)
    print(len(differences))

if __name__=='__main__':
    main()
