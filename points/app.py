from service.PositionCalculator import calculate_rover_position

__author__ = 'Jayden'


def calculate_rover_position(ur_coordintes, rover_list):
    coordinates = ur_coordintes.split()
    row = int(coordinates[0])
    col = int(coordinates[1])
    final_positions = []

    for rover in rover_list:
        rover_position = calculate_rover_position(row, col, rover)
        final_positions.append(rover_position)
    print(final_positions)


def main():
    urcoordintes = "5 5"
    roverList = []
    roverOneStartPosition = "1 2 N"
    roverOneCommand = "LMLMLMLMM"
    roverTwoStartPosition = "3 3 E"
    roverTwoCommand = "MMRMMRMRRM"
    roverOne = [roverOneStartPosition, roverOneCommand]
    roverTwo = [roverTwoStartPosition, roverTwoCommand]
    roverList.append(roverOne)
    roverList.append(roverTwo)
    calculate_final_position(urcoordintes, roverList)

main()

