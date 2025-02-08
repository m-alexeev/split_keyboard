from kmk.extensions.rgb import RGB
from kmk.modules.split import Split, SplitType, SplitSide
from storage import getmount
import board

HUES = [4, 120, 180]
side = SplitSide.RIGHT if str(getmount("/").label)[-1] == "R" else SplitSide.LEFT

rgb = RGB(
    pixel_pin=board.A0,
    num_pixels=36,
    val_limit=100,
    hue_default=HUES[0],
    sat_default=255,
    rgb_order=(1, 0, 2),
    val_default=255,
    hue_step=5,
    sat_step=5,
    val_step=5,
    reverse_animation=False,
    refresh_rate=60,
)

split = Split(
    split_flip=False,  # If both halves are the same, but flipped, set this True
    split_side=side,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    data_pin=board.D1,  # The primary data pin to talk to the secondary device with
    data_pin2=board.D0,  # Second uart pin to allow 2 way communication
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)
