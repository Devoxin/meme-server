import os
import uuid

from flask import after_this_request, send_file
from moviepy.editor import CompositeVideoClip, TextClip, VideoFileClip
from moviepy.video.fx.rotate import rotate

from utils.endpoint import Endpoint, setup


@setup(rate=1, per=30)
class Kowalski(Endpoint):
    """
    This endpoint returns an MP4 file. Make sure your application knows how to handle this format.
    Malformed requests count against your ratelimit for this endpoint.
    Separate text with a comma.
    """
    params = ['text']

    def generate(self, avatars, text, usernames, kwargs):
        name = uuid.uuid4().hex + '.gif'

        @after_this_request
        def remove(response):  # pylint: disable=W0612
            try:
                os.remove(name)
            except (FileNotFoundError, OSError, PermissionError):
                pass

            return response
        clip = VideoFileClip("assets/kowalski/kowalski.gif")  # pylint: disable=E1111
        text = TextClip(text, fontsize=36, method='caption', size=(245, None), align='West', color='black',  # pylint: disable=E1111
                        stroke_color='black', stroke_width=1,
                        font='Verdana').set_duration(clip.duration)
        text = text.set_position((340, 65)).set_duration(clip.duration)
        text = rotate(text, angle=10, resample='bilinear')

        video = CompositeVideoClip([clip, text]).set_duration(clip.duration)  # pylint: disable=E1111

        video.write_gif(name)
        clip.close()
        video.close()
        return send_file(name, mimetype='image/gif')
