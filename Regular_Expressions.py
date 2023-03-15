import re

pattern = r"[a-z]+.[^abc]"
text = """General relativity was developed by Einstein in the years 1907 - 1915.
General relativity postulates that the global Lorentz covariance of special relativity becomes a local Lorentz covariance in the presence of matter.
The presence of matter "curves" spacetime, and this curvature affects the path of free particles (and even the path of light).
General relativity uses the mathematics of differential geometry and tensors in order to describe gravitation as an effect of the geometry of spacetime.
Einstein based this new theory on the general principle of relativity, and he named the theory after the underlying principle.
"""

matches = re.finditer(pattern=pattern, string=text)
for match in matches:
    print(match)
