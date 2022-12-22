import concurrent.futures



def dispatch(action, adb, location_x, location_y):

    def adb_tap(adb,tap_x, tap_y):
        x = adb.shell(f'input tap {tap_x} {tap_y}')
        result = x
        return 'pressed'





    with concurrent.futures.ThreadPoolExecutor() as executor:

        match action:
            case "tap":
                # future =executor.submit(dispatch, action=action, adb=adb, location_x=location_x, location_y=location_y)
                # locs = location
                # print(f'FROM ACTIIION::{location_x} {location_y}')
                # quit()

                future = [executor.submit(adb_tap(adb=adb, tap_x=location_x, tap_y=location_y))]
                for f in future:
                    results = executor.map([future])

                    print(f'FROM ACTIIION RESULTS::', results)




                # return 'results'


            case "main":
                return "one"
            case "dailies":
                return "two"
            case default:
                return "something"



