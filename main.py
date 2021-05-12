@namespace
class SpriteKind:
    PIZZA = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.start_countdown(160)
    info.change_score_by(1)
    RENO.set_position(randint(10, 160), randint(10, 120))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

RENO: Sprite = None
scene.set_background_color(12)
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
RENO = sprites.create(assets.image("""
    PIZZA
"""), SpriteKind.food)