import unittest


class Solution:

    def getMaxUnits(self, boxes, unitsPerBox, truckSize):
        # boxes.sort(key=lambda x: x[1], reverse=True)
        # max_units = 0
        # i = 0
        #
        # while truckSize > 0 and i < len(boxes):
        #     box_count = min(truckSize, boxes[i][0])
        #     max_units += box_count * boxes[i][1]
        #     truckSize -= box_count
        #     i += 1
        #
        # return max_units
        size_n_count = zip(unitsPerBox, boxes)
        size_n_count = sorted(size_n_count, reverse=True)
        max_units = 0

        for unit, count in size_n_count:
            if truckSize >= count:
                max_units += unit * count
                truckSize -= count
            else:
                max_units += unit * truckSize
                break

        return max_units


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.get_max_units = Solution().getMaxUnits

    def test_1(self):
        boxes = [1, 2, 3]
        units_per_box = [3, 2, 1]
        truck_size = 3
        self.assertEqual(7, self.get_max_units(boxes, units_per_box, truck_size))

    def test_2(self):
        boxes = [1, 1]
        units_per_box = [9, 6]
        truck_size = 1
        self.assertEqual(9, self.get_max_units(boxes, units_per_box, truck_size))

    def test_3(self):
        boxes = [3, 1, 6]
        units_per_box = [2, 7, 4]
        truck_size = 6
        self.assertEqual(27, self.get_max_units(boxes, units_per_box, truck_size))
