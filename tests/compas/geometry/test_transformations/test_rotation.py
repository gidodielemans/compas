from compas.geometry import Frame
from compas.geometry import Rotation
from compas.geometry import Transformation
from compas.tolerance import TOL
from compas.geometry import normalize_vector


def test_from_basis_vectors():
    xaxis = [0.68, 0.68, 0.27]
    yaxis = [-0.67, 0.73, -0.15]
    R = Rotation.from_basis_vectors(xaxis, yaxis)
    matrix = [
        [0.6807833515407016, -0.6687681611113407, -0.29880282253789103, 0.0],
        [0.6807833515407016, 0.7282315114847181, -0.07882160714891209, 0.0],
        [0.2703110366411609, -0.14975954908850603, 0.9510541192112079, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    assert TOL.is_allclose(R.matrix, matrix)


def test_from_frame():
    f1 = Frame([1, 1, 1], [0.68, 0.68, 0.27], [-0.67, 0.73, -0.15])
    T = Transformation.from_frame(f1)
    f2 = Frame.from_transformation(T)
    assert TOL.is_allclose(f1, f2)


def test_from_quaternion():
    q1 = [0.945, -0.021, -0.125, 0.303]
    R = Rotation.from_quaternion(q1)
    q2 = R.quaternion
    assert TOL.is_allclose(q1, q2, atol=1e-3)


def test_from_axis_angle_vector():
    axis1 = normalize_vector([-0.043, -0.254, 0.617])
    angle1 = 0.1
    R = Rotation.from_axis_and_angle(axis1, angle1)
    axis2, angle2 = R.axis_and_angle
    assert TOL.is_allclose(axis1, axis2)
    assert TOL.is_allclose([angle1], [angle2])


def test_from_euler_angles():
    ea1 = 1.4, 0.5, 2.3
    args = False, "xyz"
    R1 = Rotation.from_euler_angles(ea1, *args)
    ea2 = R1.euler_angles(*args)
    assert TOL.is_allclose(ea1, ea2)

    alpha, beta, gamma = ea1
    xaxis, yaxis, zaxis = [1, 0, 0], [0, 1, 0], [0, 0, 1]
    Rx = Rotation.from_axis_and_angle(xaxis, alpha)
    Ry = Rotation.from_axis_and_angle(yaxis, beta)
    Rz = Rotation.from_axis_and_angle(zaxis, gamma)
    R2 = Rx * Ry * Rz
    assert TOL.is_allclose(R1, R2)


def test_quaternion():
    q1 = [0.945, -0.021, -0.125, 0.303]
    R = Rotation.from_quaternion(q1)
    q2 = R.quaternion
    assert TOL.is_allclose(q1, q2, atol=1e-3)


def test_axis_and_angle():
    axis1 = normalize_vector([-0.043, -0.254, 0.617])
    angle1 = 0.1
    R = Rotation.from_axis_and_angle(axis1, angle1)
    axis2, angle2 = R.axis_and_angle
    assert TOL.is_allclose(axis1, axis2)
    assert TOL.is_allclose([angle1], [angle2])


def test_axis_angle_vector():
    aav1 = [-0.043, -0.254, 0.617]
    R = Rotation.from_axis_angle_vector(aav1)
    aav2 = R.axis_angle_vector
    assert TOL.is_allclose(aav1, aav2)


def test_euler_angles():
    ea1 = 1.4, 0.5, 2.3
    args = False, "xyz"
    R1 = Rotation.from_euler_angles(ea1, *args)
    ea2 = R1.euler_angles(*args)
    assert TOL.is_allclose(ea1, ea2)


def test_basis_vectors():
    ea1 = 1.4, 0.5, 2.3
    args = False, "xyz"
    R = Rotation.from_euler_angles(ea1, *args)
    basis_vectors = [
        [-0.5847122176808724, -0.18803656702967916, 0.789147560317086],
        [-0.6544178905170501, -0.4655532858863264, -0.5958165511058404],
    ]
    assert TOL.is_allclose(R.basis_vectors, basis_vectors)
