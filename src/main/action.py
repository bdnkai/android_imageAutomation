



def dispatch(action, adb, location):

        match action:
            case "tap":
                adb.shell(f'input tap {location}')
            case "main":
                return "one"
            case "dailies":
                return "two"
            case default:
                return "something"



