import os
from tempfile import NamedTemporaryFile
from typing import Annotated # can this be replaced with 3.10?


from fastapi import APIRouter, File

from giford.frame_wrapper import SingleImage, MultiImage
from giford.frame_batch import FrameBatch
from giford.image_actions.scroll import Scroll

router = APIRouter()

@router.get('/test/')
async def test() -> dict[str, str]:
    return {"hello": "world"}

@router.post('/slide')
async def slide(img: Annotated[bytes, File()]):
    simg = SingleImage()
    with NamedTemporaryFile('wb') as fd:
        fd.write(img)
        simg.load(fd.name)

    batch = FrameBatch.create_from_single_image(simg)

    s = Scroll()
    out_batch = s.process(batch, is_horizontal_scroll=True, is_vertical_scroll=True)
    
    mimg = MultiImage.create_from_frame_batch(out_batch)
    test_output = './test_data/test.gif'
    if os.path.exists(test_output):
        os.remove(test_output)
    mimg.save(test_output)
        
    return "written to server idiot"