namespace SpriteKind {
    export const PIZZA = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.startCountdown(160)
    info.changeScoreBy(1)
    RENO.setPosition(randint(10, 160), randint(10, 120))
})
let RENO: Sprite = null
scene.setBackgroundColor(12)
let mySprite = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . 2 2 2 2 2 2 2 . . . . . . 
    . . 2 . . . . . . . 2 . . . . . 
    . . 2 . 2 . . . 2 . 2 . . . . . 
    . . 2 . . . 2 . . . 2 . . . . . 
    . . 2 . . . 2 . . . 2 . . . . . 
    . . 2 . 2 . . . 2 . 2 . . . . . 
    . . 2 . 2 2 2 2 2 . 2 . . . . . 
    . . 2 . . . . . . . 2 . . . . . 
    . . . 2 2 2 2 2 2 2 . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
RENO = sprites.create(assets.image`PIZZA`, SpriteKind.Food)
