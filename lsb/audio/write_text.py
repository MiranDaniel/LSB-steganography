import wave
import struct


def write(audio_path, message, output_path):
    with wave.open(audio_path, "rb") as original_audio:
        num_frames = original_audio.getnframes()
        sample_width = original_audio.getsampwidth()
        framerate = original_audio.getframerate()
        num_channels = original_audio.getnchannels()
        frames = original_audio.readframes(num_frames)

        # Check if the message can fit in the audio file
        message_length = len(message)
        max_message_length = (num_frames * sample_width) // 8
        if message_length > max_message_length:
            raise ValueError("Message is too long to hide in the audio file.")

        binary_message = "".join(format(ord(c), "08b") for c in message)
        print(len(binary_message))

        # Create a new audio file for writing the modified frames
        with wave.open(output_path, "wb") as modified_audio:
            modified_audio.setnchannels(num_channels)
            modified_audio.setsampwidth(sample_width)
            modified_audio.setframerate(framerate)
            modified_frames = bytearray()

            # Modify the least significant bit of each audio sample with the binary message
            message_index = 0
            for i in range(0, len(frames), sample_width):
                current_sample = frames[i : i + sample_width]
                sample_value = struct.unpack("<h", current_sample)[0]
                modified_sample_value = (sample_value & ~1) | int(
                    binary_message[message_index]
                )
                modified_frames.extend(struct.pack("<h", modified_sample_value))
                message_index += 1

                # If the entire message has been hidden, stop modifying the audio
                if message_index == len(binary_message):
                    modified_frames.extend(frames[i + sample_width :])
                    break

            # If there are remaining audio frames, copy them as they are
            if message_index < len(binary_message):
                modified_frames.extend(frames[i + sample_width :])

            modified_audio.writeframes(modified_frames)
