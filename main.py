from typing import List,  Dict 
import json

def colocar_panel(roof_grid: List[List[int]], panel_w: int, panel_h: int) -> bool:
    for col in range(len(roof_grid)):
        for row in range(len(roof_grid[0])):
            if roof_grid[col][row] != 0:
                continue 
            if (
                col + panel_w <= len(roof_grid) and 
                roof_grid[col + panel_w - 1][row] == 0 and
                row + panel_h <= len(roof_grid[0]) and 
                roof_grid[col][row + panel_h - 1] == 0
            ):
                for w in range(panel_w):
                    for h in range(panel_h):
                        roof_grid[col + w][row + h] = 1
                return True
    return False

def colocar_paneles_recursivamente(roof_grid: List[List[int]], panel_width: int, panel_height: int) -> int:
    orientacion_normal = 0
    orientacion_rotada = 0
    grid_normal = [col[:] for col in roof_grid]
    grid_rotada = [col[:] for col in roof_grid]

    if colocar_panel(grid_normal, panel_width, panel_height):
        orientacion_normal = 1 + colocar_paneles_recursivamente(
            grid_normal, panel_width, panel_height
        )

    if colocar_panel(grid_rotada, panel_height, panel_width):
        orientacion_rotada = 1 + colocar_paneles_recursivamente(
            grid_rotada, panel_height, panel_width
        )

    return max(orientacion_normal, orientacion_rotada)

def calculate_panels(panel_width: int, panel_height: int,
                     roof_width: int, roof_height: int) -> int:
    roof_grid  = [[0 for _ in range(roof_height)] for _ in range(roof_width)]

    return colocar_paneles_recursivamente(
        roof_grid, panel_width, panel_height
    )

def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
