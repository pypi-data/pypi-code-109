# -*- coding: utf-8 -*-

import numpy as np
from scipy.spatial.transform import Rotation as sstr
from OpenGL.GL import *

from . import text
from . import cmap

FM = text.FontManager()
CM = cmap.ColorManager()

def y2v(v):
    """返回y轴正方向到向量v的旋转矩阵"""
    
    h =  np.linalg.norm(v)
    a_z = np.arccos(v[1]/h)
    
    if v[0] == 0:
        if v[2] == 0:
            a_x = 0
        elif v[2] > 0:
            a_x = -np.pi/2
        else:
            a_x = np.pi/2
    else:
        a_x = np.arctan(-v[2]/v[0]) + (np.pi if v[0] < 0 else 0)
    
    return np.float32(sstr.from_euler('zxy', [a_z, a_x, 0], degrees=False).as_matrix())

def rotate(axis_angle):
    """返回旋转矩阵
    
    axis_angle  - 轴角，由旋转向量和旋转角度组成的元组、列表或numpy数组。旋转方向使用右手定则
    """
    
    a, v = -axis_angle[3], np.array(axis_angle[:3])
    m = sstr.from_rotvec(np.radians(a)*v/np.linalg.norm(v)).as_matrix()
    m = np.hstack((m, np.array([[0.0], [0.0], [0.0]])))
    m = np.vstack((m, np.array([0.0, 0.0, 0.0, 1.0])))
    
    return np.float32(m)
    
def translate(shift):
    """返回平移矩阵
    
    shift       - 由xyz轴偏移量组成的元组、列表或numpy数组
    """
    
    v = np.array(shift).reshape(3,1)
    m = np.eye(4)
    m[3] += np.sum((m[:3] * v), axis=0)
    
    return np.float32(m)
    
def scale(k):
    """返回缩放矩阵
    
    k           - 缩放系数
    """
    
    v = np.array([k,k,k]).reshape(3,1)
    m = np.eye(4)
    m[:3] *= v
    
    return np.float32(m)

def model_matrix(*args):
    """返回模型矩阵
    
    args        - 旋转（4元组）、平移（3元组）、缩放（数值型）参数
    """
    
    m = np.eye(4)
    for item in args[::-1]:
        if isinstance(item, (int, float)):
            m = np.dot(m, scale(item))
        elif len(item) == 3:
            m = np.dot(m, translate(item))
        else:
            m = np.dot(m, rotate(item))
    
    return np.float32(m)
    
def view_matrix(cam_pos, cam_up, oecs):
    """返回视点矩阵
    
    cam_pos     - 相机位置
    cam_up      - 指向相机上方的单位向量
    oecs        - 视点坐标系ECS原点
    """
    
    camX, camY, camZ = cam_pos
    oecsX, oecsY, oecsZ = oecs
    upX, upY, upZ = cam_up
    
    f = np.array([oecsX-camX, oecsY-camY, oecsZ-camZ])
    f /= np.linalg.norm(f)
    s = np.array([f[1]*upZ - f[2]*upY, f[2]*upX - f[0]*upZ, f[0]*upY - f[1]*upX])
    s /= np.linalg.norm(s)
    u = np.cross(s, f)
    
    m = np.array([
        [s[0], u[0], -f[0], 0],
        [s[1], u[1], -f[1], 0],
        [s[2], u[2], -f[2], 0],
        [- s[0]*camX - s[1]*camY - s[2]*camZ, 
        - u[0]*camX - u[1]*camY - u[2]*camZ, 
        f[0]*camX + f[1]*camY + f[2]*camZ, 1]
    ], dtype=np.float32)
    
    return m
    
def proj_matrix(proj, hexa, zoom):
    """返回投影矩阵
    
    proj        - 投影模式，'ortho' - 正射投影，'frustum' - 透视投影
    hexa        - 视锥体的左右下上距离中心线的距离以及前后面距离相机的距离组成的元组
    zoom        - 视口缩放因子
    csize       - GL窗口宽高元组
    """
    
    left, right, bottom, top, near, far = hexa
    left, right, bottom, top = zoom*left, zoom*right, zoom*bottom, zoom*top
    rw, rh, rd = 1/(right - left), 1/(top - bottom), 1/(far - near)
    
    if proj == 'ortho':
        m = np.array([
            [2 * rw, 0, 0, 0],
            [0, 2 * rh, 0, 0],
            [0, 0, -2 * rd, 0],
            [-(right+left) * rw, -(top+bottom) * rh, -(far+near) * rd, 1]
        ], dtype=np.float32)
    else:
        m = np.array([
            [2 * near * rw, 0, 0, 0],
            [0, 2 * near * rh, 0, 0],
            [(right+left) * rw, (top+bottom) * rh, -(far + near) * rd, -1],
            [0, 0, -2 * near * far * rd, 0]
        ], dtype=np.float32)
    
    return m

def text2image(text, size, color, family=None, weight='normal'):
    """生成文本图像
    
    text        - 文本字符串
    size        - 字号，整型，默认32
    color       - 文本颜色，浮点型元组、列表或numpy数组，值域范围[0,1]，None表示使用场景默认的前景颜色
    family      - 字体，None表示当前默认的字体
    weight      - 字体的浓淡：'normal'-正常（默认），'light'-轻，'bold'-重
    """
    
    return FM.text2img(text, size, color, family=family, weight=weight)

def font_list():
    """返回当前系统可用字体列表"""
    
    return FM.get_font_list()
    
def color2c(color, drop=False, outsize=None):
    """检查颜色参数，将字符串、元组、列表等类型的颜色转为值域范围[0,1]的numpy数组颜色
    
    color       - 待处理的颜色
    drop        - 舍弃alpha通道
    outsize     - 返回颜色的数量：整型或整型元组，None表示不改变返回颜色的数量
    """
    
    return CM.color2c(color, drop=drop, outsize=outsize)
    
def color_list():
    """颜色列表"""
    
    return CM.color_list
    
def cmap_list():
    """调色板列表"""
    
    return CM.cmap_list
    
def color_help():
    """返回颜色中英文对照表"""
    
    return CM.color_help()
    
def cmap_help():
    """返回调色板分类列表"""
    
    return CM.cmap_help()
    
def cmap(data, cm, invalid=np.nan, invalid_c=(0,0,0,0), drange=None, alpha=None, drop=False):
    """数值映射到颜色
        
    data        - 数据
    cm          - 调色板
    invalid     - 无效数据的标识
    invalid_c   - 无效数据的颜色
    drange      - 数据动态范围，None表示使用data的动态范围
    alpha       - 透明度，None表示不改变当前透明度
    drop        - 舍弃alpha通道
    """
    
    return CM.cmap(data, cm, invalid=np.nan, invalid_c=(0,0,0,0), drange=None, alpha=None, drop=False)

def isosurface(data, level):
    """返回基于MarchingCube算法的等值面"""
    
    data = np.ascontiguousarray(data)
    mask = data < level
    face_shift_tables, edge_shifts, edge_table, n_table_faces = _get_data_cache()
    
    index = np.zeros([x-1 for x in data.shape], dtype=np.ubyte)
    fields = np.empty((2, 2, 2), dtype=object)
    slices = [slice(0, -1), slice(1, None)]
    for i in [0, 1]:
        for j in [0, 1]:
            for k in [0, 1]:
                fields[i, j, k] = mask[slices[i], slices[j], slices[k]]
                vertIndex = i - 2*j*i + 3*j + 4*k
                index += (fields[i, j, k] * 2**vertIndex).astype(np.ubyte)
    
    cut_edges = np.zeros([x+1 for x in index.shape]+[3], dtype=np.uint32)
    edges = edge_table[index]
    for i, shift in enumerate(edge_shifts[:12]):        
        slices = [slice(shift[j], cut_edges.shape[j]+(shift[j]-1)) 
                  for j in range(3)]
        cut_edges[slices[0], slices[1], slices[2], shift[3]] += edges & 2**i
    
    m = cut_edges > 0
    vertex_inds = np.argwhere(m)
    vertexes = vertex_inds[:, :3].astype(np.float32).copy()
    dataFlat = data.reshape(data.shape[0]*data.shape[1]*data.shape[2])
    
    cut_edges[vertex_inds[:, 0], 
              vertex_inds[:, 1], 
              vertex_inds[:, 2], 
              vertex_inds[:, 3]] = np.arange(vertex_inds.shape[0])
    
    for i in [0, 1, 2]:
        vim = vertex_inds[:, 3] == i
        vi = vertex_inds[vim, :3]
        vi_flat = (vi * (np.array(data.strides[:3]) // 
                         data.itemsize)[np.newaxis, :]).sum(axis=1)
        v1 = dataFlat[vi_flat]
        v2 = dataFlat[vi_flat + data.strides[i]//data.itemsize]
        vertexes[vim, i] += (level-v1) / (v2-v1)
    
    n_faces = n_table_faces[index]
    tot_faces = n_faces.sum()
    faces = np.empty((tot_faces, 3), dtype=np.uint32)
    ptr = 0
    
    cs = np.array(cut_edges.strides)//cut_edges.itemsize
    cut_edges = cut_edges.flatten()
    
    for i in range(1, 6):
        cells = np.argwhere(n_faces == i)  
        if cells.shape[0] == 0:
            continue
        cellInds = index[cells[:, 0], cells[:, 1], cells[:, 2]]
        
        verts = face_shift_tables[i][cellInds]
        verts[..., :3] += (cells[:, np.newaxis, np.newaxis, :]).astype(np.uint16)
        verts = verts.reshape((verts.shape[0]*i,)+verts.shape[2:])
        
        verts = (verts * cs[np.newaxis, np.newaxis, :]).sum(axis=2)
        vert_inds = cut_edges[verts]
        nv = vert_inds.shape[0]
        faces[ptr:ptr+nv] = vert_inds
        ptr += nv
    
    return vertexes, faces

def _get_data_cache():
    edge_table = np.array([
        0x0,   0x109, 0x203, 0x30a, 0x406, 0x50f, 0x605, 0x70c,
        0x80c, 0x905, 0xa0f, 0xb06, 0xc0a, 0xd03, 0xe09, 0xf00,
        0x190, 0x99,  0x393, 0x29a, 0x596, 0x49f, 0x795, 0x69c,
        0x99c, 0x895, 0xb9f, 0xa96, 0xd9a, 0xc93, 0xf99, 0xe90,
        0x230, 0x339, 0x33,  0x13a, 0x636, 0x73f, 0x435, 0x53c,
        0xa3c, 0xb35, 0x83f, 0x936, 0xe3a, 0xf33, 0xc39, 0xd30,
        0x3a0, 0x2a9, 0x1a3, 0xaa,  0x7a6, 0x6af, 0x5a5, 0x4ac,
        0xbac, 0xaa5, 0x9af, 0x8a6, 0xfaa, 0xea3, 0xda9, 0xca0,
        0x460, 0x569, 0x663, 0x76a, 0x66,  0x16f, 0x265, 0x36c,
        0xc6c, 0xd65, 0xe6f, 0xf66, 0x86a, 0x963, 0xa69, 0xb60,
        0x5f0, 0x4f9, 0x7f3, 0x6fa, 0x1f6, 0xff,  0x3f5, 0x2fc,
        0xdfc, 0xcf5, 0xfff, 0xef6, 0x9fa, 0x8f3, 0xbf9, 0xaf0,
        0x650, 0x759, 0x453, 0x55a, 0x256, 0x35f, 0x55,  0x15c,
        0xe5c, 0xf55, 0xc5f, 0xd56, 0xa5a, 0xb53, 0x859, 0x950,
        0x7c0, 0x6c9, 0x5c3, 0x4ca, 0x3c6, 0x2cf, 0x1c5, 0xcc, 
        0xfcc, 0xec5, 0xdcf, 0xcc6, 0xbca, 0xac3, 0x9c9, 0x8c0,
        0x8c0, 0x9c9, 0xac3, 0xbca, 0xcc6, 0xdcf, 0xec5, 0xfcc,
        0xcc,  0x1c5, 0x2cf, 0x3c6, 0x4ca, 0x5c3, 0x6c9, 0x7c0,
        0x950, 0x859, 0xb53, 0xa5a, 0xd56, 0xc5f, 0xf55, 0xe5c,
        0x15c, 0x55,  0x35f, 0x256, 0x55a, 0x453, 0x759, 0x650,
        0xaf0, 0xbf9, 0x8f3, 0x9fa, 0xef6, 0xfff, 0xcf5, 0xdfc,
        0x2fc, 0x3f5, 0xff,  0x1f6, 0x6fa, 0x7f3, 0x4f9, 0x5f0,
        0xb60, 0xa69, 0x963, 0x86a, 0xf66, 0xe6f, 0xd65, 0xc6c,
        0x36c, 0x265, 0x16f, 0x66,  0x76a, 0x663, 0x569, 0x460,
        0xca0, 0xda9, 0xea3, 0xfaa, 0x8a6, 0x9af, 0xaa5, 0xbac,
        0x4ac, 0x5a5, 0x6af, 0x7a6, 0xaa,  0x1a3, 0x2a9, 0x3a0,
        0xd30, 0xc39, 0xf33, 0xe3a, 0x936, 0x83f, 0xb35, 0xa3c,
        0x53c, 0x435, 0x73f, 0x636, 0x13a, 0x33,  0x339, 0x230,
        0xe90, 0xf99, 0xc93, 0xd9a, 0xa96, 0xb9f, 0x895, 0x99c,
        0x69c, 0x795, 0x49f, 0x596, 0x29a, 0x393, 0x99,  0x190,
        0xf00, 0xe09, 0xd03, 0xc0a, 0xb06, 0xa0f, 0x905, 0x80c,
        0x70c, 0x605, 0x50f, 0x406, 0x30a, 0x203, 0x109, 0x0   
    ], dtype=np.uint16)
    
    triTable = [
        [],
        [0, 8, 3],
        [0, 1, 9],
        [1, 8, 3, 9, 8, 1],
        [1, 2, 10],
        [0, 8, 3, 1, 2, 10],
        [9, 2, 10, 0, 2, 9],
        [2, 8, 3, 2, 10, 8, 10, 9, 8],
        [3, 11, 2],
        [0, 11, 2, 8, 11, 0],
        [1, 9, 0, 2, 3, 11],
        [1, 11, 2, 1, 9, 11, 9, 8, 11],
        [3, 10, 1, 11, 10, 3],
        [0, 10, 1, 0, 8, 10, 8, 11, 10],
        [3, 9, 0, 3, 11, 9, 11, 10, 9],
        [9, 8, 10, 10, 8, 11],
        [4, 7, 8],
        [4, 3, 0, 7, 3, 4],
        [0, 1, 9, 8, 4, 7],
        [4, 1, 9, 4, 7, 1, 7, 3, 1],
        [1, 2, 10, 8, 4, 7],
        [3, 4, 7, 3, 0, 4, 1, 2, 10],
        [9, 2, 10, 9, 0, 2, 8, 4, 7],
        [2, 10, 9, 2, 9, 7, 2, 7, 3, 7, 9, 4],
        [8, 4, 7, 3, 11, 2],
        [11, 4, 7, 11, 2, 4, 2, 0, 4],
        [9, 0, 1, 8, 4, 7, 2, 3, 11],
        [4, 7, 11, 9, 4, 11, 9, 11, 2, 9, 2, 1],
        [3, 10, 1, 3, 11, 10, 7, 8, 4],
        [1, 11, 10, 1, 4, 11, 1, 0, 4, 7, 11, 4],
        [4, 7, 8, 9, 0, 11, 9, 11, 10, 11, 0, 3],
        [4, 7, 11, 4, 11, 9, 9, 11, 10],
        [9, 5, 4],
        [9, 5, 4, 0, 8, 3],
        [0, 5, 4, 1, 5, 0],
        [8, 5, 4, 8, 3, 5, 3, 1, 5],
        [1, 2, 10, 9, 5, 4],
        [3, 0, 8, 1, 2, 10, 4, 9, 5],
        [5, 2, 10, 5, 4, 2, 4, 0, 2],
        [2, 10, 5, 3, 2, 5, 3, 5, 4, 3, 4, 8],
        [9, 5, 4, 2, 3, 11],
        [0, 11, 2, 0, 8, 11, 4, 9, 5],
        [0, 5, 4, 0, 1, 5, 2, 3, 11],
        [2, 1, 5, 2, 5, 8, 2, 8, 11, 4, 8, 5],
        [10, 3, 11, 10, 1, 3, 9, 5, 4],
        [4, 9, 5, 0, 8, 1, 8, 10, 1, 8, 11, 10],
        [5, 4, 0, 5, 0, 11, 5, 11, 10, 11, 0, 3],
        [5, 4, 8, 5, 8, 10, 10, 8, 11],
        [9, 7, 8, 5, 7, 9],
        [9, 3, 0, 9, 5, 3, 5, 7, 3],
        [0, 7, 8, 0, 1, 7, 1, 5, 7],
        [1, 5, 3, 3, 5, 7],
        [9, 7, 8, 9, 5, 7, 10, 1, 2],
        [10, 1, 2, 9, 5, 0, 5, 3, 0, 5, 7, 3],
        [8, 0, 2, 8, 2, 5, 8, 5, 7, 10, 5, 2],
        [2, 10, 5, 2, 5, 3, 3, 5, 7],
        [7, 9, 5, 7, 8, 9, 3, 11, 2],
        [9, 5, 7, 9, 7, 2, 9, 2, 0, 2, 7, 11],
        [2, 3, 11, 0, 1, 8, 1, 7, 8, 1, 5, 7],
        [11, 2, 1, 11, 1, 7, 7, 1, 5],
        [9, 5, 8, 8, 5, 7, 10, 1, 3, 10, 3, 11],
        [5, 7, 0, 5, 0, 9, 7, 11, 0, 1, 0, 10, 11, 10, 0],
        [11, 10, 0, 11, 0, 3, 10, 5, 0, 8, 0, 7, 5, 7, 0],
        [11, 10, 5, 7, 11, 5],
        [10, 6, 5],
        [0, 8, 3, 5, 10, 6],
        [9, 0, 1, 5, 10, 6],
        [1, 8, 3, 1, 9, 8, 5, 10, 6],
        [1, 6, 5, 2, 6, 1],
        [1, 6, 5, 1, 2, 6, 3, 0, 8],
        [9, 6, 5, 9, 0, 6, 0, 2, 6],
        [5, 9, 8, 5, 8, 2, 5, 2, 6, 3, 2, 8],
        [2, 3, 11, 10, 6, 5],
        [11, 0, 8, 11, 2, 0, 10, 6, 5],
        [0, 1, 9, 2, 3, 11, 5, 10, 6],
        [5, 10, 6, 1, 9, 2, 9, 11, 2, 9, 8, 11],
        [6, 3, 11, 6, 5, 3, 5, 1, 3],
        [0, 8, 11, 0, 11, 5, 0, 5, 1, 5, 11, 6],
        [3, 11, 6, 0, 3, 6, 0, 6, 5, 0, 5, 9],
        [6, 5, 9, 6, 9, 11, 11, 9, 8],
        [5, 10, 6, 4, 7, 8],
        [4, 3, 0, 4, 7, 3, 6, 5, 10],
        [1, 9, 0, 5, 10, 6, 8, 4, 7],
        [10, 6, 5, 1, 9, 7, 1, 7, 3, 7, 9, 4],
        [6, 1, 2, 6, 5, 1, 4, 7, 8],
        [1, 2, 5, 5, 2, 6, 3, 0, 4, 3, 4, 7],
        [8, 4, 7, 9, 0, 5, 0, 6, 5, 0, 2, 6],
        [7, 3, 9, 7, 9, 4, 3, 2, 9, 5, 9, 6, 2, 6, 9],
        [3, 11, 2, 7, 8, 4, 10, 6, 5],
        [5, 10, 6, 4, 7, 2, 4, 2, 0, 2, 7, 11],
        [0, 1, 9, 4, 7, 8, 2, 3, 11, 5, 10, 6],
        [9, 2, 1, 9, 11, 2, 9, 4, 11, 7, 11, 4, 5, 10, 6],
        [8, 4, 7, 3, 11, 5, 3, 5, 1, 5, 11, 6],
        [5, 1, 11, 5, 11, 6, 1, 0, 11, 7, 11, 4, 0, 4, 11],
        [0, 5, 9, 0, 6, 5, 0, 3, 6, 11, 6, 3, 8, 4, 7],
        [6, 5, 9, 6, 9, 11, 4, 7, 9, 7, 11, 9],
        [10, 4, 9, 6, 4, 10],
        [4, 10, 6, 4, 9, 10, 0, 8, 3],
        [10, 0, 1, 10, 6, 0, 6, 4, 0],
        [8, 3, 1, 8, 1, 6, 8, 6, 4, 6, 1, 10],
        [1, 4, 9, 1, 2, 4, 2, 6, 4],
        [3, 0, 8, 1, 2, 9, 2, 4, 9, 2, 6, 4],
        [0, 2, 4, 4, 2, 6],
        [8, 3, 2, 8, 2, 4, 4, 2, 6],
        [10, 4, 9, 10, 6, 4, 11, 2, 3],
        [0, 8, 2, 2, 8, 11, 4, 9, 10, 4, 10, 6],
        [3, 11, 2, 0, 1, 6, 0, 6, 4, 6, 1, 10],
        [6, 4, 1, 6, 1, 10, 4, 8, 1, 2, 1, 11, 8, 11, 1],
        [9, 6, 4, 9, 3, 6, 9, 1, 3, 11, 6, 3],
        [8, 11, 1, 8, 1, 0, 11, 6, 1, 9, 1, 4, 6, 4, 1],
        [3, 11, 6, 3, 6, 0, 0, 6, 4],
        [6, 4, 8, 11, 6, 8],
        [7, 10, 6, 7, 8, 10, 8, 9, 10],
        [0, 7, 3, 0, 10, 7, 0, 9, 10, 6, 7, 10],
        [10, 6, 7, 1, 10, 7, 1, 7, 8, 1, 8, 0],
        [10, 6, 7, 10, 7, 1, 1, 7, 3],
        [1, 2, 6, 1, 6, 8, 1, 8, 9, 8, 6, 7],
        [2, 6, 9, 2, 9, 1, 6, 7, 9, 0, 9, 3, 7, 3, 9],
        [7, 8, 0, 7, 0, 6, 6, 0, 2],
        [7, 3, 2, 6, 7, 2],
        [2, 3, 11, 10, 6, 8, 10, 8, 9, 8, 6, 7],
        [2, 0, 7, 2, 7, 11, 0, 9, 7, 6, 7, 10, 9, 10, 7],
        [1, 8, 0, 1, 7, 8, 1, 10, 7, 6, 7, 10, 2, 3, 11],
        [11, 2, 1, 11, 1, 7, 10, 6, 1, 6, 7, 1],
        [8, 9, 6, 8, 6, 7, 9, 1, 6, 11, 6, 3, 1, 3, 6],
        [0, 9, 1, 11, 6, 7],
        [7, 8, 0, 7, 0, 6, 3, 11, 0, 11, 6, 0],
        [7, 11, 6],
        [7, 6, 11],
        [3, 0, 8, 11, 7, 6],
        [0, 1, 9, 11, 7, 6],
        [8, 1, 9, 8, 3, 1, 11, 7, 6],
        [10, 1, 2, 6, 11, 7],
        [1, 2, 10, 3, 0, 8, 6, 11, 7],
        [2, 9, 0, 2, 10, 9, 6, 11, 7],
        [6, 11, 7, 2, 10, 3, 10, 8, 3, 10, 9, 8],
        [7, 2, 3, 6, 2, 7],
        [7, 0, 8, 7, 6, 0, 6, 2, 0],
        [2, 7, 6, 2, 3, 7, 0, 1, 9],
        [1, 6, 2, 1, 8, 6, 1, 9, 8, 8, 7, 6],
        [10, 7, 6, 10, 1, 7, 1, 3, 7],
        [10, 7, 6, 1, 7, 10, 1, 8, 7, 1, 0, 8],
        [0, 3, 7, 0, 7, 10, 0, 10, 9, 6, 10, 7],
        [7, 6, 10, 7, 10, 8, 8, 10, 9],
        [6, 8, 4, 11, 8, 6],
        [3, 6, 11, 3, 0, 6, 0, 4, 6],
        [8, 6, 11, 8, 4, 6, 9, 0, 1],
        [9, 4, 6, 9, 6, 3, 9, 3, 1, 11, 3, 6],
        [6, 8, 4, 6, 11, 8, 2, 10, 1],
        [1, 2, 10, 3, 0, 11, 0, 6, 11, 0, 4, 6],
        [4, 11, 8, 4, 6, 11, 0, 2, 9, 2, 10, 9],
        [10, 9, 3, 10, 3, 2, 9, 4, 3, 11, 3, 6, 4, 6, 3],
        [8, 2, 3, 8, 4, 2, 4, 6, 2],
        [0, 4, 2, 4, 6, 2],
        [1, 9, 0, 2, 3, 4, 2, 4, 6, 4, 3, 8],
        [1, 9, 4, 1, 4, 2, 2, 4, 6],
        [8, 1, 3, 8, 6, 1, 8, 4, 6, 6, 10, 1],
        [10, 1, 0, 10, 0, 6, 6, 0, 4],
        [4, 6, 3, 4, 3, 8, 6, 10, 3, 0, 3, 9, 10, 9, 3],
        [10, 9, 4, 6, 10, 4],
        [4, 9, 5, 7, 6, 11],
        [0, 8, 3, 4, 9, 5, 11, 7, 6],
        [5, 0, 1, 5, 4, 0, 7, 6, 11],
        [11, 7, 6, 8, 3, 4, 3, 5, 4, 3, 1, 5],
        [9, 5, 4, 10, 1, 2, 7, 6, 11],
        [6, 11, 7, 1, 2, 10, 0, 8, 3, 4, 9, 5],
        [7, 6, 11, 5, 4, 10, 4, 2, 10, 4, 0, 2],
        [3, 4, 8, 3, 5, 4, 3, 2, 5, 10, 5, 2, 11, 7, 6],
        [7, 2, 3, 7, 6, 2, 5, 4, 9],
        [9, 5, 4, 0, 8, 6, 0, 6, 2, 6, 8, 7],
        [3, 6, 2, 3, 7, 6, 1, 5, 0, 5, 4, 0],
        [6, 2, 8, 6, 8, 7, 2, 1, 8, 4, 8, 5, 1, 5, 8],
        [9, 5, 4, 10, 1, 6, 1, 7, 6, 1, 3, 7],
        [1, 6, 10, 1, 7, 6, 1, 0, 7, 8, 7, 0, 9, 5, 4],
        [4, 0, 10, 4, 10, 5, 0, 3, 10, 6, 10, 7, 3, 7, 10],
        [7, 6, 10, 7, 10, 8, 5, 4, 10, 4, 8, 10],
        [6, 9, 5, 6, 11, 9, 11, 8, 9],
        [3, 6, 11, 0, 6, 3, 0, 5, 6, 0, 9, 5],
        [0, 11, 8, 0, 5, 11, 0, 1, 5, 5, 6, 11],
        [6, 11, 3, 6, 3, 5, 5, 3, 1],
        [1, 2, 10, 9, 5, 11, 9, 11, 8, 11, 5, 6],
        [0, 11, 3, 0, 6, 11, 0, 9, 6, 5, 6, 9, 1, 2, 10],
        [11, 8, 5, 11, 5, 6, 8, 0, 5, 10, 5, 2, 0, 2, 5],
        [6, 11, 3, 6, 3, 5, 2, 10, 3, 10, 5, 3],
        [5, 8, 9, 5, 2, 8, 5, 6, 2, 3, 8, 2],
        [9, 5, 6, 9, 6, 0, 0, 6, 2],
        [1, 5, 8, 1, 8, 0, 5, 6, 8, 3, 8, 2, 6, 2, 8],
        [1, 5, 6, 2, 1, 6],
        [1, 3, 6, 1, 6, 10, 3, 8, 6, 5, 6, 9, 8, 9, 6],
        [10, 1, 0, 10, 0, 6, 9, 5, 0, 5, 6, 0],
        [0, 3, 8, 5, 6, 10],
        [10, 5, 6],
        [11, 5, 10, 7, 5, 11],
        [11, 5, 10, 11, 7, 5, 8, 3, 0],
        [5, 11, 7, 5, 10, 11, 1, 9, 0],
        [10, 7, 5, 10, 11, 7, 9, 8, 1, 8, 3, 1],
        [11, 1, 2, 11, 7, 1, 7, 5, 1],
        [0, 8, 3, 1, 2, 7, 1, 7, 5, 7, 2, 11],
        [9, 7, 5, 9, 2, 7, 9, 0, 2, 2, 11, 7],
        [7, 5, 2, 7, 2, 11, 5, 9, 2, 3, 2, 8, 9, 8, 2],
        [2, 5, 10, 2, 3, 5, 3, 7, 5],
        [8, 2, 0, 8, 5, 2, 8, 7, 5, 10, 2, 5],
        [9, 0, 1, 5, 10, 3, 5, 3, 7, 3, 10, 2],
        [9, 8, 2, 9, 2, 1, 8, 7, 2, 10, 2, 5, 7, 5, 2],
        [1, 3, 5, 3, 7, 5],
        [0, 8, 7, 0, 7, 1, 1, 7, 5],
        [9, 0, 3, 9, 3, 5, 5, 3, 7],
        [9, 8, 7, 5, 9, 7],
        [5, 8, 4, 5, 10, 8, 10, 11, 8],
        [5, 0, 4, 5, 11, 0, 5, 10, 11, 11, 3, 0],
        [0, 1, 9, 8, 4, 10, 8, 10, 11, 10, 4, 5],
        [10, 11, 4, 10, 4, 5, 11, 3, 4, 9, 4, 1, 3, 1, 4],
        [2, 5, 1, 2, 8, 5, 2, 11, 8, 4, 5, 8],
        [0, 4, 11, 0, 11, 3, 4, 5, 11, 2, 11, 1, 5, 1, 11],
        [0, 2, 5, 0, 5, 9, 2, 11, 5, 4, 5, 8, 11, 8, 5],
        [9, 4, 5, 2, 11, 3],
        [2, 5, 10, 3, 5, 2, 3, 4, 5, 3, 8, 4],
        [5, 10, 2, 5, 2, 4, 4, 2, 0],
        [3, 10, 2, 3, 5, 10, 3, 8, 5, 4, 5, 8, 0, 1, 9],
        [5, 10, 2, 5, 2, 4, 1, 9, 2, 9, 4, 2],
        [8, 4, 5, 8, 5, 3, 3, 5, 1],
        [0, 4, 5, 1, 0, 5],
        [8, 4, 5, 8, 5, 3, 9, 0, 5, 0, 3, 5],
        [9, 4, 5],
        [4, 11, 7, 4, 9, 11, 9, 10, 11],
        [0, 8, 3, 4, 9, 7, 9, 11, 7, 9, 10, 11],
        [1, 10, 11, 1, 11, 4, 1, 4, 0, 7, 4, 11],
        [3, 1, 4, 3, 4, 8, 1, 10, 4, 7, 4, 11, 10, 11, 4],
        [4, 11, 7, 9, 11, 4, 9, 2, 11, 9, 1, 2],
        [9, 7, 4, 9, 11, 7, 9, 1, 11, 2, 11, 1, 0, 8, 3],
        [11, 7, 4, 11, 4, 2, 2, 4, 0],
        [11, 7, 4, 11, 4, 2, 8, 3, 4, 3, 2, 4],
        [2, 9, 10, 2, 7, 9, 2, 3, 7, 7, 4, 9],
        [9, 10, 7, 9, 7, 4, 10, 2, 7, 8, 7, 0, 2, 0, 7],
        [3, 7, 10, 3, 10, 2, 7, 4, 10, 1, 10, 0, 4, 0, 10],
        [1, 10, 2, 8, 7, 4],
        [4, 9, 1, 4, 1, 7, 7, 1, 3],
        [4, 9, 1, 4, 1, 7, 0, 8, 1, 8, 7, 1],
        [4, 0, 3, 7, 4, 3],
        [4, 8, 7],
        [9, 10, 8, 10, 11, 8],
        [3, 0, 9, 3, 9, 11, 11, 9, 10],
        [0, 1, 10, 0, 10, 8, 8, 10, 11],
        [3, 1, 10, 11, 3, 10],
        [1, 2, 11, 1, 11, 9, 9, 11, 8],
        [3, 0, 9, 3, 9, 11, 1, 2, 9, 2, 11, 9],
        [0, 2, 11, 8, 0, 11],
        [3, 2, 11],
        [2, 3, 8, 2, 8, 10, 10, 8, 9],
        [9, 10, 2, 0, 9, 2],
        [2, 3, 8, 2, 8, 10, 0, 1, 8, 1, 10, 8],
        [1, 10, 2],
        [1, 3, 8, 9, 1, 8],
        [0, 9, 1],
        [0, 3, 8],
        []
    ]
    
    edge_shifts = np.array([
        [0, 0, 0, 0],   
        [1, 0, 0, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [1, 0, 1, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 2],
        [1, 0, 0, 2],
        [1, 1, 0, 2],
        [0, 1, 0, 2]
    ], dtype=np.uint16) 
    
    n_table_faces = np.array([len(f)/3 for f in triTable], dtype=np.ubyte)
    face_shift_tables = [None]
    for i in range(1, 6):
        faceTableI = np.zeros((len(triTable), i*3), dtype=np.ubyte)
        faceTableInds = np.argwhere(n_table_faces == i)[:, 0]
        faceTableI[faceTableInds] = np.array([triTable[j] for j in faceTableInds])
        faceTableI = faceTableI.reshape((len(triTable), i, 3))
        face_shift_tables.append(edge_shifts[faceTableI])
        
    return face_shift_tables, edge_shifts, edge_table, n_table_faces
