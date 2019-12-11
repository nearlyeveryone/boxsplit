import data.mongo_setup as mongo_setup

import services.data_service as svc

import services.fast_api as fa
import uvicorn
import json


def main():
    secrets = read_secrets()
    mongo_setup.global_init(secrets)

    print(svc.find_user_by_email('poog@split.box'))
    # user = svc.find_user_by_email("poog@split.box")
    # box = svc.find_box_by_id("5dbc8670e3e74473175d283f")
    # split = svc.find_split_by_id("5dbc8670e3e74473175d283e")
    #
    # svc.add_split_to_box(box, split)
    # svc.add_split_to_user

    #app = fa.app
    #uvicorn.run(app, host="0.0.0.0", port=8000)




def read_secrets():
    with open("secrets.json", "r") as read_file:
        data = json.load(read_file)
    return data


if __name__ == '__main__':
    main()