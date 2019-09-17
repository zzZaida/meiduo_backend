from fdfs_client.client import Fdfs_client
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import Brand
from apps.meiduo_admin.serializers.brand import BrandSerializer
from apps.meiduo_admin.utils import PageNum


class BrandViewSet(ModelViewSet):

    queryset = Brand.objects.all()

    serializer_class = BrandSerializer

    pagination_class = PageNum

    def create(self, request, *args, **kwargs):

        # 1.获取图片资源
        # InMemoryUploadedFile
        data = request.FILES.get('logo')

        # 调用文件的 read方法来获取图片的二进制
        # data.read()

        # 2.通过Fdfs实现图片的保存
        client = Fdfs_client('utils/fastdfs/client.conf')
        # 将读取的二进制图片  上传到服务器中
        result = {
            'Remote file_id': 'group1/M00/00/02/CtM3BVrRbvmAJ0cWAAAefuA2Xqo3496149'
        }

        # 3.获取remote file_id
        # 判断上传图片的状态,如果成功,则可以获取 file_id
        # if result.get('Status') == "Upload successed.":
        file_id = result.get("Remote file_id")

        # 4.保存到数据库中
        new_object = Brand.objects.create(
            name= request.data.get('name'),
            first_letter=request.data.get('first_letter'),
            logo=file_id
        )

        # 5.返回响应
        from rest_framework import status
        return Response({
            "id": new_object.id,
            "name":new_object.name,
            "first_letter": new_object.first_letter,
            "logo": new_object.logo.url
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # 创建FastDFS连接对象
        from fdfs_client.client import Fdfs_client
        client = Fdfs_client('utils/fastdfs/client.conf')
        # 获取前端传递的image文件
        data = request.FILES.get('logo')
        # 上传图片到fastDFS
        # res = client.upload_by_buffer(data.read())
        res = {
            'Remote file_id': 'group1/M00/00/02/CtM3BVrRbvmAJ0cWAAAefuA2Xqo3496149'
        }

        # 判断是否上传成功
        # if res['Status'] != 'Upload successed.':
        #     return Response(status=403)
        # 获取上传后的路径
        image_url = res['Remote file_id']
        # 获取sku_id
        # sku_id = request.data.get('sku')
        # 查询图片对象
        img = Brand.objects.get(id=kwargs['pk'])
        # 更新图片
        img.logo = image_url
        img.name = request.data.get('name')
        img.first_letter = request.data.get('first_letter')
        img.save()
        # 返回结果
        return Response(
            {
                'id': img.id,
                'name': img.name,
                'logo': img.logo.url,
                'first_letter': img.first_letter
            },
            status=201  # 前端需要接受201状态码
        )