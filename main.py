def on_up_pressed():
    if PLAYING == 1 and mySprite.vy == 0 and JUMP == "up":
        mySprite.vy = -200
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    global LEVEL
    LEVEL = 2
    startLevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def BACK():
    story.show_player_choices("PLAY", "OPTIONS", "CONTROLS")
    if story.check_last_answer("OPTIONS"):
        OPTIONS()
    elif story.check_last_answer("CONTROLS"):
        CONTROLS()
    elif story.check_last_answer("PLAY"):
        PLAY()

def on_a_pressed():
    if PLAYING == 1 and mySprite.vy == 0 and JUMP == "a":
        mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite2, location2):
    tiles.set_wall_at(tiles.get_tile_location(60, 7), True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile12
    """),
    on_overlap_tile2)

def on_left_pressed():
    global LastKeyPressed
    LastKeyPressed = "l"
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . 
                        . . . . f f f f f . f f f . 
                        . . . f f c c c c f f f f f 
                        . . f c c c c c c b f f f f 
                        . . f c c c c c c 3 c f f f 
                        . f c c c c c c c c 3 3 f . 
                        . f c c 4 c c c c c f f f . 
                        . f f c 4 4 c c c f f f f . 
                        . f f f 4 4 f b f 4 4 f f . 
                        . . f f d d f 1 4 d 4 f . . 
                        . . . f d d d e e f f f . . 
                        . . . f e 4 e d d 4 f . . . 
                        . . . f 3 3 e d d e f . . . 
                        . . f f 6 6 f e e f f f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f f . . . f f . . .
            """),
            img("""
                . . . . . . . . . . . . . . 
                        . . . . f f f f f . f f f . 
                        . . . f f c c c c f f f f f 
                        . . f c c c c c c b f f f f 
                        . . f c c c c c c 3 c f f f 
                        . f c c c c c c c c 3 3 f . 
                        . f c c 4 c c c c c f f f . 
                        . f f c 4 4 c c c f f f f . 
                        . f f f 4 4 f b f 4 4 f f . 
                        . . f c d d f 1 4 d 4 f f . 
                        . . . f d d d d 4 f f f . . 
                        . . . f e 4 4 4 e d d 4 . . 
                        . . . f 3 3 3 3 e d d e . . 
                        . . f f 6 6 6 6 f e e f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f f . . . f f . . .
            """),
            img("""
                . . . . f f f f f . f f f . 
                        . . . f f c c c c f f f f f 
                        . . f c c c c c c b f f f f 
                        . . f c c c c c c 3 c f f f 
                        . f c c c c c c c c 3 3 f . 
                        . f c c 4 c c c c c f f f . 
                        . f f e 4 4 c c c f f f f . 
                        . f f e 4 4 f b f 4 4 f f . 
                        . . f f d d f 1 4 d 4 f . . 
                        . . . f d d d d 4 f f f . . 
                        . . . f e 4 4 4 e e f . . . 
                        . . . f 3 3 3 e d d 4 . . . 
                        . . . f 3 3 3 e d d e . . . 
                        . . . f 6 6 6 f e e f . . . 
                        . . . . f f f f f f . . . . 
                        . . . . . . f f f . . . . .
            """)],
        150,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    global LastKeyPressed
    LastKeyPressed = "r"
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(img("""
        . f f f . f f f f f . . . . 
                f f f f f c c c c f f . . . 
                f f f f b c c c c c c f . . 
                f f f c 3 c c c c c c f . . 
                . f 3 3 c c c c c c c c f . 
                . f f f c c c c c 4 c c f . 
                . f f f f c c c 4 4 e f f . 
                . f f 4 4 f b f 4 4 e f f . 
                . . f 4 d 4 1 f d d f f . . 
                . . f f f 4 d d d d f . . . 
                . . . f e e 4 4 4 e f . . . 
                . . . 4 d d e 3 3 3 f . . . 
                . . . e d d e 3 3 3 f . . . 
                . . . f e e f 6 6 6 f . . . 
                . . . . f f f f f f . . . . 
                . . . . . f f f . . . . . .
    """))
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    global LastKeyPressed
    LastKeyPressed = "l"
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(img("""
        . . . . f f f f f . f f f . 
                . . . f f c c c c f f f f f 
                . . f c c c c c c b f f f f 
                . . f c c c c c c 3 c f f f 
                . f c c c c c c c c 3 3 f . 
                . f c c 4 c c c c c f f f . 
                . f f e 4 4 c c c f f f f . 
                . f f e 4 4 f b f 4 4 f f . 
                . . f f d d f 1 4 d 4 f . . 
                . . . f d d d d 4 f f f . . 
                . . . f e 4 4 4 e e f . . . 
                . . . f 3 3 3 e d d 4 . . . 
                . . . f 3 3 3 e d d e . . . 
                . . . f 6 6 6 f e e f . . . 
                . . . . f f f f f f . . . . 
                . . . . . . f f f . . . . .
    """))
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def CONTROLS():
    story.show_player_choices("LEFT", "RIGHT", "JUMP", "BACK")
    if story.check_last_answer("LEFT"):
        game.show_long_text("Left arrow to move left.", DialogLayout.CENTER)
        BACK()
    elif story.check_last_answer("RIGHT"):
        game.show_long_text("Right arrow to move right.", DialogLayout.CENTER)
        BACK()
    elif story.check_last_answer("JUMP"):
        game.show_long_text("" + JUMP + " to jump.", DialogLayout.CENTER)
        BACK()
    elif story.check_last_answer("BACK"):
        BACK()

def on_right_pressed():
    global LastKeyPressed
    LastKeyPressed = "r"
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . 
                        . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 c f f . 
                        . f f 4 4 f b f 4 4 f f f . 
                        . f f 4 d 4 1 f d d c f . . 
                        . . f f f 4 d d d d f . . . 
                        . . 4 d d e 4 4 4 e f . . . 
                        . . e d d e 3 3 3 3 f . . . 
                        . . f e e f 6 6 6 6 f f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . . . . . . . . . 
                        . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 c f f . 
                        . f f 4 4 f b f 4 4 f f f . 
                        . . f 4 d 4 1 f d d f f . . 
                        . . f f f e e d d d f . . . 
                        . . . f 4 d d e 4 e f . . . 
                        . . . f e d d e 3 3 f . . . 
                        . . f f f e e f 6 6 f f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f . . . f f f . . .
            """),
            img("""
                . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 e f f . 
                        . f f 4 4 f b f 4 4 e f f . 
                        . . f 4 d 4 1 f d d f f . . 
                        . . f f f 4 d d d d f . . . 
                        . . . f e e 4 4 4 e f . . . 
                        . . . 4 d d e 3 3 3 f . . . 
                        . . . e d d e 3 3 3 f . . . 
                        . . . f e e f 6 6 6 f . . . 
                        . . . . f f f f f f . . . . 
                        . . . . . f f f . . . . . .
            """)],
        150,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def SONG():
    music.play(music.create_sound_effect(WaveShape.SINE,
            1883,
            3314,
            5,
            255,
            432,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LOGARITHMIC),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_overlap_tile3(sprite3, location3):
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile8
    """),
    on_overlap_tile3)

def OPTIONS():
    global JUMP
    story.show_player_choices("VOLUME", "JUMP KEY", "BACK")
    if story.check_last_answer("VOLUME"):
        music.set_volume(game.ask_for_number("VOLUME BETWEEN 0 - 255", 3))
        BACK()
    elif story.check_last_answer("JUMP KEY"):
        JUMP = game.ask_for_string("JUMP KEY WILL BE: \"a\" or \"up\"", 2)
        BACK()
    elif story.check_last_answer("BACK"):
        BACK()
    else:
        pass
def PLAY():
    global mySprite, LastKeyPressed, PLAYING
    mySprite = sprites.create(img("""
            . f f f . f f f f . f f f . 
                    f f f f f c c c c f f f f f 
                    f f f f b c c c c b f f f f 
                    f f f c 3 c c c c 3 c f f f 
                    . f 3 3 c c c c c c 3 3 f . 
                    . f c c c c 4 4 c c c c f . 
                    . f f c c 4 4 4 4 c c f f . 
                    . f f f b f 4 4 f b f f f . 
                    . f f 4 1 f d d f 1 4 f f . 
                    . . f f d d d d d d f f . . 
                    . . e f e 4 4 4 4 e f e . . 
                    . e 4 f b 3 3 3 3 b f 4 e . 
                    . 4 d f 3 3 3 3 3 3 c d 4 . 
                    . 4 4 f 6 6 6 6 6 6 f 4 4 . 
                    . . . . f f f f f f . . . . 
                    . . . . f f . . f f . . . .
        """),
        SpriteKind.player)
    LastKeyPressed = "0"
    scene.camera_follow_sprite(mySprite)
    controller.move_sprite(mySprite, 100, 0)
    startLevel()
    PLAYING = 1
    SONG()

def on_on_overlap(sprite4, otherSprite):
    sprites.destroy(otherSprite)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_overlap_tile4(sprite5, location4):
    global LEVEL
    LEVEL += 1
    startLevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile10
    """),
    on_overlap_tile4)

def startLevel():
    global KOIN
    if LEVEL == 1:
        sprites.destroy_all_sprites_of_kind(SpriteKind.food)
        tiles.set_current_tilemap(tilemap("""
            level6
        """))
        mySprite.ay = 300
    elif LEVEL == 2:
        sprites.destroy_all_sprites_of_kind(SpriteKind.food)
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        mySprite.ay = 300
    elif LEVEL == 3:
        sprites.destroy_all_sprites_of_kind(SpriteKind.food)
        tiles.set_current_tilemap(tilemap("""
            level10
        """))
        mySprite.ay = 300
    else:
        game.game_over(True)
    for value in tiles.get_tiles_by_type(assets.tile("""
        myTile0
    """)):
        tiles.place_on_random_tile(mySprite, assets.tile("""
            myTile0
        """))
        tiles.set_tile_at(value, assets.tile("""
            transparency16
        """))
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        myTile9
    """)):
        KOIN = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.food)
        animation.run_image_animation(KOIN,
            [img("""
                    . . b b b b . . 
                                . b 5 5 5 5 b . 
                                b 5 d 3 3 d 5 b 
                                b 5 3 5 5 1 5 b 
                                c 5 3 5 5 1 d c 
                                c d d 1 1 d d c 
                                . f d d d d f . 
                                . . f f f f . .
                """),
                img("""
                    . . . b b . . . 
                                . . b 5 5 b . . 
                                . b 5 d 1 5 b . 
                                . b 5 3 1 5 b . 
                                . c 5 3 1 d c . 
                                . c 5 1 d d c . 
                                . . f d d f . . 
                                . . . f f . . .
                """),
                img("""
                    . . . b b . . . 
                                . . b 5 5 b . . 
                                . . b 1 1 b . . 
                                . . b 5 5 b . . 
                                . . b d d b . . 
                                . . c d d c . . 
                                . . c 3 3 c . . 
                                . . . f f . . .
                """),
                img("""
                    . . . b b . . . 
                                . . b 5 5 b . . 
                                . b 5 1 d 5 b . 
                                . b 5 1 3 5 b . 
                                . c d 1 3 5 c . 
                                . c d d 1 5 c . 
                                . . f d d f . . 
                                . . . f f . . .
                """),
                img("""
                    . . . b b b . . 
                                . . b 5 5 5 b . 
                                . b 5 d 3 d 5 b 
                                . b 5 1 5 3 5 b 
                                . c d 1 5 3 5 c 
                                . c d d 1 d 5 c 
                                . . f d d d f . 
                                . . . f f f . .
                """)],
            100,
            True)
        KOIN.set_scale(1.5, ScaleAnchor.MIDDLE)
        tiles.place_on_tile(KOIN, value2)
        tiles.set_tile_at(value2, assets.tile("""
            transparency16
        """))
def SET():
    global PLAYING, LEVEL, JUMP
    PLAYING = 0
    scene.set_background_image(img("""
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffff
                ffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffc
                fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffff
                fffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffffffffffff
                fff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbffffffffffff
                ffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffff
                f33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccffffffffffffffffffff
                ff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffff
                ffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffff
                fffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffff
                fffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcfffff
                ffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffff
                fffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                fcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcffffffffffff
                fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                ffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffff
                ffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffff
                ffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffff
                fffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccf
                ccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffccccccccccccccccccccccccccccc
                cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
                cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
                bbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbb
                bbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbb
                bbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbb
                bbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbb
                bbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbb
                bbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbb
                3bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb33333333
                333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb
                cc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccc
                cccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcc
                cccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccc
                cbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccc
                bbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
                bbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbb
                bbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bb
                dddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddd
                dddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33d
                dddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbd
                ddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbdd
                ddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33ddddddddddddd
                ddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbdddddddddddddd
                ddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3ddddddddddddddd
                d333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333dddddddddddddddddd
                333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3
                33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333d
                33ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd33
                d333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333dddddddddddddddd
                ddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3d
                b3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbb
                bb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbb
                bbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbb
                b3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbb
                dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
                dddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddd
                dddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddd
                dddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddd
                dd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddd
                3333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd333
                33333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
                3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    """))
    LEVEL = 1
    JUMP = "a"
    music.set_volume(100)
    game.set_dialog_cursor(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . 7 7 7 7 7 7 7 . . . . 
                . . . 7 7 3 3 3 3 3 3 3 7 7 . . 
                . . 7 e 3 4 4 f f f 4 4 3 e 7 . 
                . . 7 3 4 5 f f f f 5 5 4 3 7 . 
                . 7 3 4 5 e f f f f 9 e 5 4 3 7 
                . 7 3 4 5 f f 2 2 f f 9 5 4 3 7 
                . 7 3 4 5 f f a a f f 9 5 4 3 7 
                . 7 3 4 5 f f a e f f 9 5 4 3 7 
                . 7 3 4 f f f f f f f 9 5 4 3 7 
                . 7 3 4 f f f f f f f f 5 4 3 7 
                . 7 3 f f e 9 9 9 9 f f 5 4 3 7 
                . . 7 f f 5 5 5 5 5 f f 4 3 7 . 
                . . 7 f f 4 4 4 4 4 4 f f e 7 . 
                . . . 7 7 3 3 3 3 3 3 3 7 7 . . 
                . . . . . 7 7 7 7 7 7 7 . . . .
    """))
    info.set_score(0)

def on_overlap_tile5(sprite6, location5):
    global LEVEL
    LEVEL += 1
    startLevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile11
    """),
    on_overlap_tile5)

KOIN: Sprite = None
LastKeyPressed = ""
LEVEL = 0
JUMP = ""
mySprite: Sprite = None
PLAYING = 0
SET()
BACK()