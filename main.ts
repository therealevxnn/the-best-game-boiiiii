controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 50, 50)
    projectile.follow(mySprite2, 50)
    music.play(music.createSoundEffect(WaveShape.Square, 1600, 925, 42, 61, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    pause(500)
    info.changeLifeBy(-1)
})
info.onLifeZero(function () {
    game.gameOver(false)
    game.setGameOverMessage(false, "UR TRASH")
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    game.gameOver(true)
    game.setGameOverEffect(true, effects.confetti)
    game.setGameOverMessage(true, "YOU KILLED HIM!")
})
let projectile: Sprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
scene.setBackgroundColor(8)
info.setLife(4)
game.setGameOverMessage(false, "UR TRASH!")
scene.cameraFollowSprite(mySprite)
mySprite2 = sprites.create(img`
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
    `, SpriteKind.Enemy)
mySprite2.follow(mySprite, 70.5)
game.showLongText("press z to shoot the self homing projectiles. when you shoot the enemy, you win! but be careful because if the enemy touches you with the black box you die. when done reading, press z on keyboard and make sure to move out of the way quick, good luck! ", DialogLayout.Full)
