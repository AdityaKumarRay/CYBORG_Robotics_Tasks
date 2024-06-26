from main import detect_arena_parameters
import cv2 as cv

file_name = "test_images/maze_0.png"

input_maze_image = cv.imread(f'{file_name}',1)

output_dict = detect_arena_parameters(input_maze_image)
print('Arena Parameters: ', output_dict)

output_params = ['traffic_signals','start_node','medicine_packages_present','horizontal_roads_under_construction','vertical_roads_under_construction']
maze_0_dict = {'traffic_signals': ['C5', 'D4', 'D6', 'G4'], 'start_node': ['A7'], 'horizontal_roads_under_construction': ['C5-D5', 'E7-F7', 'F5-G5'], 'vertical_roads_under_construction': ['B2-B3', 'B3-B4', 'B6-B7', 'C5-C6', 'D5-D6', 'E5-E6', 'E6-E7', 'F6-F7'], 'medicine_packages_present': [['Shop_1', 'Green', 'Square', [130, 130]], ['Shop_1', 'Orange', 'Square', [130, 170]], ['Shop_1', 'Pink', 'Square', [170, 130]], ['Shop_1', 'Skyblue', 'Square', [170, 170]], ['Shop_2', 'Green', 'Triangle', [270, 130]], ['Shop_2', 'Orange', 'Triangle', [270, 170]], ['Shop_6', 'Green', 'Circle', [630, 170]], ['Shop_6', 'Pink', 'Circle', [670, 170]], ['Shop_6', 'Skyblue', 'Circle', [670, 130]]]}

# ## To test your output for maze_0 uncomment the below part.


# print()
# passed = False
# for i,param in enumerate(output_params):
#     if i>2:
#         break
#     if maze_0_dict[param] == output_dict[param]:
#         passed = True
#     else:
#         passed = False
#         break 

# if passed:
#     print("Hurray! Test case Passed.")
# else:
#     print("Sorry your Test case Failed.")





# ## If you have completed the Bonus configuration uncomment the below part.
# print()
# passed = False
# for i,param in enumerate(output_params):
#     if maze_0_dict[param] == output_dict[param]:
#         passed = True
#     else:
#         passed = False
#         break
# if passed:
#     print("Hurray! Bonus Task Completed.")
# else:
#     print("Failed!")