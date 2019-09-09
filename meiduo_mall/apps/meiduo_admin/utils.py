def jwt_response_payload_handler(token, user=None, request=None):
    # token jwt生成的token
    # user 我们的登录用户信息
    # request 请求
    return{
        'token': token,
        'username': user.username,
        'id': user.id
    }