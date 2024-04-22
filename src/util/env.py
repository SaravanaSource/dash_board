# environments util
# optimize the default value for blank result

import os


def get_env(key: str, default: str = ""):
    v= os.environ.get(key)
    if v:
        #not blank (None, " ")
        return v
    else:
        default


def get_basepath() ->str:
    return get_env("BASE_PATH","/")


def get_pub_key_url() ->str :
    return get_env("PUBLIC_KEY_URL", "")

def get_ui_url()-> str:
    return get_env("UI_URL", "")


def get_run_env() -> str:
    return get_env("RUN_ENV", "dev")

