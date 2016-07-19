import json

__secrets = {
    'secret_key': 'a',
}


def getter(path):
    try:
        with open(path) as handle:
            return json.load(handle)
    except IOError:
        return __secrets


def generator():

    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    __secrets['secret_key'] = get_random_string(50, chars)

    return __secrets

if __name__ == '__main__':
    data = json.dumps(generator())
    print(data)
