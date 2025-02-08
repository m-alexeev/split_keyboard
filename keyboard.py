import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from binds import *

from configs import rgb, split
from layers import layers


keyboard = KMKKeyboard()
# Set the keyboard row and col pins
col_pins = (
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
)
row_pins = (
    board.D7,
    board.D8,
    board.D9,
    board.D10,
)
keyboard.col_pins = col_pins
keyboard.row_pins = row_pins

# Keyboard diode orientation for the row and col pins
# Either ROW2COL or COL2ROW
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.modules = [split, layers, rgb]

# fmt: off
keyboard.keymap = [
    # Base Layer
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,       KC.Y, KC.U, KC.I, KC.O, KC.P,
        KC.A, KC.S, KC.D, KC.F, KC.G,       KC.H, KC.J, KC.K, KC.L, KC.SCLN,
        KC.Z, KC.X, KC.C, KC.V, KC.B,       KC.N, KC.M, KC.COMMA, KC.DOT,KC.SLASH,
            KC.MO(1), KC.SPC, KC.LSFT,   X, X,  KC.BSPACE, KC.ENTER,KC.MO(2),
    ],
    # Function Layer 1
    [
        KC.ESC,KC.GRAVE, KC.TILDE,T,T,      T,T,KC.MINS,KC.EQL,KC.BSLASH,
        ALL,SAVE,T,T,T,                     KC.LEFT,KC.DOWN,KC.UP,KC.RIGHT,KC.QUOT,
        UNDO,CUT,COPY,PASTE,KC.LCTL,        T,T,T,T,T,
        T,KC.LALT,T,                X,X,    KC.LCTL, KC.TAB, KC.RSFT,
    ],
    [
        KC.N1, KC.N2,KC.N3,KC.N4,KC.N5,     KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,
        T,KC.HOME,KC.END,T,KC.DEL,          T,KC.LPRN,KC.RPRN,KC.LBRACKET,KC.RBRACKET,
        T,KC.LGUI,T,T,T,                    CMD_TAB,T,T,T,T,
        T,T,T,                      X,X,    T,T,T,
    ],
]
