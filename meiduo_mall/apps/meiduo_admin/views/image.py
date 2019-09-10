from fdfs_client.client import Fdfs_client
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SKUImage, SKU
from apps.meiduo_admin.serializers.image import SKUImageSerializer, SimpleSKUSerializer
from apps.meiduo_admin.utils import PageNum


class ImageModelViewSet(ModelViewSet):

    queryset = SKUImage.objects.all()

    serializer_class = SKUImageSerializer

    pagination_class = PageNum

    def create(self, request, *args, **kwargs):
        """
        自己实现  Fdfs的图片上传
        把file_id 保存到数据库中

        1.获取图片资源
        2.通过Fdfs实现图片的保存
        3.获取remote file_id
        4.保存到数据库中
        5.返回响应

        """
        # 1.获取图片资源
        # InMemoryUploadedFile
        data = request.FILES.get('image')

        # 调用文件的 read方法来获取图片的二进制
        # data.read()

        # 2.通过Fdfs实现图片的保存
        client = Fdfs_client('utils/fastdfs/client.conf')
        # 将读取的二进制图片  上传到服务器中
        result = client.upload_by_buffer(data.read())
        # result = {
        #     "Status":"Upload successed.",
        #     "Remote file_id":"group1/M00/00/00/wKjlhFsTgJ2AJvG_AAAyZgOTZN0850.jpg"
        # }
        """
        {
        'Remote file_id': 'group1/M00/00/00/wKjlhFsTgJ2AJvG_AAAyZgOTZN0850.jpg',
        'Uploaded size': '12.00KB',
        'Local file name': '/home/python/Desktop/images/0.jpg',
        'Storage IP': '192.168.229.132',
        'Group name': 'group1',
        'Status': 'Upload successed.'
        }
        """

        # 3.获取remote file_id
        # 判断上传图片的状态,如果成功,则可以获取 file_id
        if result.get('Status') == "Upload successed.":
            file_id = result.get("Remote file_id")

        # 4.保存到数据库中
        new_object = SKUImage.objects.create(
            sku_id=request.data.get('sku'),
            image=file_id
        )

        # 5.返回响应
        from rest_framework import status
        return Response({
            "id": new_object.id,
            "sku": new_object.sku.id,
            "image": new_object.image.url
        }, status=status.HTTP_201_CREATED)

"""
想要新增图片,必须先获取所有SKU信息

1.查询所有的sku  [sku, sku, sku...]
2.对象列表转换为字典列表
3.返回响应
"""


class SimpleSKUListAPIView(ListAPIView):

    queryset = SKU.objects.all()

    serializer_class = SimpleSKUSerializer


