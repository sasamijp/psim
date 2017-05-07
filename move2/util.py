import numpy as np


def rotate(vec2, theta):
    c = np.cos(theta)
    s = np.sin(theta)
    r = np.array([[c, -s],
                  [s, c]])
    return np.dot(r, vec2)


def intersection2d(l_start, l_end, m_start, m_end):
    """

    :type l_start: np.array(2)
    :type l_end: np.array(2)
    :type m_start: np.array(2)
    :type m_end: np.array(2)

    """

    ax = l_start[0]
    ay = l_start[1]
    bx = l_end[0]
    by = l_end[1]
    cx = m_start[0]
    cy = m_start[1]
    dx = m_end[0]
    dy = m_end[1]

    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)

    return tc * td < 0 and ta * tb < 0


def min_distance2d2(l_start, l_end, p):  # 2darray
    x0 = p[0]
    y0 = p[1]
    x1 = l_start[0]
    y1 = l_start[1]
    x2 = l_end[0]
    y2 = l_end[1]

    a = x2 - x1
    b = y2 - y1
    a2 = a * a
    b2 = b * b
    r2 = a2 + b2
    tt = -(a * (x1 - x0) + b * (y1 - y0));
    if tt < 0:
        return (x1 - x0) * (x1 - x0) + (y1 - y0) * (y1 - y0)

    if tt > r2:
        return (x2 - x0) * (x2 - x0) + (y2 - y0) * (y2 - y0)

    f1 = a * (y1 - y0) - b * (x1 - x0)
    return (f1 * f1) / r2
