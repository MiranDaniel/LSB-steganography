from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np

def _get_bit_plane(data, bit):
    return (data & (1 << bit)) >> bit

def analyze(input_audio):
    audio = AudioSegment.from_file(input_audio)
    samples = np.array(audio.get_array_of_samples())

    bit_planes = [_get_bit_plane(samples, bit) for bit in range(16)]

    fig, axes = plt.subplots(4, 4, figsize=(12, 12), sharex=True)

    for i in range(4):
        for j in range(4):
            bit_idx = i * 4 + j
            _, _, Sxx, im = axes[i, j].specgram(bit_planes[bit_idx], Fs=audio.frame_rate, cmap='viridis')
            axes[i, j].set_title(f"Bit {bit_idx}")
            axes[i, j].set_ylim([0, audio.frame_rate / 2])  # Limit the y-axis to the relevant frequency range
            axes[i, j].axes.get_xaxis().set_visible(False)

    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.tight_layout()
    plt.savefig("./output/spectogram.png")
    return axes
