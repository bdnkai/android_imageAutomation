


def dispatch(action, _device=None, location=None):
    match action:
        case "tap":
            _device.shell(f'input tap {location}')
            return "start"
        case "main":
            return "one"
        case "dailies":
            return "two"
        case default:
            return "something"



