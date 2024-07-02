from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from User.serializers import UserFriendsSerializer
from django.contrib.auth import get_user_model
from friendship.models import Friend
from friendship.models import FriendshipRequest
from django.http import HttpRequest


class FriendsOperationsView(ModelViewSet):
    serializer_class = UserFriendsSerializer
    
    @action(methods=['POST'], detail=False)
    def add_friend(self, request: HttpRequest) -> Response:
        user_model = get_user_model()
        pst = request.POST
        try:
            from_user = user_model.objects.get(pk=pst['from_user'])
            to_user = user_model.objects.get(pk=pst['to_user'])
            
            Friend.objects.add_friend(
            from_user,
            to_user)
        except Exception as er:
            return Response({"response": er.args[0]})
        
        
        FriendshipRequest.objects.get(
            from_user=from_user,
            to_user=to_user).accept()
        
        return Response({"response": "Пользователи теперь друзья"})
        
    @action(
        methods=['DELETE'],
        detail=False,
        url_path=r'delete_friends/[\w-]+/[\w-]+'
        )
    def delete_friends(self, request: HttpRequest) -> Response:
        user_model = get_user_model()
        users = request.path.split('/')
        
        from_user = users[-3]
        to_user = users[-2]
        
        try:
            from_user = user_model.objects.get(tag_user=from_user)
            to_user = user_model.objects.get(tag_user=to_user)

            Friend.objects.remove_friend(from_user, to_user)

        except Exception as er:
            return Response({"response": er.args[0]})
        
        return Response({"response": "Вы теперь не друзья :<"})
    

# В конце проекта нужно подумать о безопасности API