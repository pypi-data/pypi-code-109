# Tencent is pleased to support the open source community by making ncnn available.
#
# Copyright (C) 2020 THL A29 Limited, a Tencent company. All rights reserved.
#
# Licensed under the BSD 3-Clause License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# https://opensource.org/licenses/BSD-3-Clause
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import pytest

import ncnn


def test_blob():
    blob = ncnn.Blob()

    blob.name = "myblob"
    assert blob.name == "myblob"

    blob.producer = 0
    assert blob.producer == 0

    blob.consumer = 0
    assert blob.consumer == 0

    blob.shape = ncnn.Mat(1)
    assert blob.shape.dims == 1 and blob.shape.w == 1
