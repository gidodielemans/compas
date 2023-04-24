from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .predicates_2 import (  # noqa: F401
    is_ccw_xy,
    is_colinear_xy,
    is_polygon_convex_xy,
    is_point_on_line_xy,
    is_point_on_segment_xy,
    is_point_on_polyline_xy,
    is_point_in_triangle_xy,
    is_point_in_polygon_xy,
    is_point_in_convex_polygon_xy,
    is_point_in_circle_xy,
    is_polygon_in_polygon_xy,
    is_intersection_line_line_xy,
    is_intersection_segment_segment_xy,
)
from .predicates_3 import (  # noqa: F401
    is_colinear,
    is_colinear_line_line,
    is_coplanar,
    is_polygon_convex,
    is_point_on_plane,
    is_point_infront_plane,
    is_point_behind_plane,
    is_point_in_halfspace,
    is_point_on_line,
    is_point_on_segment,
    is_point_on_polyline,
    is_point_in_triangle,
    is_point_in_circle,
    is_point_in_polyhedron,
    is_intersection_line_line,
    is_intersection_segment_segment,
    is_intersection_line_triangle,
    is_intersection_line_plane,
    is_intersection_segment_plane,
    is_intersection_plane_plane,
)
