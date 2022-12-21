import concurrent.futures



def dispatch(action, adb, location_x, location_y):

    with concurrent.futures.ThreadPoolExecutor() as executor:


        def adb_tap(input):
            return adb.shell(input)




        match action:
            case "tap":
                future = executor.submit(dispatch,action, adb, location_x, location_y)
                # locs = location
                print(f'{location_x} {location_y}')
                # quit()

                results = [executor.submit(adb.shell(f'input tap{location_x} {location_y}'))]

                print(future.result())




                return 'results'


            case "main":
                return "one"
            case "dailies":
                return "two"
            case default:
                return "something"



