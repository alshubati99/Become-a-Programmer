from memory_profiler import profile
@profile
def main():
    x =2
    y =5
    items = [x,y]*3000
    more_items = [x]*10000
    del items
if __name__ == "__main__":
    main()
    
# install wheel ,memory_profiler and matplotlib
