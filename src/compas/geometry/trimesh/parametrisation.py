from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.plugins import pluggable


@pluggable(category="trimesh")
def trimesh_harmonic(M, boundary, values):
    """Compute the harmonic parametrisation of a triangle mesh within a fixed circular boundary.

    Parameters
    ----------
    M : tuple[sequence[[float, float, float] | :class:`~compas.geometry.Point`], sequence[[int, int, int]]]
        A mesh represented by a list of vertices and a list of faces.
    boundary : list[int]
        The vertices on the boundary.
    values : list[[float, float]]
        The parametrisation values of the boundary vertices.

    Returns
    -------
    list[[int, int]]
        The u, v parameters per vertex.

    Examples
    --------
    >>>

    """
    raise NotImplementedError


@pluggable(category="trimesh")
def trimesh_lscm(M, boundary):
    """Compute the least squares conformal map of a triangle mesh.

    Parameters
    ----------
    M : tuple[sequence[[float, float, float] | :class:`~compas.geometry.Point`], sequence[[int, int, int]]]
        A mesh represented by a list of vertices and a list of faces.
    boundary : list[int]
        The vertices on the boundary.

    Returns
    -------
    list[[int, int]]
        The u, v parameters per vertex.

    Examples
    --------
    >>>

    """
    raise NotImplementedError
