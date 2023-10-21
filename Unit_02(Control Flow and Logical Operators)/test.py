num = input("Enter a number(1-7):")
match num:
    case "1":
        print("Sunday")
    case "2":
        print("Monday")
    case "3":
        print("Tue")
    case "4":
        print("Wed")
    case "5":
        print("Thu")
    case "6":
        print("Fri")
    case "7":
        print("Sat")
    case default:
        print("Invalid day number.")