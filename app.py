# function style

from controllers import get_controller
def main():
    # main (starting) point
    state = (None, None) # starting with no state
    while True:
        controller = get_controller(state[0])
        state = controller(state[1])


if __name__ == "__main__":
    main()