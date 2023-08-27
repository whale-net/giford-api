import os
from tempfile import NamedTemporaryFile
from typing import Annotated # can this be replaced with 3.10?


from fastapi import APIRouter, UploadFile

from giford.image import SingleImage, MultiImage
from giford.frame import FrameBatch
from giford.action.scroll import Scroll

router = APIRouter()

@router.get('/test/')
async def test() -> dict[str, str]:
    return {"hello": "world"}

# TODO - https://fastapi.tiangolo.com/tutorial/request-files/#file-parameters-with-uploadfile
@router.post('/slide')
async def slide(img: UploadFile):
    simg = SingleImage()
    simg.load(img.file)

    batch = FrameBatch.create_from_image(simg)

    s = Scroll()
    out_batch = s.process(batch, is_horizontal_scroll=True, is_vertical_scroll=True)
    
    mimg = MultiImage.create_from_frame_batch(out_batch)
    test_output = './test_data/test.gif'
    if os.path.exists(test_output):
        os.remove(test_output)
    mimg.save(test_output)
        
    return "written to server idiot"