from fractions import Fraction as fr


def gcd(x, y):
    def gcd_new(x, y):
        if y == 0:
            return x
        return gcd_new(y, x % y)
    return gcd_new(abs(x), abs(y))


def observe(x, y):
    g = gcd(x, y)
    return fr(long(x/g), long(y/g))


def lcm(x, y):
    return long(x*y/gcd(x, y))


def form_change(material):
    new_list = list(map(sum, material))
    boolean_indices = list(map(lambda x: x == 0, new_list))
    indices = set([i for i, x in enumerate(boolean_indices) if x])
    new_material = []
    for i in range(len(material)):
        new_material.append(list(map(lambda x: fr(0, 1) if(
            new_list[i] == 0) else observe(x, new_list[i]), material[i])))
    transform_material = []
    zeros_mat = []
    for i in range(len(new_material)):
        if i not in indices:
            transform_material.append(new_material[i])
        else:
            zeros_mat.append(new_material[i])
    transform_material.extend(zeros_mat)
    tmat = []
    for i in range(len(transform_material)):
        tmat.append([])
        extend_mat = []
        for j in range(len(transform_material)):
            if j not in indices:
                tmat[i].append(transform_material[i][j])
            else:
                extend_mat.append(transform_material[i][j])
        tmat[i].extend(extend_mat)
    return [tmat, len(zeros_mat)]


def copy_material(material):
    c_material = []
    for i in range(len(material)):
        c_material.append([])
        for j in range(len(material[i])):
            c_material[i].append(
                fr(material[i][j].numerator, material[i][j].denominator))
    return c_material


def gauss_theme(m, values):
    material = copy_material(m)
    for i in range(len(material)):
        ind = -1
        for j in range(i, len(material)):
            if material[j][i].numerator != 0:
                ind = j
                break
        if ind == -1:
            raise ValueError('Gauss theorem failed to execute!')
        material[i], material[ind] = material[ind], material[j]
        values[i], values[ind] = values[ind], values[i]
        for j in range(i+1, len(material)):
            if material[j][i].numerator == 0:
                continue
            ratio = -material[j][i]/material[i][i]
            for k in range(i, len(material)):
                material[j][k] += ratio * material[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(material))]
    for i in range(len(material)):
        ind = len(material) - 1 - i
        end = len(material) - 1
        while end > ind:
            values[ind] -= material[ind][end] * res[end]
            end -= 1
        res[ind] = values[ind]/material[ind][ind]
    return res


def transposition(material):
    tmat = []
    for i in range(len(material)):
        for j in range(len(material)):
            if i == 0:
                tmat.append([])
            tmat[j].append(material[i][j])
    return tmat


def inverse(material):
    tmat = transposition(material)
    mat_inv = []
    for i in range(len(tmat)):
        values = [fr(int(i == j), 1) for j in range(len(material))]
        mat_inv.append(gauss_theme(tmat, values))
    return mat_inv


def material_multiplication(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(fr(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res


def splitQR(material, lengthR):
    lengthQ = len(material) - lengthR
    Q = []
    R = []
    for i in range(lengthQ):
        Q.append([int(i == j)-material[i][j] for j in range(lengthQ)])
        R.append(material[i][lengthQ:])
    return [Q, R]


def solution(material):
    res = form_change(material)
    if res[1] == len(material):
        return [1, 1]
    Q, R = splitQR(*res)
    inv = inverse(Q)
    res = material_multiplication(inv, R)
    row = res[0]
    l = 1
    for item in row:
        l = lcm(l, item.denominator)
    res = list(map(lambda x: long(x.numerator*l/x.denominator), row))
    res.append(l)
    return res
