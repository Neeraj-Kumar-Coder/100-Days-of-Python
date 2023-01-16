try:
    hidden_list = [12, 23, 34, 45, 56, 67, 78, 89, 90, 100]
    index = int(input("Enter the index you want for the hidden list: "))
    print(f"The element at index {index} is = {hidden_list[index]}")
except Exception as e:
    print(f"Error occured: {e}")
finally:
    print("Performing cleanups")


# Usage of finally

def returner():
    try:
        hidden_list = [12, 23, 34, 45, 56, 67, 78, 89, 90, 100]
        index = int(input("Enter the index you want for the hidden list: "))
        print(f"The element at index {index} is = {hidden_list[index]}")
        return 0
    except Exception as e:
        print(f"Error occured: {e}")
        return -1
    finally:
        print("Performing cleanups")
        # return 1 # This will be returned if uncommented


print(returner())
