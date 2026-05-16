from wrotools import *

async def main():
    #await moveAttachmentArms(30, -270)
    await moveAttachmentArms(30, 360+180)
    await db.straight(180)
    await db.turn(90)
    await db.straight(300)
    await moveAttachmentArms(30, -270)
    

    
    
    


if __name__ == "__main__":
    run_task(main())
