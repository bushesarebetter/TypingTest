import mss

def take_region_screenshot(x1, y1, x2, y2, filename):

    with mss.mss() as sct:
        monitor = {"left": x1,
                "top": y1,
                "width": x2-x1,
                "height": y2-y1}
        output = f"{filename}.png".format(**monitor)

        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
