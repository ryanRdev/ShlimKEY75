from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.col_pins = (1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20)
keyboard.row_pins = (21, 22, 24, 25, 26)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    # Row 0
    [KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,
     KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.NO,   KC.NO,   KC.NO],

    # Row 1
    [KC.GRV,  KC._1,   KC._2,   KC._3,   KC._4,   KC._5,   KC._6,   KC._7,
     KC._8,   KC._9,   KC._0,   KC.MINS, KC.EQL,  KC.BSPC, KC.NO,   KC.NO],

    # Row 2
    [KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,
     KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.NO,   KC.NO],

    # Row 3
    [KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,
     KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.NO,   KC.NO,   KC.NO],

    # Row 4 (physical rows 5 + 6 merged)
    [KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,
     KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.LCTL, KC.LGUI, KC.LALT, KC.SPC]
]