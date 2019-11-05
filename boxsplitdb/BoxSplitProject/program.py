import data.mongo_setup as mongo_setup

import services.data_service as svc


def main(): 
    mongo_setup.global_init()

    user = svc.find_user_by_email("poog@split.box")
    box = svc.find_box_by_id("5dbc8670e3e74473175d283f")
    split = svc.find_split_by_id("5dbc8670e3e74473175d283e")

    svc.add_split_to_box(box, split)
    svc.add_split_to_user(user, split)






if __name__ == '__main__':
    main()