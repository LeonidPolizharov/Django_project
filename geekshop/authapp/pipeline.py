import requests
from datetime import date, datetime
from social_core.exceptions import AuthForbidden


def get_user_gender(user, response, *args, **kwargs):
    access_token = response['access_token']
    vk_response = requests.get(
        f'https://api.vk.com/method/users.get?access_token={access_token}&fields=bdate,sex&v=5.131'
    )
    data = vk_response.json()['response'][0]
    bdate = datetime.strptime(data['bdate'], "%d.%m.%Y").date()
    age = datetime.now().date().year - bdate.year
    if age < 18:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    user.profile.about = data;
    user.profile.save()

    return {}