from lab11.geo.area import square_area, triangle_area
from lab11.geo.distance import distance


STUDENT_ID = "202534060"

def test_square():
    assert square_area(4) == 16

def test_triangle():
    assert triangle_area(10, 5) == 25.0

def test_distance():
    assert distance(0, 0, 3, 4) == 5.0

if __name__ == "__main__":
    test_square()
    test_triangle()
    test_distance()


    print(f"Success {STUDENT_ID}")
