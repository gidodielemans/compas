"""
.. _compas.datastructures:

********************************************************************************
datastructures
********************************************************************************

.. module:: compas.datastructures


Network
=======

.. autosummary::
    :toctree: generated/

    Network
    FaceNetwork


network.operations
------------------

.. autosummary::
    :toctree: generated/

    network_split_edge


network.algorithms
------------------

.. autosummary::
    :toctree: generated/

    network_bfs
    network_bfs_paths
    network_count_crossings
    network_dfs
    network_dfs_paths
    network_dijkstra_distances
    network_dijkstra_path
    network_dual
    network_embed_in_plane
    network_find_faces
    network_find_crossings
    network_is_xy
    network_is_crossed
    network_is_planar
    network_is_planar_embedding
    network_shortest_path
    network_smooth_area
    network_smooth_centroid
    network_smooth_length
    network_smooth_mass
    network_smooth_mixed
    network_vertex_coloring


Mesh
====

Package for working with mesh objects.

.. autosummary::
    :toctree: generated/

    Mesh


mesh.operations
---------------

.. autosummary::
    :toctree: generated/

    mesh_collapse_edge
    mesh_insert_edge
    mesh_split_edge
    mesh_split_face
    mesh_unweld_vertices


.. autosummary::
    :toctree: generated/

    trimesh_collapse_edge
    trimesh_split_edge
    trimesh_swap_edge


mesh.algorithms
---------------

.. autosummary::
    :toctree: generated/

    mesh_circularize
    mesh_delaunay_from_points
    mesh_dual
    mesh_flip_cycles
    mesh_planarize
    mesh_smooth_centroid
    mesh_smooth_centerofmass
    mesh_smooth_length
    mesh_smooth_area
    mesh_smooth_angle
    mesh_subdivide
    mesh_subdivide_tri
    mesh_subdivide_catmullclark
    mesh_subdivide_doosabin
    mesh_unify_cycles
    mesh_voronoi_from_points


.. autosummary::
    :toctree: generated/

    trimesh_optimise_topology
    trimesh_subdivide_loop


VolMesh
=======


volmesh.operations
------------------


volmesh.algorithms
------------------


"""

from __future__ import print_function


class Datastructure(object):
    pass


from .network import *
from .mesh import *
from .volmesh import *

from .network import __all__ as a
from .mesh import __all__ as b
from .volmesh import __all__ as c

__all__ = a + b + c
