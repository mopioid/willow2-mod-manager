from mods_base import get_pc

from typing import Literal


type RewardMessageIcon = Literal[
    "token",
    "head",
    "playerSkin",
    "vehicleSkin",
]


def show_reward_message(msg: str, icon: RewardMessageIcon, play_sound: bool = False) -> None:
    """
    Displays a short, non-blocking message in the main in-game hud.

    Uses the same message style as badass rank rewards.

    Args:
        msg: The message to display.
        play_sound: If True, plays the badass reward ding sound.
        image_shown:
            The type of icon that shows next to the pop up.
            "token" = Badass Token
            "head" = Player Head
            "playerSkin" = Player Skin
            "vehicleSkin" = Vehicle Skin

    """
    pc = get_pc()

    hud_movie = pc.GetHUDMovie()

    if hud_movie is None:
        return

    hud_movie.SingleArgInvokeS("p1.badassToken.gotoAndStop", "stop")
    hud_movie.SingleArgInvokeS("p1.badassToken.gotoAndPlay", "go")

    if icon not in RewardMessageIcon.__value__.__args__:
        raise ValueError(f"icon must be one of {RewardMessageIcon.__value__.__args__}")

    hud_movie.SingleArgInvokeS("p1.badassToken.inner.gotoAndStop", icon)

    if play_sound:
        hud_movie.PlayUISound("RewardCustomization")

    hud_movie.SetVariableString("p1.badassToken.inner.dispText.text", msg)
