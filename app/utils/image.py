import io
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt

def fig_to_image(fig):
    # Create an buffer to store image
    buf = io.BytesIO() 
    # Save fig to buffer and free up memory (?)
    fig.savefig(buf, format="png")
    plt.close(fig)
    # Reset and read the buffer
    buf.seek(0)
    return 
    


 