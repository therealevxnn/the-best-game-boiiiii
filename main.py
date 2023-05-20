def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 3 3 3 3 . . . . . . . . 
                    . . . . 3 3 3 3 . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        50,
        50)
    projectile.follow(mySprite2, 50)
    music.play(music.create_sound_effect(WaveShape.SQUARE,
            1600,
            925,
            42,
            61,
            300,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    pause(500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_life_zero():
    game.game_over(False)
    game.set_game_over_message(False, "UR TRASH")
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite2, otherSprite2):
    game.game_over(True)
    game.set_game_over_effect(True, effects.confetti)
    game.set_game_over_message(True, "YOU KILLED HIM!")
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . f f f f f f f f . . . . 
            . . . . f . . . . . . f . . . . 
            . . . . f . f . . f . f . . . . 
            . . . . f . . . . . . f . . . . 
            . . . . f . . . . . . f . . . . 
            . . . . f f f f f f f f . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . f f f f f f f f f f . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . . f f . . . . . . . 
            . . . . . . f f f f . . . . . . 
            . . . . . f f . . f f . . . . . 
            . . . . . f . . . . f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
scene.set_background_color(8)
info.set_life(4)
game.set_game_over_message(False, "UR TRASH!")
scene.camera_follow_sprite(mySprite)
mySprite2 = sprites.create(img("""
        f f f f f f f f f f f f f f f f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . 3 3 3 3 3 . . . . . . f 
            f . . . 3 f . f 3 . . . . . . f 
            f . . . 3 . . . 3 . . . . . . f 
            f . . . 3 f f f 3 . . . . . . f 
            f . . 3 3 3 . 3 3 3 . . . . . f 
            f . . 3 . 3 . 3 . 3 . . . . . f 
            f . . 3 3 3 . 3 3 3 . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f . . . . . . . . . . . . . . f 
            f f f f f f f f f f f f f f f f
    """),
    SpriteKind.enemy)
mySprite2.follow(mySprite, 70.5)
game.show_long_text("press z to shoot the self homing projectiles. when you shoot the enemy, you win! but be careful because if the enemy touches you with the black box you die. when done reading, press z on keyboard and make sure to move out of the way quick, good luck! ",
    DialogLayout.FULL)