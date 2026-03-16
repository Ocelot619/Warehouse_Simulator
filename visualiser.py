# visualizer.py
def print_map(racks, robot, width=12, height=12):
    """Prints warehouse map as matrix"""
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    # RACKS
    for stock_item in racks.stock_list:
        x, y = stock_item.pos_x, stock_item.pos_y
        if 0 <= x < width and 0 <= y < height:
            grid[y][x] = stock_item.item_name[0].upper()
    
    # ROBOT
    rx, ry = robot.pos_x, robot.pos_y
    if 0 <= rx < width and 0 <= ry < height:
        grid[ry][rx] = 'R' if not robot.is_busy else 'B'  # B=busy
    
    # TARGET
    if robot.is_busy and robot.found_target:
        tx, ty = robot.target_x, robot.target_y
        if 0 <= tx < width and 0 <= ty < height:
            grid[ty][tx] = 'T'
    
    # Print
    print("\n" + "-" * (width*2 + 1))
    print(f"Robot: ({rx},{ry}) {'busy' if robot.is_busy else 'free'} -> {robot.target_x},{robot.target_y}" if robot.is_busy else f"Robot: ({rx},{ry}) free")
    for row in reversed(grid):
        print('| ' + ' | '.join(row) + ' |')
    print("-" * (width*2 + 1))

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')