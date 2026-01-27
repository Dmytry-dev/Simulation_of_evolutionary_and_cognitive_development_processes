import display.display as display
import structures.Gen as Gen
import structures.Cells as Cells


def main():
    display.display_open()


def make_cell(world_x, world_y):
    cell = Cells.Cell("test", (100,100,100))
    cell.user_spawn(world_x, world_y)

    return cell


if __name__ == "__main__":
    main()