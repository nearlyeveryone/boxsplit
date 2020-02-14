import data.mongo_setup as mongo_setup

import services.data_service as svc

import services.fast_api as fa
import uvicorn
import json


def main():
    print("ree")
    secrets = read_secrets()
    mongo_setup.global_init(secrets)
    print("asdf")

    user = svc.create_user("poog", "poog@split.box")
    print(user)
    box = svc.create_box("testbox", "this is a test box")
    print(box)
    split = svc.create_split("testsplit", "this is a test split", 12)
    print(split)


    # print(svc.find_user_by_email('poog@split.box'))
    # user = svc.find_user_by_email("poog@split.box")
    #
    # svc.add_split_to_box(box, split)
    # svc.add_split_to_user

    # app = fa.app
    # uvicorn.run(app, port=8000)




def read_secrets():
    with open("secrets.json", "r") as read_file:
        data = json.load(read_file)
    return data


if __name__ == '__main__':
    main()