import cv2
from matcher import Matcher

# Load the screenshot containing the empty fields and the field template. When
# running the script from this folder we can use the relative paths directly.
farm_img = cv2.imread('empty_fields.png', cv2.IMREAD_UNCHANGED)
field_img = cv2.imread('../templates/environment/field.png', cv2.IMREAD_UNCHANGED)

m = Matcher()

# Find each empty field. ``match_template`` returns a rectangle for every match
# so we can simply print the number of results.
field_matches = m.match_template(field_img, farm_img, 0.7)
print(f"found {len(field_matches)} field matches")

# Visualisation with ``cv2.imshow`` requires GUI support which isn't always
# available in headless environments, so we only show the image when possible.
# Visualization with cv2 requires a display which may not be available on all
# systems used for testing. The following lines can be re-enabled locally to
# inspect the matches.
# m.mark_matches(field_matches, farm_img, (255, 255, 0))
# cv2.imshow('Result', farm_img)
# cv2.waitKey()
